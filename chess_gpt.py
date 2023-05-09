import openai
from api_key import API_KEY
from pprint import pprint
from chess_game import get_most_recent_game

openai.api_key = API_KEY


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
            max_tokens = 750,
        )

    reply = response.choices[0]["message"]["content"]
    # print(reply)
    return reply

# gpt_response('proctor89')

    #reply = response.choices[0].text.mstrip()

    # print(response)

    # print(response.choices[0].text)

    # def format_response(response):
    #     # Split the response into individual mistakes
    #     mistakes = response.split('\n')

    #     # Create an unordered list of mistakes
    #     response_html = '<ul>'
    #     for mistake in mistakes:
    #         if mistake.strip() != '':
    #             response_html += f'<li>{mistake.strip()}</li>'
    #     response_html += '</ul>'

    #     return response_html

    # response_formatted = format_response(reply)
