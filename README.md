# Computer Vision - Parmak Sayma Uygulaması

Bu proje, **Python**, **OpenCV** ve **MediaPipe** kullanılarak geliştirilmiş gerçek zamanlı bir **parmak sayma uygulamasıdır**.

Uygulama, bilgisayar kamerasından alınan görüntü üzerinde eli algılar, **21 el eklem noktasını (landmark)** tespit eder ve açık olan parmakların sayısını anlık olarak ekranda gösterir.

---

## Özellikler

*  Gerçek zamanlı kamera görüntüsü işleme
*  El algılama ve takip
*  21 el eklem noktasının tespiti
*  Açık parmakların otomatik sayılması
*  Hızlı ve düşük gecikmeli çalışma

---

## 🛠️ Kullanılan Teknolojiler

* Python
* OpenCV
* MediaPipe
* MediaPipe Hand Landmarker

---

## Kurulum

Gerekli kütüphaneleri yükleyin:

```bash
pip install opencv-python mediapipe
```

---

##  Çalıştırma

Projeyi aşağıdaki komut ile başlatabilirsiniz:

```bash
python main.py
```

Program çalıştıktan sonra kamera açılacak ve eliniz algılanarak açık parmak sayısı ekranda gösterilecektir.

Programdan çıkmak için **0** tuşuna basmanız yeterlidir.

---

##  Proje Yapısı

```text
.
├── main.py
├── hand_landmarker.task
└── README.md
```

### Dosyalar

| Dosya                  | Açıklama                         |
| ---------------------- | -------------------------------- |
| `main.py`              | Uygulamanın kaynak kodu          |
| `hand_landmarker.task` | MediaPipe Hand Landmarker modeli |
| `README.md`            | Proje dokümantasyonu             |

---

##  Çalışma Mantığı

1. Kamera görüntüsü alınır.
2. MediaPipe Hand Landmarker ile el tespit edilir.
3. El üzerindeki **21 landmark** belirlenir.
4. Parmak uçları ve eklem noktaları karşılaştırılarak açık parmaklar hesaplanır.
5. Toplam açık parmak sayısı gerçek zamanlı olarak ekranda gösterilir.


