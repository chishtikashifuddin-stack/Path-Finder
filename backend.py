import os 
from flask import Flask,request,render_templet
app=Flask(__name__)
@app.route('/',methods=["GET","POST"])
def a():
    if request.method == "POST":    
        data=request.form.get("data")
        b=f"{data}.txt"
        data=os.popen(r"where /r c:\ "+b).read()
        for d1 in data:
            if "user" in d1:
                data=d1
        return f"Your file path is {result}"
    return render_templet("pathfinder.html")    
        
if __name__ == __main__:
    app.run(host == "0.0.0.0", port=5000, debug=True)
