from flask import Flask, render_template ,request
from ImageCaptioning import caption
import model
import webScrap
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/image')
def image():  
    return render_template('image.html')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/summary')
def getSummary():
    return render_template('summerise.html')

@app.route('/short',methods=['GET', 'POST'])  
def short():
    print(request.form.to_dict())
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        if len(data['topic'])>3:
            text=webScrap.text(data['topic'])
            textSummary=model.generate_summary(text)
            return render_template('results.html', my_string=textSummary)
    else:
        return render_template('results.html', my_string="Something is missing")


@app.route('/')
def hello():
    return render_template("home.html")

@app.route('/summarize',methods=['GET', 'POST'])
def summary():
    if request.method == 'POST':
        data = request.form.to_dict()        
        if 'test' in data and len((data['test']))>10:
            data['test']=data['test'].replace("\r\n"," ")
            text=model.generate_summary(data['test'])
            return render_template('results.html', my_string=text) 
        else:
            text=webScrap.getUrl(data['web'])
            if text:
                text=model.generate_summary(text)
            else:
                text="There is some problem in the url"
            return render_template('results.html', my_string=text) 
    else:
        return render_template('results.html', my_string="Something Not Right")
    


@app.route('/after', methods=['GET', 'POST'])
def after():
    print("\n"*10,request.files)
    img = request.files['file1']
    print(img)
    final=caption(img)
    
    return render_template('after.html', data=final)




if __name__ == '__main__':
    app.run()