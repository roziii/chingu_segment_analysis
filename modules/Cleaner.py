import numpy as np 
import pandas as pd
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import itertools
from statsmodels.tsa.seasonal import seasonal_decompose
import re

warnings.filterwarnings('ignore')

class DataCleaner:
    def __init__(self, file_path):
        """Initialize with file path and load the dataset."""
        self.file_path = file_path
        self.df = pd.read_csv(self.file_path)
    
    def describe_df(self):
        print(self.df.head(10))
        print(self.df.describe())
        print(self.df.info())

    
    def clean_timestamps(self):
        """Automatically detect and convert timestamp columns."""
        date_columns = []
        for col in self.df.columns:
            try:
                sample_values = self.df[col].dropna().astype(str).head(10)
                converted_sample = pd.to_datetime(sample_values, errors='coerce')
                if converted_sample.notna().mean() > 0.7:  # If at least 70% can be converted
                    date_columns.append(col)
            except Exception:
                pass  # Skip columns that raise errors

        for col in date_columns:
            self.df[col] = pd.to_datetime(self.df[col], errors='coerce')

    
    def show_missing_values(self, title="Dataset"):
        """Illustrate the missing values using a heatmap."""
        fig1 = px.imshow(self.df.isnull(),
                         color_continuous_scale=['gray', 'blue'],
                         labels=dict(color="NaN"),
                         title=f'Missing Values Heatmap for {title}')
        fig1.update_layout(width=700, height=700)
        fig1.update_coloraxes(showscale=True)
        fig1.show()

        missing_values = self.df.isna().sum()
        print(f'\nMissing Values in {title}:\n{missing_values}')


    def handle_missing_values(self, column,fill_value):
        """Fill or drop missing values for a given column."""
        dtype = self.df[column].dtype
    
        # Check if it's datetime and value is string
        if pd.api.types.is_datetime64_any_dtype(dtype):
            try:
                fill_value = pd.to_datetime(fill_value)
            except Exception as e:
                print(f"Cannot convert {fill_value} to datetime: {e}")
                return
    
        # Convert numeric fill to proper type
        if pd.api.types.is_numeric_dtype(dtype):
            try:
                fill_value = float(fill_value)
            except Exception as e:
                print(f"Cannot convert {fill_value} to float: {e}")
                return
    
        # Fill NaN
        self.df[column] = self.df[column].fillna(fill_value)

    
    def drop_column(self , columns):
        for col in columns:
            self.df.drop(col  , axis = 1, inplace = True)

    
    def standardize_categorical_data(self, columns):
        """Ensure categorical columns are standardized."""
        for col in columns:
            if col in self.df.columns:
                self.df[col] = self.df[col].astype(str).str.strip().str.title()
        
                

    def remove_duplicates(self):
        """Remove duplicate entries based on 'Unique ID'."""
        if "Unique ID" in self.df.columns:
            self.df.drop_duplicates(subset=["Unique ID"], keep="first", inplace=True)

    def convert_numeric_columns(self):
        """Convert appropriate columns to numeric types."""
        numeric_object_cols = [
            col for col in self.df.select_dtypes(include=['object']).columns
            if self.df[col].apply(lambda x: pd.to_numeric(x, errors='coerce')).notna().mean() > 0.7
        ]
        for col in numeric_object_cols:
            self.df[col] = pd.to_numeric(self.df[col], errors='coerce')

    
    def convert_currency_column(self, columns):
        """
        Converts a column with currency values to numeric by removing any currency symbols and commas.
        Args:
        df (pd.DataFrame): The input DataFrame.
        column_name (str): The name of the column to convert.
    
        Returns:
        pd.DataFrame: The modified DataFrame with the converted column.
        """
        for column_name in columns:
            self.df[column_name] = (
                self.df[column_name]
                .astype(str)  # Ensure values are strings
                .apply(lambda x: re.sub(r'[^\d.-]', '', x))  # Remove non-numeric characters (currency symbols, commas)
                .astype(float)  # Convert to float
            )

    
    def save_cleaned_data(self, output_path):
        """Save the cleaned data to a new CSV file."""
        self.df.to_csv(output_path, index=False)

    def _clean_column_name(self, col):
        col = col.strip().lower()
        col = col.replace("?", "")                  # remove all question marks
        col = re.sub(r"[\s\-()]+", "_", col)      # replace spaces, hyphens, and parentheses with underscores
        col = re.sub(r"[^\w]", "", col)             # remove any other non-word characters
        col = re.sub(r"_+", "_", col)                # collapse multiple underscores into one
        col = col.strip("_")                         # remove leading/trailing underscores
        return col

    def standardize_column_names(self):
        self.df.columns = [self._clean_column_name(col) for col in self.df.columns]

