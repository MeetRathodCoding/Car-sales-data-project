import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import base64


def add_bg_from_local(image_file):
   
    with open(image_file, "rb") as file:
        encoded_string = base64.b64encode(file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpg;base64,{encoded_string});
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Example usage of add_bg_from_local function
absolute_image_path = "C:/Users/meeth/OneDrive/Desktop/project/bgg.jpeg"
add_bg_from_local(absolute_image_path)  # Use the absolute path to the image


st.title('CAR SALES DATA ANALYSIS')

# Load data with error handling
try:
    df = pd.read_csv('car_sales_data.csv')
except FileNotFoundError:
    st.error('File not found. Please check the file path.')
    st.stop()
except pd.errors.EmptyDataError:
    st.error('File is empty. Please make sure it is proper.')
    st.stop()
except Exception as e:
    st.error(f'An unexpected error occurred: {e}')
    st.stop()

# Display DataFrame
st.header('')
st.subheader("Car Sales Data File")
if st.button('Open File'):
    st.write(df)

# Show DataFrame shape
st.header('')
st.subheader('Implementation of describe function')
if st.button("Show DataFrame Shape"):
    st.markdown(f"Shape of the DataFrame: {df.shape}")

# Clean and display dataset
st.header('')
st.header('Dataset:')
dataset = df.drop_duplicates()
st.write(f'Total records before cleaning: {len(df)}')
st.write(f'Total records after removing duplicates: {len(dataset)}')

# Implement head function
st.header('')
st.subheader('Implementation of Head Function')
if st.button('Show First 10 Rows'):
    st.write(dataset.head(10))

# Implement tail function
st.header('')
st.subheader('Implementation of Tail Function')
if st.button('Show Last 10 Rows'):
    st.write(dataset.tail(10))

# Implement describe function
st.header('')
st.subheader('Implementation of Describe Function')
if st.button('Show Describe'):
    st.write(dataset.describe())

# Plotting
st.header('')
st.sidebar.header('Plotting Options')
column = st.sidebar.selectbox('Select Column', df.columns, index=2)

if column:
    st.header('')
    st.subheader('Bar Chart')
    st.bar_chart(df[column].head(10))

    st.header('')
    st.subheader('Line Chart')
    st.line_chart(df[column].head(10))
    
    st.header('')
    st.subheader('Scatter Plot')
    st.scatter_chart(df[column].head(10))
    
    st.header('')
    st.subheader("Pie Chart using Matplotlib")
    plt.figure(figsize=(8, 8))
    plt.pie(df['Car Make'].value_counts().values, autopct='%1.1f%%', labels=df['Car Make'].value_counts().index)
    st.pyplot(plt)
else:
    st.error('Please select a column for plotting.')

