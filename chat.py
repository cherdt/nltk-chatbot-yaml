import argparse
import nltk.chat
from nltk.chat.util import Chat, reflections
import requests
import yaml

def get_chatbot_source_from_file(filepath):
    try:
        with open(filepath) as f:
            chatbot_src = f.read()
    except:
        print("ERROR: unable to open " + filepath)
        exit(1)
    return chatbot_src

def get_chatbot_source_from_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        print("ERROR: unable to open " + url)
        exit(1)
    return r.text

def main():

    # create arg parser
    parser = argparse.ArgumentParser(description='Talk with a chatbot.')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-f', '--file', dest='file', help='YAML file with chatbot source')
    group.add_argument('-u', '--url', dest='url', help='URL of a chatbot source file')

    args = parser.parse_args()

    if args.file:
        chatbot_src = get_chatbot_source_from_file(args.file)
    if args.url:
        chatbot_src = get_chatbot_source_from_url(args.url)

    # load the source file
    try:
        chatbot = yaml.load(chatbot_src)
    except:
        print("ERROR: unable to parse YAML")
        exit(1)

    # Convert source into Chat-compatible list-of-pairs
    pairs = []
    try:
        for pair in chatbot:
            pairs.append((pair["match"], pair["replies"]))
    except:
        print("ERROR: missing match or replies")
        exit(1)

    # Create the bot
    try:
        bot = Chat(pairs, reflections)
    except:
        print("ERROR: something went wrong, blame Chris")
        exit(1)

    # print header, instructions
    print("\n")
    print("You're online with a chatbot!")
    print("When you're done chatting, just type 'exit' or 'quit'")
    print("\n")

    # User input loop
    user_input = "intro"
    while user_input != "exit" and user_input != "quit":
        user_input = raw_input(bot.respond(user_input) + '\n> ')

if __name__ == '__main__':
    main()
