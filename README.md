# 🛡️ ORCHESTR AI

**Gelişmiş Yapay Zeka Takım Orkestrasyon Platformu**

ORCHESTR AI, **Microsoft AutoGen** ve **Streamlit** üzerine inşa edilmiş, çoklu yapay zeka ajanlarının (Multi-Agent Systems) işbirliği içinde çalışmasını sağlayan modüler bir arayüzdür. Kullanıcılar, özelleştirilmiş ajan ekipleri kurabilir, RAG (Retrieval-Augmented Generation) ile belge analizi yaptırabilir ve karmaşık görevleri dinamik tur yönetimi ile çözüme kavuşturabilir.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32-red)
![AutoGen](https://img.shields.io/badge/Microsoft%20AutoGen-0.2-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

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
git clone [https://github.com/Yerlifan/orchestr-ai.git](https://github.com/Yerlifan/orchestr-ai.git)
cd orchestr-ai
````

**2. Gerekli Kütüphaneleri Yükleyin:**

```bash
pip install -r requirements.txt
```

**3. Uygulamayı Başlatın:**

```bash
streamlit run main.py
```

## 🔑 Yapılandırma ve API Anahtarları

Uygulamanın çalışması için LLM sağlayıcılarından API anahtarına ihtiyacınız vardır. Uygulama arayüzünden şu modelleri kullanabilirsiniz:

  * **OpenAI:** GPT-4o, GPT-4.1
  * **Google:** Gemini 2.5 Pro, Gemini 2.5 Flash

**Not:** API anahtarlarını kod içine yazmanıza gerek yoktur. Uygulamaya giriş yaptıktan sonra **Sidebar \> API Erişimi (Anahtar)** menüsünden anahtarlarınızı güvenle girebilirsiniz.

## 📖 Kullanım Rehberi

1.  **Giriş Yapın:**

      * Uygulama açıldığında giriş ekranı sizi karşılar.
      * **Kayıt Ol** sekmesinden kaydolup sisteme giriş yapın. 
      * **Varsayılan Admin Şifresi:** `yerlifan123`
      * *Bu şifreyi `config.py` dosyasından değiştirebilirsiniz.*

2.  **API Anahtarlarını Girin:**

      * Sol menüdeki kilit simgeli alana tıklayın.
      * Yönetici şifresini (`yerlifan123`) girerek kilidi açın.
      * OpenAI ve/veya Google API anahtarınızı yapıştırın.

3.  **Ekibi Kurun:**

      * Sidebar menüsünden "Yeni Ajan Ekle" diyerek ekibinizi oluşturun.
      * Ajanlara İsim, Rol ve Model atayın ve "Kaydet" butonuna basın.

4.  **Görev Verin:**

      * Sohbet kutusuna görevi yazın. İsterseniz bir PDF dosyası ekleyin (RAG sistemi otomatik devreye girer).
      * Ajanlar belirlediğiniz tur sayısı kadar tartışıp sonucu sunacaktır.

## ⚙️ Gereksinimler (`requirements.txt`)

```text
streamlit
pyautogen
PyPDF2
watchdog
openai
google-generativeai
```

## 🤝 Katkıda Bulunma

1.  Bu projeyi Fork'layın.
2.  Yeni bir özellik dalı (branch) oluşturun (`git checkout -b feature/YeniOzellik`).
3.  Değişikliklerinizi Commit edin (`git commit -m 'Yeni özellik eklendi'`).
4.  Dalınızı Push edin (`git push origin feature/YeniOzellik`).
5.  Bir Pull Request oluşturun.

## 📄 Lisans

Bu proje MIT Lisansı ile lisanslanmıştır.
