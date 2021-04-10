#Author: Tran Duy Thanh
#Email: thanhtd@uel.edu.vn
#Date: 2021/04/10
#Description:
    #These codes I improved from Professor's document and translate to English to.
    #1.List all Toiec Score for each Student acquired: Score-Frequency- Frequency rate
    #2.List all Score with range complex for Student acquired: Base Score-Frequency- Frequency rate
    #3.See all the scores with the same max frequency.
    #4.See all the scores with the same min frequency.
    #5.A function to find the average of the TOEIC students acquired.
#initialize data for Toiec Score that Student acquired
toiecScores=[510,630,750,910,620,805,930,650,840,670,510,780,990,990,720,510,780,200,170,400,250,256,750,915]
#this function to calcuate the Frequency, store value in an array
def frequency(toiecScores):
    counters=[0]*10
    for toiecScore in toiecScores:
        counters[toiecScore//100]+=1
    return counters
#this function use to reduce and sort the score
# (for print all score student acquired: Score, frequency,rate)
def reduceAndSortScores(toiecScores):
    scoreList=[]
    for score in toiecScores:
        if scoreList.__contains__(score) == False:
            scoreList.append(score)
    scoreList.sort()
    return  scoreList

#This function use to count the frequency of each Score that Student acquired
def countFrequency(toiecScores,toiecScoreCheck):
    count=0
    for toiecScore in toiecScores:
        if toiecScoreCheck==toiecScore:
            count = count +1
    return  count

#this function print all score of Student and calculate the Frequency and Rate:
def frequencyIndividual(toiecReduceAndSortScores):
    print("Score\tFre\tFre. Rate")
    lenOfToiecScores=len(toiecScores)
    for toiecScoreCheck in toiecReduceAndSortScores:
        fre=countFrequency(toiecScores,toiecScoreCheck)
        rate=round((fre/lenOfToiecScores)*100,2)
        print (toiecScoreCheck,"\t",fre,'\t',rate,"%")

#this function use to show the Frequency and the Rate with complex range:
def frequencyClassified(toiecScores):
    counters =frequency(toiecScores)
    print("\tScore\t\tFre\t\tFre. Rate")
    for i in range(len(counters)):
        if counters[i]!=0:
            baseScore=i*100
            rate=round((counters[i]/len(toiecScores))*100,2)
            rightRange=baseScore+99
            if rightRange >990 :
                rightRange=990
            print("[",baseScore,"-",rightRange,"]","\t",counters[i],"\t\t",rate,"%")

#this function use to find a max value in an array
def findMaxValue(counters):
    max = 0
    for i in counters:
        if max<i:
            max=i
    return max

#this function get all max frequency that the same value
def max_frequency_all(toiecScores):
    counters = frequency(toiecScores)
    maxFrequency=findMaxValue(counters)
    list_scoreBase=[]#the list to store all scorebase that the same max frequency
    N=len(counters)
    for i in range(N):
        if maxFrequency==counters[i]:#if the same max value, we store in to the list
            list_scoreBase.append(i * 100)
    return list_scoreBase,maxFrequency
#this function gets the value: list_scoreBase,maxFrequency from max_frequency_all function and print data out
def printAllMaxFrequency():
    list_scoreBase,maxFrequency=max_frequency_all(toiecScores)
    print("Max Frequency = ",maxFrequency)
    print("The range of the Scores base have the same max frequency:")
    print("Score\tFre\t\tFre. Rate")
    rate = round((maxFrequency / len(toiecScores)) * 100, 2)
    for baseScore in list_scoreBase:
        print(baseScore, "\t", maxFrequency, "\t\t", rate, "%")

#this function use to find a min value in an array
def findMinValue(counters):
    min = findMaxValue(counters)
    for i in counters:
        if i!=0 and i<min:
            min=i
    return min

#this function get all min frequency that the same value
def min_frequency_all(toiecScores):
    counters = frequency(toiecScores)
    minFrequency=findMinValue(counters)
    list_scoreBase=[]#the list to store all scorebase that the same min frequency
    N=len(counters)
    for i in range(N):
        if minFrequency==counters[i]:#if the same max value, we store in to the list
            list_scoreBase.append(i * 100)
    return list_scoreBase,minFrequency

#this function gets the value: list_scoreBase,minFrequency from min_frequency_all function and print data out
def printAllMinFrequency():
    list_scoreBase,minFrequency=min_frequency_all(toiecScores)
    print("Min Frequency = ",minFrequency)
    print("The range of the Scores base have the same min frequency:")
    print("Score\tFre\t\tFre. Rate")
    rate = round((minFrequency / len(toiecScores)) * 100, 2)
    for baseScore in list_scoreBase:
        print(baseScore, "\t", minFrequency, "\t\t", rate, "%")

#this function use to calculate the Average Toiec Score that Student Acquired
def averageOfToiecScore(toiecScores):
    avg=sum(toiecScores)/len(toiecScores)
    return int(round(avg,0))

#test and debug functions:
# 1.List all Toiec Score for each Student acquired: Score-Frequency- Frequency rate

toiecReduceAndSortScores=reduceAndSortScores(toiecScores)
frequencyIndividual(toiecReduceAndSortScores)

# 2.List all Score with range comple for Student acquired: Base Score-Frequency- Frequency rate
frequencyClassified(toiecScores)

# 3.See all the scores with the same max frequency.
printAllMaxFrequency()

# 4.See all the scores with the same min frequency.
printAllMinFrequency()

# 5.A function to find the average of the TOEIC students acquired.
print("Average Toeic Score that Student acquired=",averageOfToiecScore(toiecScores))