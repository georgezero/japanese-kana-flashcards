import curses
import random
import csv
import sys
import os

# Default flashcards with metadata
default_flashcards = {
    "__meta__": {"front": "Katakana", "back": "Romanji"},
    "ア": "a", "イ": "i", "ウ": "u", "エ": "e", "オ": "o",
    "カ": "ka", "キ": "ki", "ク": "ku", "ケ": "ke", "コ": "ko",
    "サ": "sa", "シ": "shi", "ス": "su", "セ": "se", "ソ": "so",
    "タ": "ta", "チ": "chi", "ツ": "tsu", "テ": "te", "ト": "to",
    "ナ": "na", "ニ": "ni", "ヌ": "nu", "ネ": "ne", "ノ": "no",
    "ハ": "ha", "ヒ": "hi", "フ": "fu", "ヘ": "he", "ホ": "ho",
    "マ": "ma", "ミ": "mi", "ム": "mu", "メ": "me", "モ": "mo",
    "ヤ": "ya", "ユ": "yu", "ヨ": "yo", "ラ": "ra", "リ": "ri",
    "ル": "ru", "レ": "re", "ロ": "ro", "ワ": "wa", "ヲ": "wo",
    "ン": "n", "ガ": "ga", "ギ": "gi", "グ": "gu", "ゲ": "ge",
    "ゴ": "go", "ザ": "za", "ジ": "ji", "ズ": "zu", "ゼ": "ze",
    "ゾ": "zo", "ダ": "da", "ヂ": "ji", "ヅ": "zu", "デ": "de",
    "ド": "do", "バ": "ba", "ビ": "bi", "ブ": "bu", "ベ": "be",
    "ボ": "bo", "パ": "pa", "ピ": "pi", "プ": "pu", "ペ": "pe", "ポ": "po",
}

def load_csv_flashcards(file_path):
    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)
            if len(headers) < 2:
                raise ValueError("CSV must have at least two columns.")
            front, back = headers[0], headers[1]
            flashcards = {row[0]: row[1] for row in reader if len(row) >= 2}
            flashcards["__meta__"] = {"front": front, "back": back}
            return flashcards
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return None

def flashcard_app(stdscr, flashcards):
    stdscr.clear()
    stdscr.nodelay(False)

    front_label = flashcards.get("__meta__", {}).get("front", "Front")
    back_label = flashcards.get("__meta__", {}).get("back", "Back")

    flashcard_list = [(k, v) for k, v in flashcards.items() if k != "__meta__"]
    random.shuffle(flashcard_list)

    index = 0
    show_answer = False
    show_front_first = True
    total = len(flashcard_list)

    while True:
        stdscr.clear()
        front, back = flashcard_list[index]

        if show_front_first:
            stdscr.addstr(5, 2, f"{front_label}: {front}", curses.A_BOLD)
            stdscr.addstr(8, 2, f"{back_label}: {back}" if show_answer else f"{back_label}: ", curses.A_BOLD if show_answer else curses.A_DIM)
        else:
            stdscr.addstr(5, 2, f"{back_label}: {back}", curses.A_BOLD)
            stdscr.addstr(8, 2, f"{front_label}: {front}" if show_answer else f"{front_label}: ", curses.A_BOLD if show_answer else curses.A_DIM)

        stdscr.addstr(16, 2, f"Card {index + 1} of {total}")
        stdscr.addstr(18, 2, "Press any key to reveal answer.")
        stdscr.addstr(19, 2, "Press any key again for next card.")
        stdscr.addstr(20, 2, "Press 'P' to go back.")
        stdscr.addstr(21, 2, "Press 'M' to toggle front/back order.")
        stdscr.addstr(22, 2, "Press 'Q' to quit.")
        stdscr.refresh()

        key = stdscr.getch()
        if key in [ord("q"), ord("Q")]:
            break
        elif key in [ord("p"), ord("P")]:
            if index > 0:
                index -= 1
                show_answer = False
        elif key in [ord("m"), ord("M")]:
            show_front_first = not show_front_first
        else:
            if show_answer:
                if index < len(flashcard_list) - 1:
                    index += 1
                    show_answer = False
            else:
                show_answer = True

    stdscr.clear()
    stdscr.addstr(5, 2, "Flashcard session ended.", curses.A_BOLD)
    stdscr.addstr(7, 2, "Press any key to exit.")
    stdscr.refresh()
    stdscr.getch()

if __name__ == "__main__":
    flashcards = default_flashcards
    if len(sys.argv) > 1 and os.path.isfile(sys.argv[1]):
        csv_flashcards = load_csv_flashcards(sys.argv[1])
        if csv_flashcards:
            flashcards = csv_flashcards
    curses.wrapper(flashcard_app, flashcards)

