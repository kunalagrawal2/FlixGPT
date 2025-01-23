from hugchat import hugchat
from hugchat.login import Login

EMAIL = "flix6975@gmail.com"
PASSWD = "Open!ProjectFlix123"
cookie_path_dir = "./cookies/"

def get_chatbot():
    sign = Login(EMAIL, PASSWD)
    cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)
    return hugchat.ChatBot(cookies=cookies.get_dict())

def get_chatbot_recommendation(query: str) -> str:
    chatbot = get_chatbot()
    movie_recommendation = 'Extract the key points from the sentence, in the form of tags for movies that can be identified in IMDB, only return the tags and nothing else '
    movie_recommendation += f'"{query}"'
    return chatbot.chat(movie_recommendation).text
