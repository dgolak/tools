#!/usr/bin/env python

import sys
class B:
    ch="abcdefghijk"	#set it
    max_depth=4		#set max depth

    s=""
    depth=1
    arr=[]

    def __init__(self,search):
        if search:
            self.search=search
        else:
            self.search="abcd"
        self.brute("")


    def anyCheck(self,st):
        #for example xor()
        if st==self.search:
            return True

    def stat(self,st):
        print "-----------------------------"
        print "Found: "+st
        print "-----------------------------"
        print "Chars: %d" % len(self.ch)
        print "Count of chars: %d" % int(self.max_depth+1)
        print "Combination %d" % len(self.arr)
        print "-----------------------------"
        sys.exit()

    def brute(self,r):
        for i in self.ch:
            st=r+i
            anyC=self.anyCheck(st)
            if anyC==True:
                self.stat(st)

            self.arr.append(st)
            if self.depth<=self.max_depth:
                self.depth=self.depth+1
                self.brute(st)
        self.depth=self.depth-1


if sys.argv[1]:
    search=sys.argv[1]
else:
    search="abcd"
B=B(search)

#print sorted(B.arr,key=len)


