import csv
from nba_game_regex import find_data 

def load_data(data):
    with open(data, 'r') as data:
        csv_reader = csv.reader(data, delimiter='|')
        return [row for row in csv_reader] 

players_data = []

def analyse_nba_game(play_by_play_moves):
    for row in play_by_play_moves:
        if len(find_data(row[-1])) > 0:
            for movement in find_data(row[-1]):
                player_name = movement[0][1]
                point_field = movement[1]
                if player_name not in [i["player_name"] for i in players_data]:
                    players_data.append(
                        { "player_name" : player_name, "FG" : 0, "FGA" : 0, "FG%" : 0, "3P" : 0, "3PA" : 0, "3P%" : 0, "FT" : 0, 
                          "FTA" : 0, "FT%" : 0, "ORB" : 0, "DRB" : 0, "TRB" : 0, "AST" : 0, "STL" : 0, "BLK" : 0, "TOV" : 0,
                          "PF" : 0, "PTS" : 0})
                index = [players_data.index(i) for i in players_data if i["player_name"] == player_name][0]
                players_data[index][point_field] += 1
                if point_field not in ("STL", "BLK", "PF"): players_data[index]["is_home_team"] = row[2] == row[4]
                else: players_data[index]["is_home_team"] = row[2] != row[4]


def calculate(players_data):
    for players in players_data:
        players["3PA"] += players["3P"]
        players["FGA"] += players["FG"]
        players["FGA"] += players["3PA"]
        players["FG"] += players["3P"]
        players["FTA"] += players["FT"]
        players["TRB"] = players["ORB"] + players["DRB"]
        players["FG%"] = "{:.3f}".format(round(players["FG"] / players["FGA"], 3)) if players["FGA"] != 0 else 0
        players["FT%"] = "{:.3f}".format(round(players["FT"] / players["FTA"], 3)) if players["FTA"] != 0 else 0
        players["3P%"] = "{:.3f}".format(round(players["3P"] / players["3PA"], 3)) if players["3PA"] != 0 else 0
        players["PTS"] = 2 * (players["FG"] - players["3P"]) + 3 * players["3P"] + players["FT"]


def print_nba_game_stats(team_dict):   
    for team in team_dict.items():
        fg, fga, fgp, p3, p3a, p3p, ft, fta, ftp, orb, drb, trb, ast, stl, blk, tov, pf, pts = 0, 0, 0.0, 0, 0, 0.0, 0, 0, 0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0
        print(f'{"Players name":<17}|{"FG":<5}|{"FGA":<5}|{"FG%":<6}|{"3P":<5}|{"3PA":<5}|{"3P%":<6}|{"FT":<5}|{"FTA":<5}|{"FT%":<6}|{"ORB":<5}|{"DRB":<5}|{"TRB":<5}|{"AST":<5}|{"STL":<5}|{"BLK":<5}|{"TOV":<5}|{"PF":<5}|{"PTS":<5}')      
        for player in team[1]["players_data"]:
            print(f'{player["player_name"]:<17}|{player["FG"]:<5}|{player["FGA"]:<5}|{player["FG%"]:<6}|{player["3P"]:<5}|{player["3PA"]:<5}|{player["3P%"]:<6}|{player["FT"]:<5}|{player["FTA"]:<5}|{player["FT%"]:<6}|{player["ORB"]:<5}|{player["DRB"]:<5}|{player["TRB"]:<5}|{player["AST"]:<5}|{player["STL"]:<5}|{player["BLK"]:<5}|{player["TOV"]:<5}|{player["PF"]:<5}|{player["PTS"]:<5}')
            fg += player["FG"]
            fga += player["FGA"];           p3 += player["3P"]
            p3a += player["3PA"];            ft += player["FT"]
            fta += player["FTA"];           orb += player["ORB"]
            drb += player["DRB"];            ast += player["AST"]
            stl += player["STL"];            blk += player["BLK"]
            tov += player["TOV"];            pf += player["PF"]
            pts += player["PTS"];       
            fgp = player["FG%"]
            p3p = player["3P%"]       
            ftp = player["FT%"]
            trb = player["TRB"]      
        print(f'{"Team totals":<17}|{fg:<5}|{fga:<5}|{fgp:<6}|{p3:<5}|{p3a:<5}|{p3p:<6}|{ft:<5}|{fta:<5}|{ftp:<6}|{orb:<4} |{drb:<5}|{trb:<5}|{ast:<5}|{stl:<5}|{blk:<5}|{tov:<5}|{pf:<5}|{pts:<5}\n\n')


def main():
    analyse_nba_game(load_data("nba_game_warriors_thunder_20181016.txt"))
    calculate(players_data)
    away_team = load_data("nba_game_warriors_thunder_20181016.txt")[0][3]
    home_team = load_data("nba_game_warriors_thunder_20181016.txt")[0][4]
    result = {"home_team" : {"name" : home_team, "players_data" : []}, "away_team" : {"name" : away_team, "players_data" : []}}
    for i in players_data:
        if i["is_home_team"]:
            result["home_team"]["players_data"].append(i)
        else:
            result["away_team"]["players_data"].append(i)
    print_nba_game_stats(result)


if __name__ == "__main__":
    main()
