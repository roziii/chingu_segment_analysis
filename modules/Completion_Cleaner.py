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

class DataCleaner_completion(DataCleaner):
    def __init__(self, file_path):
        super().__init__(file_path)

    def manage_status(self , status):
        """
        Extracts the last status if multiple are separated by commas.
    
        Parameters:
        status (str): The status of a voyager (may contain multiple values like 'active,inactive,complete')

        Returns:
        str: The last status value
        """
        if isinstance(status, str) and ',' in status:
            return status.split(',')[-1]
        else:
            return 'not_defined'
        return status
    def apply_status_management(self):
        # Apply status cleanup on the 'status_from_voyage_signups_link' column
        # Keeps only the final status in case of comma-separated values
        self.df['Status (from Voyage Signups Link)'] = self.df['Status (from Voyage Signups Link)'].apply(self.manage_status)

    def remove_rows_without_voyage_number(self):
        # Remove rows where the 'what_is_your_voyage' column is missing (NaN)
        self.df.dropna(subset=['what_is_your_voyage'] , inplace= True)

    def update_tier(self, tier):
        """
        Extracts the Tier number string (e.g., 'Tier 2') from entries like:
        'Tier 3 - Advanced Projects - Apps having both Front-end and Back-end components (FULL STACK)'
        """
        if isinstance(tier, str):
            if '-' in tier:
                return tier.split('-')[0].strip()
            return tier.strip()
        return tier  # return as-is if not string (e.g., NaN)
    
    def apply_tier_update(self):
        self.df['What is your Tier?'] = self.df['What is your Tier?'].apply(self.update_tier)
    
    def _clean_column_name(self, col):
        col = col.strip().lower()
        col = re.sub(r"[\s\-]+", "_", col)
        col = re.sub(r"[^\w]", "", col)
        return col

    def standardize_column_names(self):
        self.df.columns = [self._clean_column_name(col) for col in self.df.columns]