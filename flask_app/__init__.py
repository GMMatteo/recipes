from flask import Flask, request, render_template, redirect, session
app = Flask(__name__)
app.secret_key = '598'