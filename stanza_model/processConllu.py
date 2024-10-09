import stanza
from stanza import Pipeline
from stanza.utils.conll import CoNLL
import sys

from stanza.utils.conll import CoNLL
doc = CoNLL.conll2doc(sys.argv[2])



nlp = stanza.Pipeline(lang='it', dir=sys.argv[1], download_method=None, processors='tokenize,pos,lemma,depparse', tokenize_pretokenized=True)
doc = nlp(doc)

if len(sys.argv) >3 :
    CoNLL.write_doc2conll(doc, sys.argv[3])
else:
    CoNLL.write_doc2conll(doc,sys.stdout)