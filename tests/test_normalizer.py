#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from normalizer import Normalizer

normalize = Normalizer().normalize

class TestNormalizations(unittest.TestCase):
    
    def test_normalize(self):
        self.assertEqual(normalize(u'പൂമ്പാററ'), u'പൂമ്പാറ്റ')
        
        # ൺൻർൽൾൿ are atomic chillus and should get converted to ണ്‍ന്‍ര്‍ല്‍ള്‍ക്‍ respectively
        
        self.assertEqual(normalize(u'അവിൽ'), u'അവില്‍')
        
        # TODO make this work
        # self.assertEqual(normalize("അവിൽപൊതി"), "അവില്‍പൊതി")
        
        
if __name__ == '__main__':
    unittest.main()
