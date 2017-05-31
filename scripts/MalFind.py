# -*- coding: utf-8 -*-
"""
    File name: MalFind.py
    Author: Dawid Golak
    Date created: 15/04/2017
    Date last modified: 01/06/2017
    Python Version: 2.7
    Description: MalFInd is a script which gets the mail message from the file
    (filename = argv[1]) and puts into database.
"""

import base64
import email
import sys

from email.header import decode_header

from classes import MalData


class MalFind:
    """class MalFind."""

    def __init__(self):
        """init."""
        f = open(sys.argv[1]).read()
        self.msg = email.message_from_string(f)
        sub, enc = decode_header(self.msg['subject'])[0]
        try:
            self.msg['msg_sub'] = sub.decode(enc)
        except:
            self.msg['msg_sub'] = sub

        for part in self.msg.walk():
            if part.get_content_type() == "text/html":
                self.msg['bodyhtml'] = part.get_payload()
            elif part.get_content_type() == "text/plain":
                try:
                    b = base64.b64decode(part.get_payload())
                except:
                    b = part.get_payload()
                self.msg['body'] = b
        if self.msg['bodyhtml']:
            if len(self.msg['bodyhtml']) > 0:
                self.msg['msg_body'] = self.msg['bodyhtml']
        else:
                self.msg['msg_body'] = self.msg['body']

    def showmessage(self):
        """showmessage."""
        print("--------------------------------------------")
        print("FROM:" + self.msg['from'])
        print("TO:" + self.msg['to'])
        print("SUBJECT:" + self.msg['msg_sub'])
        print("---------------------")
        print("BODY:" + self.msg['msg_body'])

    def addmessage2database(self):
        """addmessage2database."""
        mdata = MalData()
        mdata.adddata(
            self.msg['from'],
            self.msg['to'],
            self.msg['sub'],
            self.msg['msg_body']
        )

# m = MalFind()
# m.showmessage()
# m.addmessage2database()
