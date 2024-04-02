import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt

st.header('Interactive Charts')
chart_data = pd.DataFrame(np.random.randn(20,3), columns=['Line_1','Line_2','Line_3'])

st.subheader('Line Chart')
st.line_chart(chart_data)

st.subheader('Area Chart')
st.area_chart(chart_data)

st.subheader('Bar Chart')
st.bar_chart(chart_data)

st.header('2. Data Visualization with Matplotlib and Seaborn')
st.subheader('2.1 Loading the file in dataframe')
df = pd.read_csv('iris.csv')
st.dataframe(df)

st.subheader('2.2 Bar Graph with Matplotlib')
fig = plt.figure(figsize=(15,8))
df['sepal_length'].value_counts().plot(kind='bar')
st.write(df['sepal_length'].value_counts())
st.pyplot(fig)

st.subheader('2.3 Distribution plot with seaborn')
fig = plt.figure(figsize=(15,8))
sn.distplot(df['sepal_length'])
st.pyplot(fig)

st.header('3. Multiple graphs in a row')
col1, col2, col3 = st.columns(3)
with col1:
    col1.header = 'KDE - false'
    fig = plt.figure(figsize=(5,5))
    sn.distplot(df['sepal_length'], kde = False)
    st.pyplot(fig)
with col2:
    col2.header = 'Hist - false'
    fig = plt.figure(figsize=(5,5))
    sn.distplot(df['sepal_length'], hist = False)
    st.pyplot(fig)
with col3:
    col3.header = 'both hist & KDE'
    fig = plt.figure(figsize=(5,5))
    sn.distplot(df['sepal_length'])
    st.pyplot(fig)

st.header('4. Changing Styles')
col1, col2, col3 = st.columns(3)
with col1:
    fig = plt.figure()
    sn.set_style('darkgrid')
    sn.set_context('notebook')
    sn.distplot(df['sepal_length'], kde = False)
    st.pyplot(fig)
with col2:
    fig = plt.figure()
    sn.set_theme(context = 'poster', style='darkgrid')
    sn.distplot(df['sepal_length'], kde = False)
    st.pyplot(fig)
with col3:
    fig = plt.figure(figsize=(5,5))
    sn.distplot(df['sepal_length'], kde= False)
    st.pyplot(fig)

st.header('5. Exploring different graphs in Seaborn')
st.subheader('5.1 Scatter plot')
fig,ax = plt.subplots()
ax.scatter(*np.random.random(size=(2,50)), s=10, marker='>')     #'*' means random number generated for both x amd y
st.pyplot(fig)

st.subheader('5.2 Count plot')
fig = plt.figure()
sn.countplot(data=df, x='species')
st.pyplot(fig)

st.subheader('5.3 Box plot')
fig = plt.figure()
sn.boxplot(data=df, x='species', y='petal_length')
st.pyplot(fig)

st.subheader('5.1 Violin plot')
fig = plt.figure()
sn.violinplot(data=df, x='species', y='petal_length')
st.pyplot(fig)
