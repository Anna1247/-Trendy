import logging
import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

API_TOKEN = '7561490504:AAG76Hia5ZltDVaIZz5MXtJhnwWgwIa4X7Y'
MANAGER_ID = 5119450021
MEDIA_PATH = './media'


logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class RegistrationForm(StatesGroup):
    name = State()
    phone = State()
    messenger = State()

# ==============================
# 🎬 Анимированная приветственная Trendi + Главное меню
# ==============================

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    try:
        with open(os.path.join(MEDIA_PATH, "trendi_welcome_animation.mp4"), "rb") as video:
            await message.answer_video(video)
    except FileNotFoundError:
        await message.answer("👋 Анімація тимчасово відсутня.")

    text = "👋 Привіт! Я — Trendi, твоя гідка у школі краси NEW TREND 💖\n\nОбирай розділ нижче:"
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
    InlineKeyboardButton("📚 Про школу", callback_data="about_school"),
        InlineKeyboardButton("📑 Курси", callback_data="programs"),
        InlineKeyboardButton("🗓️ Розклад", callback_data="schedule"),
        InlineKeyboardButton("📞 Контакти", callback_data="contacts"),
        InlineKeyboardButton("💳 Передоплата", callback_data="prepayment"),
        InlineKeyboardButton("❓ FAQ", callback_data="faq"),
        InlineKeyboardButton("📝 Подати заявку", callback_data="registration"),
        InlineKeyboardButton("📋 Реєстрація", callback_data="registration_form"),
        InlineKeyboardButton("🏢 Франшиза для салонів", callback_data="franchise")
    )
    await message.answer(text, reply_markup=keyboard)


 # ==============================
# 🔧 Дополнительные кнопки для возврата в меню
# ==============================

def back_to_main_menu():
    return InlineKeyboardMarkup().add(
        InlineKeyboardButton("🔙 Назад", callback_data="start")
    )

def back_to_about_school():
    return InlineKeyboardMarkup().add(
        InlineKeyboardButton("🔙 Назад", callback_data="about_school"),
        InlineKeyboardButton("🏠 В початок", callback_data="start")
    )

# ==============================
# 📚 Блок: Про курси та школу (добавленный)
# ==============================
# ==============================
# 📚 Блок: Про курси та школу
# ==============================
@dp.callback_query_handler(lambda c: c.data == 'about_school')
async def about_school(callback: types.CallbackQuery):
    try:
        with open(os.path.join(MEDIA_PATH, "logo.jpg"), "rb") as logo:
            await callback.message.answer_photo(logo)
    except FileNotFoundError:
        pass
        
    text = "📚 Дозволь розповісти тобі більше про нашу школу краси NEW TREND — місце, де народжуються справжні професіонали!"
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton("📖 Історія школи", callback_data="school_history"),
        InlineKeyboardButton("🎓 Наші переваги", callback_data="advantages"),
        InlineKeyboardButton("👩‍🏫 Наші викладачі", callback_data="teachers"),
        InlineKeyboardButton("🌍 Формати навчання", callback_data="formats"),
        InlineKeyboardButton("🔙 Назад", callback_data="start")
    )
    await callback.message.answer(text, reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data == 'school_history')
async def school_history(callback: types.CallbackQuery):
    try:
        with open(os.path.join(MEDIA_PATH, "school_history.png"), "rb") as photo:
            await callback.message.answer_photo(photo)
    except FileNotFoundError:
        await callback.message.answer("Фото тимчасово відсутнє.")

    text = (
        "📖 Історія школи NEW TREND\n\n"
        "✨ Засновниця школи — Світлана Попова — працює в б’юті-сфері з 2011 року.\n"
        "За цей час вона пройшла шлях від майстра до тренера, спікера, розробника авторських програм і творця власної академії.\n"
        "✨ У 2013 році була створена перша студія Lash&Brow Stylist у Запоріжжі.\n"
        "✨ У 2015 році запущена власна лінійка матеріалів та аксесуарів для майстрів.\n"
        "✨ Світлана — багаторазовий призер чемпіонатів, міжнародний суддя, спікер та лауреат премії Lash Empress.\n"
        "✨ Створено понад 10 авторських програм навчання, підготовлено понад 1000 учнів.\n"
        "✨ У 2018 році школа отримала зареєстрований торговий знак, дипломи видаються з голограмою."
    )
    await callback.message.answer(text, reply_markup=back_to_about_school())


@dp.callback_query_handler(lambda c: c.data == 'advantages')
async def advantages(callback: types.CallbackQuery):
    text = (
        "🎓 Наші переваги:\n\n"
        "✅ Авторські технології формування пучків\n"
        "✅ Методика “2 майстри – 1 клієнт” — прискорене нарощування\n"
        "✅ Онлайн та офлайн формати навчання\n"
        "✅ Індивідуальне наставництво та підтримка після навчання\n"
        "✅ Франшиза та готові бізнес-рішення для салонів\n"
        "✅ Супровід та кураторство кожного студента"
    )
    await callback.message.answer(text, reply_markup=back_to_about_school())


@dp.callback_query_handler(lambda c: c.data == 'teachers')
async def teachers(callback: types.CallbackQuery):
    try:
        with open(os.path.join(MEDIA_PATH, "teacher.png"), "rb") as photo:
            await callback.message.answer_photo(photo)
    except FileNotFoundError:
        await callback.message.answer("📸 Фото викладача тимчасово відсутнє.")

    text = "👩‍🏫 Наші викладачі:\n\nСвітлана Попова — засновниця, тренер, міжнародний спікер з 12-річним досвідом."
    await callback.message.answer(text, reply_markup=back_to_about_school())

@dp.callback_query_handler(lambda c: c.data == 'formats')
async def formats(callback: types.CallbackQuery):
    text = (
        "🌍 Формати навчання:\n\n"
        "🔸 Міні-групи (до 2 осіб)\n"
        "🔸 Індивідуальне навчання\n"
        "🔸 Онлайн з підтримкою куратора"
    )
    await callback.message.answer(text, reply_markup=back_to_about_school())

# ==============================
# 📑 Блок: Навчальні програми
# ==============================
@dp.callback_query_handler(lambda c: c.data == 'programs')
async def programs(callback: types.CallbackQuery):
    text = (
        "✨ Навчальні програми:\n\n"
        "Базові (для початківця):\n"
        "✅ [Нарощення вій](https://sites.google.com/view/lashbrowstylist/%D0%BD%D0%B0%D0%B2%D1%87%D0%B0%D0%BD%D0%BD%D1%8F/offline/%D0%B2%D1%96%D1%97-%D0%B1%D0%B0%D0%B7%D0%B0)\n"
        "✅ [Ламінування вій і брів](https://sites.google.com/view/lashbrowstylist/%D0%BD%D0%B0%D0%B2%D1%87%D0%B0%D0%BD%D0%BD%D1%8F/offline/%D0%B1%D1%80%D0%BE%D0%B2%D0%B8/%D0%BE%D1%84%D0%BE%D1%80%D0%BC%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B1%D1%80%D0%BE%D0%B2%D0%B5%D0%B9)\n\n"
        "Підвищення кваліфікації:\n"
        "▶️ [Нарощення вій](https://sites.google.com/view/lashbrowstylist/навчання/offline/вії-підвищення?fbclid=PAQ0xDSwK5dRhleHRuA2FlbQIxMQABp-YuB-W6aIbv8BMM8eTk5e0aUYS5cAbDIWKubHThiBWOARxp_JaJpdjp83rI_aem_OYbf3od68vZl6PWXTOqeWQ)"
    )
    await callback.message.answer(text, parse_mode="Markdown", reply_markup=back_to_main_menu())

# ==============================
# 📅 Блок: Розклад з посиланням та фото
# ==============================
@dp.callback_query_handler(lambda c: c.data == 'schedule')
async def schedule(callback: types.CallbackQuery):
    text = (
        "📅 Розклад:\n\n"
        "👉 [Переглянути актуальний розклад базового курсу Нарощення вій](https://sites.google.com/view/lashbrowstylist/%D0%BD%D0%B0%D0%B2%D1%87%D0%B0%D0%BD%D0%BD%D1%8F/offline/%D0%B2%D1%96%D1%97-%D0%B1%D0%B0%D0%B7%D0%B0)"
    )
    await callback.message.answer(text, parse_mode="Markdown")
    try:
        with open(os.path.join(MEDIA_PATH, "schedule_4days.jpg"), "rb") as photo1:
            await callback.message.answer_photo(photo1)
        with open(os.path.join(MEDIA_PATH, "schedule_2days.jpg"), "rb") as photo2:
            await callback.message.answer_photo(photo2)
    except FileNotFoundError:
        await callback.message.answer("📸 Фото розкладу тимчасово відсутнє.")
    await callback.message.answer("Повернутись в головне меню:", reply_markup=back_to_main_menu())

# ==============================
# ☎️ Блок: Контакти
# ==============================
@dp.callback_query_handler(lambda c: c.data == 'contacts')
async def contacts(callback: types.CallbackQuery):
    text = (
        "📞 Контакти:\n\n"
        "Instagram: [@lash.brow.stylist](https://www.instagram.com/lash.brow.stylist/)\n"
        "What’s app: https://wa.me/48887806873\n"
        "Телеграмм: +48 887 806 873\n"
        "Сайт: https://sites.google.com/view/lashbrowstylist/"
    )
    await callback.message.answer(text, parse_mode="Markdown", reply_markup=back_to_main_menu())

# ==============================
# 💳 Блок: Передоплата
# ==============================
@dp.callback_query_handler(lambda c: c.data == 'prepayment')
async def prepayment(callback: types.CallbackQuery):
    text = (
        "💳 Передоплата:\n\n"
        "👩‍🏫 Отримувач: Lash Brow Stylist Svitlana Popova\n"
        "🏦 Номер рахунку: 40102024010000010206489480\n"
        "📝 Призначення платежу: ZA SZKOLENIA\n"
        "💰 Сума: 500 PLN\n"
        "⚠ Оплата протягом 2-3 днів після реєстрації."
    )
    await callback.message.answer(text, reply_markup=back_to_main_menu())

# ==============================
# 📑 Блок: FAQ (Рабочая кнопка FAQ с фото)
# ==============================
@dp.callback_query_handler(lambda c: c.data == 'faq')
async def faq(callback: types.CallbackQuery):
    try:
        with open(os.path.join(MEDIA_PATH, "certificate_photo.jpg"), "rb") as photo:
            await callback.message.answer_photo(photo)
    except FileNotFoundError:
        await callback.message.answer("📸 Фото сертифіката тимчасово відсутнє.")

    text = (
        "📌 *Часті запитання та відповіді*\n\n"

        "1️⃣ *Сертифікат*\n"
        "🔸 Чи видаєте Ви сертифікат?\n"
        "🔹 Так, по закінченню курсу видається іменний Диплом з печаткою та голограмою.\n\n"

        "2️⃣ *Оплата*\n"
        "🔸 Як проходить оплата на курс?\n"
        "🔹 Передоплата — для бронювання місця. Решту суми — оплата на місці.\n\n"

        "3️⃣ *Локація*\n"
        "🔸 Де проходить очне навчання?\n"
        "🔹 Польща, м. Катовіце, студія — 8 хвилин від залізничного вокзалу.\n\n"

        "4️⃣ *Що взяти з собою?*\n"
        "🔸 Що брати із собою на курс?\n"
        "🔹 Ми надаємо всі матеріали. З собою — перекус, змінне взуття у холодну пору.\n\n"

        "5️⃣ *Тривалість навчання*\n"
        "🔸 Скільки триває навчання?\n"
        "🔹 2 дні (вихідні) або 4 дні (будні).\n\n"

        "6️⃣ *Скільки моделей потрібно?*\n"
        "🔸 Чи потрібні моделі?\n"
        "🔹 Ми допомагаємо з підбором моделей, але можна запросити свою.\n\n"

        "7️⃣ *Післякурсовий супровід*\n"
        "🔸 Чи буде підтримка після курсу?\n"
        "🔹 Так. Ви отримаєте доступ до закритого чату та консультації куратора."
    )

    await callback.message.answer(text, parse_mode="Markdown", reply_markup=back_to_main_menu())



# ==============================
# 📝 Блок: Подати заявку (FSM)
# ==============================
@dp.callback_query_handler(lambda c: c.data == 'registration')
async def registration(callback: types.CallbackQuery):
    await callback.message.answer("📝 Введіть ваше ім'я:")
    await RegistrationForm.name.set()

@dp.message_handler(state=RegistrationForm.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("📞 Введіть номер телефону:")
    await RegistrationForm.phone.set()

@dp.message_handler(state=RegistrationForm.phone)
async def process_phone(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("💬 Оберіть зручний месенджер (Telegram / WhatsApp):")
    await RegistrationForm.messenger.set()

@dp.message_handler(state=RegistrationForm.messenger)
async def process_messenger(message: types.Message, state: FSMContext):
    await state.update_data(messenger=message.text)
    data = await state.get_data()

    user_data = (
        f"📝 Нова заявка:\n\n"
        f"👤 Ім'я: {data['name']}\n"
        f"📞 Телефон: {data['phone']}\n"
        f"💬 Месенджер: {data['messenger']}\n"
        f"🔗 @{message.from_user.username or 'немає'} (ID: {message.from_user.id})"
    )

    await bot.send_message(MANAGER_ID, user_data)
    await message.answer("✨ Дякуємо! Ваша заявка прийнята. Менеджер зв'яжеться з вами найближчим часом 💖")
    await state.finish()

# ==============================
# 📝 Блок: Реєстрація через Google Форму
# ==============================
@dp.callback_query_handler(lambda c: c.data == 'registration')
async def registration(callback: types.CallbackQuery):
    text = (
        "📝 Реєстрація на навчання:\n\n"
        "Для запису зв'яжіться з менеджером або скористайтеся формою нижче."
    )
    await callback.message.answer(text, parse_mode="Markdown", reply_markup=back_to_main_menu())

@dp.callback_query_handler(lambda c: c.data == 'registration_form')
async def registration_form(callback: types.CallbackQuery):
    text = (
        "📋 Реєстрація через форму:\n\n"
        "👉 [Перейти до форми реєстрації](https://forms.gle/FeKG4DXETt5S2Xd88)"
    )
    await callback.message.answer(text, parse_mode="Markdown", reply_markup=back_to_main_menu())

# ==============================
# 📦 Блок: Франшиза для салонів
# ==============================
@dp.callback_query_handler(lambda c: c.data == 'franchise')
async def franchise(callback: types.CallbackQuery):
    text = (
        "🏢 *Франшиза NEW TREND* — це готова бізнес-система:\n\n"
        "✅ Стандартизовані технології\n"
        "✅ Навчання персоналу\n"
        "✅ Підтримка на всіх етапах розвитку\n"
        "✅ Збільшення прибутку салону\n"
        "✅ Економія часу та матеріалів\n\n"
        "🎓 *Онлайн-платформа входить у франшизу для навчання персоналу.*"
    )
    
    # Сначала отправляем текст с описанием
    await callback.message.answer(text, parse_mode="Markdown")
    
    # Затем отправляем фото платформы
    try:
        with open(os.path.join(MEDIA_PATH, "franchise_platform.jpg"), "rb") as photo:
            await callback.message.answer_photo(photo, caption="📲 Навчальна платформа NEW TREND")
    except FileNotFoundError:
        await callback.message.answer("📸 Фото платформи тимчасово недоступне.")
    
    # После фото — отправляем кнопки
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton("📞 Більше інформації", url="https://sites.google.com/view/lashstylistnewtrend/%D0%B3%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0-%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0"),
        InlineKeyboardButton("🔙 Назад", callback_data="start")
    )
    await callback.message.answer("⬇️ Оберіть дію:", reply_markup=keyboard)


# ==============================
# 🔄 Блок: Возврат в главное меню (по кнопке назад)
# ==============================
@dp.callback_query_handler(lambda c: c.data == 'start')
async def back_to_main(callback: types.CallbackQuery):
    await cmd_start(callback.message)

# ==============================
# 🔚 Запуск бота
# ==============================
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)






