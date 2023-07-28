

# Text and wav to phoneme (IPA)



## text to phoneme (IPA)

```bash
eng-to-ipa.py
```

hɛˈloʊ, ɪts ˈfrɛdrɪk.



## wav to phoneme (IPA)
```bash
python wav2vec2-ljspeech-gruut-w2p.py
```
ɪ ɪ n m oʊ m ə n t s ə v d i p f i l ɪ n ə l aɪ k s ʌ n b ɚ s t s ə v p ɹ ɑ s p ɛ ɹ ə t i æ z ɪ n d ɑ ɹ k ɚ aʊ ɚ z m æ n m ʌ s t b i ə l oʊ n



## Comparison methodology

1. Text to IPA conversion: Convert the written text to IPA using eng_to_ipa as shown before. Let's call this transcription "A".

2. Speech to IPA conversion: For converting speech to IPA, you need an Automatic Speech Recognition (ASR) system that outputs IPA transcriptions. As of my knowledge cutoff in September 2021, there aren't any widely available pre-trained models that output IPA directly. However, you could take an ASR system that outputs ARPABET and then map these phonemes to IPA. This step might require some manual intervention to ensure accuracy of the mapping. Let's call this transcription "B".

3. Alignment and Comparison: For comparing A and B, you'll likely want to use a sequence alignment algorithm, such as the Levenshtein distance (also known as "edit distance"). This algorithm measures the minimum number of insertions, deletions, and substitutions that are necessary to change one sequence into another. You could use this to measure the difference between the expected IPA (A) and the actual IPA (B).

4. Accuracy Calculation: You can calculate the accuracy as the ratio of the number of correctly pronounced phonemes to the total number of phonemes. For example, if there are 100 phonemes and 5 of them are mispronounced, the accuracy would be 95%.