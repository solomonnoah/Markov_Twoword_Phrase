import re
import random as rand
import time
sample = input("Sample text: ")
num_of_sentences = int(input("How many sentences do you want? "))

sentences = sample.split(". ")
sample = re.sub("[^a-zA-Z ]+", "", sample)
clean = sample.split(' ')
clean = [x.lower() for x in clean]

sentence_lengths = []
for sent in sentences:
    sent = sent.split()
    sentence_lengths.append(len(sent))
    
sentlist = []
for sent in sentences:
    listsent = sent.split()
    firstword = listsent[0]
    firstword = re.sub("[^a-zA-Z ]+", "", firstword)
    sentlist.append(firstword)
    
mastdict = {}
for i in range (0, len(clean)-1):
    mastdict[clean[i]] = {}
    
for master_word in mastdict:
    temp_master_word_list = []
    for i in range (1, len(clean)-1):
        if clean[i-1] == master_word:
            twp = []
            twp.append(clean[i])
            twp.append(clean[i+1])
            temp_master_word_list.append(twp)
    mastdict[master_word] = temp_master_word_list
    
for i in range(num_of_sentences):
    sent = []
    first_word = rand.choice(sentlist)
    sent.append(first_word.title())

    for i in range (rand.choice(sentence_lengths)-1):
        if i == 0:
            prev_word = first_word
        next_two_word_phrase = rand.choice(mastdict[prev_word.lower()])
        for word in next_two_word_phrase:
            sent.append(word.lower())
        prev_word = next_two_word_phrase[-1]

    print(" ".join(sent) +". ", end = "")
    
