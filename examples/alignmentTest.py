'''
Created on Apr 11, 2017

An example of using the naive alignment code.  There are two functions
for naive alignment.  naiveWordAlignment and naivePhoneAlignment.  They
operate at the word and phone levels respectively.

Naive alignment is naive because it gives all phones the same length.
Word duration is then driven by the length of the utterance and the
number of phones in the word.

These functions are meant to maximize the efficiency of the transcription
process when forced aligners aren't available.

In general, for best performance, one should run 'naiveWordAlignment',
correct the output and then run 'naivePhoneAlignment' and correct the
output, unless the speech segments are very short and without a lot
of emotion or inflection (e.g. read speech).

@author: Tim
'''

from os.path import join

from praatio import tgio

from pysle import isletool
from pysle import praattools


inputFN = join(".", "files", "pumpkins_with_syllables.TextGrid")
outputFN = join(".", "files", "pumpkins_with_naive_alignment.TextGrid")

isleDict = isletool.LexicalTool(join(".", "files", 'ISLEdict_sample.txt'))

utteranceTierName = "utterance"
wordTierName = "word"
phoneListTierName = "phoneList"
phoneTierName = "phone"

tg = tgio.openTextGrid(inputFN)

for tierName in tg.tierNameList[:]:
    if tierName == utteranceTierName:
        continue
    tg.removeTier(tierName)
tg = praattools.naiveWordAlignment(tg, utteranceTierName, wordTierName,
                                   isleDict, phoneListTierName)
tg = praattools.naivePhoneAlignment(tg, wordTierName, phoneTierName,
                                    isleDict)
tg.save(outputFN)
