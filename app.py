from flask import Flask,render_template,request
import model as m
app=Flask(__name__)


@app.route('/',methods=["GET","POST"])
def home():
 if request.method == "POST":
    sg= request.form["sg"]
    al = request.form["al"]
    sod = request.form["sod"]
    hemo = request.form["hemo"]
    pcv = request.form["pcv"]
    htn = request.form["htn"]
    dm = request.form["dm"]
    pred=m.predection(float(sg),float(al),float(sod),float(hemo),float(pcv),float(htn),float(dm))   
    if pred==1:
     return render_template("index.html",pr="Ckd") 
    else :
     return render_template("index.html",pr="NCKD")  
 return render_template("index.html")

 
if __name__=="__main__":
 if __name__=="__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), 
            port=int(os.getenv('PORT', 4444)))
 
