#Author: Tran Duy Thanh
#Email: thanhtd@uel.edu.vn
#Date: 2021/04/25
#Description:
    #These codes I improved from Professor's document and translate to English to.
    #Improved the word memorization program if there many vocabularies to learn, take 5 sample vocabularies to learn
    #1.Update Vocabulary class
    #   1.1 use random.sample (see takeVocabularyToLearn(self) function)
    #   1.2 Difference operator ‘-’ (see updateUnmemorized(self) functin)
    #   1.3 updated 2 new attribute:  self.unmemorized (any vocabularies is unmemorized),
    #                       and self.memorized (for memorized for each periodic
    #   1.4 update check to save memorized word or not
    #   1.5 static method buildVocabularyDatabase to read vocabularies from Excel (many vocabularies)
    #   1.6 method printAllVocabularies(self) -> print all original vocabularies
    #   1.7 method printStatusProgressingLearning(self)-> show status progressing learning
    #2. Create a new class VocabularyExecutor
    #   this class use to create 4 option menuitem
    #   2.1 Overview Vocabulary -> show all vocabularies from Vocabulary Object
    #   2.2 Re-Learn Vocabulary -> learners can re learn  vocabularies
    #   2.3 Continue learning Vocabulary -> learners can continue to learn vocabulary
    #          It means: learner can learn vocabulary day by day, can stop software and continue learn from history
    #          program saved vocabulary to object file and restored for learner to continue to learn
    #   2.4 Exit program
import pickle
import random
import pandas as pd

class Vocabulary:
    def __init__(self,wdict):
        self.words=wdict.copy()
        self.untrained=set(self.words)
        self.unmemorized=self.untrained.copy()
        self.memorized=set()#variable save to correct vocabulary for each periodic

    #this function to get sample 5 vocabulary in the unmemorized list
    def takeVocabularyToLearn(self):
        #difference unmemorized and memorized
        if len(self.unmemorized)<=5:
            self.target=list(self.unmemorized)
        else:
            self.target = random.sample(self.unmemorized,5)
        random.shuffle(self.target)
        self.memorized = set()#reset correct vocabulary for feach periodic
        self.untrained = set()  # empty set

    #this function use to difference operator to get the unmemorized vocabulary
    def updateUnmemorized(self):
        self.unmemorized = self.unmemorized - self.memorized

    def target_keys(self):
        return self.target

    def check(self,key, value=None):
        if key not in self.words:
            return  None
        if value is not None:
            if self.words[key] ==value:
                #saved memorized if learning correcting
                #at least one time is unmemorized, memorized doesn't save the word
                if self.untrained.__contains__(key) ==False:
                    self.memorized.add(key)
                return Ellipsis
            self.untrained.add(key)
            #remove again memorized for next time if learning wrongting
            #eg: 1st is memorized, but 2rd is wrongunmemorized-> total is unmemorized
            if self.memorized.__contains__(key):
                self.memorized.remove(key)
        return self.words[key]

    def shuffle(self):
        random.shuffle(self.target)

    #this static method used to build vocabulary database from Excel
    @staticmethod
    def buildVocabularyDatabase():
        wdict = {}  # empty dictionary
        data = pd.read_excel(r'Database_Vocabulary.xlsx')  # read data
        df = pd.DataFrame(data, columns=['English Language', 'Korean Language'])
        for i in range(len(df.index)):
            english = df.iloc[i]["English Language"]
            korean = df.iloc[i]["Korean Language"]
            wdict[korean] = english
        voc = Vocabulary(wdict)
        return voc

    #this function use to print all orginial vocabularies
    def printAllVocabularies(self):
        print("There are ", len(self.words), " vocabularies")
        print(f'{"English Language":<20}{"Korean Language":<20}')
        print("-" * 40)
        for k, v in self.words.items():
            print(f'{v:<20}{k:<20}')
        print("-" * 40)

    #this function use to print all status progressing learning
    def printStatusProgressingLearning(self):
        print("There are ", len(self.words), " vocabularies")
        memorizeds=set(self.words)-self.unmemorized
        print("You have not yet memorized ", len(self.unmemorized), " vocabularies")
        print("You already memorized ", len(memorizeds), " vocabularies")

#this class use to parse vocabulary from Excel File
#and return Vocabulary Object
class VocabularyExecutor:
    voc=None
    filename = "vocabulary.dat"
    #this function give 4 option menuitem
    def runVocabularyExecutor(self):
        while True:
            print("1.Overview Vocabulary")
            print("2.Re-Learn Vocabulary")
            print("3.Continue learning Vocabulary")
            print("4.Exit program")
            choose=input("Please choose [1..4]:")
            if choose=="1":
                self.overviewVocabulary();
            elif choose=="2":
                self.reLearnVocabulary()
            elif choose=="3":
                self.continueLearnVocabulary()
            elif choose=="4":
                break
        print("Thank you so much for your using programming!")

    #this function: Learner will learn vocabulary
    def learnVocabulary(self):
        #before learning, program will show the status progressing learning
        self.voc.printStatusProgressingLearning()
        while len(self.voc.unmemorized)>0:
            self.voc.takeVocabularyToLearn()
            #if there are unmemorized vocabulary to learn
            if len(self.voc.target_keys())>0:
                print("\nWords to memorize:",self.voc.target_keys())#Words to memorize:
                nQNA=int(input("Number of questions and answers by word:"))#
                print()
                for index in range(0,nQNA):
                    self.voc.shuffle()
                    for meaning in self.voc.target_keys():
                        answer=input("What is the meaning of '"+meaning+"'?")#What word means "'"+meaning+"'?"
                        word=self.voc.check(meaning,answer)
                        if word is Ellipsis:
                            print("'"+answer+"' is correct")
                        else:
                            print("Wrong! '"+meaning+"' has meaning '"+word+"'")#"The correct answer is'"+word+"'"
            print("You finihsed a periodic learning")
            # Words unmemorized:
            if len(self.voc.untrained) > 0:
                print("Words unmemorized:", self.voc.untrained)
            else:
                print("Words unmemorized:0")
            #words memoried
            if len(self.voc.memorized)>0:
                print("Words memorized:", self.voc.memorized)
            else:
                print("Words memorized:0")
            #update the unmemorized word
            self.voc.updateUnmemorized()
            #save status progressing learning to file
            self.persistenceVocabulary()
            #when finishing a periodic, we we ask learner to continue or not learning
            choose=input("Do you want to continue learning?(y/n):")
            if choose=="N" or choose=="n":
                break
        if len(self.voc.unmemorized)==0:
            print("Congratulations, you memorized all vocabulary")
            self.voc.printAllVocabularies()
        else:
            #print status progressing learning again when user paused learning
            self.voc.printStatusProgressingLearning()

    #this function use to overview vocabularies
    def overviewVocabulary(self):
        if self.voc is None:
            self.voc = Vocabulary.buildVocabularyDatabase()
        if self.voc is not None:
            self.voc.printAllVocabularies()

    # this function use to open Vocabulary object from file
    # learner can continue learning from history
    def continueLearnVocabulary(self):
        try:
            with open(self.filename, 'rb') as input:
                self.voc = pickle.load(input)
        except FileNotFoundError:
            self.voc = Vocabulary.buildVocabularyDatabase()
        self.learnVocabulary()

    #this function: leaner re learns vocabulary
    #rebuild vocabulary database
    def reLearnVocabulary(self):
        self.voc = Vocabulary.buildVocabularyDatabase()
        self.learnVocabulary()

    #this function use to save the vocabularies and progressing learning to file
    #so we can restore to continue learning
    def persistenceVocabulary(self):
        with open(self.filename, 'wb') as output:  # Overwrites any existing file.
            pickle.dump(self.voc, output, pickle.HIGHEST_PROTOCOL)

#create a VocabularyExecutor object
vexecutor=VocabularyExecutor()
#call runVocabularyExecutor to start program
vexecutor.runVocabularyExecutor()