from .core import Normalizer

def normalizer_normalize(text):
    normalizer = Normalizer()
    return normalizer.normalize(text)

def normalize():
    return [normalizer_normalize, str, str]
