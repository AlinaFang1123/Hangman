from cmu_cs3_utils import loadData
from cmu_graphics import *
import random

# have a wrong list to keep track of the used characters

# use list
def onAppStart(app):
    app.wrongCount = 0
    app.faces = []
    app.rightCount = 0
    app.endGame = False
    app.word = randomWord()
    app.characters = list(app.word)
    app.rightGuessed = ['', '', '', '', '', '']
    app.lose = False
    app.win = False
    app.showHint = False
    app.fill = ['lightpink', 'skyblue', 'lightGreen', 'gold',
                'darkorange', 'tomato', 'firebrick']

def redrawAll(app):
    # draw background
    fill = app.fill[app.wrongCount]
    drawRect(0, 0, 400, 50, fill=fill, opacity=30)
    drawRect(0, 320, 400, 400, fill=fill, opacity=30)
    # draw title
    drawLabel('HANGMAN', 85, 23, size=27, bold=True)
    # draw hint
    if app.showHint:
        drawLabel(f'{app.word}', 200, 307, size=10,
                    fill='gray')
    else:
        drawLabel('(Long press SPACE for hint)', 200, 307, 
                    size=10, fill='gray')
    # draw lines
    for i in range (6):
        drawLine(45+i*55, 370, 80+i*55, 370, lineWidth=3)
    # draw guessed characters
    for c in range (len(app.rightGuessed)):
        character = app.rightGuessed[c]
        drawLabel(character.upper(), 62+c*55, 350, size=27, 
                  bold=True, align='center')
    # draw hangman face + changeface
    drawRack(app)
    changeFace(app)
    drawMan(app)
    drawHeart(app)
    # end game for lose
    if app.endGame:
        if app.lose:
            drawRect(0, 50, 400, 270, fill='red', opacity=80)
            drawLabel('BOOOOO', 200, 118, 
                      size=40, fill='white', bold=True)
            drawLabel('YOU KILLED THE HANGMAN', 200, 170, 
                      size=25, fill='white', bold=True)
            drawLabel(f'The answer was "{app.word}"', 200, 210, 
                      size=20, fill='white', bold=True)
            drawLabel('Press "enter" to restart', 200, 240, 
                      size=20, fill='white', bold=True)
        else:
            drawRect(0, 50, 400, 270, fill='mediumslateblue', opacity=80)
            drawLabel('YOU SAVED THE HANGMAN', 200, 170, 
                      size=25, fill='white', bold=True)
            drawLabel('CONGRATS', 200, 118, 
                      size=40, fill='white', bold=True)
            drawLabel('Press "enter" to restart', 200, 240, 
                      size=20, fill='white', bold=True)
            drawCircle(55, 113, 8, fill='crimson')
            drawCircle(70, 113, 8, fill='crimson')
            drawPolygon(47, 115, 78, 115, 62.5, 132, fill='crimson')
            drawCircle(330, 113, 8, fill='crimson')
            drawCircle(345, 113, 8, fill='crimson')
            drawPolygon(322, 115, 353, 115, 338, 132, fill='crimson') 
            
    # end game for win
        
def drawRack(app):
    # draw the rack
    # app.wrongCount: 1 - 6
    if app.wrongCount >= 1:
        drawRect(110, 80, 8, 200)
    if app.wrongCount >= 2:
        drawRect(95, 80, 210, 8)
    if app.wrongCount >= 3:
        drawRect(95, 280, 40, 8)
    if app.wrongCount >= 4:
        drawRect(105, 100, 60, 8, rotateAngle=135)
    if app.wrongCount >= 5:
        drawRect(265, 80, 8, 35)
    # if app.wrongCount >= 6:
    #     drawOval(150, 50, 150, 100, fill=None, border='black', borderWidth=3)
    
def changeFace(app):
    drawArc(270, 145, 20, 10, 100, 205)
    fill = app.fill[app.wrongCount]
    drawOval(270, 140, 55, 55, fill=fill, 
                 border='black', borderWidth=8)
    if app.wrongCount == 0:
        drawOval(261, 135, 8, 8)
        drawOval(279, 135, 8, 8)
        drawLabel('D', 270, 149, size=20, bold=True, rotateAngle=90)
    if app.wrongCount == 1:
        drawOval(261, 135, 8, 8)
        drawOval(279, 135, 8, 8)
        drawArc(270, 145, 20, 10, 80, 200)
    if app.wrongCount == 2:
        drawOval(261, 135, 8, 8)
        drawOval(279, 135, 8, 8)
        drawLine(260, 147, 280, 147, lineWidth=4)
    if app.wrongCount == 3:
        drawOval(261, 135, 8, 8)
        drawOval(279, 135, 8, 8)
        drawOval(270, 148, 12, 12, fill=None,
                 border='black', borderWidth=4)
    if app.wrongCount == 4:
        drawLabel('X', 261, 135, size=15, bold=True)
        drawLabel('X', 279, 135, size=15, bold=True)
        drawOval(270, 148, 12, 12, fill=None,
                 border='black', borderWidth=4)
    if app.wrongCount == 5:
        drawLabel('X', 261, 135, size=15, bold=True)
        drawLabel('X', 279, 135, size=15, bold=True)
        drawLine(260, 148, 280, 148, lineWidth=3)
    if app.wrongCount == 6:
        drawLabel('X', 261, 137, size=15, bold=True)
        drawLabel('X', 279, 137, size=15, bold=True)
        drawLabel('P', 270, 150, size=20, bold=True, rotateAngle=90)

def drawMan(app):
    # draw the man
    drawOval(270, 140, 55, 55, fill=None, border='black', borderWidth=8)
    drawRect(265, 160, 8, 70)
    # draw arm
    drawRect(263, 190, 45, 8, rotateAngle=45)
    drawRect(229, 190, 45, 8, rotateAngle=135)
    # draw leg
    drawRect(263, 240, 50, 8, rotateAngle=45)
    drawRect(225, 240, 50, 8, rotateAngle=135)
    
def drawHeart(app):
    for i in range (6):
        drawCircle(200+33*i, 20, 5, fill='crimson')
        drawCircle(210+33*i, 20, 5, fill='crimson')
        drawPolygon(195+33*i, 22,
                    215+33*i, 22,
                    205+33*i, 32, fill='crimson')
    for death in range (app.wrongCount):
        drawCircle(200+33*death, 20, 5, fill='gray')
        drawCircle(210+33*death, 20, 5, fill='gray')
        drawPolygon(195+33*death, 21,
                    215+33*death, 21,
                    205+33*death, 32, fill='gray')

def onKeyPress(app, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # add a list that keeps track of pressed keys
    # if key was already pressed, do nothing
    # rn, duplicate letters, if pressed twice, will return as error
    if key in alphabet and not app.endGame and key not in app.rightGuessed:
        if key not in app.characters:
            app.wrongCount += 1
        else:
            while key in app.characters:
                characterIndex = app.characters.index(key) # this does...
                app.rightGuessed[characterIndex] = key
                app.characters[characterIndex] = '#'


    # End game if wrong guesses = 6
    
    if '' not in app.rightGuessed:
        app.endGame = True
        app.win = True
    if app.wrongCount > 5:
        app.endGame = True
        app.lose = True

    # set up reset 
    if app.endGame:
        # make it so that no more keys can be pressed !!!!
        if key == 'enter':
            app.wrongCount = 0
            app.rightCount = 0
            app.endGame = False
            app.word = randomWord()
            app.characters = list(app.word)
            app.characterIndex = 0
            app.rightGuessed = ['', '', '', '', '', '']

def onKeyHold(app, keys):
    if 'space' in keys:
        app.showHint = True

def onKeyRelease(app, keys):
    app.showHint = False

def randomWord():
    allWords = loadData('common_words', count=1, wordLength=6)
    randomWord = random.choice(allWords)
    return randomWord

# Be clever, be creative, have fun!

def main():
    runApp()

main()
