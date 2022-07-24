from flask import Flask, render_template



def ceoController():
    return render_template('ceo.html')