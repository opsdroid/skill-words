import nltk
from nltk.corpus import swadesh
from nltk.corpus import wordnet
from random import sample

from opsdroid.matchers import match_regex


@match_regex(r'help scrabble: (.*) (.*)', case_sensitive=False)
async def help_scrabble(opsdroid, config, message):
    """Opsdroid will help you with scrabble."""
    scrabble_letters = message.regex.group(1)
    board_letter = message.regex.group(2)
    puzzle_letters = nltk.FreqDist(scrabble_letters)
    wordlist = nltk.corpus.words.words()

    await message.respond("Please give me a second, I'm thinking...")

    words = [word for word in wordlist
             if len(word) >= 4
             and board_letter in word
             and nltk.FreqDist(word) <= puzzle_letters]

    if len(words) > 5:
        words = sample(words, 5)

    if not words:
        reply = "Sorry, I can't help you. You better replace some letters."
    else:
        reply = "Hmm... How about: {}".format(words)

    await message.respond(reply)


@match_regex(r'define: (.*)', case_sensitive=False)
async def define(opsdroid, config, message):
    word = message.regex.group(1)
    try:
        definition = wordnet.synset(word + '.n.01').definition()
        examples = wordnet.synset(word + '.n.01').examples()
        synonyms = wordnet.synset(word + '.n.01').lemma_names()
        await message.respond("Definition of the word '{}': {} \n"
                              "Synonyms: {} \n"
                              "You can use this word like such: {}".format(
                                word, definition,
                                str(synonyms).replace("_", " "), examples))

    except nltk.corpus.reader.wordnet.WordNetError:
        await message.respond("Sorry, I can't find anything about that word.")


@match_regex(r'translate: (.*) to: (.*)', case_sensitive=False)
async def translate(opsdroid, config, message):
    term = message.regex.group(1)
    language = message.regex.group(2)
    languages_dict = {'spanish': 'es', 'belorussian': 'be', 'bulgarian': 'bg',
                      'catalan': 'cs', 'czech': 'cs', 'german': 'de',
                      'english': 'en', 'french': 'fr', 'croatian': 'hr',
                      'italian': 'it', 'latin': 'la', 'macedonian': 'mk',
                      'dutch': 'nl', 'polish': 'pl', 'portuguese': 'pt',
                      'romanian': 'ro', 'russian': 'ru', 'slovak': 'sk',
                      'slovenian': 'sl', 'serbian': 'sr', 'ukrainian': 'uk'}

    _dictionary = dict(swadesh.entries(
        ['en', languages_dict.get(language, 'english')]))

    translation = _dictionary.get(term, "Sorry, I can't find the "
                                        "translation for that word :(")

    await message.respond("The word '{}' in {} is: {}".format(
        term, language, translation))
