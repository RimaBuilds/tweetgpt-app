import os
from dotenv import load_dotenv
import revChatGPT
from revChatGPT.V3 import Chatbot

load_dotenv()

api_key = os.environ.get("CHATGPT_API_KEY")
chatbot = Chatbot(api_key)

class Chatter:
    def __init__(self):
        """Chatter is a wrapper of the Reverse Engineered ChatGPT"""
        self.chatbot = Chatbot(api_key)
        return None

    def get_response(self, prompt):
        """Basic ChatGPT query. Give a prompt, get a response.

        Parameters
        ----------
        prompt : str
            the instructions/dialogue provided to ChatGPT
        """
        response = ""
        for data in self.chatbot.ask(prompt):
            response += data
        return response.strip()


    def parse_tweet_job(self, job):
        """Creates a prompt from a tweet job dict

        Parameters
        ----------
        job : dict
            expects a tweet job dict with the following keys:
            {
                "topic": topic,
                "message": message,
                "tone": tone,
                "act_like": act_like,
            }
        """
        prompt = f"Write a tweet in the style of {job['act_like']} about {job['topic']} with a {job['tone']} tone. Message: {job['message']}."
        return prompt

    def tweets_from_job(self, job, num_options=2):
        """Given a tweet job dict, generates tweet options.

        Parameters
        ----------
        job : dict
            expects a tweet job dict with the following keys:
            {
                "topic": topic,
                "message": message,
                "tone": tone,
                "act_like": act_like,
            }
        num_options : int, optional
            the number of tweet options to generate, by default 2
        """
        prompts = [
        f"Write a short tweet in the style of {job['act_like']} about {job['topic']} with a {job['tone']} tone. Message: {job['message']}.",
        f"Write a thread of 1-4 tweets in the style of {job['act_like']} about {job['topic']} with a {job['tone']} tone. Message: {job['message']}.",
    ]
        options = []
        for prompt in prompts:
            tweet = self.get_response(prompt)
            options.append(tweet)
        return options

