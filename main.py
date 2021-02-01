#This is a text adventure game about shopping for plants in the current market with all the thrills of creating a beautiful collection and watching it grow along with the dangers of inflated prices, bad actors, pests and more. It's Tulip Mania for the 21st Century.
import random
#create a list of possible plants
#create dictionaries of plants, what they cost and what they are worth
import time
#variables that get reused throughout the program
money = 1000
heart_points = 10
plant_points = 0
your_plants = {}
decision = ""
#list of plants available throughout the game
available_plants = {"philodendron camposportoanum":{"name": "philodendron camposportoanum", "cost": 65, "worth": 120},"philodendron pink princess": {"name": "philodendron pink princess", "cost": 30, "worth": 200}, "philodendron gloriosum": {"name": "philodendron gloriosum", "cost": 40, "worth": 200}, "angel wing begonia": {"name": "angel wing begonia", "cost": 8, "worth": 12}, "pteris fern": {"name": "pteris fern", "cost": 8, "worth": 10}, "tradescantia zebrina": {"name": "tradescantia zebrina", "cost": 8, "worth": 10}, "philodendron Florida ghost": {"name": "philodendron Florida ghost", "cost": 35, "worth": 180}, "philodendron gigas": {"name": "philodendron gigas", "cost": 150, "worth": 200}, "anthurium vittarifolium": {"name": "anthurium vittarifolium", "cost": 35, "worth": 220}, "rattlesnake calathea": {"name": "rattlesnake calathea", "cost": 15, "worth": 15}, "philodendron Brasil": {"name": "philodendron Brasil", "cost": 0, "worth": 25}, "anthurium forgetii": {"name": "anthurium forgetii", "cost": 0, "worth": 170}, "syngonium rayii": {"name": "syngonium rayii", "cost": 25, "worth": 25}, "syngonium aurea": {"name": "syngonium aurea", "cost": 0, "worth": 175}, "philodendron pedatum": {"name": "philodendron pedatum", "cost": 20, "worth": 45}, "philodendron melanochrysum": {"name": "philodendron melanochrysum", "cost": 45, "worth": 225}, "anthurium warocqueanum": {"name": "anthurium warocqueanum", "cost": 35, "worth": 400}, "syngonium albo": {"name": "syngonium albo", "cost": 35, "worth": 50}, "hoya rotundiflora": {"name": "hoya rotundiflora", "cost": 45, "worth": 65}, "hoya obovata": {"name": "hoya obovata", "cost": 20, "worth": 60}, "pothos manjula": {"name": "pothos manjula", "cost": 20, "worth": 10}, "philodendron mayoi": {"name": "philodendron mayoi", "cost": 35, "worth": 135}, "anthurium pedatoradiatum": {"name": "anthurium pedatoradiatum", "cost": 35, "worth": 90}}
#function that randomized a choice of plants offered for trade based on a price range
def random_trade(priciness):
    list_plants = list(priciness)
    random_plant = random.choice(list_plants)
    return random_plant
#function that prints out the score during the game
def score():
    time.sleep(1)
    print(f"Current score: You have ${money}, {heart_points} heartpoints and {plant_points} plant points.")
    print()
#function that prints out the plants you have collected
def jungle():
    time.sleep(1)
    print("Here are the plants you have collected and their value: ")
    print()
    if len(your_plants) == 0:
        print ("You don't have any plants yet, sad.")
        time.sleep(1)
    else:
        for plant, plant_data in your_plants.items():
            print(f"{plant_data['name']} ${plant_data['worth']}")
#function that creates a dictionary of plants you own indexed by number, handy for using for input when offering them for sale or trade
def list_plants(plants):
    plants_fs = {}
    num_plant = 1
    for plant, plant_data in plants.items():
        plants_fs[num_plant] = plant_data
        num_plant = num_plant + 1
    return plants_fs
#function that sorts available plants by worth into bands of priciness and returns four dictionaries of those sorted plants
def sort_plants_by_worth(plants):
    cheap_plants = {}
    moderate_plants = {}
    pricey_plants = {}
    ridiculous_plants = {}
    for plant, plant_data in plants.items():
        if plant_data["worth"] < 50:
            cheap_plants[plant] = plant_data
        elif plant_data["worth"] >= 50 and plant_data["worth"] < 100:
            moderate_plants[plant] = plant_data
        elif plant_data["worth"] >= 100 and plant_data["worth"] < 150:
            pricey_plants[plant] = plant_data
        elif plant_data["worth"] >= 150:
            ridiculous_plants[plant] = plant_data
    return cheap_plants, moderate_plants, pricey_plants, ridiculous_plants
#the intro
def intro():
    print("Welcome to Plant Parenthood Marketplace: A place to buy sell and trade tropical plants.")
    time.sleep(1)
    print()
    print("Your goal is to build a beautiful collection of healthy plants to create your indoor jungle. \n\nTo do so you will start with $1000 and 10 heart points. \n\nYou will need to reach 500 plant points to win. \n\nBeware of the dangers of the marketplace that can cause you to lose\nmoney and heart points. \n\nIf you lose all of your heart points, you give up collecting and \nlose the game.")
    time.sleep(3)
    print()
    decision = input("Are you ready to get planty? > ").upper()
    time.sleep(1)
    if decision.startswith("N"):
        print("That's ridculous, but have a nice day, anyway.")
        
    elif decision.startswith("Y"):
        print()
        print("Great! Lets go!")
        print()
intro()
def pass_on_deal():
    print("You have passed on this deal.")
    print()
    time.sleep(1)
def buy_a():
    #make this into a function called globalize_score :)
    global money
    global heart_points
    global plant_points
    print ("You see a post in your local houseplant lovers group that Costa Farms has released a batch of philodendron pink princesses for $30 at Home Depots all over your metro area. The pandemic continues to rage.\n You could go to as many stores as possible and buy every plant you see so that you can re-sell them for $200 each and keep one for yourself!")
    time.sleep(1)
    print()
    decision = input("[D]eal or [P]ass? >").upper()
    print()
    time.sleep(1)
    if decision.startswith("D"):
        covid = random.randint(1, 3)
        if covid == 1 or covid == 2:
            print ("You caught COVID-19 going from store to store. You were unable to care for your plants properly, this costs you 50% of your plant points and 5 heart points. You spent $500 and all but one of the pink princesses died, because they were overwatered at the store. You managed to save on philodendron pink princess worth $200 and it was added to your collection.")
            print()
            time.sleep(3)
            money = money - 500
            plant_points = plant_points/2
            heart_points = heart_points - 5
            your_plants["philodendron pink princess"]= available_plants["philodendron pink princess"]
        else:
            print ("You got lucky! You got 5 philodendron pink princesses, sold 4 of them for $200 each and kept one for your collection! You gain 10 plant points, but no heart points, since you were lucky to evade the virus.")
            print()
            time.sleep(1)
            money = money + 800
            plant_points = plant_points + 10
            your_plants["philodendron pink princess"]= available_plants["philodendron pink princess"]
    else:
        pass_on_deal()

def buy_b():
    global money
    global heart_points
    global plant_points
    print("Instagram Sale! A plant seller you know from Instagram is having a sale. You know her plants are healthy and well cared for, and her prices are reasonable, but her plants tend to be hard to find and therefore more expensive. She has a beautiful philodendron camposportoanum with many leaves and air roots for $65. This plant is easily worth $120. It is an amazing deal, but you are not allowed to resell this plant.")
    time.sleep(1)
    print()
    decision = input("[D]eal or [P]ass? >").upper()
    print()
    time.sleep(1)
    if decision.startswith("D"):
        print("Excellent! You have bought a philodendron camposportoanum, worth $120 for $65.")
        print()
        time.sleep(1)
        money = money - 65
        plant_points = plant_points + 10
        heart_points = heart_points + 2
        your_plants["philodendron camposportoanum"] = available_plants["philodendron camposportoanum"]
    else:
        pass_on_deal()
def buy_c():
    global money
    global heart_points
    global plant_points
    print("Weekend Wishlist!! The weekend wishlist thread invites you to list a plant that you're looking for. People who have that plant to sell can offer it to you. You state that you're looking for a philodendron gloriosum. A collector you know from your local B/S/T group has a rooted node of this plant with one growth point. He is offering it to you for $40.")
    print()
    time.sleep(1)
    decision = input("[D]eal or [P]ass? >").upper()
    print()
    time.sleep(1)
    if decision.startswith("D"):
        rot = random.randint(1, 3)
        if rot == 1 or rot == 2:
            print("You bought the rooted philodendron gloriosum node for $40. It grew well and is a beautiful healthy plant now worth $200.")
            print()
            time.sleep(1)
            plant_points = plant_points + 10
            money = money - 40
            heart_points = heart_points + 2
            your_plants["philodendron gloriosum"] = available_plants["philodendron gloriosum"]
        elif rot == 3:
            print("You bought the node, but were unable to get it to grow and it evenually rotted. You are out the $40, and the failure was discouraging, -2 heart points.")
            print()
            time.sleep(1)
            money = money - 40
            heart_points = heart_points - 2
        else:
            pass_on_deal()
def buy_d():
    global money
    global heart_points
    global plant_points
    print("PLANT SALE! Your friend invites you to join her at a sale at a local nursery. They don't have anything very unusual but prices are very good and there are three plants you like for $8 each: a pteris fern, a tradescantia zebrina and an angel wing begonia.")
    print()
    time.sleep(1)
    decision = input("[D]eal or [P]ass? >").upper()
    print()
    time.sleep(1)
    if decision.startswith("D"):
        print("Congratulations you bought 3 plants, a pteris fern, a tradescantia zebrina and an angel wing begonia. You gained 6 plant points and 2 heart points, because shopping with a friend is always best.")
        print()
        time.sleep(1)
        money = money - 24
        plant_points = plant_points + 6
        heart_points = heart_points + 2
        your_plants["pteris fern"] = available_plants["pteris fern"]
        your_plants["tradescantia zebrina"] = available_plants["tradescantia zebrina"]
        your_plants["angel wing begonia"] = available_plants["angel wing begonia"]
    else:
        pass_on_deal()
def buy_e():
    global money
    global heart_points
    global plant_points
    print("***PURGE ALERT*** Someone you know to be an accomplished grower is going to host a purge on your local Rare and Tropical Plants BST group. They list several young plants and rooted cuttings that draw a large crowd. Competition is likely to be fierce. You may participate in this purge, but beware of the risks of participating in a fevered event like this. Set yourself a budget and don't buy anything over your budget. One of the rules of this purge is that you're not allowed to back out if you speak for a plant.")
    print()
    time.sleep(1)
    decision = input("[D]eal or [P]ass? >").upper()
    print()
    time.sleep(1)
    if decision.startswith("D"):
        purge_luck = random.randint(1, 4)
        if purge_luck == 1:
            print("The competition was fierce but you managed to score a beautiful young philodendron Florida Ghost, a wishlist plant of yours, for $35. This plant thives with the headstart of this grower and is now worth $180. You gain 8 plant points.")
            print()
            time.sleep(1)
            money = money - 35
            plant_points = plant_points + 8
            your_plants["philodendron Florida ghost"] = available_plants["philodendron Florida ghost"]
        elif purge_luck == 3:
            print("You got caught up in the moment and spoke for a plant without looking at the price, and to your surprise, you won. Although most of the offings were under $100, this one was $150! Nonetheless, you are the proud owner of a beautiful philodendron gigas worth $200. You gain 10 plant points, but you lose 2 heart points, because you blew your budget.")
            print()
            time.sleep(1)
            money = money - 150
            plant_points = plant_points + 10
            heart_points = heart_points -2
            your_plants["philodendron gigas"] = available_plants["philodendron gigas"]
        elif purge_luck == 4 or purge_luck == 2:
            print("You tried, but the competition was just too fierce. You did't manage to score anything, and you lose 2 heart points.")
            heart_points = heart_points -2
            print()
            time.sleep(1)
    else:
        pass_on_deal()
def buy_adventures():
    buying_scenario = [buy_a, buy_b, buy_c, buy_d, buy_e]
    print("Here is your buying adventure:\n\n")
    random.choice(buying_scenario)()
def trade_adventures():
    global heart_points
    global money
    if len(your_plants) == 0:
        print("You have nothing to trade. Go buy something!")
    else:
        listed_plants = list_plants(your_plants)
        for number, info in listed_plants.items():
            print(f"{number} {info['name']} worth ${info['worth']}")
        print()
        your_offer = int(input("Choose a plant by number to offer for trade: "))
        print()
        print (f"You offered {listed_plants[your_offer]['name']} worth ${listed_plants[your_offer]['worth']}")
        print()
    cheap, moderate, pricey, ridiculous = sort_plants_by_worth(available_plants)
    if listed_plants[your_offer]["worth"] < 50:
        trade = random_trade(cheap)
    elif listed_plants[your_offer]["worth"] >= 50 and listed_plants[your_offer]["worth"] < 100:
        trade = random_trade(moderate)
    elif listed_plants[your_offer]["worth"] >= 100 and listed_plants[your_offer]["worth"] < 150:
        trade = random_trade(pricey)
    elif listed_plants[your_offer]["worth"] >= 150:
        trade = random_trade(ridiculous)
    print (f"Someone is offering you a/an {available_plants[trade]['name']} worth ${available_plants[trade]['worth']}")
    print()
    decision = input("[D]eal or [P]ass? > ").upper()
    print()
    if decision.startswith("D"):
        print (f"You traded your {listed_plants[your_offer]['name']} worth ${listed_plants[your_offer]['worth']}, for a {available_plants[trade]['name']} worth ${available_plants[trade]['worth']}")
        print()
        trade_luck = [1, 2, 3]
        del(your_plants[listed_plants[your_offer]["name"]])
        your_plants[trade] = available_plants[trade]
        if random.choice(trade_luck) == 1 or random.choice(trade_luck) == 2:
            print("You've added a beautiful plant to your collection and you've gained 2 heart points, because trading makes you feel good inside.")
            heart_points += 2
        elif random.choice(trade_luck) == 3:
            trade_badluck = [1, 2, 3]
            if random.choice(trade_badluck) == 1:
                print("Unlucky. The plant you received in trade had been over watered and has root rot. You have to cut the roots back and propagate it. It survives and thrives in your care, but you lose 2 heart points.")
                del(your_plants[listed_plants[your_offer]["name"]])
                heart_points -= 2
            elif random.choice(trade_badluck) == 2:
                print("Worst luck. The plant you traded for had THRIPS, and they spread to your other plants. All of the plants survived, but it cost you $100 in beneficial insects to treat your jungle, and 4 heart points, because plant pests make you sad.")
                heart_points -= 4
                money -= 100
            elif random.choice(trade_badluck) == 3:
                print("Unlucky. The plant you traded for had clearly been cut and used as a mother. You are able to grow it into a beautiful plant, but it was a lot more of a project than you bargained for, and it makes you sad. Lose 2 heart points.")
                heart_points -= 2
    elif decision.startswith("P"):
        pass_on_deal()
        print()

def sell_adventures():
    pass

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
        time.sleep(2)
        print()
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
