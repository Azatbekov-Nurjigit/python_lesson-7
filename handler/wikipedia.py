
from aiogram import types, Dispatcher

from youtube_search import YoutubeSearch as YT
import hashlib


def finder(text):
    return YT(text, max_results=10).to_dict()


async def inline_wiki_handler(query: types.InlineQuery):
    text = query.query or "echo"
    link = f"https://ru.wikipedia.org/wiki/{text}"
    articles = [types.InlineQueryResultArticle(
        id=hashlib.md5(text.encode()).hexdigest(),
        title="Wiki: ",
        url=link,
        input_message_content=types.InputMessageContent(
            message_text=f"Держи смотри\n\nhttps://ru.wikipedia.org/wiki/{text}"
        )
    )]
    await query.answer(articles, cache_time=60)



def register_handler_wikipedia(dp: Dispatcher):
    dp.register_message_handler(inline_wiki_handler)