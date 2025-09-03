import pandas as pd

def transform_teams(raw_json):
    return pd.json_normalize(raw_json['teams'])

def transform_standings(raw_json):

    df = pd.json_normalize(raw_json['standings'][0]['table'])

    df = df[['team.id', 'position', 'team.shortName', 'points', 'playedGames', 'won', 'draw', 'lost', 'goalsFor', 'goalsAgainst', 'goalDifference', 'team.crest']]

    df.rename(columns={
        'team.id':'id_time',
        'position':'posicao',
        'team.shortName':'nome_time',
        'points':'pontos',
        'playedGames':'PJ',
        'won':'VIT',
        'draw':'E',
        'lost':'DER',
        'goalsFor':'GM',
        'goalsAgainst':'GC',
        'goalDifference':'SG',
        'team.crest':'link_escudo'
        }, inplace=True)
    
    print('transoformação dados standings ok!')
    
    return df

def transform_mactches(raw_json):
    return pd.json_normalize(raw_json['matches'])

