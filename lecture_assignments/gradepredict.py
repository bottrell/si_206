#Add points together
#Drop scores - sort
#Get data from file
#Convert to a letter grade

#Discussion sections: 13 but drop 2
#Homeworks          : 14 drop 2
#Lecture exercises  : 26 drop 4
#Midterms           : 2
#Projects           : 3
#Final Projects     : 1
#Total points       : 1560

import csv
import sys
#
#param:
#returns: 
def get_data():
	pass

#return a sorted list of scores for a particular type of assignment
#param: list of scores 
#return a sorted list of scores
def sort_scores(scores):
	pass

#param: list of scores
#returns: total scores after dropping lowest 4
def calculate_lecture_Exercise_score(lecture_scores):
	pass

#param: list of scores
#returns: total scores after dropping lowest 2
def calculate_discussion_score(discussion_scores):
	pass

def calculate_homework_score(homework_scores):
	pass

def calculate_midterm_score(midterm_scores):
	pass

def calculate_project_score(project_scores):
	pass

#params: an int representing total points earned
#return a float representing a percentage between [0,1]
def convert_to_percent(total_points):
	#return total_points/1560
	pass

#params: a percent between 0 and 1
#return a letter grade value
def convert_to_letter_grade(percent):
	pass
