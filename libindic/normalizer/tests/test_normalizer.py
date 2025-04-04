#!/usr/bin/env python
# -*- coding: utf-8 -*-
from testtools import TestCase

from .. import Normalizer
normalize = Normalizer('ml').normalize

class MalayalamNormalizerTest(TestCase):

    def setUp(self):
        super(MalayalamNormalizerTest, self).setUp()
        self.normalizer = Normalizer('ml')

    def test_normalize(self):
        # The chillus (ണ്‍ന്‍ര്‍ല്‍ള്‍ക്‍) defined by zero width joiners to be
        # replaced with atomic chillus (ൺൻർൽൾൿ).

        self.assertEqual(self.normalizer.normalize(u'അവില്‍'), u'അവിൽ')
        self.assertEqual(self.normalizer.normalize(u'രമണന്‍'), u'രമണൻ')
        self.assertEqual(self.normalizer.normalize(u'അവള്‍'), u'അവൾ')
        self.assertEqual(self.normalizer.normalize(u'ശ്രാവണ്‍'), u'ശ്രാവൺ')

        # Multiple normalisations in a single word
        self.assertEqual(normalize('കര്‍ണന്‍'), 'കർണൻ')

        #  ൊ=ൊ, ാെ=ൊ,ോ=ോ,ാേ=ോ: Vowel sign normalizations
        self.assertEqual(normalize('അവില്‍പാെതി'), 'അവിൽപൊതി')
        self.assertEqual(normalize('കാേടതി'), 'കോടതി')
        self.assertEqual(normalize('കോടതി'), 'കോടതി')
        self.assertEqual(normalize('പൌരൻ!!', remove_punctuations=False), 'പൗരൻ!!')


        # # Remove punctuations
        self.assertEqual(normalize('1-ാം'), '1ാം')
        self.assertEqual(normalize('1-ാം', remove_punctuations=False), '1-ാം')

        # Alternate Spellings
        self.assertEqual(normalize('കാൎത്തുമ്പി'), 'കാർത്തുമ്പി')
        self.assertEqual(normalize('ഭാൎയ്യ'), 'ഭാര്യ')
        self.assertEqual(normalize('എൻ്റെ കമ്പ്യൂട്ടറിനു് എന്റെ ഭാഷ.'), 'എന്റെ കമ്പ്യൂട്ടറിന് എന്റെ ഭാഷ')
        
        # Regex pattern for ZWJ and ZWNJ Removal, Chillu insertion, Common Mistakes
        self.assertEqual(normalize('അവൻ‌ വന്നു'), 'അവൻ വന്നു')
        self.assertEqual(normalize('അവൻ‌. വന്നു'), 'അവൻ വന്നു')
        self.assertEqual(normalize('അവൻ‌'), 'അവൻ')
        self.assertEqual(normalize('കൺ‌മണി'), 'കൺമണി')
        self.assertEqual(normalize('ഹാർഡ്‌വെയർ‌'), 'ഹാർഡ്‌വെയർ')
        self.assertEqual(normalize('സോഫ്റ്റ്‍വെയർ'), 'സോഫ്റ്റ്വെയർ') #soft_ware written with an zwj, before ‌_ware gets removed.
        self.assertEqual(normalize('ആല‌-', remove_punctuations=False), 'ആല-') #ZWNJ, if followed by punctuation is removed
        self.assertEqual(normalize('ആറ്റ്‌ലി'), 'ആറ്റ്‌ലി')
        self.assertEqual(normalize('ഇൻസ്റ്റിറ്റ്യൂട്ട്'), 'ഇൻസ്റ്റിറ്റ്യൂട്ട്')
        self.assertEqual(normalize('കാല്‍‍പനികം'), 'കാൽപനികം')
        self.assertEqual(normalize('അവര്ക്ക്'), 'അവർക്ക്')
        self.assertEqual(normalize('അവര്'), 'അവര്')
        self.assertEqual(normalize('ആര്യ '), 'ആര്യ ')
        self.assertEqual(normalize('സര്വകലാശാല '), 'സർവകലാശാല ')
        self.assertEqual(normalize('നമ്പറുള്പ്പെടെ'), 'നമ്പറുൾപ്പെടെ')
        self.assertEqual(normalize('വള്ളിച്ചെടി'), 'വള്ളിച്ചെടി')
        self.assertEqual(normalize('കാറ്ഡ്'), 'കാർഡ്')
        self.assertEqual(normalize('കാറ്-'), 'കാറ്')
        self.assertEqual(normalize('കാറ് '), 'കാറ് ')
        self.assertEqual(normalize('കാറ്റ്'), 'കാറ്റ്')
        self.assertEqual(normalize('അൽഭുതം അത്ഭുതം ചികിൽസാപിഴവ്', remove_punctuations=False), "അദ്ഭുതം അദ്ഭുതം ചികിത്സാപിഴവ്")
        self.assertEqual(normalize('ദു:ഖത്തിന്റെ–'), 'ദുഃഖത്തിന്റെ')
        self.assertEqual(normalize('ദു:ഖത്തിന്റെ-', remove_punctuations=False),
                         'ദുഃഖത്തിന്റെ-')
        self.assertEqual(normalize(' ൊന്നിലോ'), ' ഒന്നിലോ')
        self.assertEqual(normalize('ൌന്നത്യം'), 'ഔന്നത്യം')
        self.assertEqual(normalize('പാൻറ്'), 'പാന്റ്')
        self.assertEqual(normalize('കൺ്മഷി'), 'കൺമഷി')
        self.assertEqual(normalize('“ആൻസി”', remove_punctuations=False), '"ആൻസി"')
        self.assertEqual(normalize('അമ്മ’'), 'അമ്മ')
        self.assertEqual(normalize('അമ്മ’', remove_punctuations=False), "അമ്മ'")
        self.assertEqual(normalize('ഇ–മെയിൽ', remove_punctuations=False), "ഇ-മെയിൽ")
        self.assertEqual(normalize('ഇ–മെയിൽ'), "ഇമെയിൽ")
        self.assertEqual(normalize('ബീജിംഗ്'), "ബീജിങ്ങ്")
        self.assertEqual(normalize('പിംഗ് '), "പിങ്ങ് ")
        self.assertEqual(normalize('ദി കിംഗ്.', remove_punctuations=False), "ദി കിങ്ങ്.")
        self.assertEqual(normalize('ദി കിംഗ്!', remove_punctuations=True), "ദി കിങ്ങ്")
        self.assertEqual(normalize('വന്നു എന്നു പറഞ്ഞു', remove_punctuations=True), "വന്നു എന്ന് പറഞ്ഞു")
        self.assertEqual(normalize('വന്നിട്ടില്ലെന്നു പറഞ്ഞു', remove_punctuations=True), "വന്നിട്ടില്ലെന്ന് പറഞ്ഞു")
        self.assertEqual(normalize('ഒന്നു പോലെ', remove_punctuations=True), "ഒന്ന് പോലെ")
        self.assertEqual(normalize('മൂന്നു', remove_punctuations=False), "മൂന്ന്")
        self.assertEqual(normalize('ഒന്നു-രണ്ടു', remove_punctuations=False), "ഒന്ന്-രണ്ട്")
        self.assertEqual(normalize('ഒമ്പതു ഒമ്പതാമത്തെ', remove_punctuations=False), "ഒൻപത് ഒൻപതാമത്തെ")
        self.assertEqual(normalize('ഏഴു സ്വരങ്ങളും', remove_punctuations=False), "ഏഴ് സ്വരങ്ങളും")


    def test_multiline_string(self):
        expected = """കുഞ്ചൻ നമ്പ്യാർ
        ചെണ്ടമേളം"""
        input = """കുഞ്ചന്‍ നമ്പ്യാര്‍
        ചെണ്ടമേളം"""
        actual = self.normalizer.normalize(input)
        self.assertEqual(actual, expected)
