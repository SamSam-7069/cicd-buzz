import os
from flask import Flask
from buzz import rock_paper_scissors


app = Flask(__name__)

@app.route("/")
def generate_buzz():
    speler_1, speler_2, winnaar =  rock_paper_scissors.rock_paper_scissors()
    page = '<html><body><h1>'
    page += "The ultimate rock paper scissor generator, where you can do absolutely nothing</br>"
    page += "By Sam and Daan"
    page += '</h1></body></html>'
    page += '<img src="' + get_image(speler_1) + '"></img style="padding 40px">'
    page += '<img src="' + get_image(speler_2) + '"></img style="padding 40px">'
    page += "</br>"
    page += "</br>"
    page += '<html><body><h1>'
    page += "Match recap </br>"
    page += secret_gif(winnaar)
    page += winnaar + "</br>"
    page += '</h1></body></html>'
    return page




def get_image(input):
    if input == "rock":
        return "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Rock-paper-scissors_%28rock%29.png/100px-Rock-paper-scissors_%28rock%29.png" ##rock
    if input == "paper":
        return "https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Rock-paper-scissors_%28paper%29.png/100px-Rock-paper-scissors_%28paper%29.png" #paper
    if input == "scissors":
        return "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Rock-paper-scissors_%28scissors%29.png/100px-Rock-paper-scissors_%28scissors%29.png" #scissors

def secret_gif(input):
    if input == "Paper covers rock! You win!":
        return '<img src="' + "https://media4.giphy.com/media/3osxY6hXXl95Zt2jII/giphy.gif?cid=ecf05e47gfdfmcl0ubir48aa5f78pkxl2thfs43nw1z6gmao&rid=giphy.gif&ct=g" + '"></img style="padding 40px"> </br>'
    return "unfortunately there was no match replay </br>"



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))