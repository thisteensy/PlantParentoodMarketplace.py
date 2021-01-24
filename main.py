#This is a text adventure game about shopping for plants in the current market with all the thrills of creating a beautiful collection and watching it grow along with the dangers of inflated prices, bad actors, pests and more. It's Tulip Mania for the 21st Century.
import random
#create a list of possible plants
#create dictionaries of plants, what they cost and what they are worth
import time

money = 1000
heart_points = 10
plant_points = 0
your_plants = []
decision = ""
p_camposportoanum = {"name": "philodendron camposportoanum", "cost": 65, "worth": 120}
p_pink_princess = {"name": "philodendron pink princess", "cost": 30, "worth": 200}
p_gloriosum = {"name": "philodendron gloriosum", "cost": 40, "worth": 200}
b_angel_wing = {"name": "angel wing begonia", "cost": 8, "worth": 12}
f_pteris = {"name": "pteris fern", "cost": 8, "worth": 10}
t_zebrina = {"name": "tradescantia zebrina", "cost": 8, "worth": 10}

#rattlesnake_calathea, p_brasil, a_vittarifolium, a_forgetii, p_jungle_boogie, p_gloriosum, s_rayii, s_variegatum_albo, s_variegatum_aurea, pony_tail_palm, h_rotundifolia, h_krimson_queen, p_pedatum, silver_brake_fern, pothos_manjula, p_micans, h_chelsea, h_obovata, maidenhair_fern, scindapsus_pictus, epipremnum_pinatum_cebu_blue, tradescantia_zebrina, variegated_soh, h_curtisii, a_warocqueanum
# plants = [p_pink_princess, p_camposportoanum]
def score():
    time.sleep(2)
    print(f"Current score: You have ${money}, {heart_points} heartpoints and {plant_points} plant points.")
    time.sleep(2)
def jungle():
    time.sleep(2)
    print("Here are the plants you have collected and their value: ")
    for plant in your_plants:
        print()
        print (plant["name"], "$" + str(plant["worth"]))
        time.sleep(2)
    if len(your_plants) == 0:
        print()
        print ("You don't have any plants yet, sad.")
        time.sleep(2)



def intro():
    print("Welcome to Plant Parenthood Marketplace: A place to buy sell and trade tropical plants.")
    time.sleep(2)
    print()
    print("Your goal is to build a beautiful collection of healthy plants to create your indoor jungle. \nTo do so you will start with $1000 and 10 heart points. \nYou will need to reach 500 plant points to win. \nBeware of the dangers of the marketplace that can cause you to lose\nmoney and heart points. \nIf you lose all of your heart points, you give up collecting and \nlose the game.")
    time.sleep(5)
    print()
    decision = input("Are you ready to get planty? > ").upper()
    time.sleep(2)
    if decision.startswith("N"):
        print("That's ridculous, but have a nice day, anyway.")
        
    elif decision.startswith("Y"):
        print()
        print("Great! Lets go!")
        print()
        time.sleep(2)
intro()
def pass_on_deal():
    print("You have passed on this deal.")
    print()
    time.sleep(2)
def buy_a():
    #make this into a function called globalize_score :)
    global money
    global heart_points
    global plant_points
    print ("You see a post in your local houseplant lovers group that Costa Farms has released a batch of " + p_pink_princess["name"] + "for $" + str(p_pink_princess ["cost"]) + "at Home Depots all over your metro area. The pandemic continues to rage.\n You could go to as many stores as possible and buy every plant you see so that you can re-sell them for $" + str(p_pink_princess["worth"]) + " each and keep one for yourself!")
    time.sleep(2)
    print()
    decision = input("[D]eal or [P]ass? >").upper()
    print()
    time.sleep(3)
    if decision.startswith("D"):
        covid = random.randint(1, 3)
        if covid == 1 or covid == 2:
            print ("You caught COVID-19 going from store to store. You were unable to care for your plants properly, this costs you 50% of your plant points and 5 heart points. You spent $500 and all but one of the pink princesses died, because they were overwatered at the store. You managed to save on philodendron pink princess worth $200 and it was added to your collection.")
            print()
            time.sleep(5)
            money = money - 500
            plant_points = plant_points/2
            heart_points = heart_points - 5
            your_plants.append(p_pink_princess)
        else:
            print ("You got lucky! You got 5 philodendron pink princesses, sold 4 of them for $200 each and kept one for your collection! You gain 10 plant points, but no heart points, since you were lucky to evade the virus.")
            print()
            time.sleep(2)
            money = money + 800
            plant_points = plant_points + 10
            your_plants.append(p_pink_princess)
    else:
        pass_on_deal()

def buy_b():
    global money
    global heart_points
    global plant_points
    print("A plant seller you know from Instagram is having a sale. You know her plants are healthy and well cared for, and her prices are reasonable, but her plants tend to be hard to find and therefore more expensive. She has a beautiful " + p_camposportoanum["name"] + " with many leaves and air roots for $" + str(p_camposportoanum["cost"]) + ". This plant is easily worth $" + str(p_camposportoanum["worth"]) + ". It is an amazing deal, but you are not allowed to resell this plant.")
    time.sleep(2)
    print()
    decision = input("[D]eal or [P]ass? >").upper()
    print()
    time.sleep(2)
    if decision.startswith("D"):
        print(f"Excellent! You have bought a", p_camposportoanum["name"], "worth $",p_camposportoanum["worth"], "for $",p_camposportoanum["cost"])
        print()
        time.sleep(2)
        money = money - 65
        plant_points = plant_points + 10
        heart_points = heart_points + 2
        your_plants.append(p_camposportoanum)
    else:
        pass_on_deal()
def buy_c():
    global money
    global heart_points
    global plant_points
    print("Weekend Wishlist!! The weekend wishlist thread invites you to list a plant that you're looking for. Poeple who have that plant to sell can offer it to you. You state that you're looking for a philodendron gloriosum. A collector you know from your local B/S/T group has a rooted node of this plant with one growth point. He is offering it to you for $40.")
    print()
    time.sleep(2)
    decision = input("[D]eal or [P]ass? >").upper()
    print()
    time.sleep(2)
    if decision.startswith("D"):
        rot = random.randint(1, 3)
        if rot == 1 or rot == 2:
            print("You bought the rooted philodendron node for $40. It grew well and is a beautiful healthy plant now worth $200")
            print()
            plant_points = plant_points + 10
            money = money - 40
            heart_points = heart_points + 2
            your_plants.append(p_gloriosum)
        elif rot == 3:
            print("You bought the node, but were unable to get it to grow and it evenually rotted. You are out the $40, and the failure was discouraging, -2 heart points.")
            print()
            money = money - 40
            heart_points = heart_points - 2
        else:
            pass_on_deal()
def buy_d():
    global money
    global heart_points
    global plant_points
    print("Your friend invites you to join her at a sale at a local nursery. They don't have anything very unusual but prices are very good and there are three plants you like for $8 each: a pteris fern, a tradescantia zebrina and an angel wing begonia.")
    print()
    time.sleep(2)
    decision = input("[D]eal or [P]ass? >").upper()
    print()
    time.sleep(2)
    if decision.startswith("D"):
        print("Congratulations you bought 3 plants, a pteris fern, a tradescantia zebrina and an angel wing begonia. You gained 6 plant points and 2 heart points, because shopping with a friend is always best.")
        print()
        money = money - 24
        plant_points = plant_points + 6
        heart_points = heart_points + 2
        your_plants.append(f_pteris)
        your_plants.append(t_zebrina)
        your_plants.append(b_angel_wing)
    else:
        pass_on_deal()

def buy_adventures():
    buying_scenario = [buy_a, buy_b, buy_c, buy_d]
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
