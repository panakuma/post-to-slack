#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import sys
import post


def main():
    post_text = sys.argv[1]
    post.post(post_text)


if __name__ == '__main__':
    main()
