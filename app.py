import nltk
import string
import re
import heapq

# Download required NLTK resources (first time only)
nltk.download('punkt')
nltk.download('punkt_tab')  # Needed for newer NLTK versions
nltk.download('stopwords')

# Load stopwords
stopwords = nltk.corpus.stopwords.words('english')

# -------- Preprocessing Function --------
def preprocess(text):
    formatted_text = text.lower()
    formatted_text = re.sub(r'\s+', ' ', formatted_text).strip()
    tokens = nltk.word_tokenize(formatted_text)

    # Remove stopwords and punctuation
    tokens = [word for word in tokens if word not in stopwords and word not in string.punctuation]
    formatted_text = ' '.join(tokens)

    return formatted_text

# -------- Percentage-based Summarization Function --------
def summarize(text, ratio=0.3):  # ratio = percentage of sentences to include
    formatted_text = preprocess(text)

    # Word frequency
    word_frequency = nltk.FreqDist(nltk.word_tokenize(formatted_text))
    highest_frequency = max(word_frequency.values())
    for word in word_frequency.keys():
        word_frequency[word] /= highest_frequency

    # Sentence scoring
    sentence_list = nltk.sent_tokenize(text)
    score_sentences = {}
    for sentence in sentence_list:
        for word in nltk.word_tokenize(sentence.lower()):
            if word in word_frequency:
                score_sentences[sentence] = score_sentences.get(sentence, 0) + word_frequency[word]

    # Determine number of sentences to select
    select_length = max(1, int(len(sentence_list) * ratio))

    # Pick top sentences
    best_sentences = heapq.nlargest(select_length, score_sentences, key=score_sentences.get)
    summary = ' '.join(best_sentences)
    return summary

# -------- Example Usage --------
if __name__ == "__main__":
    original_text = """Artificial Intelligence (AI) is transforming the world. 
    It is being applied in healthcare, education, finance, and many other industries. 
    AI can help solve problems and improve efficiency. 
    However, it also raises concerns about ethics and job replacement. 
    Researchers are working hard to ensure AI benefits humanity."""

    print("Original Text:\n", original_text)
    print("\nSummary (30% of sentences):\n", summarize(original_text, ratio=0.3))
