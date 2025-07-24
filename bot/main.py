import asyncio
import logging
from aiogram import Bot, Dispatcher

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    logger.info("Бот запущен!")
    # Временно просто ждем
    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())