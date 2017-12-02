import urllib2


FILENAME = "README"
url = "http://codeskulptor-examples.commondatastorage.googleapis.com/examples_files_dracula.txt"
file = urllib2.urlopen(url, timeout=3)

data = file.read()

print data

netfile = open(FILENAME, "r")
data = netfile.read()
print data