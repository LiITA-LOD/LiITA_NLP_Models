# LiITA Italian Model

This repository contains the Stanza model for Italian, based on the data from the UD Italian treebanks. 

## Train data

The training data is composed as follows:

The training data for the Stanza model was obtained starting from the conllu file on which UDPipe was trained (see folder). The sentences in the conllu file were shuffled and then split into train/dev/test sets with proportions of 70/20/10, respectively. The resulting files are in the UD_italian_LiITA folder.

## How to use

Clone this repository:
```
git clone git@github.com:LiITA-LOD/LiITA_NLP_Models.git
cd LiITA_NLP_Models/stanza_model
```
If you have problem with git LFS bandwidth you can download the model file with :
```
curl -L -o LiITA_model.tgz https://datacloud.di.unito.it/index.php/s/mJQf9HNsErkrQjk/download/LiITA_model.tgz
```
or 
```
wget -O LiITA_model.tgz https://datacloud.di.unito.it/index.php/s/mJQf9HNsErkrQjk/download/LiITA_model.tgz
```
and extract with 
```
tar -xvf LiITA_model.tgz
```

Create and activate a python virtual environment (virtualenv, conda, minicoda, etc). Here an example with virtualenv:
```
virtualenv -p python3 venv
source venv/bin/activate
```
or if you installed virtualenv as a module:
```
python -m virtualenv -p python3 venv
source venv/bin/activate
```

install the Stanza module with:
```
pip install stanza
```

To perform a small test, launch the command  :
```
python processText.py ./LiITA_model "L'Italia è una Repubblica democratica, fondata sul lavoro. La sovranità appartiene al popolo, che la esercita nelle forme e nei limiti della Costituzione." italian_out.conllu
```
this commands will produce an annotated file (```Italian```) with tok,lemma,pos,parser.
If everything went correctly the conllu file should contain something similar to this:

```
# text = L'Italia è una Repubblica democratica, fondata sul lavoro.
# sent_id = 0
1	L'	il	DET	RD	Definite=Def|Number=Sing|PronType=Art	2	det	_	start_char=0|end_char=2|SpaceAfter=No
2	Italia	Italia	PROPN	SP	_	5	nsubj	_	start_char=2|end_char=8
3	è	essere	AUX	VA	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	5	cop	_	start_char=9|end_char=10
4	una	uno	DET	RI	Definite=Ind|Gender=Fem|Number=Sing|PronType=Art	5	det	_	start_char=11|end_char=14
5	Repubblica	repubblica	NOUN	S	Gender=Fem|Number=Sing	0	root	_	start_char=15|end_char=25
6	democratica	democratico	ADJ	A	Gender=Fem|Number=Sing	5	amod	_	start_char=26|end_char=37|SpaceAfter=No
7	,	,	PUNCT	FF	_	5	punct	_	start_char=37|end_char=38
8	fondata	fondare	VERB	V	Gender=Fem|Number=Sing|Tense=Past|VerbForm=Part	5	acl	_	start_char=39|end_char=46
9-10	sul	_	_	_	_	_	_	_	start_char=47|end_char=50
9	su	su	ADP	E	_	11	case	_	_
10	il	il	DET	RD	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	11	det	_	_
11	lavoro	lavoro	NOUN	S	Gender=Masc|Number=Sing	8	obl	_	start_char=51|end_char=57|SpaceAfter=No
12	.	.	PUNCT	FS	_	5	punct	_	start_char=57|end_char=58

# text = La sovranità appartiene al popolo, che la esercita nelle forme e nei limiti della Costituzione.
# sent_id = 1
1	La	il	DET	RD	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	2	det	_	start_char=59|end_char=61
2	sovranità	sovranità	NOUN	S	Gender=Fem	3	nsubj	_	start_char=62|end_char=71
3	appartiene	appartenere	VERB	V	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	0	root	_	start_char=72|end_char=82
4-5	al	_	_	_	_	_	_	_	start_char=83|end_char=85
4	a	a	ADP	E	_	6	case	_	_
5	il	il	DET	RD	Definite=Def|Gender=Masc|Number=Sing|PronType=Art	6	det	_	_
6	popolo	popolo	NOUN	S	Gender=Masc|Number=Sing	3	obl	_	start_char=86|end_char=92|SpaceAfter=No
7	,	,	PUNCT	FF	_	6	punct	_	start_char=92|end_char=93
8	che	che	PRON	PR	PronType=Rel	10	nsubj	_	start_char=94|end_char=97
9	la	la	PRON	PC	Clitic=Yes|Gender=Fem|Number=Sing|Person=3|PronType=Prs	10	obj	_	start_char=98|end_char=100
10	esercita	esercitare	VERB	V	Mood=Ind|Number=Sing|Person=3|Tense=Pres|VerbForm=Fin	6	acl:relcl	_	start_char=101|end_char=109
11-12	nelle	_	_	_	_	_	_	_	start_char=110|end_char=115
11	in	in	ADP	E	_	13	case	_	_
12	le	il	DET	RD	Definite=Def|Gender=Fem|Number=Plur|PronType=Art	13	det	_	_
13	forme	forma	NOUN	S	Gender=Fem|Number=Plur	10	obl	_	start_char=116|end_char=121
14	e	e	CCONJ	CC	_	17	cc	_	start_char=122|end_char=123
15-16	nei	_	_	_	_	_	_	_	start_char=124|end_char=127
15	in	in	ADP	E	_	17	case	_	_
16	i	il	DET	RD	Definite=Def|Gender=Masc|Number=Plur|PronType=Art	17	det	_	_
17	limiti	limite	NOUN	S	Gender=Masc|Number=Plur	13	conj	_	start_char=128|end_char=134
18-19	della	_	_	_	_	_	_	_	start_char=135|end_char=140
18	di	di	ADP	E	_	20	case	_	_
19	la	il	DET	RD	Definite=Def|Gender=Fem|Number=Sing|PronType=Art	20	det	_	_
20	Costituzione	costituzione	NOUN	S	Gender=Fem|Number=Sing	17	nmod	_	start_char=141|end_char=153|SpaceAfter=No
21	.	.	PUNCT	FS	_	3	punct	_	start_char=153|end_char=154|SpaceAfter=No
```

Similarly, if the file to be annotated is in conllu format, use:
```
python processConllu.py  ./LiITA_model <conlluFile.conllu> old_italian_out.conllu
```
## Evaluation

Model evaluation on the test set (The test suite included in Stanza was used).
```
             --------  EVALUATION ----------
End to end results for it_liita models on it_liita test data:
Metric     | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |     99.81 |     99.77 |     99.79 |
Sentences  |     89.26 |     89.66 |     89.46 |
Words      |     99.62 |     99.61 |     99.61 |
UPOS       |     97.03 |     97.02 |     97.03 |     97.41
XPOS       |     92.69 |     92.68 |     92.68 |     93.04
UFeats     |     94.66 |     94.65 |     94.65 |     95.02
AllTags    |     90.61 |     90.60 |     90.60 |     90.96
Lemmas     |     97.39 |     97.38 |     97.39 |     97.77
UAS        |     86.49 |     86.48 |     86.48 |     86.82
LAS        |     82.31 |     82.30 |     82.31 |     82.63
CLAS       |     75.90 |     75.61 |     75.76 |     76.00
MLAS       |     69.37 |     69.09 |     69.23 |     69.45
BLEX       |     73.89 |     73.60 |     73.75 |     73.99
```

