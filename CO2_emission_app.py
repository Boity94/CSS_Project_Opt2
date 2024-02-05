#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 09:48:19 2024

@author: boitumelo_mabakachaba
"""

import streamlit as st
import pandas as pd
import matplotlib as plt
import seaborn as sns

# Load the CO2 emission dataset
@st.cache
def load_data():
    df = pd.read_csv('GlobalCO2Emissions.csv')  # Replace with your dataset path
    return df

# Data exploration section
def explore_data(df):
    st.title('💨 CO2 Emission Over The 3 Decades💨')
    
    # Display the dataset
    st.subheader('Raw Data')
    st.write(df.head())

    # Display summary statistics
    st.subheader('Summary Statistics')
    st.write(df.describe())

    # Display missing values
    st.subheader('Missing Values')
    st.write(df.isnull().sum())

# Data cleaning and transformation section
def clean_and_transform_data(df):
    st.title('Clean and Transform Data')

    # Example: Drop missing values
    df_cleaned = df.dropna()

    # Example: Transform data if needed
    # df_transformed = ...

    st.success('Data cleaning and transformation complete.')
    return df_cleaned

    st.set_option('deprecation.showPyplotGlobalUse', False)
# Data visualization section
def visualize_data(df):
    st.title('Data Visualization')

    # Choose a visualization type
    visualization_type = st.sidebar.radio('Choose Visualization Type', ('Line Chart', 'Pie Chart', 'Histogram'))

    if visualization_type == 'Line Chart':
        # Line chart example
        plt.figure(figsize=(10, 6))
        sns.lineplot(x='Year', y='Emissions', data=df)
        plt.title('CO2 Emission Over Time')
        plt.xlabel('Year')
        plt.ylabel('CO2 Emission')
        #st.pyplot()

    elif visualization_type == 'Pie Chart':
        # Pie chart example
        pie_data = df['Year'].value_counts()
        plt.figure(figsize=(10, 6))
        plt.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', startangle=90)
        plt.title('CO2 Emission Distribution by year')
        #st.pyplot()

    elif visualization_type == 'Histogram':
        # Histogram example
        plt.figure(figsize=(10, 6))
        sns.histplot(df['Emissions'], bins=30, kde=True)
        plt.title('Histogram of CO2 Emission')
        plt.xlabel('CO2 Emission')
        plt.ylabel('Frequency')
        #st.pyplot()

def main():
    st.sidebar.title('Navigation')
    page = st.sidebar.radio('Go to', ('Explore Data', 'Clean and Transform Data', 'Data Visualization'))

    df = load_data()

    if page == 'Explore Data':
        explore_data(df)
    elif page == 'Clean and Transform Data':
        df_cleaned = clean_and_transform_data(df)
        explore_data(df_cleaned)
    elif page == 'Data Visualization':
        visualize_data(df)

if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
