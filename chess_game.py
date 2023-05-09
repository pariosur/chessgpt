from chessdotcom import get_leaderboards, get_player_stats, get_player_game_archives
import pprint
import requests

printer = pprint.PrettyPrinter()

def print_leaderboards():
    data = get_leaderboards().json
    categories = data.keys()
    print(categories)
    for category in categories:
        print("Category:", category)
        for idx, entry in enumerate(data[category]):
            print(f'Rank: {idx + 1} | Username: {entry["username"]} | Rating: {entry["score"]}')

def get_player_rating(username):
    data = get_player_stats(username).json['stats']
    print(data)
    categories = ['chess_blitz', 'chess_rapid', 'chess_bullet']

    for category in categories:
        print('Category:', category)
        print(f'Current: {data[category]["last"]["rating"]}')

    printer.pprint(data)

# get_player_rating("proctor89")


def get_most_recent_game(username):
    data = get_player_game_archives(username).json
    url = data['archives'][-1]
    games = requests.get(url).json()
    game = games['games'][-2]

    game_pgn = game['pgn']
    # pgn_str = ""
    # for game in game1:
    #     pgn_str += game['pgn']

    # printer.pprint(game_pgn)

    return game_pgn

get_most_recent_game("proctor89")
