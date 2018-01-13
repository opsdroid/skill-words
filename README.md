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

#### `translate: <term> to: <language>`

Opsdroid will translate a word in english into another language.

> user: translate: dog to: spanish
>
> opsdroid: The word 'dog' in spanish is: perro

