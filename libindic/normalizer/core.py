# -*- coding: utf-8 -*-
# Normalizer Program
# Copyright 2008 Santhosh Thottingal <santhosh.thottingal@gmail.com>
# http://www.smc.org.in
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#

import yaml
import os
import string
import re

class Normalizer:
    def __init__(self, language_code):
        self.language_code = language_code
        self.rules = self.load_rules()
        self.punctuation_remover = str.maketrans('', '', string.punctuation)

    def load_rules(self):
        rules_path = os.path.join(os.path.dirname(__file__), 'rules', f'normalizer.{self.language_code}.yaml')
        if not os.path.exists(rules_path):
            raise FileNotFoundError(f"Rules file for language '{self.language_code}' not found.")
        with open(rules_path, 'r', encoding='utf-8') as file:
            rules = yaml.safe_load(file)
        
        # Compile regex patterns
        if 'regex_patterns' in rules:
            rules['compiled_regex'] = {}
            for pattern, replacement in rules['regex_patterns'].items():
                rules['compiled_regex'][re.compile(pattern, re.UNICODE)] = replacement
        
        return rules
    
    def apply_regex_patterns(self, text):
        if 'compiled_regex' in self.rules:
            for pattern, replacement in self.rules['compiled_regex'].items():
                text = pattern.sub(replacement, text)
        return text
    
    def normalize(self, input_text, keep_punctuations=False, normalize_chillus=True, normalize_vowelsigns=True, normalize_typos=True, normalize_alternateforms=True, apply_regex=True):
        if normalize_chillus and 'normalize_chillus' in self.rules:
            for key, value in self.rules['normalize_chillus'].items():
                input_text = input_text.replace(key, value)
        
        if normalize_vowelsigns and 'normalize_vowelsigns' in self.rules:
            for key, value in self.rules['normalize_vowelsigns'].items():
                input_text = input_text.replace(key, value)
        
        if normalize_typos and 'normalize_typos' in self.rules:
            for key, value in self.rules['normalize_typos'].items():
                input_text = input_text.replace(key, value)
        
        if normalize_alternateforms and 'normalize_alternateforms' in self.rules:
            for key, value in self.rules['normalize_alternateforms'].items():
                input_text = input_text.replace(key, value)
        
        if apply_regex and 'regex_patterns' in self.rules:
            input_text = self.apply_regex_patterns(input_text)
        
        if keep_punctuations:
            return input_text
        return input_text.translate(self.punctuation_remover)
