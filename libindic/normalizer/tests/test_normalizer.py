#!/usr/bin/env python
# -*- coding: utf-8 -*-

from testtools import TestCase

from .. import Normalizer
normalize = Normalizer().normalize


class MalayalamNormalizerTest(TestCase):

    def setUp(self):
        super(MalayalamNormalizerTest, self).setUp()
        self.normalizer = Normalizer()

    def test_normalize(self):
        self.assertEqual(self.normalizer.normalize(u'പൂമ്പാററ'), u'പൂമ്പാറ്റ')

        # ൺൻർൽൾൿ are atomic chillus and should get
        # converted to ണ്‍ന്‍ര്‍ല്‍ള്‍ക്‍ respectively

        self.assertEqual(self.normalizer.normalize(u'അവിൽ'), u'അവിൽ')
        self.assertEqual(self.normalizer.normalize(u'രമണൻ'), u'രമണൻ')
        self.assertEqual(self.normalizer.normalize(u'അവൾ'), u'അവൾ')
        self.assertEqual(self.normalizer.normalize(u'ശ്രാവൺ'), u'ശ്രാവൺ')

        # TODO make this work
        # self.assertEqual(normalize("അവിൽപൊതി"), "അവില്‍പൊതി")

    def test_multiline_string(self):
        expected = """കുഞ്ചൻ നമ്പ്യാർ
            ചെണ്ടമേളം"""
        input = """കുഞ്ചന്‍ നമ്പ്യാര്‍
            ചെണ്ടമേളം"""
        actual = self.normalizer.normalize(input)
        self.assertEqual(actual, expected)
