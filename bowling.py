import random
class Game:
    def __init__(self, player_count):
        self.player_count = player_count
        self.frame = 0
        self.player_list = []
        loop = 0
        while loop < int(player_count):
            self.player_list.append(Player())
            loop += 1
            
    def play(self):
        while self.frame < 10:
            for player in self.player_list:
                player.player_frames[self.frame].roll()
                player.total_score += player.player_frames[self.frame].score
            self.frame += 1
        print("\n---FINAL SCORES---")
        for player in self.player_list:
            print(f"{player.player_name}  {player.total_score}")
            


class Player:
    def __init__(self):
        self.player_name = self.get_name()
        self.player_frames = []
        self.total_score = 0
        loop = 0
        while loop < 10:
            self.player_frames.append(Frame())
            loop += 1
        
        
    def get_name(self):
        player_name = input("Please enter players name:\n")
        return player_name
    
    
class Frame:
    def __init__(self):
        self.score = 0
        self.strike = False
        self.spare = False
        
    def roll(self):
        roll = random.randint(0,10)
        if roll == 10:
            self.strike = True
            self.score = 10
            return
        else:
            self.score = roll
            roll = random.randint(0, (10 - self.score))
            if roll + self.score == 10:
                self.spare = True
                self.score = 10
                return
            self.score = roll + self.score
            return
            
            
            
        
def main():
    print("Hello and welcome to terminal-bowl!")
    player_count = input('Please enter the number of players:\n')
    play_game = Game(player_count)
    play_game.play()
    
    
    
    
    
    
if __name__ == "__main__":
    main()