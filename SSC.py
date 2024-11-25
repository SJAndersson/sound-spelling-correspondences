from collections import defaultdict

#Function to get the index of the last vowel phoneme in a string
def getLastVowel(string):

    for i in range(len(string) - 1, -1, -1):

        if string[i] in "iɪuʊeəoɛæʌɔɑīōūyɜ":

            return i

    return -1

#Dictionary for sound-spelling correspondences
#Lightly edited from Wikipedia "English orthography"
#The phoneme transcriptions are a bit idiosyncratic
#but it's important that they are a single character
#I've included x for the sequence ks
#and y for the sequence ju
spelling = {}

spelling["m"] = ["m", "mm", "chm", "gm", "lm", "mb", "mh", "mn", "mp", "sm", "tm"]
spelling["n"] = ["pn", "ln", "gn", "dn", "kn", "mn", "mp", "n", "nt", "nd", "sn", "hn", "nh", "cn", "nn", "ng"]
spelling["ŋ"] = ["ngu", "n", "nd", "ngh", "nc", "ng"]
spelling["p"] = ["gh", "ph", "p", "pp", "lfp"]
spelling["b"] = ["bh", "b", "pb", "bb"]
spelling["t"] = ["d", "bt", "t", "ght", "cht", "th", "phth", "pt", "ct", "tt"]
spelling["d"] = ["dd", "d", "dh", "ddh", "t", "ld"]
spelling["k"] = ["kh", "kk", "cc", "lk", "qh", "ch", "q", "x", "k", "c", "ck", "cu", "g", "cq", "cqu", "cch", "qu"]
spelling["ɡ"] = ["g", "gh", "gu", "ckg", "gg"]
spelling["s"] = ["ss", "cc", "sw", "t", "st", "c", "tsw", "th", "z", "sh", "sth", "ts", "ps", "sc", "s", "tzs"]
spelling["z"] = ["cz", "sp", "ss", "zz", "ds", "x", "z", "tz", "sh", "sth", "ts", "sc", "s"]
spelling["ʃ"] = ["ss", "schsch", "psh", "sc", "s", "ch", "sch", "shi", "c", "ci", "sci", "zh", "ssi", "chsi", "chi", "ti", "sh", "si", "sj", "shh"]
spelling["ʒ"] = ["g", "zh", "ssi", "zi", "j", "ti", "z", "si", "ci", "s"]
spelling["f"] = ["u", "gh", "lf", "ft", "ff", "ph", "f", "v", "pph"]
spelling["v"] = ["ph", "w", "f", "v", "lv", "mh", "zv", "vv"]
spelling["θ"] = ["h", "chth", "th", "phth", "tth"]
spelling["ð"] = ["dd", "th", "dh"]
spelling["j"] = ["y", "j", "i", "ll", "r"]
spelling["h"] = ["h", "ch", "wh", "x", "j"]
spelling["r"] = ["wr", "l", "rh", "rr", "rrh", "rt", "r"]
spelling["l"] = ["sl", "lh", "ll", "l"]
spelling["w"] = ["u", "hw", "ww", "wh", "w", "hu", "o", "ou", "ju"]
spelling["ʧ"] = ["cz", "tsch", "cc", "ch", "t", "cs", "q", "chi", "c", "ti", "th", "tz", "tch", "ts", "tzsch", "tzs", "tsh"]
spelling["ʤ"] = ["g", "d", "ch", "jj", "dj", "j", "dg", "dzh", "di", "gi", "gg"]
spelling["x"] = ["cz", "cks", "cc", "cast", "xc", "xs", "qus", "xsc", "cs", "x", "xsw", "chs", "xx", "lks", "ks", "cqus"]

spelling["i"] = ["ix", "ui", "ea", "e", "ae", "eo", "ie", "ey", "oi", "ue", "iee", "uy", "y", "a", "is", "oe", "eye", "i", "ay", "ei", "ee"]
spelling["ɪ"] = ["ui", "ea", "o", "e", "ae", "ie", "ia", "ey", "ue", "uy", "y", "a", "oe", "eye", "i", "ei", "ee", "ai", "u", "ii"]
spelling["u"] = ["ougha", "wo", "ui", "o", "uo", "ough", "oeu", "eu", "ooe", "oo", "oup", "ue", "ieu", "ew", "oe", "u", "w", "eew", "ioux", "ou"]
spelling["ʊ"] = ["u", "or", "o", "w", "ou", "oo", "oul"]
spelling["e"] = ["oeh", "aa", "alf", "ea", "ete", "aie", "eh", "eg", "e", "au", "ae", "aig", "er", "ie", "eie", "ez", "eighe", "ey", "es", "ue", "ao", "a", "al", "eigh", "eye", "aye", "ee", "ay", "ai", "ei", "et", "aigh", "ere", "uet", "eig", "ais"]
spelling["ə"] = ["ui", "ua", "o", "ea", "uo", "eh", "wae", "e", "ough", "au", "eu", "ae", "eo", "ie", "anc", "oa", "ah", "eau", "oo", "oi", "ue", "y", "a", "oe", "oh", "op", "i", "ei", "ai", "u", "gh", "ou", "eou", "eig"]
spelling["o"] = ["o", "eaue", "ough", "au", "eo", "oa", "eau", "oo", "aux", "oughe", "owe", "ew", "oe", "ot", "oh", "ow", "ore", "w", "ou", "aoh"]
spelling["ɛ"] = ["ai", "ee", "u", "a", "ie", "oe", "ieu", "ea", "eh", "ei", "ue", "e", "ae", "eo", "ay"]
spelling["æ"] = ["ai", "au", "a", "al", "aa", "ea", "ag", "ah", "e", "i", "ar", "ei"]
spelling["ʌ"] = ["u", "wo", "a", "oe", "uddi", "o", "ou", "oo", "au"]
spelling["ɔ"] = ["u", "a", "al", "aughe", "aue", "o", "oa", "ough", "oh", "uo", "oo", "ou", "oss", "aw", "awe", "au", "eo", "augh"]
spelling["ɑ"] = ["ow", "a", "ach", "o", "oh", "eau", "ou", "au", "au", "a", "aa", "ea", "o", "aah", "ag", "ah", "aae", "aahe", "e", "i", "ae"]
spelling["ī"] = ["igh", "ui", "oy", "aie", "ae", "ie", "ia", "ey", "oi", "ic", "uy", "aille", "y", "is", "eigh", "eye", "ig", "aye", "i", "ei", "ay", "ai", "ye", "ighe", "uye", "ais"]
spelling["ō"] = ["oll", "uoy", "oy", "oye", "uoye", "oi", "eu", "awy"]
spelling["ū"] = ["ao", "odh", "ow", "o", "aow", "ou", "oughe", "aowe", "aw", "ough", "owe", "au"]
spelling["y"] = ["u", "ew", "iew", "ueue", "ewe", "ugh", "ui", "uu", "eu", "eau", "ou", "ut", "ue", "ieu", "eo"]
spelling["ɜ"] = ["ear", "irr", "erre", "olo", "eur", "ere", "or", "urr", "ore", "ur", "oeu", "eure", "yrrh", "our", "err", "ir", "er", "irre", "ueur", "urre", "yr"]

#Code to figure out sound-spelling alignment
#It goes through every phoneme from left to right
#And starts checking for sequences, in decreasing
#order of length, which could spell that phoneme
#If it finds a match, it updates the alignment
#and moves on to the next phoneme
#For a word like 'soup', it does not consider
#the possibility that /u/ might be spelled 'oup'
#as it is in 'coup', because it knows that if it
#considered that a match, that would leave no
#letters left to match up with the final /p/
#If you are interested in seeing how the
#algorithm works, uncomment the input
#statements in the for loops below, and run
#the program
def getAlignment(wordOrth, wordPhon):
    
    alignment = [-1] * len(wordOrth)

    for i in range(len(wordPhon)):

        #input("Current alignment: " + str(alignment))
        #input("Looking for sequence that spells: " + str(wordPhon[i]))
        
        for stop in range(len(alignment) - (len(wordPhon) - i - 1), alignment.index(-1), -1):

            #input("Does " + wordOrth[start:stop] + " spell " + str(wordPhon[i]) + "?")
            
            if wordOrth[alignment.index(-1):stop] in spelling[wordPhon[i]]:

                #input("Yes!")
                    
                for j in range(alignment.index(-1), stop):
                            
                    alignment[j] = i

                #input("Modified alignment: " + str(alignment))

                break

        if i not in alignment:

            #print("Could not find any letters which are pronounced " + wordPhon[i] + " in " + wordOrth[i])
            return []

    if not alignment:

        return []

    #Code designed specially to deal with silent E
    #If the last letter of a word is unassigned to
    #a phoneme, assign it to the last vowel
    if alignment[-1] == -1:

        alignment[-1] = getLastVowel(wordPhon)

    if -1 in alignment:

        return []

    return alignment

###Uncommend this code if you want to play around with single words
##wOrth = "pneumonia"
##wPhon = "numoniə"
##myAlign = getAlignment(wOrth, wPhon)
##
###Print a human-readable alignment of letters and sounds
##for i in range(len(myAlign)):
##
##    print(wOrth[i] + ": " + wPhon[myAlign[i]])
##
###How is every phoneme token in this word spelled?
###Print an alignment which answers this question
###For 'race', the phoneme /e/ is reported as
###being spelled a_e, with the _ marking other
###letters
##print("")
##
##tempSpelling = ""
##
##for i in range(len(wPhon)):
##
##    tempSpelling = ""
##
##    for j in range(len(myAlign)):
##
##        if myAlign[j] == i:
##
##            tempSpelling += wOrth[j]
##
##        if not myAlign[j] == i and len(tempSpelling) > 0:
##
##            if not tempSpelling[-1] == "_":
##
##                tempSpelling += "_"
##
##    if tempSpelling[-1] == "_":
##
##        tempSpelling = tempSpelling[:-1]
##
##    print(wPhon[i] + ": " + tempSpelling)

###Output the sound-spelling correspondences in the whole lexicon
#(ignoring words you can't analyze)
#This code also analyzes how commonly each phoneme is represented
#by any particular sequence of characters. E.g. how often
#is the vowel sound in 'head' written 'ea' vs. 'e' in English?
correspondences = defaultdict(lambda: defaultdict(lambda: 0))

orth = []
phon = []

tempAlign = []
tempSaveAlign = ""

saveOrth = []
savePhon = []
saveAlign = []

tempSpelling = ""

with open("newOrth.txt", encoding = "utf-8") as f:

    orth = f.read().split("\n")

with open("newPhon.txt", encoding = "utf-8") as f:

    phon = f.read().split("\n")

for i in range(len(phon)):

    tempSaveAlign = ""
    tempAlign = getAlignment(orth[i], phon[i])

    if tempAlign:

        saveOrth.append(orth[i])
        savePhon.append(phon[i])

        for j in range(len(tempAlign)):

            tempSaveAlign += str(tempAlign[j]) + ","

        saveAlign.append(tempSaveAlign[:-1])

        #Analyze frequencies of correspondences

        #input(phon[i])
        #input(str(tempAlign))
        
        for k in range(len(phon[i])):

            #input("Identifying correspondence of " + str(k) + ", i.e. " + phon[i][k])

            tempSpelling = ""

            for l in range(len(tempAlign)):

                if tempAlign[l] == k:

                    tempSpelling += orth[i][l]

                    #input("tempSpelling now: " + tempSpelling)

                if (not tempAlign[l] == k) and len(tempSpelling) > 0:

                    #input("Reached new letter")

                    if not tempSpelling[-1] == "_":

                        #input("Adding underscore")

                        tempSpelling += "_"

            if not tempSpelling:

                input(orth[i] + " " + phon[i] + ", " + str(tempAlign))

            if tempSpelling[-1] == "_":

                #input("Removing underscore")

                tempSpelling = tempSpelling[:-1]

            #input("Adding 1 to the count of times that " + phon[i][k] + " is spelled " + tempSpelling)

            correspondences[phon[i][k]][tempSpelling] += 1

saveOutput = ""

for i in range(len(savePhon)):

    saveOutput += saveOrth[i] + "\t" + savePhon[i] + "\t" + saveAlign[i] + "\n"

with open("alignedCMU.txt", encoding = "utf-8", mode = "w") as f:

    f.write(saveOutput)

#Write alignment statistics to a file
saveOutput = ""

for k, v in correspondences.items():

    saveOutput += "Ways to write " + k + " (spelling: frequency):\n"

    for innerK in sorted(v, key = v.get, reverse = True):

        saveOutput += "\t" + innerK + ": " + str(v[innerK]) + "\n"

with open("SSC frequencies.txt", encoding = "utf-8", mode = "w") as f:

    f.write(saveOutput)
