import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

df=pd.read_csv('worldcities.csv')

st.title('World Major Cities - Caroline ')

population_filter=st.slider('choose minimal population',0,40,15) #min, max, default

capital_filter=st.sidebar.multiselect('capital filter',df.capital.unique(),df.capital.unique())

form=st.sidebar.form('country-form')
country_filter=form.text_input('Enter Country Name', 'ALL')
form.form_submit_button('Apply')

#population filter

df=df[df.population>population_filter]
#capitol filter
df=df[df.capital.isin(capital_filter)]
# country filter
if country_filter != 'ALL':
    df=df[df.country==country_filter]

st.map(df)

st.write(df[['city','country','population']])

fig, ax = plt.subplots(figsize=(20, 5))
pop_sum = df.groupby('country')['population'].sum()
pop_sum.plot.bar(ax=ax)
st.pyplot(fig)