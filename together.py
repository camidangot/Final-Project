from psychopy import visual, monitors
from psychopy.visual import Window
from psychopy import core, event
import csv
import numpy as np
import pandas as pd
from PIL import Image
import random

win = visual.Window([600,400], color='white', fullscr=0)


# first piece of instructions - welcoming player to game
ready_text = visual.TextStim(win, text='Hey players! Welcome to Language Master950! Click the space bar for instructions on how to play!', color='black')
ready_text.draw()
win.flip()
event.waitKeys(maxWait=3, keyList=['space'], clearEvents=True)
win.flip()



# next piece of instructions
ready_text = visual.TextStim(win, text='To begin, please select any languages you speak by clicking on the corresponding boxes', color='black')
end_text = visual.TextStim(win, text='Press the space bar for options', pos=(0,-.5), color='black')
ready_text.draw()
end_text.draw()
win.flip()
event.waitKeys(maxWait=3, keyList=['space'], clearEvents=True)
win.flip()
#creating buttons so players can select languages
mymouse = event.Mouse(visible=True, win=win)


label1 = visual.TextStim(win,pos=(-.5,0),text='English',color='black')
mybutton1 = visual.Rect(win,pos=(-.5,0),fillColor='blue',width=.5,height=.2)
label2 = visual.TextStim(win,pos=(.5,0),text='Spanish',color='black')
mybutton2 = visual.Rect(win,pos=(.5,0),fillColor='red',width=.5,height=.2)
label3 = visual.TextStim(win,pos=(0,0),text='done',color='white')
mybutton3 = visual.Rect(win,pos=(0,0),fillColor='black',width=.5,height=.2)

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
		languages.append('English')
	if mymouse.isPressedIn(mybutton2):
		languages.append('Spanish')
	if mymouse.isPressedIn(mybutton3):
		notdone = False

languages = list(set(languages)) # will remove the extras

lang_text = visual.TextStim(win, text='Thanks, you picked '+' '.join(languages), color='black')
end_text = visual.TextStim(win, text='press space to continue.', pos=(0,-.5), color='black')
lang_text.draw()
end_text.draw()
win.flip()
event.waitKeys(maxWait=3, keyList=['space'], clearEvents=True,)
win.flip()



#Next piece of instructions:
ready_text = visual.TextStim(win, text='Now let me tell you how the game works. You will see an image appear on your screen with a specific background color. Each color corresponds to a language. Once you see the image, type in the word in the language corresponding to the background as fast as you can. Press the space bar for the key!', color='black')
ready_text.draw()
win.flip()
event.waitKeys(maxWait=30, keyList=['space'], clearEvents=True)
win.flip()

#making a dictionary for the key
language_to_color_dict = {}
language_to_color_dict['spanish'] = 'red'
language_to_color_dict['english'] = 'blue'


ready_text = visual.TextStim(win, text='This will be the key for the game:', color='black')
end_text = visual.TextStim(win, text= language_to_color_dict, pos=(0,-.5), color='black')
ready_text.draw()
end_text.draw()
win.flip()
event.waitKeys(maxWait=30, keyList=['space'], clearEvents=True)
win.flip()



#instructions for example
ready_text = visual.TextStim(win, text='Let me show you an example...', color='black')
end_text = visual.TextStim(win, text='(press space to continue)', pos=(0,-.5), color='black')
ready_text.draw()
end_text.draw()
win.flip()
event.waitKeys(maxWait=30, keyList=['space'], clearEvents=True)
win.flip()

#remember to change the image of hand cause this is only on my computer
ready_text = visual.TextStim(win, text='If you see an image like this on a blue background...',pos=(0,.7), color='white')
end_text = visual.TextStim(win, text='Type the word "hand" in English', pos=(0,-.7), color='white')
final_text = visual.TextStim(win, text='press space to continue', pos=(0,-.8), color='white')
bluebackground = visual.Rect(win,pos=(0,0),fillColor='blue',width=200,height=200)
image1 = visual.ImageStim(win=win, image='handpicture.png', units="pix", pos=(0,0),size=[200,200])
bluebackground.draw()
image1.draw()
ready_text.draw()
end_text.draw()
final_text.draw()
win.flip()
event.waitKeys(maxWait=5, keyList=['space'], clearEvents=True)

ready_text = visual.TextStim(win, text='If you are ready to play press the space bar!', color='black')
end_text = visual.TextStim(win, text='remember the key:', pos=(0,-.5), color='black')
final_text = visual.TextStim(win, text= language_to_color_dict, pos=(0,-.7), color='black')
ready_text.draw()
end_text.draw()
final_text.draw()
win.flip()
event.waitKeys(maxWait=30, keyList=['space'], clearEvents=True)
win.flip()

#where camilas code ends

#win = visual.Window([600,400], color='white', fullscr=0)

#2: make dataframe of languages/images
df = pd.DataFrame(columns=['trialnumber','imagefile','English','Spanish'])
df = df.append({'trialnumber':1, 'imagefile':'dog.jpeg','English':['dog'],'Spanish':['perro']},ignore_index=True)
df = df.append({'trialnumber':2, 'imagefile':'chair.jpeg','English':['chair'],'Spanish':['silla']},ignore_index=True)
df = df.append({'trialnumber':3, 'imagefile':'stairs.jpeg','English':['stairs'],'Spanish':['escaleras']},ignore_index=True)
df = df.append({'trialnumber':4, 'imagefile':'ccar.png','English':['car'],'Spanish':["carro", "automovil", "coche"]},ignore_index=True)
df = df.append({'trialnumber':5, 'imagefile':'tree.webp','English':['tree'],'Spanish':['arbol']},ignore_index=True)

#sample, give it a fraction of one to shuffle a data frame and run through each trial, you should shuffle rows


#making dictionary of languages/background
language_to_color_dict = {}
language_to_color_dict['English'] = 'blue'
language_to_color_dict['Spanish'] = 'red'
languages_list = list(language_to_color_dict.keys())
color_list = list(language_to_color_dict.values())




score = {}
for L in languages_list:
	score[L] = []

time_dict = {}
for T in languages_list:
	time_dict[T] = []


for trial in range(5):
	this_trial = random.choice(df.trialnumber)
	this_trial_language = random.choice(languages_list)
	this_trial_color = language_to_color_dict[this_trial_language]
	this_trial_picture = df.loc[df.trialnumber==this_trial]['imagefile'].values[0]
	this_trial_answer = df.loc[df.trialnumber==this_trial][this_trial_language].values[0]


	background_color = visual.Rect(win,pos=(0,0),fillColor=this_trial_color,width=1000,height=1000)
	image = visual.ImageStim(win=win, image=this_trial_picture, units="pix", pos=(0,0),size=[300,300])
	background_color.draw()
	image.draw()
	event.waitKeys(maxWait=1, keyList=['return'], clearEvents=True)

	instruction = visual.TextStim(win, color="black", pos=(0,-.8))
	quitKeys = ['escape', 'esc']
	ansKeys = ['return']
	keyboardKeys = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','space']
	answer = ''
	complete_answer = False
	timer = core.Clock()
	while not complete_answer:
		instruction.setText(u'answer : {0}'.format(answer))
		background_color.draw()
		image.draw()
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
	trial_time = timer.getTime()

	print(answer)

	correct_or_not = answer in this_trial_answer
	if correct_or_not == True:
		message = 'correct!'
	else:
		message = 'incorrect'
	result_text = visual.TextStim(win, text=message , color="black", pos=(0,0), height=0.3)
	result_text.draw()
	win.flip()
	event.waitKeys(maxWait=1, keyList=['space'], clearEvents=True)

	score[this_trial_language].append(correct_or_not)
	time_dict[this_trial_language].append(trial_time)



final_scores = {}
mean_time = {}

for lang in score.keys():
	score_list_lang = [int(x) for x in score[lang]]
	score_percent_language = np.mean(score_list_lang)
	#score_percent_language = (sum(score_list_lang))/(len(score_list_lang))
	final_scores[lang] = score_percent_language

for seconds in time_dict.keys():
	average_time = np.mean(time_dict[seconds])
	mean_time[seconds] = average_time


print(final_scores)
print(mean_time)

intro_string = "Your score is: "
for key in final_scores.keys():
	intro_string += key
	intro_string += " = "
	intro_string += str(final_scores[key])

next_string = "Your average response time is: "
for K in mean_time.keys():
	next_string += K
	next_string += " = "
	next_string += str(mean_time[K])

ready_text = visual.TextStim(win, text= intro_string, color="black", pos=(0,.5))
end_text = visual.TextStim(win, text= next_string, color="black", pos=(0,-.5))
ready_text.draw()
end_text.draw()
win.flip()
event.waitKeys(maxWait=30, keyList=['space'], clearEvents=True)
win.flip()

#intro string = "your score is"
#for key in scores.keys()
	#intro.string += key
	#intro string += "="
	#intro string += score[key] have to turn this into a string then just when doing text stim do text = intro.string
