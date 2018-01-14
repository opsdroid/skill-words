# opsdroid skill words

A skill for [opsdroid](https://github.com/opsdroid/opsdroid) that uses the NLTK module to play with words.

## Requirements

NLTK module + NLTK data

To download NLTK data you can type in the command line the following:
```
python -m nltk.downloader all
```

[Read more](http://www.nltk.org/data.html) on the official NLTK site.

## Configuration

None.

## Usage

#### `help scrabble: <letters> <board letter>`

Opsdroid will help you in scrabble. Just type your unused letters followed by one board letter and opsdroid will give you words that you can use.

> user: help scrabble: igetadl e
>
> opsdroid: Please give me a second, I'm thinking...
>
> opsdroid: Hmm... How about: ['gaited', 'aiglet', 'detail', 'taigle', 'ligate']

Opsdroid will choose words that are at least 4 letters long. If no combination is possible Opsdroid will let you know.

> user: help scrabble: aeiouff f
>
> opsdroid: Please give me a second, I'm thinking...
>
> opsdroid: Sorry, I can't help you with these letters, you better replace some.

#### `define: <term>`

Opsdroid will give you the meaning of a word and how you can use it in a sentence.

> user: define: car
>
> opsdroid: 
> Definition of the word 'car': a motor vehicle with four wheels; usually propelled by an internal combustion engine 
> Synonyms: ['car', 'auto', 'automobile', 'machine', 'motorcar'] 
> You can use this word like such: ['he needs a car to get to work']

#### `translate: <term> from: <language> to: <language>`

Opsdroid will translate a word from a language into another language.

> user: translate: dog from: english to: portuguese
>
> opsdroid: The english word 'dog' in portuguese is: cão, cachorro

**Note:**

NLTK saves the different languages to translate a word into a tuple.  To get the translation from _language 1_ to _language 2_ a list is passed and NLTK builds a list containing a two element tuple that looks like this:

`(<lang 1 term>, <lang 2 term>)`

In some languages, there are different ways to name the same thing so the tuple will contain both terms. 

_example: 'dog' in Portuguese can be translated to: 'cão, cachorro'_

So when you try to translate the word 'dog' from English to Portuguese, you will get the right results. But if you try to translate 'cão' to English, no result will show because both terms are being stored in the dictionary.

If Opsdroid keeps complaining that it couldn't find a translation for that word, the reason for that, is that, there are more than one word stored in the dictionary.
