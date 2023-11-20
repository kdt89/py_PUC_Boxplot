
import string

def replace_special_characters(text, accepted_character):
    for wildcard in string.punctuation:
        text = text.replace(wildcard, accepted_character)

    return text

# Example usage
text = "Hello|world|how|are|you"
accepted_character = "-"


new_text = replace_special_characters(text, accepted_character)
print(new_text)  # Output: Hello-world-how-are-you