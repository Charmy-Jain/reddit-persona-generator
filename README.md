# Reddit Persona Generator 🧠

This project scrapes a Reddit user's public posts and comments, then generates a detailed user persona using OpenAI's GPT-4. The persona includes traits like interests, tone, values, profession hints, and cites Reddit posts/comments to justify each trait.

---

## 🚀 Features

- Scrapes a Reddit user's posts and comments
- Generates a qualitative persona using GPT-4
- Cites Reddit content for each trait
- Saves persona as a `.txt` file in the `output/` directory

---

## 🛠️ Technologies Used

- Python 3
- PRAW (Python Reddit API Wrapper)
- OpenAI GPT-4 API
- `dotenv` for environment variable handling

---

## 📦 Installation

1. **Clone this repo**
   ```bash
   git clone https://github.com/your-username/reddit-persona-generator.git
   cd reddit-persona-generator

2. **Create and activate a virtual environment**
    python -m venv venv
    
3. **Install Dependencies**
    pip install -r requirements.txt

4. **Create a .env File in the Root Folder**
    CLIENT_ID=your_reddit_client_id
    CLIENT_SECRET=your_reddit_client_secret
    USER_AGENT=script by u/your_reddit_username
    OPENAI_API_KEY=your_openai_api_key


