import sys
import os
import pprint
import pandas as pd

muscle_groups = ['shoulders', 'core', 'upper back','back', 'lower back', 'hamstrings','quadriceps', 'biceps','triceps','pectorals','chest']

fullbody_a = ['horizontal_push','vertical_push_flexion','horizontal_pull','squat','core','biceps']

fullbody_b = ['vertical_push_extension','vertical_pull','horizontal_pull','hip_hinge','core', 'shoulders']

components = {
        'horizontal_push' : ['inclined pushup','pushup','diamond pushup','ring/archer pushup'],
        'horizontal_pull': ['inverted rows [rings]','inverted rows elevate feet','inverted rows [bent knees]' ],
        'vertical_push_extension': ['bench dip','regular dip','ring dip'],
        'vertical_push_flexion':['pike press', 'elevated pike press','deep elevated pike press','wall handstand pushups'],
        'vertical_pull' : ['foot-assist pullup','eccentric pullups (slow on down)', 'pullups','L-pullups'],
        'squat': ['squat','assisted pistol','pistol squat'],
        'hip_hinge':['glut bridge', 'single-leg glut bridge','back extensions'],
        'core': ['L-sit compression','hollow bodyhold', 'hanging knee-raise', 'hanging leg-raise'],
        'shoulders':['pike press', 'side curl', 'iron cross','athleanX vid'],
        'biceps': ['body curl','ChinUps', 'CU+headbang']
        }

def generate_workout(categories, components):
	temp_dict = {}
	for category in categories:
		temp_dict[category] = pd.Series(components[category])
	df = pd.DataFrame(temp_dict)
	print(df)
	#pprint.print(temp_dict, depth = 3)

with open('/Users/richardhausman/Documents/workout/last_workout.txt','r') as f:
	workout_type = f.read()
	f.close()
	if workout_type =='A':
		workout_type ='B'
	else:
		workout_type = 'A'

if len(sys.argv)>1: #if workout type specified
	workout_type = sys.argv[1] # A or B

print('Workout type: ', workout_type,
	'\n--------------------------')
if workout_type == 'A':
	generate_workout(fullbody_a,components)
	with open('/Users/richardhausman/Documents/workout/last_workout.txt','w') as f:
		f.write(workout_type)
		f.close()
elif workout_type == 'B':
	generate_workout(fullbody_b, components)
	with open('/Users/richardhausman/Documents/workout/last_workout.txt','w') as f:
		f.write(workout_type)
		f.close()
else:
	print('invalid workout type: {}'.format(workout_type))

