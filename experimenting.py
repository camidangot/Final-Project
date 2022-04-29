from psychopy import visual, monitors
from psychopy.visual import Window
from psychopy import core, event
import csv
import numpy as np
import pandas as pd

win = visual.Window([600,400], color='black', fullscr=0)

#trying to create a textbox - need to fix
#textbox=visual.TextBox(window=win,text='hello')
#textbox.draw()
#win.flip()
#event.waitKeys(maxWait=3, keyList=['1', '2'], clearEvents=True)
#win.flip()


#try to figure out how to change background color
visual.Window(color='blue') #possibly blue
event.waitKeys(maxWait=3, keyList=['1', '2'], clearEvents=True)
print(1/0)

# basic text
ready_text = visual.TextStim(win, text='hello world!')
# drawing draws "behind the screen"
ready_text.draw()
# flipping the window is how to show things - you can get whatever ready you want in the background in the mean time
win.flip()
event.waitKeys(maxWait=3, keyList=['1', '2'], clearEvents=True)
win.flip()
# I like using print(1/0) as a catch all exception that kills my python scripts while I'm testing them
# strictly speaking this is bad coding practice and you should throw an exception


# move to the middle and change color
ready_text = visual.TextStim(win, text='hello world!', pos=(300, 0), color='red', units='pix')
ready_text.draw()
win.flip()
event.waitKeys(maxWait=3, keyList=['1', '2'], clearEvents=True)
win.flip()



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

#print(1/0)


# we made those response lists, but we didn't do anything to save them
# lets write them to a dataframe and save that as a csv
df = pd.DataFrame({'responses': responses, 'rts': rts})
df.to_csv('data.csv')








# finish
win.close()














# eof
