mysp = __import__('my-voice-analysis')
p="converted"
c=r"C:\Users\ishan\OneDrive\Documents\EngHack"

import wave

params = ()




rating = mysp.myspgend(p,c)

pauses = mysp.mysppaus(p,c)
speed = mysp.myspsr(p,c)
articulation = mysp.myspatc(p,c)

pronounce = mysp.mysppron(p,c)



pauses_response = []
speed_response = []
articulation_response = []

speed_dict = {
'0': [0,'Too Slow'],
 '1': [25, 'Slow'],
 '2': [50, 'Slow'],
 '3': [75, 'Good Speed, could be a bit faster'],
 '4': [100, 'Perfect Speed'],
 '5': [75, 'Good speed, could be a little slower'],
 '6': [50, 'Fast'],
 '7': [25, 'Fast'],
 '8': [0, 'Too fast']}


articulation_dict = {
'0': [0,'Too Slow'],
 '1': [0, 'Too Slow'],
 '2': [25, 'Slow'],
 '3': [50, 'Slow'],
 '4': [75, 'Good Articluation, could be a bit faster'],
 '5': [100, 'Perfect Articluation'],
 '6': [75, 'Good Articulation, could be a little slower'],
 '7': [50, 'Fast'],
 '8': [25, 'Fast'],
 '9': [0, 'Too fast']}


if pauses > 100:
    pauses_response = [0, 'Too many pauses']
elif pauses > 80:
    pauses_response = [25, 'Too many pauses']
elif pauses > 60:
    pauses_response = [50, 'Just a few too many pauses']

elif pauses > 40:
    pauses_response = [75, 'Good, try to reduce the amount of pauses']

else:
    pauses_response = [100, 'Very few pauses, well done!']

try:
    speed_response = speed_dict[str(speed)]
except KeyError:
    speed_response = [0, 'Too fast']

try:
    articulation_response = articulation_dict[str(articulation)]
except KeyError:
    articluation_response = [0, 'Too fast']


percentages = [pauses_response[0], speed_response[0], articulation_response[0], pronounce]

mean_percent = sum(percentages)/len(percentages)

feedback_statement = 'Feedback for Speed: ' + speed_response[1] + ' Feedback for Articulation: ' + articulation_response[1] + ', Feedback for Pausing: ' + pauses_response[1] + ', Pronounce Rating (out of 100): ' + str(pronounce)

print('\n'*5)
print(mean_percent, feedback_statement)
print('\n'*5)


