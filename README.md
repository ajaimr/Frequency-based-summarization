# Frequency-Based Text Summarizer

A Python project that automatically summarizes paragraphs by selecting the most important sentences based on word frequency.

## Overview
This project uses **Natural Language Processing (NLP)** techniques to perform **extractive text summarization**. It analyzes a paragraph, calculates word frequencies, scores each sentence, and generates a concise summary by picking the most relevant sentences.

### How It Works
1. **Preprocessing the text**
   - Converts text to lowercase
   - Removes stopwords and punctuation

2. **Calculating word frequency**
   - Counts the occurrence of each word
   - Normalizes word frequencies

3. **Scoring sentences**
   - Each sentence is scored based on the sum of word frequencies

4. **Selecting important sentences**
   - Chooses the top sentences dynamically using a **percentage-based approach**
   - Generates a concise summary of the text

### Features
- Works for **any length of paragraph**
- Adjustable **summary ratio** (e.g., 30% of sentences)
- Easy to extend for longer documents

### Technologies Used
- Python 3
- NLTK (Natural Language Toolkit)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/frequency-based-summarizer.git
