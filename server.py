from flask import Flask, render_template, request
import Han2B , B2Han, SaveTheImage, TTS
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
    
        
        return render_template('index.html')

@app.route("/TTS", methods=['GET', 'POST'])
def gTTS():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        String= str(request.form['mp3'])
        # 파라미터를 전달 받습니다.

        TTS.TTS(String)
        TTS.Playing(String)
        #os.remove('C:/Users/tjaud/Documents/motor/Flask/Speech/'+String+'.mp3') 
        return render_template('index.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000, debug = True)