Create a chatbot with NLTK and YAML
===================================

The Python [Natural Language Toolkit](https://www.nltk.org/) (NLTK) has built-in chatbot functionality.

I find the default format for defining a chatbot a little intimidating though, so I created this so that you can define a chatbot with YAML.

Requirements
------------

It's Python2 for now.

You'll need to install the nltk and requests packages. If you have pip installed, try:

    pip install nltk requests

Example
-------

I've included an example chatbot to get you started. It's not very bright, but it may give you some ideas:

    python chat.py --file greetings.yaml

