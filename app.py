import re
from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def index_func():
    render_template("index.html")
@app.route('/',methods=['GET','POST'])
def output_func():
    if request.method=='POST':
        regex=request.form['testString']
        string=request.form['regex']
        match=[(ele.start(),ele.end()) for ele in re.finditer(regex,string,flags=re.IGNORECASE)]
        count=len(match)
    return render_template('backend.html',r=regex,s=string,match=match,count=count)

if __name__=='__main__':
    app.run(debug=True)