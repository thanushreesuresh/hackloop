import google.generativeai as genai

# ✅ Your Gemini API key
genai.configure(api_key="AIzaSyAbA6G9h6gnWz73QiZYcS5EMZu5L5xZ4pk")

# 💬 Create the Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# 🎤 Ask user for a joke
user_joke = input("Tell me a joke 😁: ")

# 🤖 Prompt Gemini to respond with laugh time + roast
prompt = f"""
Here's a user's joke: "{user_joke}"

Rate how funny the joke is on a scale of 1-10, tell me how many seconds you laughed, and roast the user  in malayalam if the joke was lame.
Keep it short and funny.
"""

# 🧠 Get response from Gemini
response = model.generate_content(prompt)

# 📤 Print the funny result
print("\n🤖 Sir Laughs-a-Lot says:")
print(response.text)