from flask import Flask, render_template, request,session,url_for,redirect
import RPi.GPIO as GPIO

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/on')
def on():
    print("on")
    GPIO.output(18,GPIO.HIGH)
    return render_template('index.html',message='on')
    
@app.route('/off')
def off():
    print("off")
    GPIO.output(18,GPIO.LOW)
    return render_template('index.html',message='off')
    
if __name__ == '__main__':
    app.run()
