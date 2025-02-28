




# Import Libraries
import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup

# Matplotlib & Seaborn settings
sns.set(style="darkgrid")

st.set_page_config(page_title= "FIN429 Monte Carlo Simulation")
st.title("FIN429 Monte Carlo Simulation")
st.subheader("Test your current portfolio or build a new one through our Monte Carlo Simulation and Portfolio Optimization Platform!")


# PARAMETERS & CONFIGURATION
num_portfolios = 10_000   # Random portfolios for optimization
mc_sims = 1_000           # Number of Monte Carlo simulation paths
T = 252                   # Simulation horizon in days
initial_value = 100_000   # Initial portfolio value in USD
alpha = 5                 # Percentile for risk metrics (5 implies 95% confidence)
import streamlit as st

# User Input
user_input = st.text_input("Enter the ticker symbols in your portfolio separated by commas:")

# Split Input into a list
if user_input:
    user_tickers = [ticker.strip() for ticker in user_input.split(',')]
    st.write("You entered the following tickers:", user_tickers)
