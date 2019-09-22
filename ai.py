import eliza as liz
import howtodo.hdi as htd
import wiki.simplewiki as ws
import summy.summarize as sumz
import nltk
import botogram
import jokes.joke as j
import random
import botogram

bot = botogram.create("YOUR-API-KEY-HERE")
bot.about = """Liza :-)
            I am a simple bot, My responses are severely limited and are mostly nonsensical.
            Anything other than command shall be taken by chat engine.
            I apologize in advance if my responses are rude. 
            Commands: 
            liz summarise <url>,
            liz please summarise <url>,
            liz how to <query>,
            liz what is <query>,
            liz tell me about yourself,
            liz about you creator,
            liz your code,
            liz tell me a joke
            """

bot.owner = "@airplaneblahblah"
@bot.command("start")
def gettingstarted(chat,message,args):
    chat.send("Whooa a new user!")
    chat.send("Hi I am liza :D, type /help for a bit intro")

@bot.command("help")
def gettinghelp(chat,message,args):
    chat.send(bot.about)


def getSummary(query):
    print("getting summary")
    print("Okay ^_^ lemme see")
    argument = query
    print(argument)
    response = sumz.summarize(argument)
    response.replace("\n\n","")
    return response

def getHdi(query):
    print("Finding for you :-)")
    solution = htd.solve_query(query)
    return solution

def getDefinition(query):
    print("---->",query)
    print("Lemme wiki it for you")
    solution =  ws.retrieve(query)
    return solution

def getAboutme():
    print("I am a simple bot made up of tonnes of if else statements and stuffs. My creator is a not a genius but still he made me. I am not automatically learning type of model. Akuma sama chose to name me Liza because I am derived from eliza senpai.... \n please donot be rude with me cuz it will make mew sad UwU")


def getAboutakuma():
    output = "I love Aeres senpai.He is my god,teacher or whatever. I exist because of him and he worked hard on his birthday to create me. I am forever greatful to him and I love him UwU"
    return output

def yourSourceCode():
    output = "My source is not anywhere else other than Akuma sama's laptop. Ask him personally please"
    return output

def getJokes():
    n = random.randint(0,965)
    if(n%2):
        output=j.jokeapi()
    else:
        output=j.jokeapi2()
    return output

liza = liz.eliza()
commands = ["liz summarise ",
            "liz please summarise",
            "liz how to",
            "liz what is",
            "liz tell me about yourself",
            "liz about you creator",
            "liz your code",
            "liz tell me a joke"
           ]
debug = False
reply = ""

@bot.process_message
def process_message(chat,message):
    tmp = message.text.lower()
    user_input = message.text
    print("-->", tmp)
    if "liz" in tmp:
        if "summarise" in tmp:              #summarize
            query = user_input.split("summarise")[1]
            solution = getSummary(query)
            print("sent to function")
            print(">>",solution)
            chat.send(solution)

        elif "how to" in user_input:              #how to
            answer=getHdi(tmp.split("to")[1])
            print(">>", answer)
            chat.send(answer)

        elif "what is" in tmp or "define" in tmp:              #what is
            answer = getDefinition(tmp.split("is")[1])
            print(">>",answer)
            chat.send(answer)

        elif "about yourself" in user_input:
            answer=getAboutme()
            chat.send(answer)

        elif "your creator" in user_input:
            print("Whoa")
            details = getAboutakuma()
            print(">>",details)
            chat.send(details)

        elif tmp == commands[6]:
           response = yourSourceCode()
           print(">>",response)
           chat.send(response)

        elif tmp == commands[7]:
            solution=getJokes()
            print(">>",solution)
            chat.send(solution)

        else:
           reply = liza.respond(tmp)
           print(">>",reply)
           chat.send(reply)

    else:
        reply = liza.respond(tmp)
        print(">>",reply)
        chat.send(reply)


if __name__ == "__main__":
    bot.run()






