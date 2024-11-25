transcription = {}

transcription["AY"] = "ī"
transcription["ER"] = "ɜ"
transcription["IY"] = "i"
transcription["K"] = "k"
transcription["L"] = "l"
transcription["R"] = "r"
transcription["T"] = "t"
transcription["AW"] = "ū"
transcription["M"] = "m"
transcription["AE"] = "æ"
transcription["JH"] = "ʤ"
transcription["AA"] = "ɑ"
transcription["OW"] = "o"
transcription["ZH"] = "ʒ"
transcription["DH"] = "ð"
transcription["G"] = "ɡ"
transcription["CH"] = "ʧ"
transcription["V"] = "v"
transcription["P"] = "p"
transcription["S"] = "s"
transcription["UW"] = "u"
transcription["IH"] = "ɪ"
transcription["TH"] = "θ"
transcription["SH"] = "ʃ"
transcription["EX"] = "ə"
transcription["D"] = "d"
transcription["B"] = "b"
transcription["EH"] = "ɛ"
transcription["EY"] = "e"
transcription["HH"] = "h"
transcription["NG"] = "ŋ"
transcription["W"] = "w"
transcription["AO"] = "ɔ"
transcription["Z"] = "z"
transcription["AH"] = "ʌ"
transcription["Y"] = "j"
transcription["OY"] = "ō"
transcription["F"] = "f"
transcription["N"] = "n"
transcription["UH"] = "ʊ"

def retranscribe(string):

    newString = ""

    for phoneme in string.split(" "):

        if phoneme:

            newString += transcription[phoneme]

    newString = newString.replace("ks", "x")
    newString = newString.replace("ju", "y")

    return newString

def filt(string):

    return "".join([c for c in string if c in "abcdefghijklmnopqrstuvwxyz"])

phon = []

with open("phon.txt") as f:

    phon = f.read().replace("0", "").replace("1", "").replace("2", "").split("\n")

orth = []

with open("spell.txt") as f:

    orth = f.read().lower().split("\n")

newPhon = []
newOrth = []

for i in range(len(orth)):

    if orth[i] == filt(orth[i]):

        newPhon.append(retranscribe(phon[i]))
        newOrth.append(orth[i])

with open("newPhon.txt", encoding = "utf-8", mode = "w") as f:

    f.write("\n".join(newPhon))

with open("newOrth.txt", encoding = "utf-8", mode = "w") as f:

    f.write("\n".join(newOrth))
