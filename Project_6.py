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
            
            if data == 'L':
                lefty += 1
            if data == 'R':
                righty += 1
                
    return righty, lefty
        
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
        
        for line in left_or_right and position:
            if left_or_right == 'R'and position == 'L':
                left_wing_shoots_right += 1
            if left_or_right == 'L' and position == 'R':
                right_wing_shoots_left +=1
                 
    return left_wing_shoots_right, right_wing_shoots_left
        
    
    
def points_per_game(master_list):
    
    list_tuple = []
    
    for line in master_list:
        player_name = str(line[0])
        points_per_game = (line[18])
        position = line[2]
    
        
        tuple_line = (float(points_per_game), player_name, position)
    
        list_tuple.append(tuple_line)
        
        """ sort and list only the top 10"""
        list_tuple.sort(key=lambda x:x[0], reverse = True)
  
        list_tuple = list_tuple[0:10]
    
    # returns top 10
    return list_tuple
    


def games_played(master_list):
    
    list_of_games_played =[]
    
    for line in master_list:
        player_name =str(line[0])
        games_player = int(line[3].replace(',',''))
       
        
        tuple_of_games_playerd = (player_name, games_player)
        
        list_of_games_played.append(tuple_of_games_playerd)
        
        """ sort and list only the top 10"""
        
        list_of_games_played.sort(key=lambda  x:x[1], reverse = True)
        list_of_games_played =  list_of_games_played[0:10]
        
        
    return list_of_games_played

 

def shots_taken(master_list):
    
    list_of_shots_taken = []
    
    
    for line in master_list:
        player_name = str(line[0])
        
        if line[9] in (None, '--'):
            pass
        else:
            shots_taken = int(line[9].replace(',',''))
        
        
                
            tuple_of_shots_taken = ((shots_taken), player_name)
            
            """ sort and list only the top 10 shots taken"""
            
            list_of_shots_taken.append(tuple_of_shots_taken)
            list_of_shots_taken.sort(key = lambda  x:x[0], reverse = True)
            
            
            
             
    list_of_shots_taken = list_of_shots_taken[0:10]   
                
    return list_of_shots_taken
        
    
def main():
   
    #open file
   fp = open_file()

   master_list = read_file(fp)

   
   # shoots left, shoots right
   
   righty, lefty = shoots_left_right(master_list)
   
   print(("{:^10s}".format("Shooting")))

   print("left:  {:4d}".format (lefty))
   

   print("right: {:4d}".format( righty))
   

   # position
   
   left_wing, right_wing, center, defense = position(master_list)
   
   print("\n{:^12s}".format("Position"))
   print("left:    {:4d}".format(left_wing))
   print("right:   {:4d}".format(right_wing))
   print("center:  {:4d}".format(  center))
   print("defense: {:4d}".format( defense))
   
  #off-side shoots
    
   left_wing_shoots_right, right_wing_shoots_left = off_side_shooter(master_list)
    
   print("\n{:^24s}".format("Off-side Shooter"))
   print("left-wing shooting right: {:4d}".format(left_wing_shoots_right))

   print("right-wing shooting left: {:4d}".format(right_wing_shoots_left))
   
   
   #Top Ten Points-Per-Game
      
   list_tuple  = points_per_game(master_list)
   
   
   print("\n{:^36s}".format("\nTop Ten Points-Per-Game"))
   
   print("{:<20s}{:>8s}{:>16s}".format("Player", "Position", "Points Per Game"))
   
   for line in list_tuple:
       print("{:<20s}{:>8s}{:>16.2f}".format(line[1],line[2],line[0]))
       
   



   
   #games played
   
   list_of_games_played = games_played(master_list)
   
   print("\n{:^36s}".format("Top Ten Games-Played"))
   print("{:<20s}{:>16s}".format("Player", "Games"))
   
   for row in list_of_games_played:
       print("{:<20s}{:>16,d}".format(row[0],row[1]))

  
   

   # list of shots taken
   
   list_of_shots_taken = shots_taken(master_list)
   
   print("\n{:^36s}".format("Top Ten Shots-Taken"))
   
   for line in list_of_shots_taken:
       print("{:<20s}{:>16,d}".format(line[1],line[0]))
   
    
  

if __name__ == "__main__":
    main()