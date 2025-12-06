# 🛡️ ORCHESTR AI

**Gelişmiş Yapay Zeka Takım Orkestrasyon Platformu**

ORCHESTR PRO, **Microsoft AutoGen** ve **Streamlit** üzerine inşa edilmiş, çoklu yapay zeka ajanlarının (Multi-Agent Systems) işbirliği içinde çalışmasını sağlayan modüler bir arayüzdür. Kullanıcılar, özelleştirilmiş ajan ekipleri kurabilir, RAG (Retrieval-Augmented Generation) ile belge analizi yaptırabilir ve karmaşık görevleri dinamik tur yönetimi ile çözüme kavuşturabilir.

## 🌟 Temel Özellikler

  * **🧠 Dinamik Ajan Yönetimi:** Özelleştirilebilir rol, isim ve model (GPT-4, Gemini Pro vb.) seçenekleriyle sınırsız ajan oluşturma ve yönetme.
  * **🔄 Akıllı Tur (Cycle) Mantığı:** Standart mesaj sayısı yerine, döngü bazlı tur hesaplama. (Örn: 2 Ajan x 5 Tur = 10 Etkileşim).
  * **📂 RAG & Dosya Analizi:** PDF ve TXT dosyalarını yükleyerek ajanların bu belgeler üzerinden çalışmasını sağlama.
  * **🤝 Takım Farkındalığı (Team Awareness):** Ajanlar, ekipte başka kimlerin olduğunu ve rollerini bilir; birbirlerinin çıktılarını analiz eder.
  * **🎨 Gelişmiş UI/UX:**
      * Kişiselleştirilebilir Temalar ve Arka Planlar.
      * Çoklu Dil Desteği (TR / EN).
      * Otomatik Kaydırma (Auto-Scroll) ve Canlı Terminal Logları.
  * **💾 Kalıcı Hafıza:** Kullanıcılar, ajanlar ve sohbet geçmişi yerel veritabanında (`orchestr_db`) güvenle saklanır.
  * **🛡️ Güvenli Mimari:** Modüler 4 dosyalı yapı, şifreli kullanıcı girişi ve "Zombi Veri" koruması.

## 📂 Proje Mimarisi

Proje, sürdürülebilirlik ve performans için **4 temel modüle** ayrılmıştır:

| Dosya | Açıklama |
| :--- | :--- |
| `main.py` | Uygulamanın ana giriş noktası. UI mantığı, sohbet döngüsü ve AutoGen orkestrasyonunu yönetir. |
| `config.py` | Sabit ayarlar, dil paketleri (TR/EN), model listeleri ve sistem parametrelerini içerir. |
| `data_handler.py` | Veritabanı (JSON) işlemleri, şifreleme, dosya okuma (RAG) ve ajan transferi işlemlerini yürütür. |
| `styles.py` | CSS enjeksiyonları, görsel tasarım, tema motoru ve canlı terminal sınıfını barındırır. |

## 🚀 Kurulum

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:

**1. Depoyu Klonlayın:**

```bash
git clone https://github.com/Yerlifan/orchestr-ai.git
cd orchestr-ai
```

**2. Gerekli Kütüphaneleri Yükleyin:**

```bash
pip install -r requirements.txt
```

*(Not: `requirements.txt` dosyasının içeriği aşağıdadır)*

**3. Uygulamayı Başlatın:**

```bash
streamlit run orchestr_streamlit.py
```

## ⚙️ Gereksinimler (`requirements.txt`)

Eğer dosyanız yoksa, şu içeriği `requirements.txt` olarak kaydedin:

```text
streamlit
pyautogen
PyPDF2
watchdog
openai
google-generativeai
```

## 📖 Kullanım Rehberi

1.  **Giriş Yapın:** Varsayılan kullanıcı veya yeni kayıt ile sisteme girin.
2.  **Ekibi Kurun:** Sidebar menüsünden "Yeni Ajan Ekle" diyerek ekibinizi oluşturun. Modelleri (GPT-4, Gemini vb.) seçin.
3.  **Ayarları Yapın:** Yaratıcılık seviyesi, İlk Tur ve Feedback Turu limitlerini belirleyin.
4.  **Görev Verin:** Sohbet kutusuna görevi yazın. İsterseniz bir PDF dosyası ekleyin.
5.  **İzleyin ve Yönetin:** Ajanların tartışmasını izleyin. Gerektiğinde "Görevi Durdur" butonu ile müdahale edin veya yönlendirme yapın.

## 🤝 Katkıda Bulunma

1.  Bu projeyi Fork'layın.
2.  Yeni bir özellik dalı (branch) oluşturun (`git checkout -b feature/YeniOzellik`).
3.  Değişikliklerinizi Commit edin (`git commit -m 'Yeni özellik eklendi'`).
4.  Dalınızı Push edin (`git push origin feature/YeniOzellik`).
5.  Bir Pull Request oluşturun.

## 📄 Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakınız.
