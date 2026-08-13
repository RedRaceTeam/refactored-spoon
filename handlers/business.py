from aiogram import Router, types
from core.ai import get_ai_response
from handlers.commands import bot_active, stats

router = Router()

@router.message()
async def business_message(message: types.Message):
    if message.chat.type != "business":
        return
    if not message.text:
        return
    if not bot_active:
        return

    stats["processed"] += 1
    response = await get_ai_response(message.text)
    await message.answer(response)
