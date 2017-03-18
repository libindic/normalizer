# LibIndic Normalizer


[![Build Status](https://travis-ci.org/libindic/normalizer.svg?branch=master)](https://travis-ci.org/libindic/normalizer)
[![Coverage Status](https://coveralls.io/repos/github/libindic/normalizer/badge.svg?branch=master)](https://coveralls.io/github/libindic/normalizer?branch=master)


LibIndic's normalizer module may be used to normalize the text to a canonical
format to handle inconsistencies in text. Right now, it supports
Malayalam language only.

## Installation
1. Clone the repository `git clone https://github.com/libindic/normalizer.git`
2. Change to the cloned directory `cd normalizer`
3. Run setup.py to create installable source `python setup.py sdist`
3. Install using pip `pip install dist/normalizer*.tar.gz`

Note: Prefer using virtualenv for installation as the library is in experimental stage

## Usage
```
Input: Unicode text...
Output: Normalized unicode text

>>> from libindic.normalizer import Normalizer
>>> normalizer = Normalizer()
>>> result = normalizer.normalize(u'പൂമ്പാററ')
>>> print(result)
പൂമ്പാറ്റ
```

For more details read the [docs](http://indicstemmer.rtfd.org/)

## Running tests
To run tests, 

```
cd normalizer
pip install -r test-requirements.txt
python setup.py test
```
Sample output:

```
running test
running=${PYTHON:-python} -m subunit.run discover libindic --list 
running=${PYTHON:-python} -m subunit.run discover libindic  --load-list /tmp/tmpggnsy1r0
Ran 1 tests in 0.001s (-0.000s)
PASSED (id=9)

```
