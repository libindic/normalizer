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

        self.assertEqual(self.normalizer.normalize(u'അവിൽ'), u'അവില്‍')

        # TODO make this work
        # self.assertEqual(normalize("അവിൽപൊതി"), "അവില്‍പൊതി")
