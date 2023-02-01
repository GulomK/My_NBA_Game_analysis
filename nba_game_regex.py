import re

def find_data(current_action):
    three_point = (re.compile(r'([\S]. [\S]*) makes 3-pt jump shot from').search(current_action),"3P")
    two_point = (re.compile(r'([\S]. [\S]*) makes 2-pt jump shot from').search(current_action),"FG")
    layup = (re.compile(r'([\S]. [\S]*) makes 2-pt layup').search(current_action),"FG")
    dunk = (re.compile(r'([\S]. [\S]*) makes 2-pt dunk').search(current_action), "FG")
    three_point_missed = (re.compile(r'([\S]. [\S]*) misses 3-pt jump shot from').search(current_action),"3PA")
    two_point_missed = (re.compile(r'([\S]. [\S]*) misses 2-pt jump shot from').search(current_action),"FGA")
    layup_missed = (re.compile(r'([\S]. [\S]*) misses 2-pt layup').search(current_action),"FGA")
    offensive_rebounds = (re.compile(r' Offensive rebound by ([\S]. [\S]*[^) ])').search(current_action),"ORB")
    defensive_rebounds = (re.compile(r'Defensive rebound by ([\S]+\. [\S]*)').search(current_action),"DRB")
    free_throw = (re.compile(r'([\S]. [\S]*) makes free throw (.*) of (.*)').search(current_action),"FT")
    clear_path_free_throw = (re.compile(r'([\S]. [\S]*) makes clear path free throw (.*) of (.*)').search(current_action),"FT")
    free_throw_missed = (re.compile(r'([\S]. [\S]*) misses free throw (.*) of (.*)').search(current_action),"FTA")
    hook_shot = (re.compile(r'([\S]. [\S]*) makes 2-pt hook shot').search(current_action), "FG")
    hook_shot_missed = (re.compile(r'([\S]. [\S]*) misses 2-pt hook shot').search(current_action),"FGA")
    turnover = (re.compile(r'Turnover by ([\S]. [\S]*[^) ])').search(current_action), "TOV")
    assists = (re.compile(r'assist by ([\S]. [\S]*[^) ])').search(current_action), "AST")
    stolen = (re.compile(r'steal by ([\S]. [\S]*[^) ])').search(current_action), "STL")
    block = (re.compile(r'block by ([\S]. [\S]*)[^) ]').search(current_action), "BLK")
    personal_f = (re.compile(r'Personal foul by ([\S]+\. [\S]*[^) ])').search(current_action), "PF")
    shooting_f = (re.compile(r'Shooting foul by ([\S]+\. [\S]*[^) ])').search(current_action), "PF")
    offensive_f = (re.compile(r'Offensive foul by ([\S]. [\S]*[^) ])').search(current_action), "PF")
    clear_path_f = (re.compile(r'Clear path foul by ([\S]. [\S]*[^) ])').search(current_action), "PF")
    lose_ball_f = (re.compile(r'Louse ball foul by ([\S]. [\S]*[^) ])').search(current_action), "PF")

    re_data = (three_point, two_point, layup, dunk, three_point_missed, two_point_missed, layup_missed, offensive_rebounds, defensive_rebounds, free_throw, clear_path_free_throw, 
               free_throw_missed, hook_shot, hook_shot_missed, turnover, assists, stolen, block, personal_f, shooting_f, offensive_f, clear_path_f, lose_ball_f)
     
    return [a for a in re_data if a[0] is not None]
