# japanese kana flashcards

Learn kana using flashcards.  Each time you run, the script with select the flashcards in a random order. 


Use `uv` or `python` to run:

```sh
uv run flashcards_hiragana.py
```

```sh
uv run flashcards_katakana.py
```

--

Added a more general flashcard script: `flashcards_zenbu.py` which can take a csv file with two columns as input:

eg, `sat_vocabulary.csv` with [word, definition]  

Create flashcards content in Google Sheets or Excel, and export as CSV.  First row defines the flashcard front and back 'labels' (eg, word, definition)

```sh
uv run flashcards_zenbu.py sat_vocabulary.csv
```

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) here
