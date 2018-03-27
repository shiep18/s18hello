# import our RPi.GPIO module and reference it as gpio
import RPi.GPIO as gpio

from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")
def status():
    # get the current input state from our feedback loop
    input_state = gpio.input(17)
    # Check out input state and map it to a human readable status
    if input_state :
        led_status = "Off"
    else:
        led_status = "On" 
    return """<html><body><div style="text-align: center;"><h2 style="text-align: center;"> %s or Off,click on it. </h2></br><a href="/off">Off</a>  |  <a href="/on">On</a></div>""" % led_status

@app.route("/off")
def led_on():
    # Turn pin 4 Off (low)
    gpio.output(04,False)
    return redirect(url_for('status'))

@app.route("/on")
def led_off():
    # Turn pin 4 off (high)
    gpio.output(04,True)
    return redirect(url_for('status'))

if __name__ == "__main__":
    # specify the setmode method were going to use, Im using the BCM mode, as this seems to corrolate with the wikis pin layout.
    gpio.setmode(gpio.BCM)
    # register GPIO 4 as an output pin
    gpio.setup(04,gpio.OUT)
    # register GPIO 17 as an input pin
    gpio.setup(17,gpio.IN)
    app.run(host="192.168.35.74")
