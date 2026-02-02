import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Researcher Profile Page with STEM Data")

# Collect basic information
name = "Mr. Scelo Khumalo"
field = "MSc Chemical Pathology"
institution = "Sefako Makgatho Health Sciences University "

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

st.image(
    "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg",
    caption="Nature (Pixabay)"
)

#About me
st.title("About me")
st.write("An Intern Medical Scientist, specialized in chemical pathology. The primary goal is to be equiped with medical research, being able to analyze and interprete data using different statistical tools such as python, excel, bioinformatics, stata, spss etc. Passionate with medical research and publications")

st.title("My Project")
st.write(" Honours Level,title, Analysis of reasons for the rejections of biological sample in a tertiary hospital, Dr. George Mukhari Academic Hospital.We focused on samples on sample rejections and analyzed the data using Excel. To be pushled in 2026. On Masters Level, titled, Quantification of short-chain fatty acids in type 2 diabetes mellitus patients and non-diabetic individuals, by Chloroformate isobutyl derivatization combined with GC–MS. A review paper published in 2024 and an the article of the findings to be published in 2026")
# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "2024" in publications.columns:
        year_counts = publications["2024"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("2024")

# Add STEM Data Section
st.header("Explore STEM Data")





# Add a contact section
st.header("Contact Information")
email = "scelokhumaloo@gmail.com"
st.write(f"You can reach {name} at {email}.")
