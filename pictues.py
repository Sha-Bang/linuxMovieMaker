#!/usr/bin/env python

import sys
import png

def main(argv):
	inFile=argv[1]
	picFile= open(inFile, 'rb')
	picFile= png.Reader(file=picFile)
	print picFile.asRGB()
#	print list(l[2])






if __name__ == '__main__':
        main(sys.argv)
