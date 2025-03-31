# japanese kana flashcards

Help from ChatGPT

```sh
uv run flashcards_hiragana.py
```

```sh
uv run flashcards_katakana.py
```

--
Update: added `flashcards_zenbu.py` and sample csv file (`sat_vocabulary.csv`) with some [word, definition] examples.  Can use as a general flashcard tool. 

Create flashcards in Google Sheets or Excel, and export as CSV.  First row defines the flashcard front and back 'labels' (eg, Word, Definition)

```sh
uv run flashcards_zenbu.py sat_vocabulary.csv
```


Can install [uv](https://docs.astral.sh/uv/getting-started/installation/) here
