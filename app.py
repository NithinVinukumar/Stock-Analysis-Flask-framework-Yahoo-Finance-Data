from flask import Flask, request, render_template, url_for
import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import yfinance as yf
from io import BytesIO
import base64

app = Flask(__name__)

def fetch_data(company, start, end):
    return yf.download(company, start, end)

def plot_volume(traded_data):
    plt.figure(figsize=(10, 5))
    traded_data['Volume'].plot()
    plt.title('Volume of Stock Traded')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.grid(True)
    plt.tight_layout()
    plot_img = get_img_data()
    return plot_img
1
def plot_market_cap(data):
    data['MarketCap'] = data['Open'] * data['Volume']
    plt.figure(figsize=(10, 5))
    data['MarketCap'].plot()
    plt.title('Market Cap')
    plt.xlabel('Date')
    plt.ylabel('Market Cap')
    plt.grid(True)
    plt.tight_layout()
    plot_img = get_img_data()
    return plot_img

def plot_moving_average(data):
    data['MA50'] = data['Open'].rolling(50).mean()
    data['MA200'] = data['Open'].rolling(200).mean()
    plt.figure(figsize=(10, 5))
    data['Open'].plot(label='Open Price')
    data['MA50'].plot(label='MA50')
    data['MA200'].plot(label='MA200')
    plt.title('Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plot_img = get_img_data()
    return plot_img

def plot_scatter_matrix(data):
    plt.figure(figsize=(10, 10))
    scatter_matrix(data, alpha=0.2, figsize=(10, 10), diagonal='kde')
    plt.title('Scatter Matrix')
    plt.tight_layout()
    plot_img = get_img_data()
    return plot_img

def plot_volatility(data):
    data['returns'] = (data['Close'] / data['Close'].shift(1)) - 1
    plt.figure(figsize=(10, 5))
    data['returns'].hist(bins=100, alpha=0.5)
    plt.title('Volatility')
    plt.xlabel('Returns')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.tight_layout()
    plot_img = get_img_data()
    return plot_img

def get_img_data():
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_img = base64.b64encode(img.getvalue()).decode()
    plt.close()  # Close the plot to avoid memory leaks
    return plot_img

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/companylist')
def companylist():
    return render_template('companylist.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    company = request.form['company']

    data = fetch_data(company, start_date, end_date)

    if data is not None:
        volume_plot = plot_volume(data)
        market_cap_plot = plot_market_cap(data)
        moving_average_plot = plot_moving_average(data)
        scatter_matrix_plot = plot_scatter_matrix(data)
        volatility_plot = plot_volatility(data)

        return render_template('analyze.html', 
                               volume_plot=volume_plot, 
                               market_cap_plot=market_cap_plot,
                               moving_average_plot=moving_average_plot,
                               scatter_matrix_plot=scatter_matrix_plot,
                               volatility_plot=volatility_plot)
    else:
        return "Error fetching data. Please try again."

if __name__ == "__main__":
    app.run(debug=True)
