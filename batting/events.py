import pandas as pd

class GameObj:
    def __init__(self, id, team, date, num):
        self.id = id
        self.team = team
        self.date = date
        self.num = num


class Appearances:
    def __init__(self) -> None:
        pass       

class HomeLineup:
    def __init__(self) -> None:
        pass

class AwayLineup:
    def __init__(self) -> None:
        pass

def main():

    '''get the data file, in the future make it iterate over a list'''
    file = open('../baseball data/event/2022eve/2022ARI.EVN', 'r')

    '''instanciate the classes'''
    game = GameObj('Nothing', 'NAN', '3000-01-01', '1')
    app = []
    home = HomeLineup()
    away = AwayLineup()

    for aline in file:
        
        '''split the row into it's part'''
        row = aline.split(',')

        if row[0] == 'id':

            row[1] = row[1].replace('\n', '')

            if game.id != row[1] and game.id != 'Nothing':
                '''some code to store the game data somewhere for the next iteration'''
                print('----------------------\n',game.__dict__,app)
                game = None
            elif game.id == 'Nothing':
                game = None

            team = row[1][:3]
            date = row[1][3:7] + '-' + row[1][7:9] + '-' + row[1][9:11]
            num = row[1][11:12] if int(row[1][11:12]) > 0 else 1

            game = GameObj(row[1], team, date, num)
    
        elif row[0] == 'info':
            setattr(game, row[1], row[2].replace('\n', ''))

        elif row[0] in ('start', 'sub'):

            app_date = game.date
            app_player_id = row[1]
            app_home_team = row[3]
            app_bat_ord = row[4]
            app_f_pos = row[5].replace('\n', '')
            app_start = 1 if row[0] == 'start' else 0

            app.append([app_date, app_player_id, app_home_team, app_bat_ord, app_f_pos, app_start])
            





            

main()