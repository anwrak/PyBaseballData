import pandas as pd
from datetime import datetime as dt

class GameObj:
    def __init__(self, id, team, date, num):
        self.id = id
        self.team = team
        self.date = date
        self.num = num
        self.app = []

def position(x):

    if x == '1':
        return 'P'
    if x == '2':
        return 'C'
    if x == '3':
        return '1B'
    if x == '4':
        return '2B'
    if x == '5':
        return '3B'
    if x == '6':
        return 'SS'
    if x == '7':
        return 'LF'
    if x == '8':
        return 'CF'
    if x == '9':
        return 'RF'
    if x == '10':
        return 'DH'
    if x == '11':
        return 'PH'
    if x == '12':
        return 'PR'

   
def main():

    '''get the data file, in the future make it iterate over a list'''
    file = open('../baseball data/event/2022eve/2022ARI.EVN', 'r')

    '''instanciate the classes'''
    game = GameObj('Nothing', 'NAN', '3000-01-01', '1')
    app_df = pd.DataFrame(columns=['game_id', 'appearance_date', 'player_id', 'player_team_id', 'home_appearance', 'bat_order_position', 'fielding_positon', 'start'])

    for aline in file:
        
        #split the row into it's part
        row = aline.split(',')

        if row[0] == 'id':
            
            print('----------------------\n',game.__dict__)

            #save data to the right place
            pass

            #clean up row
            row[1] = row[1].replace('\n', '')

            #instanciate new game object
            team = row[1][:3]
            date = dt.strptime(row[1][3:7] + '-' + row[1][7:9] + '-' + row[1][9:11], '%Y-%m-%d')
            num = row[1][11:12] if int(row[1][11:12]) > 0 else 1
            game = GameObj(row[1], team, date, num)

            if game.id != row[1] and game.id != 'Nothing':
                '''some code to store the game data somewhere for the next iteration'''
                app_df = pd.DataFrame(columns=['game_id', 'appearance_date', 'player_id', 'player_team_id', 'home_appearance', 'bat_order_position', 'fielding_positon', 'start'])
                
    
        elif row[0] == 'info':
            setattr(game, row[1], row[2].replace('\n', ''))

        elif row[0] in ('start', 'sub'):

            app_game_id = game.id
            app_date = game.date
            app_player_id = row[1]
            app_player_team_id = game.hometeam if row[3] == '1' else game.visteam
            app_home_team = row[3]
            app_bat_ord = row[4]
            app_f_pos = position(row[5].replace('\n', ''))
            app_start = 1 if row[0] == 'start' else 0

            game.app.append([app_game_id, app_date, app_player_id, app_player_team_id, app_home_team, app_bat_ord, app_f_pos, app_start])

            

main()