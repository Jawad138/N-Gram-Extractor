import streamlit as st
from nltk import ngrams
from nltk.tokenize import word_tokenize

# Download the punkt resource if not already downloaded
import nltk
nltk.download('punkt')

# Function to generate n-grams from a text passage
def generate_ngrams(text, n):
    tokens = word_tokenize(text)
    n_grams = list(ngrams(tokens, n))
    return n_grams

# Streamlit UI
def main():
    st.title("N-gram Extractor")

    # Input text area
    text_input = st.text_area("Enter text:")

    # N-gram selection
    n_gram_option = st.selectbox("Select N-gram type:", ["Bigram", "Trigram", "Custom"])

    if n_gram_option == "Custom":
        n = st.number_input("Enter the value of N:", min_value=1, value=2, step=1)
    else:
        n = 2 if n_gram_option == "Bigram" else 3

    # Button to generate n-grams
    if st.button("Generate N-grams"):
        if text_input:
            st.subheader(f"{n}-grams:")
            n_grams = generate_ngrams(text_input, n)
            st.write(n_grams)
        else:
            st.warning("Please enter some text.")

if __name__ == "__main__":
    main()
