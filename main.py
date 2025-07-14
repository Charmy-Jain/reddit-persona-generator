import praw
import os
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    user_agent=os.getenv("USER_AGENT")
)

def fetch_user_data(username):
    user = reddit.redditor(username)
    posts = []
    comments = []

    print(f"Fetching posts and comments for u/{username}...")

    for submission in user.submissions.new(limit=None):
        posts.append(f"Title: {submission.title}\nText: {submission.selftext}\n")

    for comment in user.comments.new(limit=None):
        comments.append(f"Comment: {comment.body}\n")

    return posts, comments



import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_persona(posts, comments):
    combined_text = "\n".join(posts + comments)
    prompt = (
        "You're an AI tasked with creating a detailed user persona. "
        "Based on the following Reddit activity, summarize the user's personality traits, interests, profession, values, tone, etc. "
        "For each trait, include a quote or summary from a post/comment that supports it:\n\n"
        f"{combined_text}"
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error generating persona: {e}"

def save_persona(username, persona_text):
    filename = f"output/{username}_persona.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(persona_text)
    print(f"Persona saved to {filename}")



if __name__ == "__main__":
    reddit_url = input("Enter Reddit profile URL: ")
    username = reddit_url.rstrip("/").split("/")[-1]
    
    posts, comments = fetch_user_data(username)
    persona = generate_persona(posts, comments)
    save_persona(username, persona)
