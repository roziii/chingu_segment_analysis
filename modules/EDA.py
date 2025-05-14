import numpy as np 
import pandas as pd
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import itertools
from statsmodels.tsa.seasonal import seasonal_decompose
import re


class EDA:
    def __init__(self, file_path):
        """Initialize with file path and load the dataset."""
        self.file_path = file_path
        self.df = pd.read_csv(self.file_path)

    def display_column_value_counts(self):
        """Display the top 10 most frequent values for each column."""
        for column in self.df.columns:
            print('-' * 30)
            print(f'{self.df[column].value_counts()}')
            print('_' * 30)

    def show_data_distribution(self):
        """ ploting histograms, box plots, violin plots, and scatter plots."""
        numeric_columns = self.df.select_dtypes(include=[np.number]).columns.tolist()

        print('*' * 33)
        print('********** Distributions **********')

        # Pie Charts for Categorical Columns
        for column in self.df.columns:
            if column not in numeric_columns:
                counts = self.df[column].value_counts()
                if len(counts) <= 10:  # Only plot if unique values are manageable
                    fig = px.pie(names=counts.index,
                                 values=counts.values,
                                 title=f'Distribution of {column}')
                    fig.update_layout(height=500)
                    fig.show()

        print('*' * 33)
        print('********** Histograms **********')

        # Histograms for Numeric Columns
        for col in numeric_columns:
            fig = px.histogram(self.df, x=col, title=f'Histogram of {col}')
            fig.update_layout(height=500)
            fig.show()

        print('*' * 33)
        print('********** Box Plots **********')

        # Box Plots for Numeric Columns
        for column in numeric_columns:
            fig = px.box(self.df, y=column, title=f'Box Plot of {column}')
            fig.update_layout(height=500, width=500)
            fig.show()

        print('*' * 33)
        print('********** Violin Plots **********')

        # Violin Plots for Numeric Columns
        for column in numeric_columns:
            fig = px.violin(self.df, y=column, title=f"Violin Plot of {column}")
            fig.update_layout(width=500, height=500)
            fig.show()

        print('*' * 33)
        print('********* Scatter Plots *********')

        # Scatter Plots for Numeric Columns
        for col1, col2 in itertools.combinations(numeric_columns, 2):
            fig = px.scatter(self.df, x=col1, y=col2, title=f'Scatter Plot of {col1} vs {col2}')
            fig.update_layout(height=500)
            fig.show()

        print('*' * 33)
        print('********* Scatter Plot With Trend Lines *********')

        # Scatter Plots with Trend Lines
        for col1, col2 in itertools.combinations(numeric_columns, 2):
            fig = px.scatter(self.df,
                             x=col1,
                             y=col2,
                             title=f'Scatter Plot of {col1} Vs {col2} With The Trend Line',
                             trendline='ols')
            fig.update_traces(line=dict(color='red', width=3))
            fig.update_layout(height=500)
            fig.show()

    def show_seasonal_decomposition(self):
        """Perform seasonal decomposition on numeric columns."""
        numeric_columns = self.df.select_dtypes(include=[np.number]).columns.tolist()
        print(numeric_columns)

        for column in numeric_columns:
            df_copy = self.df[column].copy()

            # Handle missing values by interpolation
            if df_copy.isnull().any():
                df_copy = df_copy.interpolate()

            df_copy = df_copy.dropna()

            # Ensure no infinite values
            if not np.isfinite(df_copy).all():
                print(f'Column {column} contains non-finite values, decomposition is skipped.')
                continue

            # Perform Seasonal Decomposition
            try:
                decomposition = seasonal_decompose(df_copy, model='additive', period=12)
                fig = decomposition.plot()

                plt.gcf().set_size_inches(10, 6)
                plt.suptitle(f'Decomposition of the temporal series of {column}', fontsize=16, y=1.05)
                plt.show()
            except ValueError:
                print(f"Skipping decomposition for {column}, not enough data points.")

