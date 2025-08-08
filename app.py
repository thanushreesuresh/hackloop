from flask import Flask, render_template, request, url_for
import google.generativeai as genai
import random
import os

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['APP_NAME'] = 'Chali Meter'

# Replace with your actual API key
GOOGLE_API_KEY = "AIzaSyAbA6G9h6gnWz73QiZYcS5EMZu5L5xZ4pk"
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

# Store scores across sessions (for demo; not production-safe)
joke_scores = []

# Fun roast responses in English
roast_lines = [
    "That joke was so bad, even crickets stayed silent!",
    "Is that a joke or a cry for help?",
    "I've heard better jokes from a broken toaster!",
    "That joke was so dry, it turned the Sahara green!",
    "Congratulations, you've invented anti-humor!"
]

def roast_user(joke):
    prompt = f"Here's a user's joke: \"{joke}\"\n\nRoast the user for this joke in a funny and witty way. Limit the response to 3 sentences."
    response = model.generate_content(
        prompt
    )
    return response.text.strip()

def get_random_sticker():
    stickers_folder = os.path.join(app.static_folder, 'stickers')
    stickers = [f for f in os.listdir(stickers_folder) if os.path.isfile(os.path.join(stickers_folder, f))]
    return url_for('static', filename=f'stickers/{random.choice(stickers)}')

@app.route("/", methods=["GET", "POST"])
def home():
    response = None
    seconds = None
    roast = None
    sticker_url = None

    if request.method == "POST":
        joke = request.form.get("joke", "")
        seconds = round(random.uniform(0.1, 10.0), 2)  # Simulate laugh duration with decimal values
        roast = roast_user(joke)  # Generate a roast using the Gemini API
        score = random.randint(1, 10)  # Simulate a joke rating
        joke_scores.append(score)  # Add the score to the list
        sticker_url = get_random_sticker()  # Get a random sticker
        response = f"😂 I laughed for {seconds} seconds! {roast}"

    return render_template("index.html", response=response, seconds=seconds, roast=roast, scores=joke_scores, sticker_url=sticker_url)

@app.route("/generate_joke", methods=["POST"])
def generate_joke():
    user_input = request.form["user_input"]
    temperature = float(request.form["temperature"])
    max_output_tokens = int(request.form["max_output_tokens"])

    # Generate a joke using the AI model
    response = model.generate(
        prompt=f"Tell a joke about {user_input}",
        temperature=temperature,
        max_output_tokens=max_output_tokens
    )

    joke = response.generations[0].text.strip()

    # For demo: score the joke (higher is funnier)
    score = random.randint(1, 10)
    joke_scores.append(score)

    return render_template("index.html", joke=joke, score=score)

@app.route("/roast", methods=["POST"])
def roast():
    user_input = request.form["user_input"]
    temperature = float(request.form["temperature"])
    max_output_tokens = int(request.form["max_output_tokens"])

    # Generate a roast using the AI model
    response = model.generate(
        prompt=f"Roast me for {user_input}",
        temperature=temperature,
        max_output_tokens=max_output_tokens
    )

    roast = response.generations[0].text.strip()

    return render_template("index.html", roast=roast)

@app.route("/fun_roast", methods=["POST"])
def fun_roast():
    roast = roast_user()
    return render_template("index.html", roast=roast)

@app.route("/chali_matcher", methods=["GET", "POST"])
def chali_matcher():
    vibe_match = None
    if request.method == "POST":
        joke1 = request.form.get("joke1", "")
        joke2 = request.form.get("joke2", "")
        # Simulate vibe matching logic
        vibe_match = random.randint(0, 100)
    return render_template("chali_matcher.html", vibe_match=vibe_match)

@app.route("/dad_jokes_course")
def dad_jokes_course():
    return render_template("dad_jokes_course.html")

@app.route("/bachelors_in_chali")
def bachelors_in_chali():
    return render_template("bachelors_in_chali.html")

if __name__ == "__main__":
    app.run(debug=True)