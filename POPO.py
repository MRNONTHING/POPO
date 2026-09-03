import sqlite3
from pyrogram import Client, filters
from pyrogram.types import (
    InlineQuery,
    InlineQueryResultCachedAnimation,
    ChosenInlineResult
)
import config

app = Client(
    "popo_session",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

def init_database():
    conn = sqlite3.connect("gifs.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS gifs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            file_id TEXT NOT NULL,
            use_count INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

init_database()

def save_gif(user_id: int, file_id: str) -> int:
    conn = sqlite3.connect("gifs.db")
    cursor = conn.cursor()
    cursor.execute('INSERT INTO gifs (user_id, file_id, use_count) VALUES (?, ?, 0)', (user_id, file_id))
    new_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return new_id

def get_sorted_gifs(user_id: int):
    conn = sqlite3.connect("gifs.db")
    cursor = conn.cursor()
    cursor.execute('SELECT id, file_id FROM gifs WHERE user_id = ? ORDER BY use_count DESC', (user_id,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def increment_use_count(gif_id: int):
    conn = sqlite3.connect("gifs.db")
    cursor = conn.cursor()
    cursor.execute('UPDATE gifs SET use_count = use_count + 1 WHERE id = ?', (gif_id,))
    conn.commit()
    conn.close()

@app.on_message(filters.command("start"))
async def start_cmd(client, message):
    await message.reply_text("Hello! POPO GIF Bot is ready 🚀\nSend me any GIF to save it.")

@app.on_message(filters.private & filters.animation)
async def receive_gif(client, message):
    file_id = message.animation.file_id
    user_id = message.from_user.id
    gif_num = save_gif(user_id, file_id)
    await message.reply_text(f"Your gif successfully saved!\nNumber of the gif is: {gif_num}")

@app.on_inline_query()
async def handle_inline_query(client, inline_query: InlineQuery):
    user_id = inline_query.from_user.id
    gifs = get_sorted_gifs(user_id)
    results = []
    
    for gif_id, file_id in gifs:
        results.append(
            InlineQueryResultCachedAnimation(
                id=str(gif_id),
                animation_file_id=file_id
            )
        )
    
    await inline_query.answer(results, cache_time=0, is_personal=True)

@app.on_chosen_inline_result()
async def handle_chosen_result(client, chosen_result: ChosenInlineResult):
    clicked_id = int(chosen_result.result_id)
    increment_use_count(clicked_id)

if __name__ == "__main__":
    print("POPO Bot is running...")
    app.run()