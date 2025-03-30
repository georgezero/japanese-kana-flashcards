import curses
import random

# Katakana dictionary
katakana_dict = {
    "ア": "a", "イ": "i", "ウ": "u", "エ": "e", "オ": "o",
    "カ": "ka", "キ": "ki", "ク": "ku", "ケ": "ke", "コ": "ko",
    "サ": "sa", "シ": "shi", "ス": "su", "セ": "se", "ソ": "so",
    "タ": "ta", "チ": "chi", "ツ": "tsu", "テ": "te", "ト": "to",
    "ナ": "na", "ニ": "ni", "ヌ": "nu", "ネ": "ne", "ノ": "no",
    "ハ": "ha", "ヒ": "hi", "フ": "fu", "ヘ": "he", "ホ": "ho",
    "マ": "ma", "ミ": "mi", "ム": "mu", "メ": "me", "モ": "mo",
    "ヤ": "ya", "ユ": "yu", "ヨ": "yo",
    "ラ": "ra", "リ": "ri", "ル": "ru", "レ": "re", "ロ": "ro",
    "ワ": "wa", "ヲ": "wo", "ン": "n",
    "ガ": "ga", "ギ": "gi", "グ": "gu", "ゲ": "ge", "ゴ": "go",
    "ザ": "za", "ジ": "ji", "ズ": "zu", "ゼ": "ze", "ゾ": "zo",
    "ダ": "da", "ヂ": "ji", "ヅ": "zu", "デ": "de", "ド": "do",
    "バ": "ba", "ビ": "bi", "ブ": "bu", "ベ": "be", "ボ": "bo",
    "パ": "pa", "ピ": "pi", "プ": "pu", "ペ": "pe", "ポ": "po"
}

# Katakana dictionary (one per line)
katakana_dict = {
    "ア": "a",
    "イ": "i",
    "ウ": "u",
    "エ": "e",
    "オ": "o",
    "カ": "ka",
    "キ": "ki",
    "ク": "ku",
    "ケ": "ke",
    "コ": "ko",
    "サ": "sa",
    "シ": "shi",
    "ス": "su",
    "セ": "se",
    "ソ": "so",
    "タ": "ta",
    "チ": "chi",
    "ツ": "tsu",
    "テ": "te",
    "ト": "to",
    "ナ": "na",
    "ニ": "ni",
    "ヌ": "nu",
    "ネ": "ne",
    "ノ": "no",
    "ハ": "ha",
    "ヒ": "hi",
    "フ": "fu",
    "ヘ": "he",
    "ホ": "ho",
    "マ": "ma",
    "ミ": "mi",
    "ム": "mu",
    "メ": "me",
    "モ": "mo",
    "ヤ": "ya",
    "ユ": "yu",
    "ヨ": "yo",
    "ラ": "ra",
    "リ": "ri",
    "ル": "ru",
    "レ": "re",
    "ロ": "ro",
    "ワ": "wa",
    "ヲ": "wo",
    "ン": "n",
    "ガ": "ga",
    "ギ": "gi",
    "グ": "gu",
    "ゲ": "ge",
    "ゴ": "go",
    "ザ": "za",
    "ジ": "ji",
    "ズ": "zu",
    "ゼ": "ze",
    "ゾ": "zo",
    "ダ": "da",
    "ヂ": "ji",
    "ヅ": "zu",
    "デ": "de",
    "ド": "do",
    "バ": "ba",
    "ビ": "bi",
    "ブ": "bu",
    "ベ": "be",
    "ボ": "bo",
    "パ": "pa",
    "ピ": "pi",
    "プ": "pu",
    "ペ": "pe",
    "ポ": "po",
}


# Function to display flashcards
def flashcard_app(stdscr):
    stdscr.clear()
    stdscr.nodelay(False)  # Wait for user input

    # Shuffle katakana list
    katakana_list = list(katakana_dict.items())
    random.shuffle(katakana_list)

    index = 0  # Keeps track of the current flashcard
    show_romaji = False  # Initially, romaji is hidden
    show_katakana_first = True  # Initially show Katakana first

    while True:
        stdscr.clear()

        # Get the current katakana and romaji
        katakana, romaji = katakana_list[index]

        # if show_katakana_first:
        #     # Show Katakana first, Romaji is hidden
        #     stdscr.addstr(5, 10, f"Katakana: {katakana}", curses.A_BOLD)
        #     stdscr.addstr(7, 10, "Romaji: ", curses.A_DIM)
        # else:
        #     # Show Romaji first, Katakana is hidden
        #     stdscr.addstr(5, 10, f"Romaji: {romaji}", curses.A_BOLD)
        #     stdscr.addstr(7, 10, "Katakana: ", curses.A_DIM)

        if show_katakana_first:
            stdscr.addstr(5, 10, f"Katakana: {katakana}", curses.A_BOLD)
            if show_romaji:
                stdscr.addstr(7, 10, f"Romaji: {romaji}", curses.A_BOLD)
            else:
                stdscr.addstr(7, 10, "Romaji: ", curses.A_DIM)
        else:
            stdscr.addstr(5, 10, f"Romaji: {romaji}", curses.A_BOLD)
            if show_romaji:
                stdscr.addstr(7, 10, f"Katakana: {katakana}", curses.A_BOLD)
            else:
                stdscr.addstr(7, 10, "Katakana: ", curses.A_DIM)

        # Instructions
        stdscr.addstr(10, 10, "Press any key to reveal answer.")
        stdscr.addstr(11, 10, "Press any key again for next card.")
        stdscr.addstr(12, 10, "Press 'P' to go back.")
        stdscr.addstr(13, 10, "Press 'M' to toggle Katakana/Romaji order.")
        stdscr.addstr(14, 10, "Press 'Q' to quit.")

        stdscr.refresh()

        key = stdscr.getch()

        if key in [ord("q"), ord("Q")]:  # Quit the program
            break
        elif key in [ord("p"), ord("P")]:  # Go back to previous flashcard
            if index > 0:
                index -= 1
                show_romaji = False  # Reset romaji visibility
        elif key in [
            ord("m"),
            ord("M"),
        ]:  # Toggle between Katakana first or Romaji first
            show_katakana_first = not show_katakana_first
        else:  # Any other key advances the flashcard or reveals romaji
            if show_romaji:
                if index < len(katakana_list) - 1:
                    index += 1
                    show_romaji = False  # Reset romaji visibility
            else:
                show_romaji = True  # Reveal romaji

    # Exit message
    stdscr.clear()
    stdscr.addstr(5, 10, "Flashcard session ended.", curses.A_BOLD)
    stdscr.addstr(7, 10, "Press any key to exit.")
    stdscr.refresh()
    stdscr.getch()


# Run the flashcard app using curses
curses.wrapper(flashcard_app)
