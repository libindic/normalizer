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
        self.assertEqual(self.normalizer.normalize(u'രമണൻ'), u'രമണൻ')
        self.assertEqual(self.normalizer.normalize(u'അവൾ'), u'അവൾ')
        self.assertEqual(self.normalizer.normalize(u'ശ്രാവൺ'), u'ശ്രാവൺ')

        # Multiple normalisations in a single word
        self.assertEqual(normalize('കര്‍ണൻ'), 'കർണൻ')

        #  ൊ=ൊ, ാെ=ൊ,ോ=ോ,ാേ=ോ: Vowel sign normalizations
        self.assertEqual(normalize('അവില്‍പാെതി'), 'അവിൽപൊതി')
        self.assertEqual(normalize('കാേടതി'), 'കോടതി')
        self.assertEqual(normalize('കോടതി'), 'കോടതി')
        self.assertEqual(normalize('പൌരൻ!!', keep_punctuations=True), 'പൗരൻ!!')


        # # Remove punctuations
        self.assertEqual(normalize('1-ാം'), '1ാം')
        self.assertEqual(normalize('1-ാം', keep_punctuations=True), '1-ാം')

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
        self.assertEqual(normalize('കാറ്'), 'കാറ്')
        self.assertEqual(normalize('കാറ് '), 'കാറ് ')
        self.assertEqual(normalize('പൂമ്പാററ'), 'പൂമ്പാറ്റ')
        self.assertEqual(normalize('കാറ്റ്'), 'കാറ്റ്')
        self.assertEqual(normalize('ദു:ഖത്തിന്റെ'), 'ദുഃഖത്തിന്റെ')
        self.assertEqual(normalize('ദു:ഖത്തിന്റെ', keep_punctuations=True),
                         'ദുഃഖത്തിന്റെ')
        self.assertEqual(normalize(' ൊന്നിലോ'), ' ഒന്നിലോ')
        self.assertEqual(normalize('ൌന്നത്യം'), 'ഔന്നത്യം')
        self.assertEqual(normalize('പാൻറ്'), 'പാന്റ്')





    def test_multiline_string(self):
        expected = """കുഞ്ചൻ നമ്പ്യാർ
            ചെണ്ടമേളം"""
        input = """കുഞ്ചന്‍ നമ്പ്യാര്‍
            ചെണ്ടമേളം"""
        actual = self.normalizer.normalize(input)
        self.assertEqual(actual, expected)
