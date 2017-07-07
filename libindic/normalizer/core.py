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

import codecs
import os
import sys


class Normalizer:

    def __init__(self):
        self.rules_file = os.path.join(
            os.path.dirname(__file__), "normalizer_ml.rules")
        self.rulesDict = dict()

    def normalize(self, text):
        self.rulesDict = self.LoadRules()
        words = text.split(" ")
        result = []
        for word in words:
            word = self.trim(word)
            word_length = len(word)
            suffix_pos_itr = 2
            word_stemmed = ""
            while suffix_pos_itr < word_length:
                suffix = word[suffix_pos_itr:word_length]
                if suffix in self.rulesDict:
                    word_stemmed = word[
                        0:suffix_pos_itr] + self.rulesDict[suffix]
                    break
                suffix_pos_itr = suffix_pos_itr + 1
            if(word_stemmed == ""):
                word_stemmed = word
            result.append(word_stemmed)
        return "  ".join(result)

    def LoadRules(self):
        rules_dict = dict()
        line = []
        line_number = 0
        rule_number = 0
        rules_file = codecs. open(
            self.rules_file, encoding='utf-8', errors='ignore')
        while True:
            line_number = line_number + 1
            text_raw = rules_file.readline()
            try:
                text = text_raw.decode('utf-8')
            except:
                text = text_raw
            if text == "":
                break
            if text[0] == '#':
                continue  # this is a comment - ignore
            text = text.split("#")[0]  # remove the comment part of the line
            line = text.strip()  # remove unwanted space
            if(line == ""):
                continue
            if(len(line.split("=")) != 2):
                print(
                    "[Error] Syntax Error in the Rules. Line number: ",
                    line_number)
                print("Line: " + text)
                continue
            lhs = line.split("=")[0].strip()
            rhs = line.split("=")[1].strip()
            rule_number = rule_number + 1
            rules_dict[lhs] = rhs
        return rules_dict

    def trim(self, word):
        punctuations = ['~', '!', '@', '#', '$', '%', '^', '&', '*',
                        '(', ')', '-', '+', '_', '=', '{', '}', '|',
                        ':', ';', '<', '>', '\,', '.', '?']
        word = word.strip()
        index = len(word) - 1
        while index > 0:
            if word[index] in punctuations:
                word = word[0:index]
            else:
                break
            index = index - 1
        return word

    def process(self, form):
        response = """
            <h2>Normalizer</h2></hr>
            <p>Enter the text for normalizing in the below text area.
             Language of each  word will be detected.
             You can give the text in any language and even with mixed language
            </p>
            <form action="" method="post">
            <textarea cols='100' rows='25' name='input_text' id='id1'>\
                    %s\
            </textarea>
            <input  type="submit" id="Stem" value="Normalize"  name="action" \
                    style="width:12em;"/>
            <input type="reset" value="Clear" style="width:12em;"/>
            </br>
            </form>
        """
        if('input_text' in form):
            text = form['input_text'].value.decode('utf-8')
            response = response % text
            result_dict = self.normalize(text)
            response = response + "<h2>Normalized Result</h2></hr>"
            response = response + \
                "<table class=\"table1\"><tr><th>Word</th>\
                <th>Normalized form</th></tr>"
            for key in result_dict:
                response = response + "<tr><td>" + key + \
                    "</td><td>" + result_dict[key] + "</td></tr>"
            response = response + "</table>"
        else:
            response = response % ""
        return response

    def get_module_name(self):
        return "Normalizer"

    def get_info(self):
        return "Malayalam Normalizer(Experimental)"


def getInstance():
    return Normalizer()
