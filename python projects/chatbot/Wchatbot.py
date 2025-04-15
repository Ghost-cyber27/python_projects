from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from cleaner import clean_corpus

CORPUS_FILE = "chat.txt"

chatbot = ChatBot("Ron Obvious")

trainer = ListTrainer(chatbot)
clean_corpus = clean_corpus(CORPUS_FILE)
trainer.train(clean_corpus)

exit_condition = ("quit", "exit", "q")
while True:
    query = input("> ")
    if query in exit_condition:
        break
    else:
        print(f"{chatbot.get_response(query)}")