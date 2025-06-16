TABLE = "Team                           | MP |  W |  D |  L |  P"
WIN_POINTS = 3
DRAW_POINTS = 1
LOSS_POINTS = 0

def tally(rows):
    
    tournament_result = dict()

    for row in rows:
        splited_row = row.split(";")
        
        if splited_row[2] == 'win':
            tournament_result = add_win(tournament_result, splited_row[0])
            tournament_result = add_loss(tournament_result, splited_row[1])

        elif splited_row[2] == "draw":
            tournament_result = add_draw(tournament_result, splited_row[1])
            tournament_result = add_draw(tournament_result, splited_row[0])

        elif splited_row[2] == "loss":
            tournament_result = add_win(tournament_result, splited_row[1])
            tournament_result = add_loss(tournament_result, splited_row[0])

        else:
            raise ValueError(f'Wrong result: {splited_row[2]}. Must be "win", "draw" or "loss"')
        
    return _get_tournament_table(tournament_result)
        
def add_win(tournament_result: dict, team: str):

    if team not in tournament_result.keys():
        tournament_result[team] = [1, 1, 0, 0, WIN_POINTS]
    else:
        tournament_result[team][0] += 1
        tournament_result[team][1] += 1
        tournament_result[team][4] += WIN_POINTS

    return tournament_result

def add_draw(tournament_result: dict, team: str):

    if team not in tournament_result.keys():
        tournament_result[team] = [1, 0, 1, 0, DRAW_POINTS]
    else:
        tournament_result[team][0] += 1
        tournament_result[team][2] += 1
        tournament_result[team][4] += DRAW_POINTS

    return tournament_result


def add_loss(tournament_result: dict, team: str):

    if team not in tournament_result.keys():
        tournament_result[team] = [1, 0, 0, 1, LOSS_POINTS]
    else:
        tournament_result[team][0] += 1
        tournament_result[team][3] += 1
        tournament_result[team][4] += LOSS_POINTS

    return tournament_result
from operator import itemgetter, attrgetter
def _get_tournament_table(tournament_result):

    result_table = []

    for team in tournament_result:
        matches_played = tournament_result[team][0]
        wins = tournament_result[team][1]
        draws = tournament_result[team][2]
        losses = tournament_result[team][3]
        points = tournament_result[team][4]
        result_table.append([team, matches_played, wins, draws, losses, points])

    result_table.sort(key=itemgetter(0))
    result_table.sort(key=itemgetter(5), reverse=True)

    printed_table = []

    for team in result_table:
        team_name = team[0]
        matches_played = team[1]
        wins = team[2]
        draws = team[3]
        losses = team[4]
        points = team[5]
        team_row = "{:<30} |  {:<1} |  {:<1} |  {:<1} |  {:<1} | {:2}".format(team_name,  matches_played, wins, draws, losses, points)
        printed_table.append(team_row)
    

    printed_table.insert(0, TABLE)

    return printed_table