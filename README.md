# LibIndic Normalizer

LibIndic's normalizer module may be used to normalize the text to a canonical
format to handle inconsistencies in text. Apply normalization rules based on the language code. Right now, it supports Malayalam language only.

## Features

- Removes punctuations by default
- Changes combination chillus to atomic chillu  characters
- Normalization of vowel signs
- Corrects some common typos in Malayalam (needs thorough review)
- Alternate spelling normalizations

## Installation

### Directly from git

```
pip install git+https://github.com/libindic/normalizer.git
```

This is similar to doing the following:

1. Clone the repository `git clone https://github.com/libindic/normalizer.git`
2. Change to the cloned directory `cd normalizer`
3. Run setup.py to create installable source `python setup.py sdist`
3. Install using pip `pip install dist/libindic-normalizer*.tar.gz`

Note: Prefer using virtualenv for installation as the library is in experimental stage

## Usage
```
Input: Unicode text
Output: Normalized unicode text

>>> from libindic.normalizer import Normalizer
>>> normalizer = Normalizer("ml")
>>> result = normalizer.normalize('ദു:ഖത്തിന്റെ')
>>> print(result)
>> ദുഃഖത്തിന്റെ
>>> result = normalizer.normalize('പൌരൻ!!', keep_punctuations=True)
>>> print(result)
>>> പൗരൻ!!
>>> result = normalizer.normalize('ദു:ഖത്തിന്റെ', keep_punctuations=True)
>>> print(result)
>>> ദുഃഖത്തിന്റെ
```

## Running tests
To run tests, 

```
cd normalizer
pip install -r test-requirements.txt
make test
```
Sample output:

```
coverage run --source=libindic -m unittest discover -s libindic
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
flake8 --max-complexity 10 libindic

```

