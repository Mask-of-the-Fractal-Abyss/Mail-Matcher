from read import *
import csv
                        
# [email, name, gender, location, introduction, interests, personality]
# registered time, email, password, name, location, gender, p0, p1, p2, interests, introduction

def cleanCsv(): # introverted thoughtful apathetic : extroverted sentimental empathetic
    indexed = list(csv.reader(open('Contact Information.csv')))
    for row in indexed:
        if countPasswords(indexed, row[2]) > 1:
            indexed.remove(row)
    for i in range(1, len(indexed)):
        userClass(row)
        indexed[i][-1] = ''
    csv.writer(open('Contact Information.csv', 'w')).writerows(indexed)
    
def updateMatched(newMatch, p):
    indexed = list(csv.reader(open('Contact Information.csv')))
    for i in range(len(indexed)):
        if indexed[i][2] == p:
            indexed[i][-1] += newMatch.password
    csv.writer(open('Contact Information.csv', 'w')).writerows(indexed)
            
def countPasswords(indexed, p):
    count = 0
    for u in indexed:
        if u[2] == p:
            count += 1
    return count

def match(male):
    topStrength = 0
    topMatch = None
    for female in userClass.females:
        if female not in male.getMatched():
            ms = male.matchStrength(female)
            if ms > topStrength:
                topStrength = ms
                topMatch = female
    updateMatched(female, male.password)
    return female        

def similarity(s1, s2, normalize=True):
    diff = abs(getAvgWordLen(s1) - getAvgWordLen(s2))
    diff += abs(getAvgSentenceLen(s1) - getAvgSentenceLen(s2))
    alphabet = 'abcdefghijklmnopqrstuvwxyz.,:;"\'?!'
    for letter in alphabet:
      diff += abs(s1.count('letter') - s2.count('letter')) // (len(s1) - len(s2))
    
    similarWords = 0
    s2Chomped = chomp(s2.lower()).split()
    for word1 in s1.lower().split():
        if len(word1) > 2:
            word1 = chomp(word1)
            similarWords += s2Chomped.count(word1)
            
    if normalize:
        return diff - 2 * (similarWords // (len(s1) + len(s2)))
    return diff - 2 * similarWords
        
        
def chomp(s):  # Took built in chomp method from ruby: removes everything that isn't a letter
    return ''.join(e for e in s if e.isalnum() or e == ' ')

def getAvgWordLen(s):
    avg = 0
    for word in s.split():
        avg += len(word)
    return avg // len(s.split())
  
def getAvgSentenceLen(s):
    avg = 0
    for sentence in s.split('.'):
        avg += len(sentence)
    return avg // len(s.split('.'))

class userClass:
    users = []
    males = []
    females = []
    
    def __init__(self, bio):
        bio = bio[1:-1]
##        couldn't unpack the values normally so I had to this verbose thing below

        self.email = bio[0]
        self.password = bio[1]
        self.name = bio[2]
        self.location = bio[3]
        self.age = bio[4]
        self.gender = bio[5].lower()
        self.p0 = bio[6]
        self.p1 = bio[7]
        self.p2 = bio[8]
        self.interests = bio[9]
        self.introduction = bio[10]
        
        userClass.users.append(self)
        if self.gender == 'male':
            userClass.males.append(self)
        else:
            userClass.females.append(self)
            
    def matchStrength(self, m):
        strength = 0
        strength += similarity(self.introduction, m.introduction, normalize=False)
        strength += similarity(self.interests, m.interests)
        strength += similarity(self.location, m.location)
        strength += similarity(str([self.p0, self.p1, self.p2]), str([m.p0, m.p1, m.p2]))
        return strength
    
    def getMatched(self):
        indexed = list(csv.reader(open('Contact Information.csv')))
        for i in range(len(indexed)):
            if indexed[i][2] == p:
                return indexed[i][-1]
        return None
