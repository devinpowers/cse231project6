#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 17:22:52 2020

@author: devinpowers
"""


''' Insert heading comments here.'''

import csv

def open_file():
    
    """
    prompt for file name
    try to open the file
    except FileNotFoundError
        print error message
    :return: fp
    """
    while True:
        file_name = input("Input a file name: ")
        try:
            fp = open(file_name)
            break
        except FileNotFoundError:
            print("Unable to open file. Please try again.")
            continue
        
    return fp
    

def read_file(fp):
    
    master_list = []
    fp.readline()
    reader = csv.reader(fp)
    
    for line in reader:
    
        master_list.append(line)
        
    return master_list

   
def shoots_left_right(master_list):
    
    lefty = 0
    righty = 0
    
    for line in master_list:
        s_c = line[1]
        
        for data in s_c:
            
            if data == 'R':
                righty += 1
            if data == 'L':
                lefty += 1
                
    return lefty, righty
        
def position(master_list):
    
    left_wing = 0
    right_wing = 0
    center = 0
    defense = 0
    
    for line in master_list:
        positions = line[2]
        
        for position in positions:
            
            if position == 'L':
                left_wing += 1
            if position == 'R':
                right_wing += 1
            if position == 'C':
                center += 1
            if position == 'D':
                defense += 1
                
    return left_wing, right_wing, center, defense
                
    
def off_side_shooter(master_list):
    
    left_wing_shoots_right = 0
    right_wing_shoots_left = 0
    
    for line in master_list:
        left_or_right = line[1]
        position = line[2]
        
        for line in left_or_right,position:
            if left_or_right == 'R'and position == 'L':
                left_wing_shoots_right += 1
            if left_or_right == 'L' and position == 'R':
                right_wing_shoots_left +=1
                 
    return left_wing_shoots_right, right_wing_shoots_left
        
    
    
def points_per_game(master_list):
    
    list_tuple = []
    
    for line in master_list:
        player_name = str(line[0])
        points_per_game = (line[20])
        position = line[2]
    
        
        tuple_line = (float(points_per_game), player_name, position)
    
        list_tuple.append(tuple_line)
        
        """ sort and list only the top 10"""
        list_tuple.sort()
        list_tuple = list_tuple[0:9]
    
    # returns top 10
    return list_tuple, player_name, points_per_game, position
    


def games_played(master_list):
    
    list_of_games_played =[]
    
    for line in master_list:
        player_name =str(line[0])
        games_player = int(line[3].replace(',',''))
       
        
        tuple_of_games_playerd = (player_name, games_player)
        
        list_of_games_played.append(tuple_of_games_playerd)
        
        list_of_games_played.sort()
        list_of_games_played =  list_of_games_played[0:9]
        
        
    return list_of_games_played

 

def shots_taken(master_list):
    
    list_of_shots_taken = []
    
    word = "--"
    
    for line in master_list:
        
        if not word in line: 
            player_name = str(line[0])
            shots_taken = int(line[9].replace(',',''))
        
      
                
            tuple_of_shots_taken = ((shots_taken), player_name)
                
            list_of_shots_taken.append(tuple_of_shots_taken)
                
            list_of_shots_taken.sort()
            list_of_shots_taken[0:9]
                
    return list_of_shots_taken
        
    
def main():
   
    #open file
   fp = open_file()

   master_list = read_file(fp)

   
   # shoots left, shoots right
   
   righty, lefty = shoots_left_right(master_list)
   
   print(" Shooting")

   print('Left:  ',lefty)
   print("Right: ", righty)
   
   
   # position
   
   left_wing, right_wing, center, defense = position(master_list)
   
   print("\n Position")
   print('Left:    ',    left_wing)
   print('Right:   ',   right_wing)
   print("Center:  ",  center)
   print("Defense: ", defense)
   
  #off-side shoots
    
   left_wing_shoots_right, right_wing_shoots_left = off_side_shooter(master_list)
    
   print("\n     Off-side Shooter")
   print('left wing shooting right: ', left_wing_shoots_right)
   print('right wing shooting left: ', right_wing_shoots_left)
   
   #Top Ten Points-Per-Game
      
   list_tuple  = points_per_game(master_list)
   
   
   print("\n Top Ten Points-Per-Game")
   
  
         

   print("\nheres a list:",list_tuple)
   

   
   #games played
   
   list_of_games_played = games_played(master_list)
   
   print("\ntuple for games played by each player:", list_of_games_played)
   
   
   # list of shots taken
   
   list_of_shots_taken = shots_taken(master_list)
   
   print("\n the number of shots taken by players and there name:", list_of_shots_taken)
   
    
  

if __name__ == "__main__":
    main()