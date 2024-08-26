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
>>> result = normalizer.normalize('ഇ–മെയിൽ ദു:ഖത്തിന്റെ  ൊന്നിലോ പാൻറ് 2011 സര്വകലാശാല അവള്‍ അവില്‍പാെതി ഹാർഡ്‌വെയർ‌ അവര്ക്ക് കാറ്ഡ് നമ്പറുള്പ്പെടെ പൌരൻ കൺ്മഷി “ഭാൎയ്യ”')
>>> print(result)
>> ഇമെയിൽ ദുഃഖത്തിന്റെ  ഒന്നിലോ പാന്റ് 2011 സർവകലാശാല അവൾ അവിൽപൊതി ഹാർഡ്‌വെയർ അവർക്ക് കാർഡ് നമ്പറുൾപ്പെടെ പൗരൻ കൺമഷി ഭാര്യ
>>> result = normalizer.normalize('പൌരൻ!!', remove_punctuations=False)
>>> print(result)
>>> പൗരൻ!!
>>> result = normalizer.normalize('ദു:ഖത്തിന്റെ', remove_punctuations=False) # This is considered a mistake and not a real punctuation
>>> print(result)
>>> ദുഃഖത്തിന്റെ
>>> result = normalizer.normalize('ഇ–മെയിൽ', remove_punctuations=False) # Punctuation not removed. But normalized to ASCII
>>> print(result)
>>> ഇ-മെയിൽ
>>> result = normalizer.normalize('ഇ–മെയിൽ') # Punctuation removed in two steps. Normalized to ASCII and then removed.
>>> print(result)
>>> ഇമെയിൽ
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
Ran 2 test in 0.014s
```

