# Create a random question quiz game.
# The game is between two teams.
# Each team has a name and a score.
#Each team is asked a question.
# If the answer is correct, the team's score is increased by 1.
# If the answer is incorrect, the team's score is not increased.
# Team takes turns to answer the question.
# The game is over when one team's score is equal to 5.
# The winner is the team with the highest score.

#greet each team
#ask each team a question
#check the answer
#if correct, increase score by 1
#if incorrect, do not increase score
#switch to next team
#Show current score for each team after each question
#repeat until one team's score is equal to 5
#display the winner


import random


class Team:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def __str__(self):
        return self.name + " " + str(self.score)

    def ask_question(self, question):
        print(self.name + ": " + question.text)
        answer = input("Your answer: ")
        if answer == question.answer:
            print("Correct!")
            self.score += 1
            print(self.name + ": " + str(self.score))

        else:
            print("Incorrect!")
            print(self.name + ": " + str(self.score))


class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


class Game:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2

    def play(self):
        #while one team's score is not equal to 5
        while self.team1.score != 5 and self.team2.score != 5:
            #switch to next team
            if self.team1.score > self.team2.score:
                self.team1.ask_question(random.choice(questions))
                self.team2.ask_question(random.choice(questions))
            else:
                self.team2.ask_question(random.choice(questions))
                self.team1.ask_question(random.choice(questions))


questions = [
    Question("What is the capital of New York?", "Albany"),
    Question("What is the capital of California?", "Sacramento"),
    Question("What is the capital of Texas?", "Austin"),
    Question("What is the capital of Florida?", "Tallahassee"),
    Question("What is the capital of Illinois?", "Springfield"),
    Question("What is the capital of Pennsylvania?", "Harrisburg"),
    Question("What is the capital of New Jersey?", "Trenton"),
    Question("What is the capital of New Mexico?", "Santa Fe"),
    Question("What is the capital of Washington?", "Olympia"),
    Question("What is the capital of Oregon?", "Salem"),
    Question("What is the capital of Utah?", "Salt Lake City"),
    Question("What is the capital of Colorado?", "Denver"),
    Question("What is the capital of Kansas?", "Topeka"),
    Question("What is the capital of Nebraska?", "Lincoln"),
    Question("What is the capital of Oklahoma?", "Oklahoma City"),
    Question("What is the capital of New Hampshire?", "Concord"),
    Question("What is the capital of Massachusetts?", "Boston"),
    Question("What is the capital of Rhode Island?", "Providence"),
    Question("What is the capital of Vermont?", "Montpelier"),
    Question("What is 100 + 100?", "200"),
    Question("What is the square root of 64?", "8"),
    Question("What is the square root of 256?", "16"),
    Question("What is the square root of 1024?", "32"),
    Question("Who is the author of the book 'The Hobbit'?", "J.R.R. Tolkien"),
    Question("Who is the author of the book 'The Lord of the Rings'?", "J.R.R. Tolkien"),
    Question("Who is the author of the book 'The Little Prince'?", "Antoine de Saint-Exupery"),
    Question("Who is the author of the book 'The Catcher in the Rye'?", "J.D. Salinger"),

]

# Create a function to greet each team.
def greet_teams(team1, team2):
    print("Welcome to the quiz game!")
    print("We have two teams:")
    print(team1)
    print(team2)
    print("Let's start the game!")


greet_teams(Team("Team 1"), Team("Team 2"))
team1 = Team("Team 1")
team2 = Team("Team 2")
game = Game(team1, team2)
game.play()
print(team1)
print(team2)







