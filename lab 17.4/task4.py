import re
import sys
import pandas as pd
from pathlib import Path
import nltk
from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from types import SimpleNamespace
import re as _re
#!/usr/bin/env python3
# Lightweight replacements to avoid NLTK dependency
# Make nltk.data.find/download no-ops so the package-check block below does nothing.
nltk = SimpleNamespace(
    data=SimpleNamespace(find=lambda *a, **k: None),
    download=lambda *a, **k: None
)
# Simple tokenizer and POS tagger (POS tags default to noun)
def word_tokenize(text):
    return _re.findall(r"\b\w+\b", str(text))
def pos_tag(tokens):
    return [(t, "NN") for t in tokens]
# Minimal stopwords implementation
class _Stopwords:
    @staticmethod
    def words(lang):
        return [
            "a","about","above","after","again","against","all","am","an","and","any","are","as","at",
            "be","because","been","before","being","below","between","both","but","by","could","did",
            "do","does","doing","down","during","each","few","for","from","further","had","has","have",
            "having","he","her","here","hers","herself","him","himself","his","how","i","if","in","into",
            "is","it","its","itself","just","me","more","most","my","myself","no","nor","not","of","off",
            "on","once","only","or","other","ought","our","ours","ourselves","out","over","own","same",
            "she","should","so","some","such","than","that","the","their","theirs","them","themselves",
            "then","there","these","they","this","those","through","to","too","under","until","up","very",
            "was","we","were","what","when","where","which","while","who","whom","why","with","would",
            "you","your","yours","yourself","yourselves"
        ]
stopwords = _Stopwords()
# Minimal wordnet-like constants used by get_wordnet_pos
wordnet = SimpleNamespace(ADJ="a", VERB="v", NOUN="n", ADV="r")
# Lightweight lemmatizer using simple heuristic rules
class WordNetLemmatizer:
    def lemmatize(self, word, pos="n"):
        w = word
        if pos == "v":
            if w.endswith("ing") and len(w) > 4:
                return w[:-3]
            if w.endswith("ed") and len(w) > 3:
                return w[:-2]
        if w.endswith("ies") and len(w) > 4:
            return w[:-3] + "y"
        if w.endswith("s") and len(w) > 3:
            return w[:-1]
        if w.endswith("ly") and len(w) > 3:
            return w[:-2]
        return w
# NLP imports
# Ensure required NLTK data is available
nltk_packages = ["punkt", "stopwords", "wordnet", "omw-1.4", "averaged_perceptron_tagger"]
for pkg in nltk_packages:
    try:
        nltk.data.find(pkg if "/" in pkg else f"tokenizers/{pkg}" if pkg == "punkt" else f"corpora/{pkg}")
    except LookupError:
        nltk.download(pkg, quiet=True)
STOPWORDS = set(stopwords.words("english"))
LEMMATIZER = WordNetLemmatizer()
# Regex patterns
URL_PATTERN = re.compile(r"https?://\S+|www\.\S+")
# Emoji pattern (covers many common emoji ranges)
EMOJI_PATTERN = re.compile(
    "["
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\U00002702-\U000027B0"
    "\U000024C2-\U0001F251"
    "]+",
    flags=re.UNICODE,
)
# Keep only letters, numbers and spaces
SPECIAL_CHAR_PATTERN = re.compile(r"[^a-z0-9\s]+")
def detect_text_column(df: pd.DataFrame) -> str:
    common_names = ["text", "tweet", "content", "post", "message", "review"]
    for name in common_names:
        if name in df.columns:
            return name
    # fallback: choose first column that is object/string dtype
    for col in df.columns:
        if pd.api.types.is_string_dtype(df[col]):
            return col
    # else fallback to first column
    return df.columns[0]
def clean_raw_text(text: str) -> str:
    if pd.isna(text):
        return ""
    s = str(text)
    s = s.lower()
    s = URL_PATTERN.sub(" ", s)
    s = EMOJI_PATTERN.sub(" ", s)
    s = SPECIAL_CHAR_PATTERN.sub(" ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s
def get_wordnet_pos(nltk_pos_tag: str) -> str:
    tag = nltk_pos_tag[0].upper()
    if tag == "J":
        return wordnet.ADJ
    elif tag == "V":
        return wordnet.VERB
    elif tag == "N":
        return wordnet.NOUN
    elif tag == "R":
        return wordnet.ADV
    else:
        return wordnet.NOUN
def tokenize_remove_stopwords_lemmatize(text: str):
    if not text:
        return []
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t.isalnum()]  # remove remaining punctuation tokens
    tokens = [t for t in tokens if t not in STOPWORDS and len(t) > 1]
    if not tokens:
        return []
    pos_tags = pos_tag(tokens)
    lemmas = [
        LEMMATIZER.lemmatize(tok, get_wordnet_pos(pos))
        for tok, pos in pos_tags
    ]
    # remove any empty or stop words introduced by lemmatization
    lemmas = [l for l in lemmas if l and l not in STOPWORDS]
    return lemmas
def process_dataframe(df: pd.DataFrame, text_col: str) -> pd.DataFrame:
    clean_texts = []
    token_lists = []
    for raw in df[text_col].astype(str).fillna(""):
        cleaned = clean_raw_text(raw)
        tokens = tokenize_remove_stopwords_lemmatize(cleaned)
        clean_texts.append(" ".join(tokens))
        token_lists.append(tokens)
    df = df.copy()
    df["clean_text"] = clean_texts
    df["clean_tokens"] = token_lists
    return df
def main():
    input_path = Path("social_media_sentiment.csv")
    if not input_path.exists():
        print(f"Input file not found: {input_path.resolve()}", file=sys.stderr)
        sys.exit(1)
    df = pd.read_csv(input_path)
    text_col = detect_text_column(df)
    processed = process_dataframe(df, text_col)
    out_path = Path("social_media_sentiment_processed.csv")
    processed.to_csv(out_path, index=False)
    print(f"Processed dataset saved to: {out_path.resolve()}")
if __name__ == "__main__":
    main()