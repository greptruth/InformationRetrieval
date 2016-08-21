#from __future__ import print_function
import sys
import glob
import errno
from nltk.tokenize import TweetTokenizer
from nltk.stem.wordnet import WordNetLemmatizer

def removeNonAscii(s): return "".join(filter(lambda x: ord(x)<128, s))

tknzr = TweetTokenizer();
lmtzr = WordNetLemmatizer();
fout = open('output.txt','w+');
path = '/home/piyush/IR_asgn1/alldocs/*'   
files = glob.glob(path)   
l=0;
for name in files: # 'file' is a builtin type, 'name' is a less-ambiguous variable name.
	try:
		with open(name) as fin: # No need to specify 'r': this is the default.
			#print(f.read())
			for line in fin:
				line = tknzr.tokenize(line);
				for i in line:
					
					if len(i)>2:
						j = i
						j = removeNonAscii(j)
						k = lmtzr.lemmatize(j)
						if len(k)>2:
							if(l==0):
								l+=1;
							else:
								print>>fout, '';
							print>>fout, k,
							print>>fout, " \t ",
							print>>fout, name[30:],
							#print("%s \t %s" %(k, name[30:]), file=fout);

	except IOError as exc:
		if exc.errno != errno.EISDIR: # Do not fail if a directory is found, just ignore it.
			raise # Propagate other kinds of IOError.