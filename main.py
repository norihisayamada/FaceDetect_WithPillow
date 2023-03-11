import streamlit as st
from PIL import Image
from PIL import UnidentifiedImageError
import cv2 as cv
import numpy as np


st.title('人間・キャラクターの顔認識アプリ')

bunnruiki = st.sidebar.radio("人間・キャラクター",('人間', 'キャラクター'))
param = st.sidebar.slider('トリミング後の画像の大きさ', -30, 30, 15)

uploaded_file = st.file_uploader("jpg画像をアップロードしてください。")

if uploaded_file is None:
    try:
        img = cv.imread('Lena.jpg')
        # img = Image.open(uploaded_file)
        if bunnruiki == "人間":
            bunnruiki = 'haarcascade_frontalface_alt.xml'
            bunnruiki_type = "人"
        elif bunnruiki == 'キャラクター':
            bunnruiki = 'lbpcascade_animeface.xml'
            bunnruiki_type = "キャラクター"

        # ダウンロードしたファイルを指定
        cascade = cv.CascadeClassifier(bunnruiki)

        # opencvの処理
        # pillow から opencvに変換
        img = np.array(img, dtype=np.uint8)
        # グレーに変換
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        gray = cv.equalizeHist(gray)
        # 顔判定
        faces = cascade.detectMultiScale(gray,
                                         # detector options
                                         scaleFactor=1.1,
                                         minNeighbors=5,
                                         minSize=(24, 24))
        i = 0
        img_trim = []
        for (x, y, w, h) in faces:
            # トリミング
            param = param

            x = x - param
            y = y - param - 6  # 気持ち上にずらす
            w = w + param * 2
            h = h + param * 2

            img_trim.append(img[y:y + h, x:x + w])
            i += 1

        tex_loc1 = st.empty()
        tex_loc2 = st.empty()
        tex_loc3 = st.empty()

        # 後から□を書いた画像を貼る
        image_loc = st.empty()

        # st.image(img , caption='判定した画像', use_column_width=True)
        st.header(bunnruiki_type + 'の顔は、' + str(i) + '人検出されました。')
        tex_loc4 = st.empty()

        col1, col2, col3, col4, col5 = st.beta_columns(5)
        # 横５列に並べる
        j = 0
        for index in range(0, int(np.ceil(i / 5))):
            if j < i:
                with col1:
                    st.image(img_trim[j], use_column_width=True)
                    j += 1
            else:
                break
            if j < i:
                with col2:
                    st.image(img_trim[j], use_column_width=True)
                    j += 1
            else:
                break
            if j < i:
                with col3:
                    st.image(img_trim[j], use_column_width=True)
                    j += 1
            else:
                break
            if j < i:
                with col4:
                    st.image(img_trim[j], use_column_width=True)
                    j += 1
            else:
                break
            if j < i:
                with col5:
                    st.image(img_trim[j], use_column_width=True)
                    j += 1
            else:
                break
        st.write("正常に終了しました。")
        # 画像に□を書く
        for (x, y, w, h) in faces:
            # □の大きさをトリミングに合わせる
            param = param

            x = x - param
            y = y - param - 6  # 気持ち上にずらす
            w = w + param * 2
            h = h + param * 2
            cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        tex_loc4.write('四角で囲われた場所をトリミングしました。')
        image_loc.image(img, width=700)

#例外処理
    except ValueError as error:
        tex_loc1.warning('ERROR : ' + str(error))
        tex_loc2.warning(' "トリミング後の画像の大きさ"の値を変更してください。')
        tex_loc3.warning('トリミング後の画像の大きさ : ' + str(param))
    except UnidentifiedImageError as error:
        st.warning('ERROR : ' + str(error))
        st.warning('画像以外がアップロードされました。または、アップロードされた画像は認識できない画像です。')
