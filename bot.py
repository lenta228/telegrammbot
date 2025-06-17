import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Настройка логгирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Токен вашего бота
TOKEN = "7431943285:AAEsgkQ0Bu00kV6eWdsdJPqWsCkvjjk4w3U"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправляет сообщение при получении команды /start."""
    user = update.effective_user
    await update.message.reply_text(f"Привет, как дела?")

def main() -> None:
    """Запуск бота."""
    # Создаем Application и передаем токен бота
    application = Application.builder().token(TOKEN).build()

    # Добавляем обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Запускаем бота
    application.run_polling()

if __name__ == "__main__":
    main()