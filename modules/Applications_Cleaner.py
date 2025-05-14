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

class DataCleaner_Application(DataCleaner):
    def __init__(self, file_path):
        super().__init__(file_path)
        
    def extract_application_month(self):
        # Extract the month from 'Application Date' and store it in 'Application Month'
        self.df['Application Month'] = self.df['Application Date'].dt.month 
        self.df['Application Week'] = self.df['Application Date'].dt.isocalendar().week
 

    def extract_application_date(self):
        # Extract the month from 'Application Date' and store it in 'Application Month'
        self.df['Subscription Status DT'] = pd.to_datetime(self.df['Subscription Status DT'], errors='coerce')
        self.df['Subscription Status Year'] = self.df['Subscription Status DT'].dt.year
        self.df['Subscription Status Month'] = self.df['Subscription Status DT'].dt.month
        self.df['Subscription Status Week'] = self.df['Subscription Status DT'].dt.isocalendar().week
        
    def categorize_source(self, source):
        source = str(source).lower()
        if any(keyword in source for keyword in ["friend", "colleague", "classmate", "mentor", "coworker", "husband", "wife", "relative"]):
            return "Friend-Recommendation"
        elif "reddit" in source:
            return "Reddit"
        elif "discord" in source:
            return "Discord"
        elif "github" in source:
            return "GitHub"
        elif "linkedin" in source:
            return "LinkedIn"
        elif "facebook" in source:
            return "Facebook"
        elif "twitter" in source:
            return "Twitter"
        elif "instagram" in source:
            return "Instagram"
        elif "tiktok" in source or "tik tok" in source:
            return "Tiktok"
        elif "slack" in source:
            return "Slack"
        elif any(keyword in source for keyword in ["google", "search"]):
            return "Google Search"
        elif "chatgpt" in source:
            return "ChatGPT Suggestion"
        elif any(keyword in source for keyword in ["blog", "medium", "website", "article", "learntocodewith.me", "nocsdegree", "post"]):
            return "Blog or Website"
        elif "podcast" in source:
            return "Podcast"
        elif any(keyword in source for keyword in ["bootcamp", "thinkful", "flatiron", "alchemy", "springboard", "hack reactor"]):
            return "Bootcamp Recommendation"
        elif any(keyword in source for keyword in ["frontend masters","frontendmasters" , "frontend master" , "\"frontendmaster\"" ,"skillcrush", "freecodecamp", "udemy", "scrimba", "zero to mastery", "codepath", "le wagon"]):
            return "Course or Coding School"
        elif any(keyword in source for keyword in ["career coach", "recruiter", "hiring manager", "mentor"]):
            return "Work or Career Advisor"
        else:
            return "Other"

    def apply_categorization(self):
        self.df['Source-Category'] = self.df['Source-Other'].apply(self.categorize_source)
        self.df.loc[self.df['Source'].str.lower() == 'other', 'Source'] = (
            self.df['Source'] + "_" + self.df['Source-Category'].astype(str)
        )
        
    def is_participated_in_voyage(self):
        """
        Adds a binary indicator column 'has_voyage' to the DataFrame.
        This column is set to 1 if 'updated_voyage_start_date' is not missing (i.e., the user participated in a voyage),
        and 0 if the date is missing (i.e., the user did not participate).
        """
        self.df['has_voyage'] = self.df['updated_voyage_start_date'].notna().astype(int)
        
    def standardize_sources(self):
        source_mappings = {
            "google": "Google Search",
            "reddit": "Reddit",
            "tiktok": "Tiktok",
            "facebook": "Facebook",
            "twitter": "Twitter",
            "github": "GitHub",
            "slack": "Slack",
            "linkedin": "LinkedIn",
            "instagram": "Instagram",
            "friend": "PERSONAL NETWORK"
        }
        self.df['Source'] = self.df['Source'].astype(str).apply(
            lambda x: next((v for k, v in source_mappings.items() if k in x.lower()), x)
        )

    def update_country_and_country_code(self):
        country_code_mapping = {
            "United States": "US", "Canada": "CA", "United Kingdom": "GB", "Germany": "DE",
            "France": "FR", "India": "IN", "Australia": "AU", "Brazil": "BR", "Spain": "ES",
            "Italy": "IT", "Mexico": "MX", "Netherlands": "NL", "Japan": "JP", "South Korea": "KR",
            "China": "CN", "South Africa": "ZA", "Namibia": "NA" , "Naigeria" : "NI"
        }
        self.df['Country Code'] = self.df['Country Code'].fillna(
            self.df['Country name (from Country)'].map(country_code_mapping)
        )
        mask = self.df['Country name (from Country)'] == '6. friday'
        reverse_country_mapping = {v: k for k, v in country_code_mapping.items()}
        self.df.loc[mask, 'Country name (from Country)'] = self.df.loc[mask, 'Country Code'].map(reverse_country_mapping)
        
        reverse_country_mapping = {v: k for k, v in country_code_mapping.items()}
        self.df['Country name (from Country)'] = self.df['Country name (from Country)'].fillna(
            self.df['Country Code'].map(reverse_country_mapping)
        )

    def explode_based_on_voyage_number(self):
        self.df['Voyage (from Voyage Signups)'] = (
            self.df['Voyage (from Voyage Signups)']
            .astype(str)
            .str.replace(' ', '')  # remove spaces
            .str.split(',')        # split into list
        )
        self.df = self.df.explode('Voyage (from Voyage Signups)').reset_index(drop=True)

    def update_voyage_details(self, df_voyage_schedule):
        self.df['Application Date'] = pd.to_datetime(self.df['Application Date'], errors='coerce')
        def find_next_voyage(application_date , df_voyage_schedule ):
            if pd.isna(application_date ):
                return None, None
            try:
                application_date = pd.to_datetime(application_date, errors='coerce')
            except Exception as e:
                print(f"Invalid date: {application_date}, error: {e}")
                return None, None
            future_voyages = df_voyage_schedule[df_voyage_schedule['Start Date'] > application_date]
            if future_voyages.empty:
                return None, None
            next_voyage = future_voyages.iloc[0]
            return next_voyage['Name'], next_voyage['Start Date']

        mask = self.df['Voyage (from Voyage Signups)'] == 'V??'
        for idx in self.df[mask].index:
            app_date = self.df.at[idx, 'Application Date']
            name, start_date = find_next_voyage(app_date , df_voyage_schedule)
            self.df.at[idx, 'Updated Voyage Number'] = name
            self.df.at[idx, 'Updated Voyage Start Date'] = start_date

        regex_mask = self.df['Voyage (from Voyage Signups)'].fillna('').str.match(r'^V\d{2,3}$')
        for idx in self.df[regex_mask].index:
            voyage_name = self.df.at[idx, 'Voyage (from Voyage Signups)']
            voyage_row = df_voyage_schedule[df_voyage_schedule['Name'] == voyage_name]
            if not voyage_row.empty:
                self.df.at[idx, 'Updated Voyage Start Date'] = voyage_row.iloc[0]['Start Date']
                self.df.at[idx, 'Updated Voyage Number'] = voyage_name
    def eleminate_inconsictencies(self):
        self.df['Application Day-of-Week'] = self.df['Application Day-of-Week'].replace('2023-12-08', '6. Friday')

        
        self.df['Day-of-Week No'] = pd.to_numeric(self.df['Day-of-Week No'], errors='coerce')
        self.df.loc[self.df['Day-of-Week No'] == 2023, 'Day-of-Week No'] = 6

        
        self.df['Voyage (from Voyage Signups)'] = self.df['Voyage (from Voyage Signups)'].astype(str)
        self.df.loc[self.df['Voyage (from Voyage Signups)'] == '6', 'Voyage (from Voyage Signups)'] = 'V45'

        
        self.df = self.df.dropna(subset=['Timestamp'])

    
    def update_gender(self):
        mask = self.df['Gender'].str.lower().isin(['non-binary', 'prefer not to say', 'trans', 'other'])
        self.df.loc[mask, 'Gender'] = 'other'

    
    def update_goal(self):
        mask = self.df['Goal'].str.lower().isin(['other', 'unknown'])
        self.df.loc[mask , 'Goal'] = 'other'

    def _clean_column_name(self, col):
        col = col.strip().lower()
        col = re.sub(r"[\s\-]+", "_", col)
        col = re.sub(r"[^\w]", "", col)
        return col

    def standardize_column_names(self):
        self.df.columns = [self._clean_column_name(col) for col in self.df.columns]