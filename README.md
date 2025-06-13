# 🎬 Movie Recommender System

A simple content-based movie recommender system built with Python, Streamlit, and machine learning techniques. Users can select a movie and get top similar movies based on genres, keywords, cast, and other metadata.

---

## 🚀 Demo

🌐 [Live App on Render](https://your-app-link.onrender.com)

---

## 🧠 How It Works

- Extracts features like **genres, keywords, cast, and overview**.
- Combines them into a single `tags` column.
- Uses **TF-IDF** model via `TfidfVectorizer`. 
- Computes similarity using **cosine similarity**.
- Recommends the **top 5 most similar movies**.

---

## 📁 Project Structure
```
movie-recommender/
├── app.py
├── models/
│ ├── movies.pkl
│ └── similarity.pkl
├── requirements.txt
├── README.md
└── .gitignore
```
---

## **Create a virtual environment (optional but Recommended)**
```
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

## Install requirements

```pip install -r requirements.txt```

## Run the app
`streamlit run app.py`

# 🧠 Model Files
**movies.pkl**: *Preprocessed movie metadata*

**similarity.pkl**: *Cosine similarity matrix*

You can generate them using your Jupyter notebook / Colab and save using joblib.

# 🛠 Tech Stack
- Python
- Pandas, Numpy, Scikit-learn
- Streamlit
- Joblib (for model persistence)

# 📦 Deployment
This app can be easily deployed to:
Render – https://render.com

# 🤝 Contributions
PRs and feedback are welcome! If you find any issues, feel free to raise them.

# 📜 License
This project is licensed under the MIT License.