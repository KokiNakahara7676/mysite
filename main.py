import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('streamlit　超入門')

#文字入力バージョン
st.write('ブログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Interation {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!'




left_column, right_column= st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここから右カラム')

expander = st.beta_expander('問い合わせ1')
expander.write('問い合わせ1内容の回答')
expander = st.beta_expander('問い合わせ2')
expander.write('問い合わせ2内容の回答')
expander = st.beta_expander('問い合わせ3')
expander.write('問い合わせ3内容の回答')




text = st.text_input('あなたの趣味を教えて下さい',)
condition = st.slider('あなたの今の調子は？',0, 10, 5)

'あなたの趣味は',text,'です'
'コンディション',condition










## サイドバー追加
# st.sidebar.write('Interactive Wiggets')

# text = st.sidebar.text_input('あなたの趣味を教えて下さい',)
# condition = st.sidebar.slider('あなたの今の調子は？',0, 10, 5)

# 'あなたの趣味は',text,'です'
# 'コンディション',condition




# #チェックボックス
# option = st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1, 10))
# )
# 'あなたの好きな数字は',option,''

# #文字入力バージョン
# st.write('Interactive Wiggets')
# text = st.text_input(
#     'あなたの趣味を教えて下さい',
# )
# 'あなたの趣味は',text,'です'







# st.write('Display Image')
# if st.checkbox('Show Image'):
#     img = Image.open('sample.png')
#     st.image(img, caption='map',use_column_width=True)








#######################################
#######################################
# st.write('DataFrame')

# df = pd.DataFrame(
#    np.random.rand(100, 2)/(50, 50) +(35.69, 139.70),
#    columns=['lat','lon']
# )

#表を出力
#st.dataframe(df.style.highlight_max(axis=0), width=300, height=300)

#グラフを出力（折線）
#st.line_chart(df)

#マップに出力（マッピング）
#st.map(df)
#######################################
#######################################




#######################################
#######################################
#マジックボックス
# """
# #章
# ##節
# ###項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """
#######################################
#######################################