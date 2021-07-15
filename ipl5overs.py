# team1={
#     {"name1":"anusha",
#     "score1":"0"},
#     {"name2":"siri",
#     "score2":"0"},
#     {"name3":"sindhu",
#     "score3":"0"},
#     {"name4":"shabu",
#     "score4":"0"},
#     {"name5":"muskan",
#     "score5":"0"},
#     {"name6":"somi",
#     "score6":"0"},
#     {"name7":"preethi",
#     "score7":"0"},
#     {"name8":"sarika",
#     "score8":"0"},
#     {"name9":"neela"
#     "score9":"0"},
#     {"name10":"namsy"
#     "score10":"0"},
#     {"name11":"saritha",
#     "score11":"0"}
# }
# # team2={
# #     {"a1":"bhavya",
# #     "score1":"0"}
# #     {}


# }
# first_team=str(input("\nenter 1st team choice:")).upper()
# firstTeam=select_team(first_team)
second_team=str(input("enter the second choice")).upper()
# secondTeam=select_team()
# #
else:
    print(f'{over}.{ball}',end="")
    start=time.time()
    input("")
    time_taken=end-start
    if time_taken<1:
        print("A sixxxxerrrr!!")
        total.append(6)
        on_strike_scores.append(6)
        player_scores=sum(on_strike_scores)
        team_total=sum(total)
        if team_total>first_scores:
            break
    elif (time_taken>1) and (time_taken<1.5):
        print("boundaryy!!!")
        total.append(4)
        on_strike_scores.append(4)
        play_scores=sum(on_strike_scores)
        team_total
