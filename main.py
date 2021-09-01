import streamlit as st 
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')


st.write('プログレスバーの表示')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!'





st.write('DataFrame')

df = pd.DataFrame({
   '1列目' : [1,2,3,4],
   '2列目' : [10,20,30,40],
})

st.dataframe(df.style.highlight_max(axis=0))

""""

# マジックコマンド
## #の数で変わる
### ダブルクオーテーション三つで挟む

```python

import streamlit as st 
import numpy as np
import pandas as pd

マークダウン記法（バッククオーてしょん三つ`）
```


"""

df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)

st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)


df = pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns=['lat','lon']
)
st.map(df)


img = Image.open('icon.png')
st.image(img,caption='Icon',use_column_width=True)

audio_file = open('audio.mp3','rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes,format='audio/mp3')

video_file = open('Movie.mov' , 'rb')
video_bytes = video_file.read()

st.video(video_bytes)


text = st.sidebar.text_input('あなたの趣味を教えてください。')
condition = st.slider('あなたの今の調子は？',0,100,50)

'あなたの趣味:',text
'コンディション:',condition

left_column,right_column = st.columns(2)
button = left_column.button('右絡むに文字を表示')
if button:
    right_column.write('表示された文字')




expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')



