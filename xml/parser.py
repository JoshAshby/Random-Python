#!/usr/bin/env python
import xml.sax
"""searchs for the value of the tag name specified
this is a precursor to parser-dom"""

debug = 0 #set to 1 to debug, 0 to not debug
tagType = ''
tagValue = ''

class colorOption(xml.sax.ContentHandler):
   if debug: print '%s' %tagType #debug tag
   def startDocument(self):
      self.seen = set()
   def startElement(self, tag, attributes):
      global tagValue
      if tag != tagType: return
      value = attributes.get('val')
      if value is not None and value not in self.seen:
         self.seen.add(value)
         tagValue = value
         if debug: print tagValue #debug tag

def update():
   p = xml.sax.make_parser()
   p.setContentHandler(colorOption())
   f = open('opt.xml', mode='r')

   while True:
      data = f.read()
      if not data: break
      p.feed(data)
      if debug: print tagValue #debug tag

   p.close()
