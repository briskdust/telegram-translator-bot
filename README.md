# Telegram Translator Bot

This Telegram bot translates messages sent by users into a specified language using the DeepL API. Users can select the source and target languages for translation by using a command, and then any subsequent text they send will be translated according to these settings.

## Features

- **Language Selection**: Users can specify the source and target languages for translation.
- **Instant Translation**: Sends back the translated text immediately after a user sends a message.
- **Support for Multiple Languages**: Leverages DeepL API for high-quality translations across various languages.

## Prerequisites

Before you can run this project, you'll need:

- Python 3.8 or higher
- A Telegram Bot Token (obtained through BotFather on Telegram)
- A DeepL API Key (obtainable from DeepL's website)

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/briskdust/telegram-translator-bot.git
cd telegram-translator-bot
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory of the project and add your Telegram Bot Token and DeepL API Key:

```env
TELEGRAM_TOKEN=your_telegram_bot_token_here
DEEPL_API_KEY=your_deepl_api_key_here
```

4. Run the bot:

```bash
python3 main.py
```

Alternatively, you can use the provided `Dockerfile` to build and run the bot in a Docker container:

```bash
docker build -t telegram-translator-bot .
docker run -d --rm telegram-translator-bot
```

## Usage

- Start the bot in Telegram by sending `/start`.
- Set the source and target languages for translation by sending `/lang <SOURCE_LANG> -> <TARGET_LANG>`. For example, `/lang EN -> DE` to translate from English to German. If you want the bot to automatically detect the source language, use `AUTO` as the source language.
- Send any text message to the bot, and it will reply with the translated text.

## Dependencies

This project relies on the following Python packages:

- `python-telegram-bot` - For interacting with the Telegram Bot API
- `aiohttp` - For making asynchronous HTTP requests to the DeepL API
- `python-dotenv` - For loading environment variables from a `.env` file

Ensure all dependencies are installed by running `pip install -r requirements.txt`.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or create an issue for any bugs, feature requests, or improvements.

## License

This project is licensed under the MIT License
