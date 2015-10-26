from RiotApi import RiotAPI

def main():
    api = RiotAPI('93d33598-7d65-444e-8daa-788818f097a1')
    name = raw_input("Inserte un nombre:")
    r = api.get_summoner_by_name(name)
    m = api.get_match_history(name)
    print r[name]['id']
    #for matches in m['matches']:
    #   print matches['champion']
    c = api.get_champion_name(m)    
    print c[:5]
    
if __name__ == '__main__':
    main()
