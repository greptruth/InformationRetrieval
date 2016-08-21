import sys, os, lucene
from lucene import QueryParser, IndexSearcher, IndexReader, StandardAnalyzer, EnglishAnalyzer,TermPositionVector, SimpleFSDirectory, File, MoreLikeThis,VERSION, initVM, Version,FieldInfo, IndexWriter, IndexWriterConfig#, DirectoryReader
# import sys
import glob
import errno
from nltk.tokenize import TweetTokenizer
from nltk.stem.wordnet import WordNetLemmatizer
from collections import OrderedDict

def make_index():
    '''Make index from data source -- bible
    Some global variables used:
        bible: a dictionary that stores all bible verses
        OTbooks: a list of books in old testament 
        NTbooks: a list of books in new testament
        chapsInBook: a list of number of chapters in each book 
    '''
    lucene.initVM()
    # path = raw_input("./index_dir")
    # 1. create an index
    # print("dzfz")

    index_path = './index_dir'#File(path)
    analyzer = StandardAnalyzer(Version.LUCENE_35)
    index = SimpleFSDirectory(File(index_path))
    config = IndexWriterConfig(Version.LUCENE_35, analyzer)
    writer = IndexWriter(index, config)

    # 2 construct documents and fill the index
    # for book in bible.keys():
    #     if book in OTbooks:
    #         testament = "Old"
    #     else:
    #         testament = "New"
    #     for chapter in xrange(1, chapsInBook[book]+1):
    #         for verse in xrange(1, len(bible[book][chapter])+1):
    #             verse_text = bible[book][chapter][verse]
    #             doc = Document()
    #             doc.add(Field("Text", verse_text, Field.Store.NO, Field.Index.ANALYZED))
    #             doc.add(Field("Testament", testament, Field.Store.YES, Field.Index.ANALYZED))
    #             doc.add(Field("Book", book, Field.Store.YES, Field.Index.ANALYZED))
    #             doc.add(Field("Chapter", str(chapter), Field.Store.YES, Field.Index.ANALYZED))
    #             doc.add(Field("Verse", str(verse), Field.Store.YES, Field.Index.ANALYZED))
    #             writer.addDocument(doc)
    path = './../TestData/alldocs/*'   
    files = glob.glob(path)   
    for name in files: # 'file' is a builtin type, 'name' is a less-ambiguous variable name.
        print(name)
        try:
            with open(name) as fin: # No need to specify 'r': this is the default.
                content = open(name,'r').read()
                doc = lucene.Document()
                doc.add(lucene.Field("Text", content, lucene.Field.Store.NO, lucene.Field.Index.ANALYZED))
                doc.add(lucene.Field("docID", name, lucene.Field.Store.YES, lucene.Field.Index.ANALYZED))
                writer.addDocument(doc)
        except IOError as exc:
            if exc.errno != errno.EISDIR: # Do not fail if a directory is found, just ignore it.
                raise # Propagate other kinds of IOError.

    # 3. close resources
    writer.close()
    index.close()


def search(indexDir,n, kwds):
    '''Simple Search
    Input paramenters:
        1. indexDir: directory name of the index
        2. kwds: query string for this simple search
    display_verse(): procedure to display the specified bible verse 
    '''
    lucene.initVM()
    # 1. open the index
    analyzer = StandardAnalyzer(Version.LUCENE_35)
    index = SimpleFSDirectory(File(indexDir))
    reader = IndexReader.open(index)
    n_docs = reader.numDocs()

    # 2. parse the query string
    queryparser = QueryParser(Version.LUCENE_35, "Text", analyzer)
    query = queryparser.parse(kwds)

    # 3. search the index 
    searcher = IndexSearcher(reader)
    hits = searcher.search(query, n_docs).scoreDocs

    # 4. display results
    for i, hit in enumerate(hits):
        doc = searcher.doc(hit.doc)
        docID = doc.getField('docID').stringValue()
        print>>fout, n,docID
    # 5. close resources
    searcher.close()

# print("fdsufhs")
make_index()

fout = open('./Results/LQueryOut.txt','w+');
fin = open('./../TestData/query.txt','rb');
for line in fin:
    # if line== <EOF> break
    k = line.split('  ');
    print(k[0])
    print(k[1])
    search('./index_dir',k[0],k[1])


# search('/home/greptruth/IR/index_dir','dsfsdjf')