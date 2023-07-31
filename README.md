

# Text and wav to phoneme (IPA)


## intall package
```
pip install -r requirements.txt
```



## text to phoneme (IPA)

```bash
eng-to-ipa.py
```

ɔl idealisation* meɪks laɪf ˈpurər



## wav to phoneme (IPA)
```bash
python wav2vec2-ljspeech-gruut-w2p.py
```
ɔ l d ə l ɪ z eɪ ʃ ə n m eɪ k s l aɪ f p ʊ ɹ



## Comparison methodology
Use difflib.SequenceMatcher

```python
seq1 = ɔlidealizationmeɪkslaɪfˈpurər
seq2 = ɔldəlɪzeɪʃənmeɪkslaɪfpʊɹ
```

`python calculate_differency.py`
> [('equal', 0, 2, 0, 2), ('delete', 2, 3, 2, 2), ('equal', 3, 4, 2, 3), ('insert', 4, 4, 3, 7), ('equal', 4, 5, 7, 8), ('replace', 5, 13, 8, 11), ('equal', 13, 23, 11, 21), ('delete', 23, 24, 21, 21), ('equal', 24, 25, 21, 22), ('replace', 25, 29, 22, 24)]


## ffmpeg

Use ffmpeg to convert any other format to wav
```bash
ffmpeg -i sample.flac sample.wav
```