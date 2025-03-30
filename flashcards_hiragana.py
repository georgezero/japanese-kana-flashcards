# flashcards_hiragana.py

import curses
import random

# Hiragana dictionary
hiragana_dict = {
    "あ": "a", "い": "i", "う": "u", "え": "e", "お": "o",
    "か": "ka", "き": "ki", "く": "ku", "け": "ke", "こ": "ko",
    "さ": "sa", "し": "shi", "す": "su", "せ": "se", "そ": "so",
    "た": "ta", "ち": "chi", "つ": "tsu", "て": "te", "と": "to",
    "な": "na", "に": "ni", "ぬ": "nu", "ね": "ne", "の": "no",
    "は": "ha", "ひ": "hi", "ふ": "fu", "へ": "he", "ほ": "ho",
    "ま": "ma", "み": "mi", "む": "mu", "め": "me", "も": "mo",
    "や": "ya", "ゆ": "yu", "よ": "yo",
    "ら": "ra", "り": "ri", "る": "ru", "れ": "re", "ろ": "ro",
    "わ": "wa", "を": "wo", "ん": "n",
    "が": "ga", "ぎ": "gi", "ぐ": "gu", "げ": "ge", "ご": "go",
    "ざ": "za", "じ": "ji", "ず": "zu", "ぜ": "ze", "ぞ": "zo",
    "だ": "da", "ぢ": "ji", "づ": "zu", "で": "de", "ど": "do",
    "ば": "ba", "び": "bi", "ぶ": "bu", "べ": "be", "ぼ": "bo",
    "ぱ": "pa", "ぴ": "pi", "ぷ": "pu", "ぺ": "pe", "ぽ": "po"
}

def flashcard_app(stdscr):
    stdscr.clear()
    stdscr.nodelay(False)

    # Shuffle hiragana list
    hiragana_list = list(hiragana_dict.items())
    random.shuffle(hiragana_list)

    index = 0
    show_answer = False
    show_hiragana_first = True
    total = len(hiragana_list)

    while True:
        stdscr.clear()
        hiragana, romaji = hiragana_list[index]

        if show_hiragana_first:
            stdscr.addstr(5, 10, f"Hiragana: {hiragana}", curses.A_BOLD)
            if show_answer:
                stdscr.addstr(7, 10, f"Romaji: {romaji}", curses.A_BOLD)
            else:
                stdscr.addstr(7, 10, "Romaji: ", curses.A_DIM)
        else:
            stdscr.addstr(5, 10, f"Romaji: {romaji}", curses.A_BOLD)
            if show_answer:
                stdscr.addstr(7, 10, f"Hiragana: {hiragana}", curses.A_BOLD)
            else:
                stdscr.addstr(7, 10, "Hiragana: ", curses.A_DIM)

        # Flashcard counter
        stdscr.addstr(10, 10, f"Card {index + 1} of {total}")

        # Instructions
        stdscr.addstr(12, 10, "Press any key to reveal answer.")
        stdscr.addstr(13, 10, "Press any key again for next card.")
        stdscr.addstr(14, 10, "Press 'P' to go back.")
        stdscr.addstr(15, 10, "Press 'M' to toggle Hiragana/Romaji order.")
        stdscr.addstr(16, 10, "Press 'Q' to quit.")

        stdscr.refresh()

        key = stdscr.getch()

        if key in [ord("q"), ord("Q")]:
            break
        elif key in [ord("p"), ord("P")]:
            if index > 0:
                index -= 1
                show_answer = False
        elif key in [ord("m"), ord("M")]:
            show_hiragana_first = not show_hiragana_first
        else:
            if show_answer:
                if index < len(hiragana_list) - 1:
                    index += 1
                    show_answer = False
            else:
                show_answer = True

    stdscr.clear()
    stdscr.addstr(5, 10, "Flashcard session ended.", curses.A_BOLD)
    stdscr.addstr(7, 10, "Press any key to exit.")
    stdscr.refresh()
    stdscr.getch()

# Run the flashcard app using curses
curses.wrapper(flashcard_app)

