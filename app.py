from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

load_dotenv() # Load variables from .env file

openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/generate_text", methods=["POST"])
def generate_text():
    prompt = request.form["prompt"]
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    generated_text = response.choices[0].text
    return render_template("generated_text.html", prompt=prompt, generated_text=generated_text)

if __name__ == '__main__':
    app.debug = True
    app.run()
