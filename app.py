# import libraries
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import zipfile
import warnings
warnings.filterwarnings("ignore")

# set title and layout
st.set_page_config(page_title="Job Descriptions Analysis", layout="wide")
st.title("Job Descriptions Analysis App")


# Load data from ZIP using @st.cache_data
@st.cache_data
def load_data():
    with zipfile.ZipFile("clean_job_descriptions.zip", 'r') as zip_ref:
        with zip_ref.open("clean_job_descriptions.csv") as file:
            df = pd.read_csv(file)
    return df

df = load_data()


# show raw data
st.subheader("Clean Data")
st.dataframe(df.head())

st.subheader("Clean Data Statistics Summary")
st.dataframe(df.describe())

# top job locations
# Preview the data
print(df[['Location', 'Title']].head())

# Count number of jobs per location
location_counts = df['Location'].value_counts().reset_index()
location_counts.columns = ['Location', 'Job Count']

# Display top 10 locations with the most jobs
top_locations = location_counts.head(10)
st.subheader("Top Job Locations")
fig1, ax1 = plt.subplots()
sns.barplot(data=top_locations, x='Location', y='Job Count', palette='viridis',ax=ax1)
st.pyplot(fig1)


# Step 1: Convert titles to lowercase and split into words
words = df['Title'].dropna().str.lower().str.split()

# Step 2: Count word frequencies
all_words = [word for title in words for word in title]
common_words = Counter(all_words).most_common(20)

# Step 3: Convert to DataFrame for plotting
word_df = pd.DataFrame(common_words, columns=['Keyword', 'Count'])
st.subheader("Common Keywords in Job Titles")
fig2, ax2 = plt.subplots()
sns.barplot(word_df['Keyword'], word_df['Count'], color='skyblue', ax=ax2)
st.pyplot(fig2)

st.subheader("Salary Range")
fig3, ax3 = plt.subplots()
sns.boxplot(x=df['Average Salary'], color='red', ax = ax3)
st.pyplot(fig3)

# Group by date and count the number of jobs posted each day
daily_posts = df.groupby(df['Date Posted'].dt.date).size()
st.subheader("job Posted Over Days/Weeks")
fig4, ax4 = plt.subplots()
daily_posts.plot(kind='line', color='teal', ax=ax4)
st.pyplot(fig4)

# github link
st.markdown("---")
st.markdown("[View Full Project on GitHub] (https://github.com/shivharebhupendra/Build_Week_Project)")
