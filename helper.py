import pickle
import numpy as np
d2v_model = pickle.load(open('word2vec.model', 'rb'))
def vectorizer(text: str) -> np.ndarray:
    words = text.split()
    vector = np.zeros(100)
    for word in words:
        if word in d2v_model.wv:
            vector += d2v_model.wv[word]
    return vector

from nltk.corpus import stopwords
def remove_stopwords(text: str) -> str:
    stop_words = set(stopwords.words('english'))
    words = text.split()
    filtered_text = ' '.join([word for word in words if word not in stop_words])
    return filtered_text
setiment_classifier = pickle.load(open('model1.pkl', 'rb'))
import torch
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
def predict_sentiment(text: str,) -> str:
    text_vector = vectorizer(text)
    text_tensor = torch.tensor(text_vector, dtype=torch.float32).to(device)
    text_tensor = text_tensor.unsqueeze(0)  # Add batch dimension
    with torch.no_grad():
        output = setiment_classifier(text_tensor)
        _, predicted = torch.max(output.data, 1)
        sentiment_mapping = {0: 'Neutral', 1: 'Positive', 2: 'Negative'}
        return sentiment_mapping[predicted.item()]
