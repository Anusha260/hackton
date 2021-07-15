import random
import time
#import randomchoice 
Atotal=[]
Btotal=[]
balls=["---------"]
out=["run out","catch out"]
print("choose teams\n")
teams={'team1':["a","b","c","d","e","f","g","h","k","l","m"],'team2':["anushu","shabbu","laddu","mahiks","manu","siri","janu","chinni","chinna","pavani"]}
keys=teams.keys
for keys in teams:
    print(keys)
def select_team(team):
    if team in teams:
        selected_team=team
        return selected_team
    else:
        selected_team=str(input("enter name"))
        return selected_team
first_team=str(input("\nenter 1st team choice:"))
firstTeam=select_team(first_team)
second_team=str(input("enter the second choice"))
secondTeam=select_team()
if secondTeam==firstTeam:
    print("this team is already choice by your ")
    secondTeam=str(input("..."))
    select_team(secondTeam)
else:
    pass
print("firstTeam")
print("secondTeam") 
players=[firstTeam,secondTeam]
print("start")
print("firstTeam")
# print("toss")
tosscall=["------"]
batball=["------"]
toss=input("enter what u want")
while toss:
    if toss in tosscall:
        print(toss)
        #randomshuffle(tosscall)
        print(tosscall)
        break
    else:
        print("-----")
        toss=input("----")
        continue
def tosstime(team_a,team_b):
    print(team_a)
    call=input("-----")
    try:
        if call not in toss:
            print("----")
            call=input("---")
    finally:
        print(team_a,call)
        if call=="bat":
            bating_team,bowling_team=teams[team_a],teams[team_b]
        elif call=="bowl":
            bating_team,bowling_team=teams[team_b],teams[team_a]
            return bating_team,bowling_team
def innings(bating_team,bowling_team,first_score):
    bating_team_list=teams[bating_team]
    bating_option=iter(bating_team_list)  
    on_strike=next(bating_option) 
    on_strike_scores=[]
    players_scores=[]
    wickets=10
    total=[]
    team_total=0
    bowling_options=teams[bowling_team][5:]
    for over in range(0,3):
        bowler=(bowling_options)
        print(on_strike,bowler)
        print("any key to respond")
    for ball in range(1,7):
        ball_delivered=(balls)
        played_for=(balls)
        if wickets==0 or bowler>first_score:
            break
        elif ball_delivered==played_for:
            print(over,ball)
            print(bowler,on_strike)
            player_scores=sum(on_strike_scores)
            team_total=sum(total)
            out_player_scores={on_strike:players_scores}
            #print(f'{batting_team} is at {team_team1}')
            print(f"batting_team is at team_team1")
            print(out_player_scores)
            on_strik=next
            print(f'{on_strike} is on_strike')
            wickets-=1
            on_strike_scores=[0]
            time.sleep(2)

        else:
            print(f'{over}.{ball}',end="")
            start=time.time()
            input("")
            time_taken="end"-start
            first_scores=0
            if time_taken<1:
                print("A sixxxxerrrr!!")
                total.append(6)
                on_strike_scores.append(6)
                player_scores=sum(on_strike_scores)
                team_total=sum(total)
                if team_total>=first_scores:
                    break
            elif (time_taken>1) and (time_taken<1.5):
                print("boundaryy!!!")
                total.append(4)
                on_strike_scores.append(4)
                player_scores=sum(on_strike_scores)
                team_total=sum(total)
                if team_total>=first_scores:
                    break
            elif (time_taken>2) and (time_taken<2.5):
                print("boundaryy!!!")
                total.append(2)
                on_strike_scores.append(2)
                player_scores=sum(on_strike_scores)
                team_total=team_total