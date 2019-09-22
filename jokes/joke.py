import requests
import json

def jokeapi():
    url = "https://api.chucknorris.io/jokes/random"
    content = requests.get(url)
    return (content.json()['value'])
def jokeapi2():
    url="https://official-joke-api.appspot.com/random_joke"
    content=requests.get(url)
    str_gap = """





    """
    stringcontent=content.json()['setup']+str_gap+content.json()['punchline']
    return stringcontent

