# player_list.py
import random

# Player Node Parameters
# name: players's name
# status: alive is true, dead is false
# target: player's target
# info: prayer request or other info
class Player:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.status = True
        self.target = None
        self.info = None

# PlayerList
class PlayerList:
    def __init__(self):
        self.head = None
        self.length = 0

    def add_player(self, new_player):
        
        self.length += 1
        if not self.head: #if list is empty
            self.head = new_player
            new_player.target = self.head 
        else:
            current = self.head
            while current.target != self.head: #move to end of the list
                current = current.target
            current.target = new_player #set the last player's target to the new player
            new_player.target = self.head #set the new player's target as head

    def eliminate_player(self, username):
        if not self.head: #check if list is empty
            return None
        
        current = self.head
        prev = None
        while current.username != username: #move to player to eliminate, and store their assasin as prev
            prev = current
            current = current.target
            if current == self.head:
                return None
        self.length -= 1
        
        if current == self.head: #if current is the head
            while current.target != self.head: #move to last player in the list
                current = current.target
            if current == self.head: #there is only one player in the whole list
                self.head = None
                return current
            else: #assign the last player's target to the current player's target
                current.target = self.head.target
                self.head = self.head.target
        else:
            prev.target = current.target #otherwise make the assasin's target this person's target
        
        # Reassign the target of the eliminated player
        prev.target = current.target
        current.status = False #the current player is dead
        return current

    def find_player(self, username):
        if not self.head: #return none if list is empty
            return None
        current = self.head
        while current.username != username: #move to player
            current = current.target
            if current == self.head: #if there is only one node, return none
                return None
        return current

    def get_target(self, username):
        player = self.find_player(username)
        if player:
            return player.target
        return None
    
    def display_list(self):
        current = self.head
        print("Number of players: ", self.length)
        for _ in range(self.length):
            print(f"Player: {current.name}, Target: {current.target.name}")
            current = current.target

# Testing the implementation
if __name__ == "__main__":

    # List of players to add (name, username, password)
    players = [
        ("Alice", "alice123", "password1"),
        ("Bob", "bob123", "password2"),
        ("Charlie", "charlie123", "password3"),
        ("Maxxie", "maxxie123", "password4"),
        ("Tony", "tony123", "password5"),
        ("Sid", "sid123", "password6")
    ]

    # Shuffle the list of players
    random.shuffle(players)
    # create instance of playerList
    player_list = PlayerList()
    
    # add players to player list
    for name, username, password in players:
        temp = Player(name, username, password)
        player_list.add_player(temp)
        print(f"Added {name} with username {username}")
    
    # Display the initial cycle of players
    player_list.display_list()
    
    # Eliminate Bob
    eliminated = player_list.eliminate_player("bob123")
    if eliminated:
        print(f"Eliminated: {eliminated.username}")
    
    # Display the new cycle of players
    player_list.display_list()

    # Display the target of Alice
    target = player_list.get_target("alice123")
    if target:
        print(f"Alice's target: {target.username}")
