from RiotApi import RiotAPI

def main():
    api = RiotAPI('93d33598-7d65-444e-8daa-788818f097a1')
    r = api.get_summoner_by_name('abosch')
    m = api.get_match_history('abosch')
    print r['abosch']['id']
    #for matches in m['matches']:
    #   print matches['champion']
    api.get_champion_name()
    
if __name__ == '__main__':
    main()
