from flask import Flask, render_template, request
import Han2B , B2Han, SaveTheImage, TTS, correction
import os
import shutil
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        # 파라미터를 전달 받습니다.
        Hangul_string= str(request.form['avg_temp'])

        Braille = Han2B.datainput(Hangul_string)
        files = SaveTheImage.SaveImage(Braille)
        print(Braille)
        FileName = ''.join(Braille)
        RealFileName = FileName[0:89]
        path = "image/"
        TypeOf = ".PNG"


        SaveTheImage.Paste_Image(files)

        SaveFileName = path + RealFileName + TypeOf
        
        return render_template('index.html', price=Braille, image = SaveFileName)

@app.route("/B2H", methods=['GET', 'POST'])
def BR():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        # 파라미터를 전달 받습니다.
        BR_list= str(request.form['min_temp'])

        Hangul = B2Han.text(BR_list)
    
        return render_template('index.html', price=Hangul)

@app.route("/FIX", methods=['GET', 'POST'])
def FIX():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        target_text = str(request.form['FIX'])
        lst = correction.nouns_case(target_text)
        num_error = len(lst)
        correction_text = correction.nouns(target_text)
        cho = correction.cho(correction_text, lst)
        jung = correction.jung(correction_text, lst)
        jong = correction.jong(correction_text, lst)
        err_chea = cho + jung + jong

        lst_up = correction.case_up(correction_text, lst)

        cho_up = correction.cho_upgrade(correction_text, lst_up)
        err_up_chea = cho_up
        
        if len(cho_up) != 1 :
            jung_up = correction.jung_upgrade(correction_text, lst_up)
            err_up_chea += jung_up
            if len(jung_up) != 1 :
                jong_up = correction.jong_upgrade(correction_text, lst_up)
                err_up_chea += jong_up

        return render_template('index.html', num = num_error, lst_error = correction_text, chea_error = err_chea, chea_up_error = err_up_chea )

@app.route("/TTS", methods=['GET', 'POST'])
def gTTS():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        String= str(request.form['mp3'])
        path = "speech/"
        TypeOf = ".mp3"
        mp3file = path + String + TypeOf
        # 파라미터를 전달 받습니다.
        #Mp3FileName = str(String) + ".mp3"
        TTS.TTS(String)
        #TTS.Playing(String)
        #os.remove('C:/Users/tjaud/Documents/motor/Flask/Speech/'+String+'.mp3') 
        return render_template('index.html', speech = mp3file)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000, debug = True)
