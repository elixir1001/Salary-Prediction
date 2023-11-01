<<<<<<< HEAD
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map

def clean_experience(x):
    if x == 'More than 50 years':
        return 50
    if x == 'Less than 1 year':
        return 0.5
    return float(x)

def clean_education(x):
    if "Bachelor" in x:
        return "Bachelors degree"
    if "Master" in x:
        return "Masters degree"
    if "Professional" in x or "Other doctoral" in x:
        return "Post grad"
    return "Less than a bachelors"

@st.cache
def load_data():
    df = pd.read_csv("survey_results_public.csv")
    df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedCompYearly"]]
    df = df.rename({"ConvertedCompYearly" : "Salary"}, axis=1)
    df = df[df["Salary"].notnull()]
    df = df.dropna()
    df = df[df["Employment"] == "Employed, full-time"]
    df = df.drop("Employment", axis=1)
    country_map = shorten_categories(df.Country.value_counts(), 400)
    df['Country'] = df['Country'].map(country_map)
    df = df[df['Salary'] <= 250000]
    df = df[df['Salary'] >= 10000]
    df = df[df['Country'] != 'Other']
    df['YearsCodePro'] = df['YearsCodePro'].apply(clean_experience)
    mapping = {
        'Master’s degree (M.A., M.S., M.Eng., MBA, etc.)': 'Master',
        'Bachelor’s degree (B.A., B.S., B.Eng., etc.)': 'Bachelor',
    }
    # Use the replace method to replace the values in the 'EdLevel' column
    df['EdLevel'] = df['EdLevel'].replace(mapping)
    df["EdLevel"] = df["EdLevel"].apply(clean_education)
    return df

df = load_data()

def show_explore_page():
    st.title("Explore Software Developer Salaries")
    st.write(
        """### Stack Overflow Developer Survey 2022"""
    )
    st.write(
        """#### Number of Data from different Countries"""
    )
    data = df["Country"].value_counts()
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
    explode_slider = st.slider("Explode", min_value=0.0, max_value=1.0, step=0.1)
    explode = (explode_slider, explode_slider, explode_slider, explode_slider, explode_slider,explode_slider,explode_slider,explode_slider,explode_slider,explode_slider,explode_slider,explode_slider,explode_slider,explode_slider,explode_slider)  # Explode the first slice
    fig1, ax1 = plt.subplots(figsize = (10,10))
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=False, startangle=90, colors=colors, explode=explode)
    ax1.axis("equal") #Equal aspect ratio ensures that pie is drawn as a circle

    
    st.pyplot(fig1)

    st.write(
        """#### Mean Salary Based on Country"""
    )

    data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data)
    st.dataframe(data)

    st.write(
        """#### Mean Salary Based on Experience"""
    )
    data = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
=======
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map

def clean_experience(x):
    if x == 'More than 50 years':
        return 50
    if x == 'Less than 1 year':
        return 0.5
    return float(x)

def clean_education(x):
    if "Bachelor" in x:
        return "Bachelors degree"
    if "Master" in x:
        return "Masters degree"
    if "Professional" in x or "Other doctoral" in x:
        return "Post grad"
    return "Less than a bachelors"

@st.cache
def load_data():
    df = pd.read_csv("survey_results_public.csv")
    df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedCompYearly"]]
    df = df.rename({"ConvertedCompYearly" : "Salary"}, axis=1)
    df = df[df["Salary"].notnull()]
    df = df.dropna()
    df = df[df["Employment"] == "Employed, full-time"]
    df = df.drop("Employment", axis=1)
    country_map = shorten_categories(df.Country.value_counts(), 400)
    df['Country'] = df['Country'].map(country_map)
    df = df[df['Salary'] <= 250000]
    df = df[df['Salary'] >= 10000]
    df = df[df['Country'] != 'Other']
    df['YearsCodePro'] = df['YearsCodePro'].apply(clean_experience)
    mapping = {
        'Master’s degree (M.A., M.S., M.Eng., MBA, etc.)': 'Master',
        'Bachelor’s degree (B.A., B.S., B.Eng., etc.)': 'Bachelor',
    }
    # Use the replace method to replace the values in the 'EdLevel' column
    df['EdLevel'] = df['EdLevel'].replace(mapping)
    df["EdLevel"] = df["EdLevel"].apply(clean_education)
    return df

df = load_data()

def show_explore_page():
    st.title("Explore Software Developer Salaries")
    st.write(
        """### Stack Overflow Developer Survey 2022"""
    )
    st.write(
        """#### Number of Data from different Countries"""
    )
    data = df["Country"].value_counts()
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']
    explode_slider = st.slider("Explode", min_value=0.0, max_value=1.0, step=0.1)
    explode = (explode_slider, explode_slider, explode_slider, explode_slider, explode_slider,explode_slider,explode_slider,explode_slider,explode_slider,explode_slider,explode_slider,explode_slider,explode_slider,explode_slider,explode_slider)  # Explode the first slice
    fig1, ax1 = plt.subplots(figsize = (10,10))
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=False, startangle=90, colors=colors, explode=explode)
    ax1.axis("equal") #Equal aspect ratio ensures that pie is drawn as a circle

    
    st.pyplot(fig1)

    st.write(
        """#### Mean Salary Based on Country"""
    )

    data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data)
    st.dataframe(data)

    st.write(
        """#### Mean Salary Based on Experience"""
    )
    data = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
>>>>>>> b41f596f6209bb1d339f7acab2f414b2e1df9978
    st.line_chart(data)