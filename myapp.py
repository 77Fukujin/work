# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
from PIL import Image
import random
#requirements.txtにpillowを記述して一緒にプッシュする
# streamlit run ファイル名.py で最初の実行


st.title('Daily Score')

st.subheader('今日の一日を振り返る(・_・)')
text = st.text_input('今日の日付を教えて。')
'今日の日付：',text,

text = st.text_input('今日がんばったこと！')
'今日がんばったこと:',text,

text = st.text_input('うれしかったこと！')
'うれしかったこと:',text,

text = st.text_input('やり残したこと！')
'やり残したこと:',text,

text = st.text_input('明日がんばること！')
'明日がんばること:',text,



image1 = Image.open('MOWチョコ.JPEG')
#st.image1(image1, caption='MOWチョコ')
image2 = Image.open('MOW抹茶.JPG')
#st.image2(image2, caption='MOW抹茶')
image3 = Image.open('アイスまんじゅう.JPEG')
#st.image3(image3, caption='あいすまんじゅう')
image4 = Image.open('あずきバー.PNG')
#st.image4(image4, caption='あいすバー')
image5 = Image.open('クーリッシュバニラ.JPG')
#st.image5(image5, caption='クーリッシュバニラ')
image6 = Image.open('パナップ.JPG')
#st.image6(image6, caption='パナップ')
image7 = Image.open('やわもち　わらびもち.JPG')
#st.image7(image7, caption='やわもち　わらびもち')

image8 = Image.open('MOWバニラ.JPG')
image9 = Image.open('ガーナスティック.JPG')
image10 = Image.open('ザ・クレープ.JPG')
image11 = Image.open('ジャイアントコーン黄色.JPG')
image12 = Image.open('スーパーカップ　チョコミント.JPG')
image13 = Image.open('ピノ.JPG')
image14 = Image.open('板チョコアイス.PNG')
image15 = Image.open('MOWあずき.JPG')
image16 = Image.open('ジャイアントコーン　チョコ.JPG')
image17 = Image.open('スーパーカップチョコチップ.JPG')
image18 = Image.open('パピコ.JPG')
image19 = Image.open('パルム.JPG')
image20 = Image.open('ビスケットサンド.JPEG')
image21 = Image.open('雪見だいふく.JPG')
image22 = Image.open('MOWラムレーズン.PNG')
image23 = Image.open('ジャージー牛乳ソフト.JPG')
image24 = Image.open('ジャイアントコーン赤.JPG')
image25 = Image.open('しろくま.JPEG')
image26 = Image.open('スーパーカップバニラ.JPG')
image27 = Image.open('チョコモナカジャンボ.JPG')
image28 = Image.open('ルマンドアイス.JPG')


#sokosokoice = [image1,image2,image3]

goodice = [image1,image2,image3,image4,image5,image6,image7]
sogoodice = [image8,image9,image10,image11,image12,image13,image14]
greatice = [image15,image16,image17,image18,image19,image20,image21]
wonderfulice = [image22,image23,image24,image25,image26,image27,image28]






#sokosoko = random.choice(sokosokoice)

#st.image(sokosoko, caption=(sokosoko,'のアイス'))
#st.image(sokosoko)




rate = st.radio("今日一日は何点だった？？",('0~30','30~60','60~90','100'))

if rate == '0~30':
    st.write('明日はきっといい日になる')
    #ここに画像を表示す
    #sokosoko = random.choice(sokosokoice)
    #st.image(sokosoko)
     
   
    wonderful = random.choice(wonderfulice)
    
    #st.image(wonderful, caption='今日は',wonderful,'のアイスを食べよう')

elif rate == '30~60':
    st.write('笑い合えたらいい日になる')
    #ここに画像を表示する
    great = random.choice(greatice)
    st.image(great)

elif rate == '60~90':
    st.write('今日よりずっといい日になる')
    #ここに画像を表示する
    sogood = random.choice(sogoodice)
    st.image(sogood)

elif rate == '100':
    st.write('君が笑えばいい日になる')
    #ここに画像を表示する
    good = random.choice(goodice)
    st.image(good)


#elif rate == 


# streamlit run すとりーむれっと.py 

