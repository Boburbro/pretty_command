def find_the_largest_word(words: list) -> int:
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
    return max_length


def format_text_in_box(words: list) -> str:
    largest_word_length = find_the_largest_word(words)
    border = "#" * (largest_word_length + 4)
    formatted_text = border + "\n"

    for word in words:
        padding = largest_word_length - len(word)
        formatted_text += f"# {word}{' ' * padding} #\n"

    formatted_text += border
    return formatted_text


file_name = input("Enter file name (or full path)>>> ")

with open(file_name, "r") as f:
    words = f.read().splitlines()

text_in_box = format_text_in_box(words)
print(text_in_box)
