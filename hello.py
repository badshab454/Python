#python // 
#hacker speak

def hacker_speak(txt):
    replacements_map = {
        "a": "4",
        "e": "3",
        "i": "1",
        "o": "0",
        "s": "5"
    }
    translation_table = str.maketrans(replacements_map)

    return txt.translate(translation_table)

print(hacker_speak("become a coder"))