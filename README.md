<img width="3188" height="1202" alt="frame (3)" src="https://github.com/user-attachments/assets/517ad8e9-ad22-457d-9538-a9e62d137cd7" />


# Chali Meter 🎯


## Basic Details
### Team Name: Hackloop


### Team Members
- Team Lead: Thanushree Suresh - Sahrdaya College of Engineering and Technology
- Member 2: Rosna P R - Sahrdaya College of Engineering and Technology

### Project Description
Our website lets users enter their lamest Malayalam jokes and tells them how many seconds it made us laugh a fun way to measure their chali (lame) factor. It also shows an improvement graph to track your joke progress, recommends courses to level up your joke game, and features a Shelley-wise matcher where two users input their jokes to get a percentage score of their vibe matching!vv

### The Problem (that doesn't exist)
Nobody has a proper way to measure how lame their jokes are, track if they’re improving, or see how well their cringe humor vibes with others. The world is missing a chali compatibility and growth tracker!

### The Solution (that nobody asked for)
The “Chali Meter” app uses AI and random numbers to rate your joke, roast you (gently, or not), and then flashes a sticker to soften the blow. Every joke gets a random score and simulated laugh time—no one asked for this much fun, but we're serving it anyway!

## Technical Details
### Technologies/Components Used
For Software:
Here are the main technologies used in the Chali Meter project:

1. **Python** – The primary programming language for backend logic.
2. **Flask** – Web framework powering the backend and routing for the web app.
3. **Google Gemini AI (gemini-1.5-flash)** – For generating roasts, joke ratings, and fun AI responses.
4. **HTML/CSS** – For structuring and styling the web pages (including forms and stickers).
5. **JavaScript (optional)** – Can be used for enhancing UI interactions, though not shown in the provided code.
6. **Random & OS Modules (Python)** – Used for randomness (scores, laugh times, vibe match) and managing file paths for stickers.
7. **Templates** – Flask’s Jinja2 templates (HTML files) for rendering dynamic content.

**Summary**: Flask (Python), Gemini AI, HTML/CSS (styling), random logic, and static assets (stickers) together make Chali Meter work!

***

## **Implementation (Short Version)**

**Install:**
```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install Flask google-generativeai
```
- Add your Gemini API key in `app.py`.
- Create `templates/` for HTML files and `static/stickers/` for images.

**Run:**
```bash
python app.py
```

***

## **Project Documentation (Short Version)**

**Chali Meter** is a fun Flask app that:
- Lets users submit jokes.
- Uses Gemini AI + randomness to rate them, roast them, and show a sticker.
- Has a “Chali Matcher” to compare two jokes.
- Includes extra joke “course” pages just for laughs.

**Tech:** Python, Flask, Gemini AI, HTML/CSS, Random + OS modules, Jinja2 templates.  
**Files:**  
- `app.py` → Backend logic & routes.  
- `sir_laughs_a_lot.py` → CLI roast tool.  
- `templates/` → HTML pages.  
- `static/stickers/` → Fun images.

***

# Screenshots (Add at least 3)
https://drive.google.com/drive/folders/1I8GKsI4B6PHpXf7jgJcnNvroMTByFvB4?usp=drive_link

### Project Demo
# Video
https://drive.google.com/drive/folders/1I8GKsI4B6PHpXf7jgJcnNvroMTByFvB4?usp=drive_link

## Team Contributions
- Thanushree Suresh: Developed the Flask backend, integrated Gemini AI, and implemented random scoring and routing logic.
- Rosna P R:  Designed and styled the frontend, managed templates and stickers, and crafted humorous UI content.
---
Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProjects--25-25?link=https%3A%2F%2Fwww.tinkerhub.org%2Fevents%2FQ2Q1TQKX6Q%2FUseless%2520Projects)



