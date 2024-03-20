import streamlit as st
import pandas as pd

st.title('Nutritional Information')

df = pd.read_csv('nutrients.csv')

st.subheader('Original Data')

st.write(df)

# Make columns numeric so we can perform operations on them
df['Protein'] = pd.to_numeric(df['Protein'], errors='coerce')
df['Calories'] = pd.to_numeric(df['Calories'], errors='coerce')

# New column
df['Protein/Calorie'] = df['Protein'] / df['Calories']

# Sort by protein/calorie ratio
sorted_df = df.sort_values(by='Protein/Calorie', ascending=False)

sorted_df = sorted_df[['Food', 'Protein', 'Calories', 'Protein/Calorie', 'Category']]

all_tab, meat_tab, dairy_tab, seafood_tab, nuts_and_seeds_tab = st.tabs(["All Foods", "Meat", "Dairy", "Seafood", "Nuts and Seeds"])

with all_tab:
    st.write(sorted_df)
with meat_tab:
    st.table(sorted_df[sorted_df["Category"] == "Meat, Poultry"])
with dairy_tab:
    st.table(sorted_df[sorted_df["Category"] == "Dairy products"])
with seafood_tab:
    st.table(sorted_df[sorted_df["Category"] == "Fish, Seafood"])
with nuts_and_seeds_tab:
    st.table(sorted_df[sorted_df["Category"] == "Seeds and Nuts"])