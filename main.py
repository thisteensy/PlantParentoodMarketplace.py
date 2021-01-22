#This is a text adventure game about shopping for plants in the current market with all the thrills of creating a beautiful collection and watching it grow along with the dangers of inflated prices, bad actors, pests and more. It's Tulip Mania for the 21st Century.
import random
#create a list of possible plants
#create dictionaries of plants, what they cost and what they are worth


money = 1000
heart_points = 10
plant_points = 0
your_plants = []
decision = ""
p_camposportoanum = {"name": "philodendron camposportoanum", "cost": 65, "worth": 120}
p_pink_princess = {"name": "philodendron pink princess", "cost": 30, "worth": 200}
#rattlesnake_calathea, p_brasil, a_vittarifolium, a_forgetii, p_jungle_boogie, p_gloriosum, s_rayii, s_variegatum_albo, s_variegatum_aurea, pony_tail_palm, h_rotundifolia, h_krimson_queen, p_pedatum, silver_brake_fern, pothos_manjula, p_micans, h_chelsea, h_obovata, maidenhair_fern, scindapsus_pictus, epipremnum_pinatum_cebu_blue, tradescantia_zebrina, variegated_soh, h_curtisii, a_warocqueanum
# plants = [p_pink_princess, p_camposportoanum]
def score():
    print(f"Current score: You have ${money}, {heart_points} heartpoints and {plant_points} plant points.")
def jungle():
    print("Here are the plants you have collected and their value: ")
    for plant in your_plants:
        print()
        print (plant["name"], "$" + str(plant["worth"]))
    if len(your_plants) == 0:
        print()
        print ("You don't have any plants yet, sad.")



def intro():
    print("Welcome to Plant Parenthood Marketplace: A place to buy sell and trade tropical plants.")
    print()
    print("Your goal is to build a beautiful collection of healthy plants to create your indoor jungle. \nTo do so you will start with $1000 and 10 heart points. \nYou will need to reach 500 plant points to win. \nBeware of the dangers of the marketplace that can cause you to lose\nmoney and heart points. \nIf you lose all of your heart points, you give up collecting and \nlose the game.")
    print()
    decision = input("Are you ready to get planty? > ").upper()
    if decision.startswith("N"):
        print("That's ridculous, but have a nice day, anyway.")
        
    elif decision.startswith("Y"):
        print()
        print("Great! Lets go!")
        print()
intro()
def buy_a(): 
    print ("You see a post in your local houseplant lovers group that Costa Farms has released a batch of " + p_pink_princess["name"] + "for $" + str(p_pink_princess ["cost"]) + "at Home Depots all over your metro area. The pandemic continues to rage.\n Do you go to as many stores as possible and buy every plant you see so that you can re-sell them for $" + str(p_pink_princess["worth"]) + " each and keep one for yourself?")

def buy_b():
    print("A plant seller you know from Instagram is having a sale. You know her plants are healthy and well cared for, and her prices are reasonable, but her plants tend to be hard to find and therefore more expensive. She has a beautiful " + p_camposportoanum["name"] + " with many leaves and air roots for $" + str(p_camposportoanum["cost"]) + ". This plant is easily worth $" + str(p_camposportoanum["worth"]) + ". It is an amazing deal, but you are not allowed to resell this plant.")
    decision = input("[D]eal or [P]ass? >").upper()
    if decision.startswith("D"):
        print(f"Excellent! You have bought a", p_camposportoanum["name"], "worth $",p_camposportoanum["worth"], "for $",p_camposportoanum["cost"])
        money == money - 65
        plant_points == plant_points + 10
        heart_points == heart_points + 2
        your_plants.append(p_camposportoanum)
    else:
        print("You have passed on this deal.")
def buy_adventures():
    buying_scenario = [buy_a, buy_b]
    print("Here is your buying adventure:\n\n")
    random.choice(buying_scenario)()
def trade_adventures():
    


    def trade_b():
        print ("something something something")
    
    trading_choices = [trade_a(), trade_b()]
    print("Here is your trading adventure:\n\n", random.choice(trading_choices))
    
    print()
    print(decision)
    print()
while True:
    score()
    jungle()
    print()
    print("Any time you want to see this information type 1 for your score or 2 for plant list.")
    print()
    if plant_points > 49:
        print ("Congratulations, you have a beautiful plant collection and you won the game and at life!! Now go relax in your indoor jungle!")
        break
    if heart_points < 1:
        print ("The trials of the plant parenthood have just been too much for you. You have given up your collecting adventure and you have lost the game.")
        break
    if money < 1 and plant_points < 20:
        print ("You have run out of money and have no way to get more. Your plant collecting adventures are over and you have lost the game.")
        break
    else:
        print("What would you like to do? [B]uy, [S]ell, [T]rade or [Q]uit")
        decision = input("> ").upper()
        if decision.startswith("Q"):
            print()
            print("Thank you for visiting. Have a nice day.")
            break
        elif decision.startswith("B"):
            buy_adventures()
        elif decision.startswith("S"):
            sell_adventures()
        elif decision.startswith("T"):
            trade_adventures()
        elif decision == "1":
            score()
            print()
        elif decision == "2":
            jungle()
            print()
        else:
            print()
            print("Sorry. That is not a valid answer.")
            print()
