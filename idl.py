from altair.vegalite.v4.schema.channels import Href
import streamlit as st
import pandas as pd
import numpy as np
from sklearn import datasets
import seaborn as sn 
import matplotlib as plt
from streamlit.elements.file_uploader import FileUploaderMixin
st.title("welcome to stream it")
dataset=st.sidebar.selectbox("select",options=["iris","breast cancer","wine"])

#classifier=st.sidebar.selectbox("select,"options=["LinearRegression","kkn"])
st.write("""## data set selected is """,dataset)
def select_dataset(dataname):
    if dataname =="iris":
        data=datasets.load_iris()
        st.write("""dataset irris""")
        print(data)
    elif dataname =="breast cancer":
        data=datasets.load_breast_cancer()
        st.write("""dataset breast""")
    else:
        data=datasets.load_wine()
        st.write("""dataset wine""")
    x=data.data
    y=data.target
    x1=pd.DataFrame(x,columns=data.feature_names)
    x2=pd.DataFrame(y)
    return x,y,x1,x2

x,y,x1,x2=select_dataset(dataset)
#x1=frame(dataset)
st.write(""" ## SHAPE OF DATA IS""",x.shape)
st.write(""" ## No of classes  """,len(np.unique(y)))
box=st.selectbox(""" display data """,options=["inputdata","targetdata"])
if box =="inputdata":
    st.write(""" ## Input Data""",x1.head())
elif box =="targetdata":
    st.write(""" ## target Data""",x2.head())
#st.write("""# heat map """,sn.heatmap(x1.corr(),annot=True))
#box1=st.selectbox("""## PLOT""",options=["inputdata","targetdata"])
st.bar_chart(x1)
st.area_chart(x1)
st.altair_chart(x1)
 
import bs4
Href="https://app.powerbi.com/reportEmbed?reportId=55021219-4186-4a3b-b904-4df92fd29bb0&autoAuth=true&ctid=bf93bb5e-ecf0-4e3d-be0e-79b5cc527a48&config=eyJjbHVzdGVyVXJsIjoiaHR0cHM6Ly93YWJpLWluZGlhLWNlbnRyYWwtYS1wcmltYXJ5LXJlZGlyZWN0LmFuYWx5c2lzLndpbmRvd3MubmV0LyJ9"
st.write(Href)



