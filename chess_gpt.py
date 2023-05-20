import openai
from pprint import pprint
from chess_game import get_most_recent_game
import os



def gpt_response(username):

    pgn = get_most_recent_game(username)

    prompt = (f"Please analyze the following chess game:\n\n"
            f"{pgn}\n\n"
            f"Based on the game, make some suggestions to {username} in order to improve their game.")



    # prompt = "Analyze this game and focus on the username player mistakes and suggestions to practice and improve its game"

    model = "gpt-3.5-turbo"

    response = openai.ChatCompletion.create(
            model = model,
            # prompt = prompt,
            messages = [{"role":"user", "content": prompt}],
            temperature=0.5,
            max_tokens = 300,
        )

    reply = response.choices[0]["message"]["content"]
    # print(reply)
    return reply
