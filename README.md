Stock News and Alerts System
This project tracks the stock price of a specific company (Tesla Inc) and sends SMS alerts when significant price changes occur. If the change exceeds a specified threshold, relevant news articles are fetched and shared to provide additional context.

Features
Fetches daily stock prices using the Alpha Vantage API.
Calculates the percentage difference between consecutive trading days.
Retrieves top news articles related to the company via the News API when price changes exceed 5%.
Sends SMS alerts with stock price details and news headlines using Twilio.
Technologies Used
Python: Core programming language.
Requests: For making API calls.
Twilio: For sending SMS alerts.
Dotenv: For securely managing API keys and credentials.
Setup Instructions
1. Clone the Repository:
 ```bash
git clone <repository-url>
cd <repository-folder>
 ```

2. Install Required Libraries:
Make sure Python 3.7+ is installed, then install the dependencies:
 ```bash
pip install requests twilio python-dotenv
 ```

3. Configure Environment Variables:
Create a .env file in the project root and add the following:

 ```env
STOCK_API_KEY=your_stock_api_key
NEWS_API_KEY=your_news_api_key
ACC_SID=your_twilio_account_sid
AUTH_TOKEN=your_twilio_auth_token
PHONE_NO=your_phone_number
 ```

4. Run the Script:
 ```bash
python main.py
 ```

Workflow
Stock Price Check:
The script queries the Alpha Vantage API for daily stock prices of Tesla (TSLA).
It compares the latest two closing prices to calculate the percentage change.
News Retrieval:
If the percentage change exceeds 5%, the script fetches the top 2 news articles related to Tesla using the News API.
SMS Alert:
The Twilio API is used to send SMS alerts containing the stock price change and news headlines.
Example SMS Alert
 ```vbnet
TSLA: ⃤⃤ 3.5%
Headline: Tesla hits new record sales
Content: Tesla Inc has reported record sales for the quarter, pushing its stock price upward.
 ```

APIs Used
Alpha Vantage API: Provides stock market data.
News API: Fetches news articles based on company name.
Twilio API: Sends SMS notifications.

Prerequisites
A Twilio account to send SMS alerts.
API keys for:
Alpha Vantage
News API
A phone number to receive SMS alerts.


Acknowledgments
Alpha Vantage for stock data.
News API for news articles.
Twilio for SMS services.

