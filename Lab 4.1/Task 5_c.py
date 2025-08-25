import re
from collections import Counter


def normalize_spacing(text: str) -> str:
	"""Normalize whitespace: ensure single spaces and trim ends."""
	# Replace any whitespace run with a single space and strip
	return re.sub(r"\s+", " ", text).strip()


def ensure_space_after_punct(text: str) -> str:
	"""Ensure a single space after commas and end punctuation, without doubling spaces."""
	# Put a space after , ? ! . if not already followed by space
	text = re.sub(r"\s*([,?.!])\s*", r"\1 ", text)
	return normalize_spacing(text)


def to_lowercase_sentence(text: str) -> str:
	"""Convert to lowercase, normalize spacing around punctuation, and end with a period if missing."""
	lowered = text.lower()
	spaced = ensure_space_after_punct(lowered)
	# Ensure sentence ends with a terminal punctuation
	if not spaced.endswith(('.', '!', '?')):
		spaced = spaced + '.'
	return spaced


def remove_punctuation(text: str) -> str:
	"""Remove punctuation characters, keep letters/digits/underscore/whitespace, and normalize spaces."""
	no_punct = re.sub(r"[^\w\s]", "", text)
	return normalize_spacing(no_punct)


def most_frequent_word(text_without_punct: str) -> str:
	"""Compute the most frequent word; ties broken by first appearance order."""
	if not text_without_punct:
		return ""
	words = text_without_punct.split()
	if not words:
		return ""
	counts = Counter(words)
	# Break ties by first occurrence
	first_index = {word: idx for idx, word in enumerate(words) if word not in locals().get('first_index', {})}
	best_word = None
	best_count = -1
	best_pos = float('inf')
	for word, count in counts.items():
		pos = first_index[word]
		if count > best_count or (count == best_count and pos < best_pos):
			best_word = word
			best_count = count
			best_pos = pos
	return best_word or ""


def main() -> None:
	paragraph = input("Enter a paragraph: ")
	# Converted lowercase sentence with normalized punctuation spacing
	converted_lower = to_lowercase_sentence(paragraph)
	# Sentence without punctuation, normalized spacing (no forced trailing period)
	no_punct = remove_punctuation(converted_lower)
	# Compute most repeated word from punctuation-free, lowercase text
	most_repeated = most_frequent_word(no_punct)
	print("Converted text:")
	print(f"•\tConverted lowercase Sentence:{converted_lower}")
	print(f"•\tSentence without any punctuation:{no_punct}")
	print(f"•\tThe most repeated word is :{most_repeated}")


if __name__ == "__main__":
	main()
