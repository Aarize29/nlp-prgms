# -*- coding: utf-8 -*-
"""NLP PRGRMS.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_-O4-8cOF7A0px_k83a2KHbg-FMCntg-
"""

#nlp prgrms
# w/t packages

#1.Study of Python and basic commands to access text data. (from notepad, pdf, word documents,online)

# Open a text file and read its contents
with open('/content/txt_file.txt', 'r') as file:
    content = file.read()
    print(content)

# Path to your PDF file
pdf_path = '/content/pdf.pdf'

# Open the PDF file in binary mode
with open(pdf_path, 'rb') as file:
    # Read the raw binary content
    content = file.read()

    # Print the raw content (for illustration purposes)
    print(content[:100])  # Print the first 100 bytes as an example

# Open a Word document and read its raw binary contents
with open('/content/cop.docx', 'rb') as file:
    content = file.read()
    # Convert bytes to string (assuming the text is ASCII encoded)
    text = content.decode('ascii', errors='ignore')
    print(text)

#2.Perform text pre - processing on a given corpus without using any pre -defined NLP packages.

import pandas as pd
import re

# Sample data creation (replace this with your actual data loading logic)
data = {'content': ["The weather was beautiful. I went for a walk in the park. It was a sunny day, and the birds were chirping happily. Suddenly, a black cat crossed my path. I stopped and watched it disappear into the bushes. After that, I continued my stroll, enjoying the tranquility of nature."]}
df = pd.DataFrame(data)

def clean_text(text):
    # Remove non-alphabetic characters
    text = re.sub(r'[^A-Za-z\s]', '', text)
    # Convert to lowercase
    text = text.lower()
    # Tokenize
    tokens = text.split()
    # Remove stopwords
    stop_words = set(["is", "an", "the", "this", "another", "i", "it", "was", "in", "for", "a", "and", "of", "my"]) # Add more as needed
    tokens = [word for word in tokens if word not in stop_words]
    # Stemming (using a simple example)
    tokens = [word[:-1] if word.endswith('s') else word for word in tokens]
    # Lemmatization (using a simple example)
    tokens = [word[:-1] if word.endswith('s') else word for word in tokens]
    return ' '.join(tokens)

# Apply the cleaning function to the DataFrame
df['cleaned_content'] = df['content'].apply(clean_text)

# Print the resulting DataFrame
print(df)

#3.)Implement N -Gram model in python without using any predefined NLPpackages. Note: use corpus of your own choice.
import pandas as pd

# Sample data creation
data = {'cleaned_content': ["this is an example sentence", "another example sentence"]}
df = pd.DataFrame(data)

# Function to generate n-grams
def generate_ngrams(text, n):
    tokens = text.split()
    ngrams_list = [' '.join(tokens[i:i+n]) for i in range(len(tokens)-n+1)]
    return ngrams_list

# Apply the function to generate bigrams
df['bigrams'] = df['cleaned_content'].apply(generate_ngrams, n=2)

# Print the dataframe
print(df)

#4. Implement Part-of-Speech (POS) Tagging.
# "The cat chased the mouse around the house. Birds sang in the trees while the
# sun shone brightly in the sky. A group of children played happily in the park,
# laughing and running around.”

import pandas as pd

# Sample data creation with provided text
data = {'cleaned_content': [
    "The cat chased the mouse around the house. Birds sang in the trees while the sun shone brightly in the sky. A group of children played happily in the park, laughing and running around."
]}
df = pd.DataFrame(data)

# Function to generate simple POS tags (Noun, Verb, Adverb)
def simple_pos_tagging(text):
    tokens = text.split()
    pos_tags = []
    for token in tokens:
        if token.endswith('ing'):
            pos_tags.append((token, 'Verb'))
        elif token.endswith('ly'):
            pos_tags.append((token, 'Adverb'))
        else:
            pos_tags.append((token, 'Noun'))
    return pos_tags

# Apply the function to generate POS tags
df['pos_tags'] = df['cleaned_content'].apply(simple_pos_tagging)

# Print the dataframe
print(df)

#5.Implement chunking to extract Noun Phrases.
import pandas as pd

# Sample data creation
data = {
    'POS_tags': [
        [('this', 'Noun'), ('is', 'Noun'), ('an', 'Noun'), ('example', 'Noun'), ('sentence', 'Noun')],
        [('another', 'Noun'), ('example', 'Noun'), ('sentence', 'Noun')]
    ]
}
df = pd.DataFrame(data)

# Function to perform simple noun phrase chunking
def simple_noun_phrase_chunking(pos_tags):
    noun_phrases = []
    current_phrase = []
    for token, tag in pos_tags:
        if tag in ['Noun', 'Adjective']:
            current_phrase.append(token)
        elif current_phrase:
            noun_phrases.append(' '.join(current_phrase))
            current_phrase = []
    if current_phrase:
        noun_phrases.append(' '.join(current_phrase))
    return noun_phrases

# Apply the function to generate noun phrases
df['noun_phrases'] = df['POS_tags'].apply(simple_noun_phrase_chunking)

# Print the dataframe
print(df)

#6.Sentence completion with words or phrases using random prompts.
import random

# Dictionary with sentence prompts and possible completions
sentence_prompts = {
    "She opened the door and saw a": ["beautiful garden", "mysterious figure", "bright light"],
    "After a long day at work, I like to relax by": ["watching my favorite TV show", "going for a walk", "reading a book"]
}

input_prompt = "After a long day at work, I like to relax by"

if input_prompt in sentence_prompts:
    possible_completions = sentence_prompts[input_prompt]
    print("Possible Completions:")
    for completion in possible_completions:
        print(f"- {input_prompt} {completion}")
else:
    print("Prompt not found in the dictionary.")

# Use random to create a random sentence completion
random_completion = random.choice(["enjoying a cup of tea", "listening to music", "playing video games"])
print(f"- {input_prompt} {random_completion}")

#7.Implement machine learning sentiment classification without using any pre defined NLP packages:
'''Training Corpus:
("I love this product", "positive"),
("This is excellent", "positive"),
("Terrible service", "negative"),
("It's okay, not great", "neutral"),
("Amazing experience", "positive"),
("Disappointing outcome", "negative"),
("Neutral feelings", "neutral"),
("I dislike it", "negative")'''

# Sample data
data = ["I love this product!", "It's terrible.", "Neutral statement."]

# Training corpus
training_corpus = [
    ("I love this product", "positive"),
    ("This is excellent", "positive"),
    ("Terrible service", "negative"),
    ("It's okay, not great", "neutral"),
    ("Amazing experience", "positive"),
    ("Disappointing outcome", "negative"),
    ("Neutral feelings", "neutral"),
    ("I dislike it", "negative")
]

# Function to determine sentiment label
def determine_sentiment_label(text):
    # Check using predefined keywords
    if "love" in text.lower():
        return 'positive'
    elif "terrible" in text.lower():
        return 'negative'
    else:
        # Check using the training corpus
        for corpus_text, label in training_corpus:
            if corpus_text.lower() in text.lower():
                return label
        # Default to neutral if no match found
        return 'neutral'

# Create result dictionary
result_dict = {'text': data, 'label': [determine_sentiment_label(text) for text in data]}

# Print results
for text, label in zip(result_dict['text'], result_dict['label']):
    print(f"Text: {text}")
    print(f"Label: {label}")
    print()

#or 7b.
data = ["I love this product!", "It's terrible.", "Neutral statement."]

def determine_sentiment_label(text):
    if "love" in text.lower():
        return 'positive'
    elif "terrible" in text.lower():
        return 'negative'
    else:
        return 'neutral'

result_dict = {'text': data, 'label': [determine_sentiment_label(text) for text in data]}

for text, label in zip(result_dict['text'], result_dict['label']):
    print(f"Text: {text}")
    print(f"Label: {label}")
    print()

#8.Text Summarization (Extractive and Abstractive)
def simple_summarization(article, num_sentences=3):
    sentences = article.split(".")
    # Remove empty strings and strip leading/trailing whitespace
    sentences = [s.strip() for s in sentences if s.strip()]

    # Calculate the importance score for each sentence (based on sentence length)
    scores = [len(sentence) for sentence in sentences]

    # Select the top N sentences with the highest importance scores
    selected_sentences = sorted(zip(sentences, scores), key=lambda x: x[1], reverse=True)[:num_sentences]

    # Extract the selected sentences
    summary = [sentence for sentence, _ in selected_sentences]

    # Join the selected sentences into a summary paragraph
    return '. '.join(summary)

# Example usage
article_text = """
Sentiment analysis is increasingly vital in modern data-driven contexts, providing crucial insights into public opinion and emotional
 trends from vast textual datasets. This project aims to enhance sentiment analysis by addressing critical challenges such as interpreting
 figurative language, including sarcasm and irony, which often confound existing models. Furthermore, the project seeks to expand the scope
 of emotional analysis beyond traditional categories, aiming for a more nuanced understanding of human emotions. By integrating advanced
 natural language processing (NLP) techniques and machine learning algorithms, the project aims to develop a robust sentiment analysis
  framework capable of delivering accurate insights across diverse platforms. Emphasis is placed on understanding platform-specific
   sentiment dynamics to ensure consistent and relevant analyses across different social media and digital platforms. Ultimately,
    these advancements are expected to empower businesses, marketers, and researchers with more reliable tools for making informed
     decisions based on a deeper understanding of public sentiment and emotional trends.
"""

# Generate a summary of the article
summary = simple_summarization(article_text)
print("Article Summary:")
print(summary)

#9.Perform Name Entity Recognition (NER) on given corpus text.
'''The capital of [France] is [Paris], a city known for its iconic [Eiffel Tower].
[John Smith] visited [Tokyo] last summer, exploring the bustling streets of
[Shibuya Crossing]. [May 5th, 2023] marks the anniversary of a significant
event in [history]. [Elon Musk] is the CEO of [SpaceX] and [Tesla].'''
import re

# Corpus text
corpus_text = "The capital of [France] is [Paris], a city known for its iconic [Eiffel Tower]. [John Smith] visited [Tokyo] last summer, exploring the bustling streets of [Shibuya Crossing]. [May 5th, 2023] marks the anniversary of a significant event in [history]. [Elon Musk] is the CEO of [SpaceX] and [Tesla]."

# Initialize lists
person_list = []
place_list = []

# Define regex pattern to find entities in brackets
pattern = r'\[(.*?)\]'

# Find all matches in the corpus text
matches = re.findall(pattern, corpus_text)

# Extract entities and populate lists
for entity in matches:
    if any(name in entity for name in ["Barack Obama", "John Smith", "Elon Musk"]):
        person_list.append(entity)
    elif any(place in entity for place in ["Hawaii", "United States", "France", "Paris", "Tokyo", "Shibuya Crossing"]):
        place_list.append(entity)

# Print the lists
print("Person List:", person_list)
print("Place List:", place_list)

#10.Perform Morphological analysis without using any pre defined NLP packages
'''The text corpus given below :
The quick brown foxes jumped over the lazy dogs. Mary's cat is playing with
a ball. Running swiftly, the athlete won the race. The painted houses lined the
street, attracting curious onlookers.'''

# Tokenizer function
def simple_tokenizer(text):
    return text.split()

# Stemming function
def simple_porter_stemmer(word):
    # A simple stemming function (for illustration purposes)
    if word.endswith("es"):
        return word[:-2]
    elif word.endswith("s"):
        return word[:-1]
    elif word.endswith("ing"):
        return word[:-3]
    return word

# Lemmatization function
def simple_wordnet_lemmatizer(word):
    # A simple lemmatization function (for illustration purposes)
    if word.endswith("es"):
        return word[:-2]
    elif word.endswith("s"):
        return word[:-1]
    elif word.endswith("ing"):
        return word[:-3]
    return word

# Function to analyze morphemes
def analyze_morphemes(word, prefixes, root, suffixes):
    morphemes = []
    for prefix in prefixes:
        if word.startswith(prefix):
            morphemes.append(prefix)
            word = word[len(prefix):]
    morphemes.append(root)
    for suffix in suffixes:
        if word.endswith(suffix):
            morphemes.append(suffix)
            word = word[:-len(suffix)]
    return morphemes

# Text corpus
text = """The quick brown foxes jumped over the lazy dogs. Mary's cat is playing with
a ball. Running swiftly, the athlete won the race. The painted houses lined the
street, attracting curious onlookers."""

# Tokenize the text into words
words = simple_tokenizer(text)

# Apply stemming and lemmatization
stemmed_words = [simple_porter_stemmer(word) for word in words]
lemmatized_words = [simple_wordnet_lemmatizer(word) for word in words]

# Print original, stemmed, and lemmatized words
print("Original words:", words)
print("Stemmed words:", stemmed_words)
print("Lemmatized words:", lemmatized_words)
print()

# Morpheme analysis example
word = "misunderstanding"
prefixes = ["mis"]
root = "understand"
suffixes = ["ing"]
morphemes = analyze_morphemes(word, prefixes, root, suffixes)

# Print morphemes
print("Word:", word)
print("Morphemes:", morphemes)

