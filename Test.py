import tkinter as tk
from tkinter import messagebox
import re

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

# import required nltk data
nltk.download('punkt')
nltk.download('stopwords')

# function to convert text to vector space
def normalize(text):
    text = re.sub('[^a-zA-Z]', ' ', text) # remove special characters
    words = word_tokenize(text) # convert text to words
    words = [word for word in words if word not in stopwords.words('english')] # remove stopwords
    return ' '.join(words)

# function to calculate similarity and get response
def get_response():
    user_input = entry.get()
    entry.delete(0, tk.END)

    if user_input.lower() == "quit":
        window.quit()
    else:
        documents = ["Document1", "Document2", "Document3"]
        labels = ['label1', 'label2', 'label3']
        questions = [user_input]

        vectorizer = TfidfVectorizer(use_idf=True, tokenizer=normalize, lowercase=True)
        tfidf_matrix = vectorizer.fit_transform(documents + questions)

        cosine_similarities = cosine_similarity(tfidf_matrix[-len(questions):], tfidf_matrix[:-len(questions)])

        label_index = cosine_similarities[0].argsort()[::-1][0]
        response = f"The most similar document label is: {labels[label_index]}"
        label.config(text=response)

# create the tkinter window
window = tk.Tk()
window.title("Chatbot")

# create the tkinter label
label = tk.Label(window, text="", bg="white", fg="black", width=60, height=20)
label.pack(pady=10)

# create the tkinter entry box
entry = tk.Entry(window, width=60)
entry.pack(pady=10)

# create the tkinter send button
send_button = tk.Button(window, text="Send", command=get_response)
send_button.pack(pady=10)

# start the tkinter event loop
window.mainloop()