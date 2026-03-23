from random import shuffle

class Card:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False
    
    def __repr__(self):
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(j, i))
        
        shuffle(self.cards)
    
    def rm_card(self):
        if len(self.cards) == 0:
            return
        else:
            return self.cards.pop()

class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name

class Game:
    def __init__(self):
        self.print_welcome()
        name1 = input("👤 Player 1 Name: ")
        name2 = input("👤 Player 2 Name: ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
    
    def print_welcome(self):
        """Print welcome message and game instructions"""
        print("=" * 60)
        print("🎴 WELCOME TO THE CARD GAME! 🎴".center(60))
        print("=" * 60)
        print()
        print("📋 GAME DESCRIPTION:")
        print("   This is a simple card battle game between two players.")
        print("   Each round, both players draw one card from the deck.")
        print("   The player with the higher card wins that round!")
        print()
        print("🎯 HOW TO PLAY:")
        print("   1. Enter the names of both players")
        print("   2. For each round, press 'c' to continue playing")
        print("   3. Cards will be drawn automatically")
        print("   4. The higher card wins the round")
        print("   5. Press 'q' to quit the game at any time")
        print()
        print("🏆 WINNING:")
        print("   The player with the most rounds won is the WINNER!")
        print()
        print("=" * 60)
        print()
    
    def wins(self, winner):
        w = "🎊 This round goes to {}"
        w = w.format(winner)
        print(w)
        print("🧩 Current score: {}: {} - {}: {}".format(self.p1.name, self.p1.wins, self.p2.name, self.p2.wins))
        print("--------------------------------------------------")

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} drew {} and {} drew {}"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("🏁 Game has begun")
        
        while len(cards) >= 2:
            m = "🚫 Press 'q' to quit \n⏩️ Press 'c' key to continue playing: "
            response = input(m)
            
            if response == 'q':
                break

            if response == 'c':
                p1c = self.deck.rm_card()
                p2c = self.deck.rm_card()
                p1n = self.p1.name
                p2n = self.p2.name
                self.draw(p1n, p1c, p2n, p2c)
                if p1c > p2c:
                    self.p1.wins += 1
                    self.wins(self.p1.name)
                else:
                    self.p2.wins += 1
                    self.wins(self.p2.name)
            
        win = self.winner(self.p1, self.p2)
        print("⏹️ Game is over. {} wins 🎉".format(win))
    
    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie ⋈"

game = Game()
game.play_game()