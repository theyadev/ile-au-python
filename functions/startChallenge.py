def startChallenge(challenge_name):
    module = __import__(challenge_name)
    module.startGame()