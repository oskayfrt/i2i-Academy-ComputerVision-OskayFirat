from pathlib import Path
import time

import cv2
import mediapipe as mp

MODEL_PATH = Path(__file__).with_name("hand_landmarker.task")
FINGER_TIPS = (8, 12, 16, 20)
HAND_CONNECTIONS = (
    (0, 1), (1, 2), (2, 3), (3, 4),
    (0, 5), (5, 6), (6, 7), (7, 8),
    (5, 9), (9, 10), (10, 11), (11, 12),
    (9, 13), (13, 14), (14, 15), (15, 16),
    (13, 17), (17, 18), (18, 19), (19, 20), (0, 17),
)


def count_open_fingers(landmarks):
    fingers = []
    thumb_is_open = (
        landmarks[4].x < landmarks[3].x
        if landmarks[5].x < landmarks[17].x
        else landmarks[4].x > landmarks[3].x
    )
    fingers.append(thumb_is_open)

    for tip in FINGER_TIPS:
        fingers.append(landmarks[tip].y < landmarks[tip - 2].y)
    return sum(fingers)


def draw_hand(frame, landmarks):
    height, width, _ = frame.shape
    points = [(int(point.x * width), int(point.y * height)) for point in landmarks]
    for start, end in HAND_CONNECTIONS:
        cv2.line(frame, points[start], points[end], (0, 255, 0), 2)
    for point in points:
        cv2.circle(frame, point, 4, (0, 0, 255), -1)


def main():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"MediaPipe el modeli bulunamadi: {MODEL_PATH}")

    options = mp.tasks.vision.HandLandmarkerOptions(
        base_options=mp.tasks.BaseOptions(model_asset_path=str(MODEL_PATH)),
        running_mode=mp.tasks.vision.RunningMode.VIDEO,
        num_hands=1,
    )
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        raise RuntimeError("Kamera acilamadi. Kamera iznini kontrol edin.")

    start_time = time.perf_counter()
    try:
        with mp.tasks.vision.HandLandmarker.create_from_options(options) as detector:
            while True:
                success, frame = camera.read()
                if not success:
                    break

                frame = cv2.flip(frame, 1)
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
                timestamp_ms = int((time.perf_counter() - start_time) * 1000)
                result = detector.detect_for_video(mp_image, timestamp_ms)

                for index, landmarks in enumerate(result.hand_landmarks):
                    finger_count = count_open_fingers(landmarks)
                    draw_hand(frame, landmarks)
                    cv2.putText(frame, str(finger_count), (50, 100),
                                cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)

                cv2.imshow("Kamera - cikmak icin 0", frame)
                if cv2.waitKey(1) & 0xFF == ord("0"):
                    break
    finally:
        camera.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
