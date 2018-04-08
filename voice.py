import speech_recognition as sr
from gtts import gTTS
import numpy
import os
import pickle
import requests
import telebot
import subprocess
import string
import random


def get_audio_text(filename):
    rec = sr.Recognizer()
    with sr.WavFile(filename) as source:
        audio = rec.record(source)
    try:
        text = rec.recognize_google(audio)
    except Exception as e:
        print(e)
        text = "Could not understand the speech"
    #os.remove(filename)
    return text


def getOutput(text):
    new_file = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)) + '.wav'
    tts = gTTS(text=text)
    tts.save(new_file)
    return new_file


def readCorpus():
    if os.path.exists('corpus'):
        with open('corpus', 'rb') as f:
            corpus = pickle.load(f)
    else:
        # corpus = [["Could not understand the speech", [["Could not understand the speech",1]]], ["switch on", [["Light is on", 1]]], ["switch off", [["light is off", 1]]]]
        corpus = [["Could not understand the speech", [["Could not understand the speech", 1]]],
                  ["hello", [["hello, how can I help you?", 1]]], ["hi", [["hello, how can I help you?", 1]]]]
        writeCorpus(corpus)
    return corpus


def writeCorpus(corpus):
    with open('corpus', 'wb') as f:
        pickle.dump(corpus, f)


def getAnswer(_input):
    corpus = readCorpus()
    output = ("I don't know what you're saying. Please teach me")
    for ind1 in range(len(corpus)):
        if(_input == corpus[ind1][0]):
            prob = []
            words = []
            for ind2 in range(len(corpus[ind1][1])):
                prob.append(corpus[ind1][1][ind2][1])
                words.append(corpus[ind1][1][ind2][0])
            output = numpy.random.choice(words, p=numpy.array(prob)/sum(prob))
    return output


def teachAndUpdate(question, answer):
    corpus = readCorpus()
    blockInd0 = 0
    blockInd1 = 0
    for ind1 in range(len(corpus)):
        if(question == corpus[ind1][0]):
         blockInd0 = 1
         for ind2 in range(len(corpus[ind1][1])):
             if(answer==corpus[ind1][1][ind2][0]):
                 blockInd1=1
                 corpus[ind1][1][ind2][1]+=1
        if blockInd1==0: 
            corpus[ind1][1].append([answer, 1])
    if blockInd0 == 0:
        corpus.append([question, [[answer, 1]]])
    writeCorpus(corpus)


def getVoice(TOKEN,bot):

  fileID = bot.get_updates()[len(bot.get_updates())-1].message.voice.file_id
  filePath = bot.get_file(fileID).file_path

  file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(TOKEN,filePath))
  if file.status_code == 200:
      with open('input.ogg', 'wb') as handle:
           for block in file.iter_content(1024):
              handle.write(block)
  subprocess.call(['ffmpeg/bin/ffmpeg', '-i', 'input.ogg','input.wav'])


def sendVoice(bot, chat_id):
    audio = open('output.wav', 'rb')
    bot.send_voice(chat_id, audio)

