# -*- coding: utf-8 -*-

"""
BPMN 2.0 parser
"""
from lxml import objectify


class BpmnParser(object):
    def __init__(self, input):
        with open(input, 'r') as stream:
            process = objectify.parse(stream).getroot().process

            for elem in process.getchildren():
                print "%s" % elem.tag


def get_args():
    import argparse

    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('--version', action='version', version='version')
    parser.add_argument('--input-file', required=True,
                        help='path to BPMN input file')
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    BpmnParser(args.input_file)


if __name__ == '__main__':
    main()
