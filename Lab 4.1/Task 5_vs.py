import string
from collections import Counter

def process_text(text):
    # Convert to lowercase
    lower_text = text.lower()
    # Add period at end if not present
    if not lower_text.strip().endswith('.'):
        lower_text = lower_text.strip() + '.'
    print("Converted text:")
    print(f"•\tConverted lowercase Sentence:{lower_text}")

    # Remove punctuation
    no_punct = lower_text.translate(str.maketrans('', '', string.punctuation))
    print(f"•\tSentence without any punctuation:{no_punct}")

    # Find most repeated word
    words = no_punct.split()
    if words:
        word_counts = Counter(words)
        most_common_word, _ = word_counts.most_common(1)[0]
        print(f"•\tThe most repeated word is :{most_common_word}")
    else:
        print("•\tThe most repeated word is :None")

if __name__ == "__main__":
    text = input("Enter the text: ")
    process_text(text)