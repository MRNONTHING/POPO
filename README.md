# Popo GIF Bot (@popoco_bot)

> An inline Telegram bot designed to manage, categorize, and serve your GIF library based on usage frequency.

---

## Overview

Popo simplifies GIF management on Telegram. By leveraging Telegram's Inline Query API, Popo enables users to store their preferred GIFs and quickly retrieve them directly inside any chat window, automatically sorted by how frequently each GIF is sent.

---

## Key Features

- Smart Frequency Ranking: Automatically tracks and orders GIFs based on usage frequency.
- Inline Integration: Access saved GIFs instantly across any chat using @popoco_bot.
- Bulk Processing: Upload and index multiple GIFs simultaneously.
- Asynchronous Architecture: Built for low latency and fast query responses.

---

## Usage Guide

1. Start the bot by sending /start to @popoco_bot on Telegram.
2. Upload or forward the GIFs you want to store in your personal library.
3. Type @popoco_bot in any Telegram chat input field to access and select your GIFs.

---

## Tech Stack

- Language: Python 3.10+
- Framework: Telegram Bot API (Async/Await)
- Primary Feature: Telegram Inline Query Interface

---

## Installation and Setup

1. Clone the repository:
  
   git clone https://github.com/MRNONTHING/POPO.git
   cd POPO
   
2. Install the required dependencies:
  
   pip install -r requirements.txt
   
3. Set up environment variables in a .env file:
  
   BOT_TOKEN=your_telegram_bot_token_here
   
4. Run the application:
  
   python main.py
   
---

## License

This project is licensed under the MIT License.
