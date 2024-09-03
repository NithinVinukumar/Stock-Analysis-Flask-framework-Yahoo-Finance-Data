# Stock Market Data Analysis Web Application using Flask

## Abstract

This project introduces a web application created with 
Flask, a Python-based web framework, designed to 
analyse and visualize historical stock market data.  By 
utilizing the Yahoo Finance API, users can input a 
specific company and date range to fetch relevant stock 
information.  
The application's key functionalities 
include generating various financial metrics such as 
volume, market capitalization, moving averages, scatter 
matrix, and volatility.  

## Components of the application

**Flask Routes:** The application defines routes for the 
homepage ("/"), a page to display a list of companies 
("/companylist"), and a route to handle form 
submission for data analysis ("/analyze").  

**DataFetching and Processing:** The fetch_data 
function retrieves historical stock data for a specified 
company within a given date range using the Yahoo 
Finance API.  

**Plotting Functions:** There are several functions to 
generate plots of different f inancial metrics such as 
volume, market capitalization, moving averages, scatter 
matrix, and volatility. These functions utilize Matplotlib 
for plotting.  

**Rendering Templates:** The Flask application renders 
HTML templates using Jinja2 templating engine to 
display the analysis results.  

**Form Submission Handling:** The /analyze route 
handles form submissions containing start date, end 
date, and company name. It then fetches the data, 
performs analysis, generates plots, and renders the 
analysis results on a dedicated page.  

**Image Encoding:** The generated plots are encoded 
as base64 strings to embed them directly into HTML 
pages.
