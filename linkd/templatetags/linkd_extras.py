# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import template

register = template.Library()

@register.filter
def keyvalue(dict, key):    
    return dict[key]




import random
colors = [
            'FF1744', 'F50057', 'D500F9', '651FFF',
            '3D5AFE', '2979FF', '00B0FF', '00E5FF',
            '1DE9B6', '00E676', '76FF03', 'C6FF00',
            'FFEA00', 'FFC400', 'FF9100', '607D8B'
        ]
color_count = 0


@register.simple_tag
def get_color():
    global color_count, colors
    if color_count % len(colors) == 0:
        last_color = colors[-1]
        random.shuffle(colors)
        while last_color == colors[0]:
            random.shuffle(colors)
    color = colors[color_count % len(colors)]
    color_count += 1
    return '#' + color
