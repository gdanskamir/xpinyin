#!/usr/bin/env python
#-*- coding:UTF-8 -*-

import sys;
from xpinyin import Pinyin
p = Pinyin()
# default splitter is `-`
print p.get_pinyin(u"上海")
# show tone marks
print p.get_pinyin(u"上海", show_tone_marks=True)
# remove splitter
print p.get_pinyin(u"上海", '')
# set splitter as whitespace
print p.get_pinyin(u"上海", ' ')
print p.get_initial(u"上")
print p.get_initials(u"上海")
print p.get_initials(u"上海", u'')
print p.get_initials(u"上海", u' ')

#如果方法中传入变量，那么直接加前缀是不可以了。而是要将变量转为utf-8编码：
wordvalue = '中国'
wordvalue= unicode(wordvalue,'utf-8')
s = p.get_initials(wordvalue, u'').lower()
print s
