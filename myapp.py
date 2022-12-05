# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st

# streamlit run ファイル名.py で最初の実行

st.title('Daily Score')

import streamlit as st
st.subheader('今日の一日を振り返る(・_・)')
text = st.text_input('今日の日付を教えて。')
'今日の日付：',text,
text = st.text_input('今日頑張ったこと！')
'今日頑張ったことは，',text,'だった。'
text = st.text_input('今日嬉しかったこと！')
'今日嬉しかったことは，',text,'だった。'
text = st.text_input('今日やり残したこと！')
'今日やり残したことは，',text,'だった。'

st.radio("今日一日は何点だった？？",('0~20','20~40','40~60','60~80','80~100'))




# streamlit run すとりーむれっと.py 

