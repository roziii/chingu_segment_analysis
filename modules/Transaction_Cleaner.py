import numpy as np 
import pandas as pd
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import itertools
from statsmodels.tsa.seasonal import seasonal_decompose
import re
from Cleaner import DataCleaner


class DataCleaner_Transactions(DataCleaner):
    def __init__(self, file_path):
        super().__init__(file_path)

    def extract_transaction_date(self):
        # Extract the Yaer, month , Week from 'Transaction Date' and store it in 'Transaction Month'
        self.df['Transaction Date'] = pd.to_datetime(self.df['Transaction Date'], errors='coerce')
        self.df['Transaction Year'] = self.df['Transaction Date'].dt.year
        self.df['Transaction Month'] = self.df['Transaction Date'].dt.month
        self.df['Transaction Week'] = self.df['Transaction Date'].dt.isocalendar().week

    def manage_subscription_status(self, subscription_status):
        subscription_status = str(subscription_status).lower()

        active_keywords = ['active', 'active-active', 'ended-active']
        ended_keywords = ['ended', 'active-ended', 'ended-ended']

        if any(keyword in subscription_status for keyword in active_keywords):
            return 'active'
        elif any(keyword in subscription_status for keyword in ended_keywords):
            return 'ended'
        else:
            return 'no-subscription'
    def manage_currency_columns(self , amount):
        if type(amount) == str:
            amount = amount.replace('$' , '')
            return float(amount)
        return amount
        
    def apply_currency_update(self):
        """Remove the currency symbol"""
        self.df['Net Payment'] = self.df['Net Payment'].apply(self.manage_currency_columns)
        self.df['Payment Amount'] = self.df['Payment Amount'].apply(self.manage_currency_columns)
        self.df['Transaction Fee'] = self.df['Transaction Fee'].apply(self.manage_currency_columns)
        self.df['Refund Amount'] = self.df['Refund Amount'].apply(self.manage_currency_columns)

    def apply_subscription_status_cleaning(self):
        """Standardize subscription status labels."""
        self.df['Subscription Status'] = self.df['Subscription Status'].apply(self.manage_subscription_status)

    def remove_rows_without_date(self):
        self.df = self.df.dropna(subset=['Transaction Date'])
    
    def _clean_column_name(self, col):
        col = col.strip().lower()
        col = re.sub(r"[\s\-()]+", "_", col)  # replace spaces, hyphens, and parentheses with underscores
        col = re.sub(r"[^\w]", "", col)        # remove any other non-word characters
        return col

    def standardize_column_names(self):
        self.df.columns = [self._clean_column_name(col) for col in self.df.columns]

    def remove_high_missing_columns(self):
        self.df.drop(columns=['payee_name', 'notes' , 'refund_amount' , 'credits_purchased' , ], inplace=True)





