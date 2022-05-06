from psychopy import visual, monitors
from psychopy.visual import Window
from psychopy import core, event
import csv
import numpy as np
import pandas as pd
from PIL import Image
import random
#fillColor and image file name will become variables


win = visual.Window([600,400], color='white', fullscr=0)

#2: make dataframe of languages/images
df = pd.DataFrame(columns=['trialnumber','imagefile','English','Spanish'])
df = df.append({'trialnumber':1, 'imagefile':'dog.jpeg','English':['dog'],'Spanish':['perro']},ignore_index=True)
df = df.append({'trialnumber':2, 'imagefile':'chair.jpeg','English':['chair'],'Spanish':['silla']},ignore_index=True)
df = df.append({'trialnumber':3, 'imagefile':'stairs.jpeg','English':['stairs'],'Spanish':['escaleras']},ignore_index=True)
df = df.append({'trialnumber':4, 'imagefile':'ccar.png','English':['car'],'Spanish':["carro", "automovil", "coche"]},ignore_index=True)
df = df.append({'trialnumber':5, 'imagefile':'tree.webp','English':['tree'],'Spanish':['arbol']},ignore_index=True)

#sample, give it a fraction of one to shuffle a data frame and run through each trial, you should shuffle rows


#making dictionary of languages/background
language_to_color_dict = {}git
language_to_color_dict['English'] = 'blue'
language_to_color_dict['Spanish'] = 'red'
#make variables based on this dictionary:
languages_list = list(language_to_color_dict.keys())
color_list = list(language_to_color_dict.values())

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
	event.waitKeys(maxWait=3, keyList=['1', '2'], clearEvents=True)

	instruction = visual.TextStim(win, color="black", pos=(0,-.8))
	quitKeys = ['escape', 'esc']
	ansKeys = ['return']
	keyboardKeys = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','space']
	answer = ''
	complete_answer = False
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


	print(answer)
	correct_or_not = answer in this_trial_answer
	if correct_or_not == True:
		message = 'correct!'
	else:
		message = 'incorrect'
	result_text = visual.TextStim(win, text=message , color="black", pos=(0,0), height=0.3)
	result_text.draw()
	win.flip()
	event.waitKeys(maxWait=3, keyList=['space'], clearEvents=True)
