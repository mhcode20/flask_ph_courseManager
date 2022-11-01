from flask import Flask, redirect, render_template
import pickle


class vid:
    def __init__(self,name,is_done=False):
        self.name = name
        self.duration = 55#vd(name)/60
        self.is_done = is_done
        self.order = int(name[6:8].replace('.',''))
    def done(self):
        self.is_done = True

file = open('data.myd','rb')
tl = pickle.load(file)

sum = 0
for i in tl:
    sum += i.duration
sum = round(sum)
class main_page:
    def __init__(self,tl,dur):
        self.totalV = len(tl)
        self.tDuration = dur
        self.done = 0
        self.ml = tl
        self.ml.sort(key=lambda x: x.order)
        self.hour,self.min = self.hnm(dur)
    def hnm(self,d):
        h = d//60
        m = d%60
        return int(h),int(m)
    def reset(self,id):
        self.done +=1
        self.tDuration -= round(self.ml[id].duration)
        self.hour,self.min = self.hnm(self.tDuration)
        self.ml[id].done()

mp = main_page(tl,sum)


app = Flask(__name__)

class vid:
    def __init__(self,name,is_done=False):
        self.name = name
        self.duration = 55#vd(name)/60
        self.is_done = is_done
        self.order = int(name[6:8].replace('.',''))
    def done(self):
        self.is_done = True

@app.route('/')
def hello_world():
    return render_template('index.html',data=mp)

@app.route("/flask/<id>")
def doneop(id):
    if mp.ml[int(id)-1].is_done != True:
        mp.reset(int(id)-1)
    return redirect("/", code=302)
app.run()