#!/usr/bin/env python
#              Libraries and other parts
import xml.dom.minidom
#              Debug settings 
debug = 0 #set to 1 to debug, 0 to not debug
tagDebug = 0 #same as above, just to help divide up the xml tag debug stuff from the other debug stuff

"""Here are the variables that will be
changed by the host program to get the
different results from the parser"""

tagType = 'col' #what, is your favorite color? Blue...No, Yellooooooooo.....
tagValue = ''

"""setup the document thats getting
parsed and make sure there is content"""

f = open('opt.xml', mode='r') #this will eventually get turned into a dynamic function so you can open whatever file you want, however, until then, you are stuck with having to change opt.xml with your own file name unless you want to take the 2 min it takes to change it to dynaimc
doc = xml.dom.minidom.parse(f)
seen = set()
parent = doc.documentElement #one would hope theres a parent in the document

if parent == 'None': #crap, somewhere we screwed up if this is true
   pass

#              Debug time
if debug: print tag #debug tag
if debug: print parent
if tagDebug:
   for a in tag:
      print '%s, %s' %(a, a.nodeName)

#              Okay, all done 
"""Here comes the industrial stuff to pull
out different parts of the xml document,
and to grab parents and siblings and so forth
for use in the main program. there will need
to be a "next" function that can be used to
grab the next sibling, and a "parent"
function to grab the parent or make sure
a node is still in the right area for what
we'll be looking for"""

def findTag(tagType):
   tag = doc.getElementsByTagName(tagType)
   if len(tag) == 0:
      return
   if len(tag) < 1:
      return tag[0].getAttribute('val')
   else:
      return tag[0].getAttribute('val')

def findNumberOfTags(tagType):
   tag = doc.getElementByTagName(tagType)
   return len(tag)

def findTagNumber(tagType, number):
   tag = doc.getElementsByTagName(tagType)
   return tag[number].getAttribute('val')

def findTags(tagType):
   tag = doc.getElementsByTagName(tagType)
   return tag
