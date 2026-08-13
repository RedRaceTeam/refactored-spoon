import logging
from aiogram import Bot, Dispatcher
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

from core.config import settings
from handlers.commands import router as commands_router
from handlers.business import router as business_router

logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()

dp.include_router(commands_router)
dp.include_router(business_router)

async def on_startup():
    await bot.set_webhook(
        url=f"{settings.WEBHOOK_URL}/webhook",
        secret_token=settings.WEBHOOK_SECRET
    )
    logging.info(f"✅ Webhook set to {settings.WEBHOOK_URL}/webhook")

async def handle_root(request):
    return web.Response(text="Piar Bot is running")

def main():
    app = web.Application()
    app.router.add_get('/', handle_root)
    
    SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
        secret_token=settings.WEBHOOK_SECRET
    ).register(app, path='/webhook')
    
    setup_application(app, dp, bot=bot)
    web.run_app(app, host="0.0.0.0", port=settings.PORT)

if __name__ == "__main__":
    main()
