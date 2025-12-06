import os
import glob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

DATA_PATH = "data/aclImdb"

def load_reviews(path):
    texts, labels = [], []
    
    for label in ["pos", "neg"]:
        folder = os.path.join(path, label)
        for file in glob.glob(folder + "/*.txt"):
            with open(file, encoding="utf-8") as f:
                texts.append(f.read())
                labels.append(1 if label == "pos" else 0)
    
    return texts, labels

print("📌 Loading training data...")
train_texts, train_labels = load_reviews(os.path.join(DATA_PATH, "train"))

print("📌 Loading testing data...")
test_texts, test_labels = load_reviews(os.path.join(DATA_PATH, "test"))

print("📌 Vectorizing text...")
vectorizer = TfidfVectorizer(stop_words="english", max_features=20000)
X_train = vectorizer.fit_transform(train_texts)
X_test = vectorizer.transform(test_texts)

print("📌 Training model...")
model = LogisticRegression(max_iter=3000)
model.fit(X_train, train_labels)

accuracy = model.score(X_test, test_labels)
print(f"✨ Model accuracy: {accuracy * 100:.2f}%")

print("💾 Saving model & vectorizer...")
joblib.dump(model, "model/sentiment_model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("🎉 Training complete! Files saved in /model folder.")
