import matplotlib.pyplot as plt
import streamlit as st

def plot_bar_chart(data, x_col, y_col, title, xlabel, ylabel, rotate_xticks=False):
    plt.figure(figsize=(10, 6))
    plt.bar(data[x_col], data[y_col], color='red')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
   

    if rotate_xticks:
        plt.xticks(rotation=45, ha='right', fontsize= 10)
        plt.subplots_adjust(bottom=0.3)

    st.pyplot(plt)


def plot_pie_chart(labels, sizes, title):
    plt.figure(figsize=(4, 4))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=60, colors=['#66b3ff','#ff9999'])
    plt.title(title)
    st.pyplot(plt)
    