import argparse
import nltk.chat
from nltk.chat.util import Chat, reflections
import yaml


def main():

    # create arg parser
    parser = argparse.ArgumentParser(description='Talk with a chatbot.')
    parser.add_argument('-f', '--file', dest="file", help='YAML file with chatbot source')
    args = parser.parse_args()

    # open the source file
    try:
        with open(args.file) as f:
            chatbot_src = f.read()
    except:
        print("ERROR: unable to open " + args.file)
        exit(1)

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
