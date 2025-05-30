
# Hücre Sayım Uygulaması

## Proje Amacı
Bu proje, mikroskop altında çekilmiş hücre görüntülerinden otomatik olarak hücre sayımı yapmayı amaçlamaktadır. 
Görüntü işleme teknikleri kullanılarak hücreler tespit edilmekte ve sayılmaktadır. 
Böylece biyomedikal araştırmalarda manuel sayım gereksinimi azalır, zamandan ve emekten tasarruf sağlanır.

## Projenin Önemi
- **Zaman Tasarrufu:** Manuel hücre sayımı çok zaman alır ve yorucu olabilir.
- **Hata Payının Azaltılması:** İnsan kaynaklı sayım hataları en aza iner.
- **Otomasyon:** Araştırmacılar ve laboratuvarlar için tekrarlanabilir ve güvenilir sonuçlar sunar.
- **Eğitim Amaçlı:** Görüntü işleme ve bilgisayarla görme alanında temel bir uygulama örneği sağlar.

## Kullanılan Teknolojiler
- Python 
- OpenCV (Bilgisayarla Görme Kütüphanesi)
- PyQt5 (Kullanıcı Arayüzü)

## Dosya Açıklamaları

| Dosya Adı           | Açıklama                                                                                         |
|---------------------|-------------------------------------------------------------------------------------------------|
| `hucre_sayim.py`    | Hücre sayımı için temel görüntü işleme ve kontur bulma algoritmasını içerir.                     |
| `arayuz.py`         | PyQt5 ile hazırlanmış arayüz tasarımı, buton ve etiketlerin tanımlandığı dosya.                  |
| `main.py`           | Arayüz ile hücre sayımı fonksiyonlarının bağlandığı, kullanıcı etkileşimlerini yöneten ana dosya.|
| `ornekler/hucre1.jpg` | Test amaçlı hücre görüntülerinin saklandığı klasör.                                            |

## Programın Kullanımı
1. `main.py` dosyasını çalıştırın.
2. Arayüzde bulunan "Fotoğraf Seç" butonuna tıklayarak hücre görüntüsü seçin.
3. Program seçilen görüntüyü analiz edip hücre sayısını hesaplayacak ve sonuçları arayüzde gösterecektir.

## Geliştirilebilir Yönler
- **Daha Gelişmiş Görüntü İşleme:** Watershed algoritması, morfolojik işlemler ve yapay zeka tabanlı segmentasyon eklenebilir.
- **Hücre Tipi Ayrımı:** Farklı hücre tiplerini sınıflandırmak için makine öğrenimi yöntemleri uygulanabilir.
- **Sonuçların Kaydedilmesi:** Sayım sonuçları ve işaretlenen görüntüler dosyaya veya veri tabanına kaydedilebilir.
- **Kullanıcı Arayüzü İyileştirmeleri:** Daha estetik ve kullanıcı dostu arayüz tasarımı yapılabilir.
- **Çoklu Görüntü Desteği:** Aynı anda birden fazla görüntü analiz edilebilir.

## Notlar
- Proje, hücre sayımı için temel bir örnektir. 
Görüntülerin kalitesi ve özelliklerine göre parametrelerin (eşik değerleri, filtre boyutları) 
ayarlanması gerekebilir.
- Yüksek doğruluk için derin öğrenme yöntemleri araştırılabilir.

---

**Hazırlayan:** Hasan Basri Marakcı 20290423 
**Tarih:** 20.05.2025
