from telegram import Update, ext
import os
from dotenv import load_dotenv
import aiohttp
import json

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
DEEPL_API_KEY = os.getenv('DEEPL_API_KEY')

# default language settings
default_lang = {"source_lang": "auto", "target_lang": "EN"}

user_lang_settings = {}


async def start(update: Update, context: ext.CallbackContext) -> None:
    await update.message.reply_text('Hello! Send me a message, and I will translate it. Use /lang source_lang -> '
                                    'target_lang to set languages.')


async def set_lang(update: Update, context: ext.CallbackContext) -> None:
    chat_id = update.message.chat_id
    try:
        args = context.args
        source_lang, target_lang = ' '.join(args).split('->')
        source_lang = source_lang.strip().upper()
        target_lang = target_lang.strip().upper()
        user_lang_settings[chat_id] = {"source_lang": source_lang, "target_lang": target_lang}
        await update.message.reply_text(f'Language settings updated: {source_lang} -> {target_lang}')
    except Exception as e:
        await update.message.reply_text('Usage: /lang <Cur> -> <Target>\nExample: /lang EN -> DE')


async def translate_text(text: str, chat_id: int) -> str:
    if chat_id in user_lang_settings:
        source_lang = user_lang_settings[chat_id]["source_lang"]
        target_lang = user_lang_settings[chat_id]["target_lang"]
    else:
        source_lang = default_lang["source_lang"]
        target_lang = default_lang["target_lang"]

    url = "https://api-free.deepl.com/v2/translate"
    headers = {
        "Authorization": f"DeepL-Auth-Key {DEEPL_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "text": [text],
        "source_lang": source_lang,
        "target_lang": target_lang
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=json.dumps(payload)) as response:
            if response.status == 200:
                result = await response.json()
                return result['translations'][0]['text']
            else:
                print(f"Error: {response.status}: {response.reason}")
                return "Sorry, I couldn't translate your text."


async def handle_message(update: Update, context: ext.CallbackContext) -> None:
    original_text = update.message.text
    chat_id = update.message.chat_id
    translated_text = await translate_text(original_text,
                                           chat_id)  # Make sure translate_text is an async function or called correctly
    await update.message.reply_text(translated_text)


def main() -> None:
    application = ext.Application.builder().token(TELEGRAM_TOKEN).build()

    application.add_handler(ext.CommandHandler("start", start))
    application.add_handler(ext.CommandHandler("lang", set_lang))
    application.add_handler(ext.MessageHandler(ext.filters.TEXT & ~ext.filters.COMMAND, handle_message))

    application.run_polling()


if __name__ == '__main__':
    main()
