#!/usr/bin/env python
# coding=utf-8

"""Can I convert namedtuple to json object (not list)?

"""

from __future__ import print_function, unicode_literals

from collections import namedtuple
import json


Point = namedtuple('Point', 'x y')


def main():
    p = Point(x=1, y=2)
    p_json_str = json.dumps(p._asdict())
    print(p_json_str)


if __name__ == '__main__':
    main()
