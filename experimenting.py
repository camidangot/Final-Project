from psychopy import visual, monitors
from psychopy.visual import Window
from psychopy import core, event
import csv
import numpy as np
import pandas as pd

win = visual.Window([600,400], color='black', fullscr=0)


# basic text
ready_text = visual.TextStim(win, text='Hey players! Welcome to Language Master950! Click the space bar for instructions on how to play!')
# drawing draws "behind the screen"
ready_text.draw()
# flipping the window is how to show things - you can get whatever ready you want in the background in the mean time
win.flip()
event.waitKeys(maxWait=3, keyList=['space'], clearEvents=True)
win.flip()
# I like using print(1/0) as a catch all exception that kills my python scripts while I'm testing them
# strictly speaking this is bad coding practice and you should throw an exception


# move to the middle and change color
ready_text = visual.TextStim(win, text='To begin, please select any languages you speak by clicking on the corresponding boxes. Press the space bar for options!', units='pix')
ready_text.draw()
win.flip()
event.waitKeys(maxWait=3, keyList=['space'], clearEvents=True)
win.flip()


mymouse = event.Mouse(visible=True, win=win)


label1 = visual.TextStim(win,pos=(-.5,0),text='english',color='black')
mybutton1 = visual.Rect(win,pos=(-.5,0),fillColor='blue',width=.5,height=.2)
label2 = visual.TextStim(win,pos=(.5,0),text='spanish',color='black')
mybutton2 = visual.Rect(win,pos=(.5,0),fillColor='red',width=.5,height=.2)
label3 = visual.TextStim(win,pos=(0,0),text='done',color='black')
mybutton3 = visual.Rect(win,pos=(0,0),fillColor='white',width=.5,height=.2)

# notice -- draw the buttons and then their labels, so the labels are on top!
mybutton1.draw()
label1.draw()
mybutton2.draw()
label2.draw()
mybutton3.draw()
label3.draw()
win.flip()


notdone = True
languages = []
while notdone:
    if mymouse.isPressedIn(mybutton1):
        languages.append('english')
    if mymouse.isPressedIn(mybutton1):
        languages.append('spanish')
    if mymouse.isPressedIn(mybutton3):
        notdone = False

languages = list(set(languages)) # will remove the extras

lang_text = visual.TextStim(win, text='thanks, you picked '+' '.join(languages))
end_text = visual.TextStim(win, text='press space to finish.', pos=(0,-.5))
lang_text.draw()
end_text.draw()
win.flip()
event.waitKeys(maxWait=3, keyList=['space'], clearEvents=True,)
win.flip()



# instruction = visual.TextStim(win,color="white")
# quitKeys = ['escape', 'esc']
# ansKeys = ['return']
# keyboardKeys = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','space']
# answer = ''
# complete_answer = False
# while not complete_answer:
#     instruction.setText(u'answer : {0}'.format(answer))
#     instruction.draw()
#     win.flip()
#     for letter in (keyboardKeys):
#         if event.getKeys([letter]):
#             answer += letter
#     if event.getKeys(['backspace']):
#         answer = answer[:-1]
#     if event.getKeys([quitKeys[0]]):
#         core.quit()
#     if event.getKeys([ansKeys[0]]):
#         complete_answer = True
#


core.quit()




#Next piece of instructions:
ready_text = visual.TextStim(win, text='Amazing! Now let me tell you how the game works. You will see an image appear on your screen with a specific backgroup color. Each color corresponds to a language. Once you see the image, type in the word in the language corresponding to the background. Press the space bar for the key!')
# drawing draws "behind the screen"
ready_text.draw()
# flipping the window is how to show things - you can get whatever ready you want in the background in the mean time
win.flip()
event.waitKeys(maxWait=30, keyList=['space'], clearEvents=True)
win.flip()

#if the person choses english and spanish show this text as the key (figure out how to do some sort of if statement for this according to buttons pressed)
ready_text = visual.TextStim(win, text='This will be your key for the game: red = English , blue = Spanish')
# drawing draws "behind the screen"
ready_text.draw()
# flipping the window is how to show things - you can get whatever ready you want in the background in the mean time
win.flip()
event.waitKeys(maxWait=30, keyList=['space'], clearEvents=True)
win.flip()


print(1/0)


#Making a textbox
instruction = visual.TextStim(win,color="white")
quitKeys = ['escape', 'esc']
ansKeys = ['return']
keyboardKeys = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','space']
answer = ''
complete_answer = False
while not complete_answer:
    instruction.setText(u'answer : {0}'.format(answer))
    instruction.draw()
    win.flip()
    for letter in (keyboardKeys):
        if event.getKeys([letter]):
            answer += letter
    if event.getKeys(['backspace']):
        answer = answer[:-1]
    if event.getKeys([quitKeys[0]]):
        core.quit()
    if event.getKeys([ansKeys[0]]):
        complete_answer = True

#print(1/0)

#try to figure out how to change background color
visual.Window(color='blue') #possibly blue
event.waitKeys(maxWait=3, keyList=['1', '2'], clearEvents=True)

#red
visual.Window(color='red')
event.waitKeys(maxWait=3, keyList=['1', '2'], clearEvents=True)

# same for an image or two
dog1 = visual.ImageStim(win=win, image='dog_cat/im0.jpeg', units="pix", pos=(-200,0))
dog2 = visual.ImageStim(win=win, image='dog_cat/im2.jpeg', units="pix", pos=(200,0))
dog1.draw()
dog2.draw()
win.flip()
event.waitKeys(maxWait=3, keyList=['1', '2'], clearEvents=True)



# lets make a trial
# show an image, get a response, 3 times
# i want to build in saving for error trials
responses = []
rts = []
for t in range(3): # python counts from 0!
	im = 'dog_cat/im' + str(t) + '.jpeg'
	dog = visual.ImageStim(win=win, image=im, units="pix", pos=(0,0))
	dog.draw()
	win.flip()
	# this line will wait for you to press one of the keys in keyList, and if nothing happens by
	# maxWait, it will not return anything and move on. try printing tup after this to see what's inside!
	tup = event.waitKeys(maxWait=3, keyList=['1', '2'], clearEvents=True)
	if tup:
		responses.append(tup[0][0])
		rts.append(tup[0][1])
	else:
		responses.append('NA')
		rts.append(np.nan)
	win.flip()



# we made those response lists, but we didn't do anything to save them
# lets write them to a dataframe and save that as a csv
df = pd.DataFrame({'responses': responses, 'rts': rts})
df.to_csv('data.csv')








# finish
win.close()














# eof
