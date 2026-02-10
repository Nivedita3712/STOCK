

# 📈 Stock Price Prediction Using LSTM with Sentiment Analysis

## 📌 Project Overview

This project aims to predict stock prices using a **Long Short-Term Memory (LSTM)** deep learning model combined with **Sentiment Analysis**.
Stock market data is **time-series, non-linear, and volatile**, and prices are influenced not only by historical trends but also by **news and public sentiment**.

By combining **historical stock prices** with **sentiment scores extracted from news or text data**, the model attempts to improve prediction accuracy and capture real-world market behavior more effectively.

This project was developed as a **Mini Project (Review–1)** under the Department of Computer Science & Engineering (AIML).

## 🎯 Objectives

* To analyze historical stock market price data
* To perform sentiment analysis on stock-related news/text
* To combine price data and sentiment features
* To build an LSTM-based deep learning model
* To predict future stock prices more accurately

## 🧠 Why LSTM + Sentiment Analysis?

* LSTM captures **long-term temporal dependencies** in price data
* Sentiment analysis captures **market psychology and investor emotions**
* Stock prices are influenced by **both numerical trends and public opinion**
* The hybrid approach improves real-world prediction capability

## 🗂️ Dataset

### 📊 Stock Market Data

Features include:

* Open Price
* High Price
* Low Price
* Close Price
* Volume

### 📰 Sentiment Data

* Stock-related news headlines / text data
* Each text is analyzed and assigned a **sentiment score**:

  * Positive
  * Negative
  * Neutral

📌 The sentiment score is merged with stock price data as an **additional feature**.

## 🧠 Sentiment Analysis Module

Sentiment analysis is performed using **Natural Language Processing (NLP)** techniques.

### Steps:

1. Text cleaning and preprocessing
2. Tokenization
3. Sentiment scoring using a sentiment analyzer
4. Conversion of sentiment into numerical values
5. Integration with stock price dataset

### Output:

* A sentiment score corresponding to each time period
* Used as an input feature to the LSTM model

## 🏗️ System Architecture

1. Stock Price Data Collection
2. News/Text Data Collection
3. Sentiment Analysis using NLP
4. Data Preprocessing & Normalization
5. Feature Fusion (Price + Sentiment)
6. LSTM Model Training
7. Stock Price Prediction
8. Performance Evaluation

## ⚙️ Technologies Used

* Python
* NumPy
* Pandas
* Matplotlib
* TensorFlow / Keras
* Scikit-learn
* NLTK / TextBlob / Vader (for sentiment analysis)
* 
## 🔧 Model Hyperparameters

* LSTM Units: 50
* Batch Size: 32
* Epochs: 50
* Time Steps (Sequence Length): 60
* Optimizer: Adam
* Loss Function: Mean Squared Error (MSE)
* Dropout Rate: 0.2

## 📊 Evaluation Metrics

* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* Visual comparison of actual vs predicted prices

## 📚 Related Research Papers

* **Hybrid Deep Learning Approaches for Stock Price Prediction Using LSTM and GRU Models**
  *Dipanshi, Nishi Gupta*

* **Comparative Evaluation for Limitations of LSTM and GRU Models in Stock Price Prediction**
  *Teranun Kitnapat*

* **A Stock Price Prediction Model Based on VMD-SSA-LSTM**
  *Peize Lu*

## 🚀 How to Run the Project

1. Clone the repository

   ```bash
   git clone https://github.com/your-username/stock-price-prediction-lstm.git
   ```

2. Install required libraries

   ```bash
   pip install -r requirements.txt
   ```

3. Run the program

   ```bash
   python stock_prediction.py
   ```

---

## 📌 Results

The combined **LSTM + Sentiment Analysis model** shows improved prediction performance compared to models trained only on historical stock prices.
Sentiment features help the model capture market reactions to news and events.

## 🔮 Future Enhancements

* Hybrid LSTM + GRU architecture
* Attention mechanism
* Real-time news sentiment integration
* Social media sentiment analysis (Twitter/X)
* Deployment as a web application
-

