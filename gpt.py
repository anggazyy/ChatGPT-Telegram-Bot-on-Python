import os
import openai # pip install openai
from aiogram import Bot, Dispatcher, executor, types # pip install aiogram



openai.api_key = "api_key"  
bot = Bot(token='token_Bot')
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!")




@dp.message_handler()
async def gpt(message: types.Message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.5,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    await message.reply(response.choices[0].text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
