from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import dp
from data.constants import ALLOWED_USERS

from states.registration_state import RegistrationState

from data_fetcher.reg_data import registration

from data.functions import check_passwd


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    if message.from_user.id not in ALLOWED_USERS.values():
        await message.answer("Здравствуйте\nВам отказано в регистрации")
        return
    else:
        await message.answer(
            """Здравствуйте, ваш username будет использован в качестве лоигна для авторизации на сайте.\n
Введите пожалуйста пароль который будеть использоваться для входа в ваш аккаунт \n
Примечание: Пароль должен быть не меньше 8 символов и состоять только из букв или цифр."""
            )
        await RegistrationState.password.set()


@dp.message_handler(state=RegistrationState.password)
async def state_password(message: types.Message, state: FSMContext):
    """
    Валидация данных и регистрация.
    :param message:
    :param state:
    """
    login = message.from_user.username
    passwd = message.text

    if not await check_passwd(passwd=message.text):
        await message.answer("Пароль не соответствует требованиям, попробуйте еще раз")
        await RegistrationState.password.set()
        return

    if await registration(login, passwd) != 201:
        await message.answer("Вы уже зарегистрированы")
        return

    await message.answer("Регистрация прошла успешно")
    await message.answer(f"Ваш логин - ```{message.from_user.username}```\nВаш пароль - ```{message.text}```",
                         parse_mode="Markdown")

    await state.finish()
