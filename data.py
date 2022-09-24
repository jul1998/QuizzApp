import requests
from configure_game import ConfigureGame

conf = ConfigureGame()


parameters = {
    "amount": conf.amount,
    "type": conf.type,
    "difficulty": conf.difficulty
}

data = requests.get("https://opentdb.com/api.php?amount=10&difficulty=easy&type=boolean", params=parameters)

questions_data = data.json()["results"]
print(questions_data)
print(parameters["amount"])