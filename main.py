from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)

english_bot = ChatBot("umesh", storage_adapter="chatterbot.storage.SQLStorageAdapter", database_uri =  'sqlite:///database.sqlite3', logic_adapters = ['chatterbot.logic.BestMatch', 'chatterbot.logic.TimeLogicAdapter'])

trainer = ListTrainer(english_bot)
trainer.train(["Hello!", "I am umesh", "How are you", "I am fine", "What are you doing", "ur mum"])
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("chatterbot.corpus.english")


@app.route("/")

def home():
    return render_template("index.html")

@app.route("/get")

def getBotResponse():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5000)