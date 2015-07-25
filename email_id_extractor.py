#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import urllib
import re
import os

class Base:
    def download(self,widget):
        address=self.weblink.get_text()
        #files=self.folder.get_text()
        main_page=urllib.urlopen(address)
        print main_page.read()
        match = re.findall(r'[a-zA-Z0-9]+[\S]+@[\w.]+',main_page.read())
        print match
        f=open('emails.txt','a')
        for email in match:
			f.write("<"+email+">")
        f.close()
        gtk.main_quit()
    def destroy(self,widget,data=None):
        print "you clicked the close button"
        gtk.main_quit()
		
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.set_size_request(600,400)
        self.window.set_title("Emial Id Scrapper")
        self.weblink = gtk.Entry()
        #self.weblink.connect("changed",self.download)
        #self.folder = gtk.Entry()
        #self.textbox2.connect("changed",self.folder)
        self.button1 = gtk.Button("Start")
        self.button1.connect("clicked",self.download)
        
        
        
        self.box1= gtk.HBox()
        self.box1.pack_start(self.weblink)
        #self.box1.pack_start(self.folder)
        self.box1.pack_start(self.button1)
        self.window.add(self.box1)
        self.window.show_all()
        self.window.connect("destroy",self.destroy)
        
    def main(self):
        gtk.main()

if __name__ == "__main__":
    base = Base()
    base.main()
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
