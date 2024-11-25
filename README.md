# sound-spelling-correspondences
Python code for adding sound-spelling correspondences to the CMU dictionary

## Description

This repo is based on the CMU dictionary, which contains phonetic transcrpitions of English words. The scripts create an alignment between spelling and pronunciation, creating outputs which look as follows:

specialize	spɛʃʌlīz	0,1,2,3,3,4,5,6,7,6

Here the orthographic word "specialize" has the pronunciation "spɛʃʌlīz" (in a modified version of the International Phonetic Alphabet), and the string "0,1,2,3,3,4,5,6,7,6" specifies the alignment between the two. The 0th letter corresponds to the 0th phoneme, the 1st to the 1st, the 2nd to the 2nd, and so on. Both the 3rd and the 4th letters, ci, correspond to the 3rd phoneme, ʃ. The final vowel sound is represented by an orthographic i + a final silent E, which is reflected in the alignment.

## Input

The scripts take as initial input two files derived from the CMUdict (version cmudict07b.txt): one called phon.txt which contains the ARPABET pronunciations of every word in the dictionary (one per line), and one called spell.txt which contains the spellings of every word in the dictionary (one per line). These files must crucially be aligned, so that a given line number contains information about the same word in both files.

## Output

The scripts first convert both input files to standardise formatting, including most notably a pseudo-IPA phonological transcription system where every sound is represented by a single character. The mappings between ARPABET and this transcription system are specified in the scripts. The outputs are saved as newPhon.txt and newOrth.txt, which each have one word per line. The scripts also output alignedCMU.txt, which is where the alignments are stored: each line contains information about one word, with spelling, pronunciation, and the alignment between the two separated by tabs. Finally, the scripts output SSC frequencies.txt, which shows the most frequent orthographic representations for each phoneme in English. It gives information like: the sound /f/ is spelled as "f" 1830 times, as "ff" 205" times, as "ph" 197 times, and as "gh" 20 times. This final output file is included in the repo.

## How to cite

Please cite the original source of the data as well as this repo. Suggested citations:

Andersson, S. (2024). sound-spelling-correspondences. <https://github.com/SJAndersson/sound-spelling-correspondences> [Accessed YYYY-MM-DD]

The Carnegie Mellon University Pronouncing Dictionary. Version 07b. Downloaded from: https://github.com/Alexir/CMUdict/blob/master/cmudict-0.7b [Accessed 2017-04-15]
