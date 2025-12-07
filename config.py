import os

# --- KLASÖR VE DOSYA YOLLARI ---
DB_FOLDER = "orchestr_db"
if not os.path.exists(DB_FOLDER):
    os.makedirs(DB_FOLDER)

USERS_FILE = os.path.join(DB_FOLDER, "users.json")
MODELS_FILE = os.path.join(DB_FOLDER, "models.json")

# --- GÜVENLİK ---
ADMIN_PASSWORD = "yerlifan123"

# --- SİSTEM AYARLARI ---
MAX_CHAR_LIMIT = 25000  
MAX_AGENT_LIMIT = 10    

# --- AVATARLAR ---
AVATARS = ["👨‍💻", "👩‍💻", "🚀", "🧠", "🦁", "🦉", "🦄", "🎨", "⚡", "🤖", "🔥", "💎", "🛡️", "👑", "👽", "👻", "🐯"]

# --- TEMA RENKLERİ ---
THEMES = {
    "Kızıl": "#FF4B4B", 
    "Mavi": "#2196F3", 
    "Yesil": "#4CAF50", 
    "Mor": "#9C27B0", 
    "Turuncu": "#FF9800", 
    "Turkuaz": "#00BCD4"
}

# --- VARSAYILAN MODELLER ---
DEFAULT_MODELS = [
    {"label": "GPT-4.1", "model": "gpt-4.1", "api_type": "openai"},
    {"label": "GPT-4o", "model": "gpt-4o", "api_type": "openai"},
    {"label": "Gemini 2.5 Pro", "model": "gemini-2.5-pro", "api_type": "google"},
    {"label": "Gemini 2.5 Flash", "model": "gemini-2.5-flash", "api_type": "google"},
    {"label": "🏠 Local Llama 3", "model": "llama3", "api_type": "local", "base_url": "http://localhost:11434/v1"}
]
MLABS = [m["label"] for m in DEFAULT_MODELS]

# --- DİL PAKETİ ---
LANG = {
    "TR": {
        "login_header": "ORCHESTR.AI", "login_sub": "Yapay Zeka Takım Orkestrasyonu",
        "username": "Kullanıcı Adı", "pass": "Şifre", "login_btn": "Giriş Yap", "reg_btn": "Kayıt Ol",
        "login_title": "Giriş Yap", "reg_title": "Kayıt Ol", "remember": "Beni Hatırla",
        "new_chat": "Yeni Ekip", "my_chats": "Projelerim", "settings": "Sistem Ayarları",
        "api_access": "API Erişimi", "start_btn": "EKİBİ KUR VE BAŞLAT", 
        "stop_task": "Görevi Durdur", "stop_icon": "✖️",
        "logout": "Çıkış", "chat_input": "Görev ver veya feedback yaz...", "feedback_label": "YÖNLENDİRME:",
        "team_setup": "Ekip Kurulumu", "add_agent": "Üye Ekle", "name": "İsim", "role": "Rol", "model": "Model",
        "save": "Kaydet", "delete": "Sil", "active_team": "Çalışan Ekip",
        "attach": "Dosya Ekle", "file_help": "Analiz için PDF/TXT yükle.",
        "upload_doc": "Döküman Yükle", "upload_img": "Resim Yükle",
        "theme_sel": "Tema Rengi", "bg_sel": "Arka Plan", "lang_sel": "Dil",
        "creativity": "Yaratıcılık", "order": "Sıra",
        "auto": "Otomatik", "seq": "Sıralı", "active_project": "Proje", "edit_title": "Başlığı Düzenle",
        "admin_pass": "Admin Şifresi", "lock": "Kilitle", "unlock": "Kilit Açıldı",
        "wrong_pass": "Hatalı Şifre", "no_api": "API Anahtarı Yok", "terminal": "Canlı Terminal", "working": "Çalışıyor...",
        "our_team": "TAKIM ARKADAŞLARIMIZ", "previous_projects": "(Önceki Projelerden)",
        "welcome": "Hoşgeldin", 
        "import_title": "♻️ Geçmişten Ajan Transfer Et", "import_btn": "Transfer Et", "no_past_agent": "Geçmiş kayıt bulunamadı.",
        "model_mgmt": "Model Yönetimi", "add_model": "Yeni Model Ekle", "model_label": "Görünecek İsim",
        "model_id": "Model API ID", "model_type": "Altyapı", "add_btn": "Listeye Ekle",
        "reset_models": "Varsayılanlara Dön", "base_url": "Sunucu Adresi", "saved_models": "Kayıtlı Modeller",
        "turn_limit": "Konuşma Turu (Döngü Sayısı)",
        "round_info": "📊 TUR DURUMU",
        "lib_title": "📚 Ajan Kütüphanesi",
        "new_template": "Yeni Şablon Oluştur",
        "template_name": "Şablon İsmi",
        "role_desc": "Rol Tanımı",
        "default_model": "Varsayılan Model",
        "save_lib": "Kütüphaneye Kaydet",
        "saved": "Kaydedildi!",
        "missing_info": "Eksik bilgi",
        "manage_templates": "Şablonları Yönet",
        "export_sys": "💾 Sistemi Dışa Aktar",
        "export_desc": "Sistemi JSON olarak indir.",
        "download_json": "📥 İndir (JSON)",
        "appearance": "🎨 Görünüm & Dil",
        "add_from_lib": "📥 Kütüphaneden Ajan Ekle",
        "select_lib": "Kütüphaneden Seç:",
        "add_to_project": "Projeye Dahil Et",
        "added": "eklendi!",
        "lib_empty": "Kütüphaneniz boş.",
        "select_past": "Geçmişten Seç:",
        "active_team_title": "### 🛡️ Aktif Proje Ekibi (Private)",
        "active_team_desc": "Bu ajanlar sadece bu sohbet için geçerlidir.",
        "project_settings_header": "📂 Proje ve Ayarlar",
        "agent_panel": "🛡️ Ajan Yönetim Paneli",
        "system_data_header": "💾 Sistem ve Veri",
        "themes": {
            "Kızıl": "Kızıl", "Mavi": "Mavi", "Yesil": "Yeşil", 
            "Mor": "Mor", "Turuncu": "Turuncu", "Turkuaz": "Turkuaz"
        },
        "lock": "Paneli Kilitle",
        "help_title": "ℹ️ Kullanım Rehberi",
        "help_text": """
        **1. 🔑 API Erişimi:**
        En alttaki 'API Erişimi' panelinden OpenAI veya Google API anahtarınızı girin.
        
        **2. 🛡️ Ekip Kurulumu:**
        * **Kütüphane:** Sol menüden 'Ajan Kütüphanesi'ne gidip şablon oluşturun.
        * **Ekleme:** Ana ekrandan 'Kütüphaneden Ekle' veya 'Manuel Ekle' ile ekibi kurun.
        
        **3. 🎛️ Ayarlar:**
        * **Yaratıcılık:** 0.0 (Mantıksal) - 1.0 (Yaratıcı).
        * **Tur Sayısı:** Ajanların kaç döngü konuşacağını belirleyin.
        
        **4. 🚀 Başlat:**
        Konuyu yazın ve 'EKİBİ KUR VE BAŞLAT' butonuna basın.
        
        **5. 📤 Export:**
        Konuşma bitince 'Sistemi Dışa Aktar' ile yedeğinizi alabilirsiniz.
        """
    },
    "EN": {
        "login_header": "ORCHESTR.AI", "login_sub": "AI Team Orchestration",
        "username": "Username", "pass": "Password", "login_btn": "Login", "reg_btn": "Register",
        "login_title": "Login", "reg_title": "Register", "remember": "Remember Me",
        "new_chat": "New Team", "my_chats": "Projects", "settings": "System Settings",
        "api_access": "API Access", "start_btn": "SETUP & START TEAM", 
        "stop_task": "Stop Task", "stop_icon": "✖️",
        "logout": "Logout", "chat_input": "Enter task...", "feedback_label": "FEEDBACK:",
        "team_setup": "Team Setup", "add_agent": "Add Member", "name": "Name", "role": "Role", "model": "Model",
        "save": "Save", "delete": "Delete", "active_team": "Active Team",
        "attach": "Attach File", "file_help": "Upload PDF/TXT.",
        "upload_doc": "Upload Doc", "upload_img": "Upload Image",
        "theme_sel": "Accent Color", "bg_sel": "Background", "lang_sel": "Language",
        "creativity": "Creativity", "order": "Order",
        "auto": "Auto (Dynamic)", "seq": "Sequential", "active_project": "Active Project", "edit_title": "Edit Title",
        "admin_pass": "Admin Password", "lock": "Lock", "unlock": "Unlocked",
        "wrong_pass": "Wrong Password", "no_api": "No API Keys", "terminal": "Live Terminal", "working": "Working...",
        "our_team": "OUR TEAM", "previous_projects": "(Previous Projects)",
        "welcome": "Welcome",
        "import_title": "♻️ Import Agent", "import_btn": "Import", "no_past_agent": "No history found.",
        "model_mgmt": "Model Management", "add_model": "Add New Model", "model_label": "Display Name",
        "model_id": "Model API ID", "model_type": "Provider", "add_btn": "Add to List",
        "reset_models": "Reset to Defaults", "base_url": "Base URL", "saved_models": "Saved Models",
        "turn_limit": "Conversation Turns (Cycles)",
        "round_info": "📊 ROUND STATUS",
        "lib_title": "📚 Agent Library",
        "new_template": "Create New Template",
        "template_name": "Template Name",
        "role_desc": "Role Description",
        "default_model": "Default Model",
        "save_lib": "Save to Library",
        "saved": "Saved!",
        "missing_info": "Missing information",
        "manage_templates": "Manage Templates",
        "export_sys": "💾 Export System",
        "export_desc": "Download system as JSON.",
        "download_json": "📥 Download (JSON)",
        "appearance": "🎨 Appearance & Language",
        "add_from_lib": "📥 Add Agent from Library",
        "select_lib": "Select from Library:",
        "add_to_project": "Add to Project",
        "added": "added!",
        "lib_empty": "Your library is empty.",
        "select_past": "Select from Past:",
        "active_team_title": "### 🛡️ Active Project Team (Private)",
        "active_team_desc": "These agents are specific to this chat only.",
        "project_settings_header": "📂 Project & Settings",
        "agent_panel": "🛡️ Agent Management Panel",
        "system_data_header": "💾 System & Data",
        "themes": {
            "Kızıl": "Red", "Mavi": "Blue", "Yesil": "Green", 
            "Mor": "Purple", "Turuncu": "Orange", "Turkuaz": "Turquoise"
        },
        "lock": "Lock Panel",
        "help_title": "ℹ️ User Guide",
        "help_text": """
        **1. 🔑 API Access:**
        Enter your OpenAI or Google API key from the 'API Access' panel at the bottom.
        
        **2. 🛡️ Team Setup:**
        * **Library:** Create templates in 'Agent Library' (Left sidebar).
        * **Add:** Build your team using 'Add from Library' or 'Manual Add' on the main screen.
        
        **3. 🎛️ Settings:**
        * **Creativity:** 0.0 (Logical) - 1.0 (Creative).
        * **Turns:** Determine how many cycles the agents will talk.
        
        **4. 🚀 Start:**
        Type your task and press 'SETUP & START TEAM'.
        
        **5. 📤 Export:**
        Backup your system using 'Export System' after the chat.
        """
    }
}