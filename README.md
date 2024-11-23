# Newspaper Bias Detection using Machine Learning

Project done by Team Code Crashers for the course CSE299.

---

# 📰 News Bias Analyzer

A web application that analyzes the political bias of news articles and suggests related articles from trusted sources. The app uses a fine-tuned ROBERTA model to classify articles as  *Left* ,  *Neutral* , or *Right* and supports analyzing headlines, article content, and URLs.

---

## 🚀 Features

* **Bias Analysis** : Detect political bias (Left, Neutral, Right) in news articles.
* **Keyword Extraction** : Automatically extract relevant keywords from headlines or content.
* **Related Articles** : Fetch related articles from multiple news sources using NewsAPI.
* **Custom Input** : Accepts article URL, headline, or full content for analysis.
* **Interactive UI** : Displays results with a visual indicator of bias and related information.

---

## 📦 Installation

1. **Clone the Repository** :

```bash
   git clone https://github.com/t4niha/news-bias-analyzer.git
   cd news-bias-analyzer
```

1. **Set Up a Virtual Environment** :

```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
```

1. **Install Dependencies** :

```bash
   pip install -r requirements.txt
```

1. **Set Up API Keys** :

* Obtain a [NewsAPI](https://newsapi.org/) key.
* Create a `.env` file in the project directory and add:
  ```
  NEWS_API_KEY=your_newsapi_key_here
  ```

1. **Run the Application** :

```bash
   uvicorn app:app --reload
```

1. **Access the App** :

* Visit `http://127.0.0.1:8000` in your browser.

---

## ⚙️ How It Works

1. **Input** :

* Enter a  **URL** , **headline** , or **full content** .

1. **Analysis** :

* The input is processed using a fine-tuned ROBERTA model for bias detection.

1. **Keyword Extraction** :

* Relevant keywords are extracted using NLP techniques.

1. **Article Search** :

* The extracted keywords are used to find related articles via NewsAPI.

1. **Output** :

* Displays the predicted bias, visual indicators, and links to related articles.

---

## 🛠️ Key Technologies

* **Backend** : Python (FastAPI)
* **Frontend** : HTML, CSS
* **Machine Learning** : Hugging Face ROBERTA
* **APIs** : NewsAPI
* **NLP** : SpaCy for keyword extraction

---

## 🔐 License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

---

## 🌟 Acknowledgments

* [Hugging Face Transformers](https://huggingface.co/transformers/)
* [NewsAPI](https://newsapi.org/)
* [FastAPI](https://fastapi.tiangolo.com/)

---

Replace placeholders (`your-username`, `your-newsapi_key_here`, `your-email@example.com`) with actual details. This `README.md` provides a polished, user-friendly overview for showcasing your project on GitHub.
