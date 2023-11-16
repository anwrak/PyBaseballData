import pandas as pd

class GameObj:
    def __init__(self, id, team, date, num):
        self.id = id
        self.team = team
        self.date = date
        self.num = num
        

def main():

    '''get the data file, in the future make it iterate over a list'''
    file = open('../baseball data/event/2022eve/2022ARI.EVN', 'r')
    game = GameObj('Nothing', 'NAN', '3000-01-01', '1')

    for aline in file:
        
        '''split the row into it's part'''
        row = aline.split(',')

        if row[0] == 'id':

            if game.id != row[1] and game.id != 'Nothing':
                '''some code to store the game data somewhere for the next iteration'''
                print('----------------------\n',game.__dict__)
                game = None
            elif game.id == 'Nothing':
                game = None

            team = row[1][:3]
            date = row[1][3:7] + '-' + row[1][7:9] + '-' + row[1][9:11]
            num = row[1][11:12] if int(row[1][11:12]) > 0 else 1

            game = GameObj(row[1], team, date, num)
    
        elif row[0] == 'info':
            setattr(game, row[1], row[2].replace('\n', ''))
            





            

main()