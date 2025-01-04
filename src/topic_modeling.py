import gensim
from gensim import corpora
from nltk.tokenize import word_tokenize
import spacy

nlp = spacy.load("en_core_web_sm")

def preprocess_for_lda(texts):
    processed_texts = []
    for text in texts:
        tokens = word_tokenize(text)
        doc = nlp(" ".join(tokens))
        lemmatized = [token.lemma_ for token in doc if token.is_stop == False and token.is_punct == False]
        processed_texts.append(lemmatized)
    return processed_texts

def lda_topic_modeling(texts, num_topics=5):
    processed_texts = preprocess_for_lda(texts)
    dictionary = corpora.Dictionary(processed_texts)
    corpus = [dictionary.doc2bow(text) for text in processed_texts]
    
    lda_model = gensim.models.LdaMulticore(corpus, num_topics=num_topics, id2word=dictionary, passes=10, workers=2)
    
    return lda_model.print_topics(num_topics=num_topics)
