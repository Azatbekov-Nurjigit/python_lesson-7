from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from Keyboard import direction_markup,submit_markup,cancel_markup
from DSA.BZD import sql_command_insert
from coin import ADMIN

class FSMAdmin(StatesGroup):
    ID = State()
    name = State()
    direction = State()
    age = State()
    Group = State()
    submit = State()

async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        await FSMAdmin.ID.set()
        await message.answer(
            f"Привет {message.from_user.full_name} ",
            reply_markup=cancel_markup
        )

    else:
        await message.answer('Пиши в личку!')


async def load_ID(message: types.Message, state: FSMContext):
    async with state.proxy() as FSMCONTEXTPROXYSTORAGE:
        FSMCONTEXTPROXYSTORAGE['id'] = message.from_user.id
        if message.from_user.id in ADMIN:
            await FSMAdmin.next()
            await message.answer('Твое имя?',
                                 reply_markup=cancel_markup
                                 )
        else:
            await message.answer('ты не админ!!!')



async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as FSMCONTEXTPROXYSTORAGE:

        FSMCONTEXTPROXYSTORAGE['name'] = message.text
    await FSMAdmin.next()
    await message.answer('НАПРАВЛЕНИЕ?',reply_markup=direction_markup)


async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as FSMCONTEXTPROXYSTORAGE:
        FSMCONTEXTPROXYSTORAGE['direction'] = message.text
    await FSMAdmin.next()
    await message.answer('Сколько лет?')


async def load_age(message: types.Message, state: FSMContext):
    try:
        if not 14 < int(message.text) < 90:
            await message.answer(f'Доступ воспрещен!'
                                 'Повторить!!')
            await state.finish()
            return
        async with state.proxy() as FSMCONTEXTPROXYSTORAGE:
            FSMCONTEXTPROXYSTORAGE['age'] = int(message.text)
        await FSMAdmin.next()
        await message.answer('В какой группе?')
    except:
        await message.answer('Пиши числа!')

async def load_Group(message: types.Message, state: FSMContext):
    async with state.proxy() as FSMCONTEXTPROXYSTORAGE:
        FSMCONTEXTPROXYSTORAGE['Group'] = message.text
    await FSMAdmin.next()
    await message.answer('Эсли  завершено  то "ДА" '
                         'или повторить?',reply_markup=submit_markup)

async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":
        await sql_command_insert(state)
        await state.finish()
        await message.answer('Регистрация завершена')
    elif message.text.lower() == 'нет':
        await state.finish()
        await message.answer('Отменено')
    else:
        await message.answer('НИПОНЯЛ')

async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Отменено')

def register_handler_fsmAdminMentor(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_reg, Text(equals='cancel', ignore_case=True),
                                state='*')
    dp.register_message_handler(fsm_start, commands=['NACHAT'])
    dp.register_message_handler(load_ID, state=FSMAdmin.ID)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_Group, state=FSMAdmin.Group)
    dp.register_message_handler(submit, state=FSMAdmin.submit)


