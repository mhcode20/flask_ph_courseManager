from flask import Flask, render_template
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
        return h,m

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

app.run()