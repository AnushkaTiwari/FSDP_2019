# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 10:24:38 2019

@author: ANISHKA
"""

# Code Challenge : Week

tuple1 = ('Monday', 'Wednesday', 'Thursday', 'Saturday')
tuple2 = (tuple1[0],) + ('Tuesday',) + tuple1[1:3] + ('Friday',) + (tuple1[-1],) + ('Sunday',)
print(tuple2)
