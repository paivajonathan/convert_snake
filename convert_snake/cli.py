import sys
import unicodedata
import re


def remove_accents(text):
    nfkd = unicodedata.normalize('NFKD', text)
    return "".join([c for c in nfkd if not unicodedata.combining(c)])


def to_snake_case(text):
    text = remove_accents(text)
    text = text.replace(" ", "_")
    text = re.sub(r'\W+', '', text)  # substitui não-alfanuméricos por ""
    return text.upper()


def main():
    if len(sys.argv) < 2:
        print("Uso: convert_snake <texto para converter>")
    else:
        input_string = " ".join(sys.argv[1:])
        print(to_snake_case(input_string))


if __name__ == "__main__":
    main()
