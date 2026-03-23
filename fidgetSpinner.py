from turtle import *

state = {'turn': 0}

def print_welcome():
    """Print welcome message and game instructions"""
    print("=" * 60)
    print("🎡 WELCOME TO THE SPINNER GAME! 🎡".center(60))
    print("=" * 60)
    print()
    print("📋 GAME DESCRIPTION:")
    print("   This is a fun spinner game with three colored dots:")
    print("   🔴 RED, 🟢 GREEN, and 🔵 BLUE")
    print("   The spinner rotates and slows down over time.")
    print()
    print("🎯 HOW TO PLAY:")
    print("   1. A spinner with three colored dots will appear")
    print("   2. Press the SPACEBAR to flick the spinner")
    print("   3. Each spacebar press gives the spinner energy")
    print("   4. The spinner will rotate and gradually slow down")
    print("   5. Try to stop it on your favorite color!")
    print()
    print("🎮 CONTROLS:")
    print("   📌 SPACEBAR = Flick the spinner (add rotation)")
    print()
    print("💡 TIP:")
    print("   The more you flick, the faster it spins!")
    print("   Watch it slow down and see where it stops!")
    print()
    print("=" * 60)
    print()

def spinner():
    clear()
    angle = state['turn']/10
    right(angle)
    forward(100)
    dot(120, 'red')
    back(100)
    right(120)
    forward(100)
    dot(120, 'green')
    back(100)
    right(120)
    forward(100)
    dot(120, 'blue')
    back(100)
    right(120)
    update()

def animate():
    if state['turn'] > 0:
        state['turn'] -= 1
    
    spinner()
    ontimer(animate, 20)

def flick():
    state['turn'] += 10

# Print welcome message first
print_welcome()

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
width(20)
onkey(flick, 'space')
listen()
animate()
done()