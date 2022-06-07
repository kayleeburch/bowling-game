import random
class Game:
    def __init__(self, player_count):
        self.player_count = player_count #this is int that user specified
        self.frame = 0
        self.player_list = []
        loop = 0 
        while loop < int(player_count):
            self.player_list.append(Player()) #calls the player class to get names and player frames for each player
            loop += 1
            
    def play(self):
        while self.frame < 10: #for each frame while less than 10 frames
            for player in self.player_list: #for each player, for each frame in player, inside of player_list
                player.player_frames[self.frame].roll() #for each player in player in player list and their player frame, run the roll method to get a score
                player.total_score += player.player_frames[self.frame].score #for each player, all all the player_frames score to total_score defines in Player
            self.frame += 1 #loop through each grame until less than 10 (at 9)
        print("\n---FINAL SCORES---")
        for player in self.player_list: #loop through the player_list with total_score now calculated
            print(f"{player.player_name}  {player.total_score}") #print the player_name and the total_score
            


class Player:
    def __init__(self):
        self.player_name = self.get_name() #setting .get_name() in attributes so it is already called
        self.player_frames = [] #player frames will hold all 10 frames inside of Player class
        self.total_score = 0 #will calculate total score for each player for 10 frames
        loop = 0 
        while loop < 10: #since a total of 10 frames
            self.player_frames.append(Frame()) #calls the Frame() call 10 times to get 10 empty frames
            loop += 1
        
        
    def get_name(self):
        player_name = input("Please enter players name:\n") #is called when player calls is called to get each name for number of players
        return player_name 
    
    
class Frame:
    def __init__(self):
        self.score = 0 #setting initial score to 0 
        self.strike = False #setting strike to False unless player gets 10/10 balls knocked first roll in one frame
        self.spare = False #setting spare to Flase unless player gets 10 balls knocked down in 2 rolls in one frame
        
    def roll(self): #roll will calculate score each time frame is called
        roll = random.randint(0,10) #roll is random in between 0 and 10
        if roll == 10: #setting score to 10 and strike to true
            self.strike = True
            self.score = 10
            return
        else:
            self.score = roll #setting score to roll if not a strike
            roll = random.randint(0, (10 - self.score)) #roll will not be 0 to whatever pins the player didn't hit
            if roll + self.score == 10: #if player hits all all pins in second roll, set spare to true and score to 10 
                self.spare = True
                self.score = 10
                return
            self.score = roll + self.score #if not strike or spare, return score as total pins knocked down in a frame
            return #returns score
            
            
            
        
def main():
    print("Hello and welcome to terminal-bowl!")
    player_count = input('Please enter the number of players:\n')
    play_game = Game(player_count) #initializing Game to play_game instance and inputs player_count int
    play_game.play() #calls play() method in Game class
    
    
    
    
    
    
if __name__ == "__main__":
    main()