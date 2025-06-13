# 📰 Live News Sentiment Dashboard

**Real-time WebSocket-powered dashboard that fetches top headlines, analyzes sentiment using NLP, and visualizes it on a live frontend.**

---

## 🔗 Live Components

- **Frontend**: React + TailwindCSS + WebSocket  
- **Backend**: FastAPI + Fluvio (streaming) + TextBlob (NLP)  
- **News Source**: [NewsAPI](https://newsapi.org/)

---

## 📦 Features

✅ Real-time streaming of sentiment-labeled news  
✅ Headline-level NLP sentiment analysis  
✅ Dynamic UI with color-coded sentiment  
✅ WebSocket-powered frontend updates  
✅ Modular backend with Fluvio integration

---

## 🧠 How It Works

### 📂 `sentiment_analysis.py`
Uses `TextBlob` to analyze the polarity of news text.

```python
def get_sentiment(text):
    # Returns sentiment ("positive", "neutral", "negative") + polarity score
```

### 📂 `news_producer.py`

- Pulls top headlines from NewsAPI every few seconds.
- Analyzes each using `get_sentiment`.
- Appends structured JSON data to `sentiment_data.json` for further use.

```json
{
  "headline": "Markets soar after tech earnings beat expectations",
  "sentiment": "positive",
  "score": 0.45,
  "timestamp": "2025-06-13T08:47:23.000Z"
}
```

---

## ⚙️ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/your-username/news-sentiment-dashboard.git
cd news-sentiment-dashboard
```

### 2. Install Python backend dependencies

```bash
pip install -r requirements.txt
```

Required packages:
- `textblob`
- `requests`
- `fastapi`
- `uvicorn`
- `fluvio`

(You may need to run `python -m textblob.download_corpora` once.)

### 3. Run the backend (Fluvio + FastAPI)

```bash
python websocket_server.py
```

This streams processed headlines from `Fluvio` to connected WebSocket clients.

### 4. Run the producer

```bash
python news_producer.py
```

This starts fetching and analyzing news headlines and pushing to Fluvio.

### 5. Start the frontend (Vite + React)

```bash
npm install
npm run dev
```

Open: [http://localhost:5173](http://localhost:5173)

---

## 🧪 Example Output (in UI)

```
📰 Apple shares hit record high after earnings beat expectations
📊 Sentiment: Positive
📈 Polarity: 0.43
```

---

## 📌 To-Do / Enhancements

- [ ] Add sentiment trend chart (Recharts)
- [ ] Filter or search sentiment by keyword
- [ ] Improve sentiment accuracy using transformer models
- [ ] Dockerize full stack

---

## 🤝 Contributions

PRs welcome! Open an issue or start a discussion.

---

## 📜 License

[MIT](LICENSE)
