Movie Sentiment Analysis Web App

A Machine Learning + Flask project using the IMDB 50K Movie Review Dataset

📌 Overview

This project predicts whether a movie review is Positive 😊 or Negative 😞 using a machine learning model trained on the Stanford IMDB Movie Review Dataset.

The web app allows users to:

Enter a movie review

Get instant sentiment prediction

Explore movie info (poster, cast, rating) (coming soon)

Analyze IMDB reviews with ML (coming soon)

This project is developed as part of a 3rd-year Diploma final project.

🚀 Features
✔ Machine Learning

Trained on 50,000 IMDB movie reviews

TF-IDF vectorization

Logistic Regression classification

~88% accuracy

✔ Web Application (Flask)

Interactive web UI

Input reviews & predict sentiment

Real-time results display

✔ Future Additions

IMDB search (movie poster, cast, rating)

Auto-analysis of real IMDB reviews

Beautiful UI with Bootstrap

API endpoints

📊 Dataset Used

IMDB Large Movie Review Dataset (50,000 reviews)
Provided by Stanford AI Lab.

Structure:

aclImdb/
│
├── train/
│   ├── pos/   → 12,500 positive reviews
│   └── neg/   → 12,500 negative reviews
│
└── test/
    ├── pos/   → 12,500 positive reviews
    └── neg/   → 12,500 negative reviews


Each review is a .txt file containing a real user-written review.

🧠 Model Architecture

Text Vectorization: TF-IDF (20,000 features)

Algorithm: Logistic Regression

Accuracy: 88%

Training code:

train_model.py


Model saved as:

model/sentiment_model.pkl
model/vectorizer.pkl

🛠 Tech Stack
Component	Technology
Backend	Flask
ML Model	Scikit-learn
Vectorizer	TF-IDF
Language	Python
Dataset	IMDB 50K reviews
Version Control	Git + GitHub
📁 Project Structure
movie-sentiment-project/
│
├── app/
│   ├── app.py
│   └── templates/
│       └── index.html
│
├── model/
│   ├── sentiment_model.pkl
│   └── vectorizer.pkl
│
├── data/
│   └── aclImdb/
│       ├── train/
│       └── test/
│
├── train_model.py
├── .gitignore
└── README.md

▶ Running the Project
1️⃣ Install required libraries
pip install flask scikit-learn joblib

2️⃣ Train the model (already trained)

If needed to retrain:

python train_model.py

3️⃣ Run the web app
cd app
python app.py


Open in browser:

http://127.0.0.1:5000

📸 Screenshots (Add your screenshots here)
![Homepage](images/homepage.png)
![Prediction](images/prediction.png)

🔮 Future Improvements

Add movie search (poster, rating, cast) using OMDB/IMDB API

Scrape IMDB reviews and auto-analyze them

Add dark/light mode UI

Deploy app on Render/Heroku

Add history of predictions

🙌 Credits

Dataset: Stanford IMDB 50K Movie Review Dataset

Developer: Jinwoo (erza3120)

Mentor: — (add your sir’s name if you want)

⭐ Final Notes

This project demonstrates:

Machine Learning pipeline

Model training, testing & evaluation

Flask backend development

Git/GitHub version control

Clean folder structure & coding practices
