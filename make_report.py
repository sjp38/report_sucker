#!/usr/bin/env python

import copy
import zipfile
import sys
import StringIO
import xml.etree.ElementTree as ElementTree
import subprocess
import shutil

trans_rule = {}

def print_elem_recursively(parent, level):
    indent = ''
    for i in range(level):
        indent += '\t'
    list_ = list(parent)
    if list_:
        list_.append(parent)
    for elem in list(parent):
        print "%stag: %s, text: %s" % (indent, elem.tag, elem.text)
        for child in list(elem):
            print_elem_recursively(child, level + 1)

def check_replace_elem(parent):
    list_ = list(parent)
    if list_:
        list_.append(parent)
    for elem in list_:
        if elem.text:
            elem.text = elem.text.lstrip()
            elem.text = elem.text.rstrip()
        if elem.text in trans_rule:
            new_texts = trans_rule[elem.text].split('\n')
            elem.text = new_texts[0]
            for i in range(1, len(new_texts)):
                new_elem = copy.deepcopy(elem)
                new_elem.text = new_texts[i]
                parent.append(new_elem)
        for child in list(elem):
            check_replace_elem(child)

def parse_trans_rule(text):
    rules = text.split('\n\n')
    for rule in rules:
        spltd = rule.split('\n')
        trans_rule[spltd[0]] = '\n'.join(spltd[1:])

if __name__ == "__main__":
    if len(sys.argv) < 4 :
        print "Usage: %s <template odt> <output odt> <trans data>" % sys.argv[0]
        quit()

    trans_input = None
    with open(sys.argv[3]) as trans_file:
            trans_input = trans_file.read()

    trans_decoded = trans_input.decode('utf-8')
    parse_trans_rule(trans_decoded)

    shutil.copyfile(sys.argv[1], sys.argv[2])
    odt = zipfile.ZipFile(sys.argv[2], 'a')
    raw_xml = odt.read('content.xml')

    fakefile = StringIO.StringIO(raw_xml)
    tree = ElementTree.parse(fakefile).getroot()

    for elem in list(tree):
        check_replace_elem(elem)

    fakefile.close()

    new_xml = ElementTree.tostring(tree, encoding='utf-8')

    odt.writestr('content.xml', new_xml)
    odt.close()
