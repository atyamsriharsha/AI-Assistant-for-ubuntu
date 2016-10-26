import os,sys
import numpy as np
from textblob.classifiers import NaiveBayesClassifier
import random
from textblob import TextBlob
from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from werkzeug.datastructures import ImmutableMultiDict
app = Flask(__name__)


@app.route('/classifier',methods=['GET','POST'])
def classifier():
    name = request.form
    sentence = name['output']
    # print sentence
    train = [
        ('Please open the terminal','open terminal'),
        ('open the terminal','open terminal'),
        ('can you open the terminal','open terminal'),
        ('Hello please open the terminal','open terminal'),
        ('hey please open the terminal','open terminal'),
        ('open terminal','open terminal'),
        ('Please close the terminal','close terminal'),
        ('close the terminal','close terminal'),
        ('can you close the terminal','close terminal'),
        ('Hello please close the terminal','close terminal'),
        ('hey please close the terminal','close terminal'),
        ('close terminal','close terminal'),
        ('Please open the browser','open browser'),
        ('open the browser','open browser'),
        ('can you open the browser','open browser'),
        ('Hello please open the browser','open browser'),
        ('hey please open the browser','open browser'),
        ('open browser','open browser'),
        ('Please close the browser','close browser'),
        ('close the browser','close browser'),
        ('can you close the browser','close browser'),
        ('Hello please close the browser','close browser'),
        ('hey please close the browser','close browser'),
        ('close browser','close browser'),
        ('Please open the media player','open vlc'),
        ('open the vlc player','open vlc'),
        ('can you open the vlc media player','open vlc'),
        ('Hello please open media player','open vlc'),
        ('hey please open the vlc media player','open vlc'),
        ('open vlc player','open vlc'),
        ('Please close the media player','close vlc'),
        ('close the vlc player','close vlc'),
        ('can you close the vlc media player','close vlc'),
        ('Hello please close media player','close vlc'),
        ('hey please close the vlc media player','close vlc'),
        ('close vlc player','close vlc'),
        ('Please open the atom editor','open atom'),
        ('open the atom','open atom'),
        ('can you open the atom','open atom'),
        ('Hello please open the text editor','open atom'),
        ('hey please open the atom text editor','open atom'),
        ('open atom text editor','open atom'),
        ('Please open the file manager','open files'),
        ('open the file manager','open files'),
        ('can you open the file manager','open files'),
        ('Hello please open the file manager','open files'),
        ('hey please open the file manager','open files'),
        ('open file manager','open files'),
        ('Please open the document viewer','open document viewer'),
        ('open the pdf viewer','open document viewer'),
        ('can you open the document viewer','open document viewer'),
        ('Hello please open pdf document viewer','open document viewer'),
        ('hey please open the document viewer','open document viewer'),
        ('open document viewer','open document viewer'),


    ]
    clf = NaiveBayesClassifier(train) #This is the classifier
    cluster = clf.classify(sentence)
    if cluster is "open terminal":
        os.system("gnome-terminal")
    elif cluster is "open browser":
        os.system("sensible-browser")
    elif cluster is "open vlc":
        os.system("vlc")
    elif cluster is "open atom":
        os.system("atom")
    elif cluster is "open files":
        os.system("nautilus")
    elif cluster is "open document viewer":
        os.system("evince")

if __name__ == '__main__':
	app.run(debug=True)
