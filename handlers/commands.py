from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from core.config import settings

router = Router()

bot_active = True
stats = {"processed": 0}

def admin_panel():
    markup = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="🟢 Статус", callback_data="status"),
            InlineKeyboardButton(text="⏹ Вкл/Выкл", callback_data="toggle")
        ],
        [
            InlineKeyboardButton(text="🧪 Тест", callback_data="test"),
            InlineKeyboardButton(text="📊 Статистика", callback_data="stats")
        ]
    ])
    return markup

@router.message(Command("start"))
async def start(message: types.Message):
    if message.from_user.id != settings.ADMIN_ID:
        await message.answer("Этот бот только для админа.")
        return
    await message.answer(
        "🤖 **Панель управления пиар-ботом**\n\nВыбери действие:",
        reply_markup=admin_panel(),
        parse_mode="Markdown"
    )

@router.callback_query()
async def admin_callback(call: types.CallbackQuery):
    global bot_active, stats

    if call.from_user.id != settings.ADMIN_ID:
        await call.answer("Недостаточно прав", show_alert=True)
        return

    if call.data == "status":
        status = "✅ Активен" if bot_active else "⛔ Выключен"
        await call.message.edit_text(
            f"**Статус бота:** {status}",
            reply_markup=admin_panel(),
            parse_mode="Markdown"
        )
        await call.answer()

    elif call.data == "toggle":
        bot_active = not bot_active
        status = "включён" if bot_active else "выключен"
        await call.message.edit_text(
            f"🔄 Бот {status}.",
            reply_markup=admin_panel()
        )
        await call.answer()

    elif call.data == "test":
        await call.message.edit_text(
            "🧪 Тест: бот работает.",
            reply_markup=admin_panel()
        )
        await call.answer()

    elif call.data == "stats":
        await call.message.edit_text(
            f"📊 **Статистика**\n\nОбработано сообщений: {stats['processed']}",
            reply_markup=admin_panel(),
            parse_mode="Markdown"
        )
        await call.answer()
