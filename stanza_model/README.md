# LiITA Italian Model

This repository contains the Stanza model for Italian, based on the data from the UD Italian treebanks. 

## Train data

The training data is composed as follows:

The training data for the Stanza model was obtained starting from the conllu file on which UDPipe was trained (see folder). The sentences in the conllu file were shuffled and then split into train/dev/test sets with proportions of 70/20/10, respectively. The resulting files are in the UD_italian_LiITA folder.

## How to use

Clone this repository:
```
git@github.com:LiITA-LOD/LiITA_NLP_Models.git
cd LiITA_NLP_Models/stanza_model
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

```


Similarly, if the file to be annotated is in conllu format, use:
```
python processConllu.py  ./LiITA_model <conlluFile.conllu> old_italian_out.conllu
```


