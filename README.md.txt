# 🍿 Popo GIF Bot (`@popoco_bot`)

> **Your ultimate inline Telegram GIF manager. Organize, access, and share your favorite GIFs seamlessly anywhere on Telegram.**

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram-Bot%20API-26A5E4?style=flat-square&logo=telegram&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

✨ **Popo** is an intuitive Telegram bot designed to make GIF management effortless. Upload your media library once, and access your most frequently used GIFs instantly in any chat using Telegram’s **Inline Mode**.

---

### 🔥 Key Features

- **📊 Smart Usage Sorting:** Popo automatically tracks and ranks your uploaded GIFs based on how often you send them.
- **⚡ Seamless Inline Integration:** Call `@popoco_bot` in any individual chat or group to access your saved GIFs instantly—no switching windows needed.
- **📂 Bulk Upload Support:** Send as many GIFs as you want in one session; Popo indexes them on the fly.
- **🚀 High Performance:** Async architecture designed for low-latency media indexing and fast querying.

---

### 🕹 How It Works

1. **Start the Bot:** Send `/start` to [@popoco_bot](https://t.me/popoco_bot) on Telegram.
2. **Upload Your GIFs:** Forward or upload any GIFs you want to save.
3. **Use Inline Anywhere:** Type `@popoco_bot` in any text input field to instantly trigger your personalized GIF drawer sorted by frequency of use.

---

### 🛠 Tech Stack

- **Language:** Python 3.10+
- **API Wrapper:** `aiogram` / `python-telegram-bot`
- **Core Feature:** Telegram Inline Query API

---

### 🚀 Quick Start

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/popo-gif-bot.git
   cd popo-gif-bot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up Environment Variables**
   Create a `.env` file in the root directory:
   ```env
   BOT_TOKEN=your_telegram_bot_token_here
   ```

4. **Launch the bot**
   ```bash
   python main.py
   ```

---

### 🌟 Support & Future Plans

If you find **Popo** useful, give this repository a ⭐ on GitHub!  
More open-source projects and Telegram utilities are in active development—stay tuned!

---

### 📝 License

This project is licensed under the MIT License.
