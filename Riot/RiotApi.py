import Constants as Consts
import champion as Champions
import requests

class RiotAPI(object):

    def __init__(self, api_key, region = Consts.REGIONS['europe_west']):
        self.api_key = api_key
        self.region = region

    def _request(self, api_url, params={}):
        args = {'api_key': self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] =  value
        response = requests.get(
            Consts.URL['base'].format(
                proxy = self.region,
                region =  self.region,
                url = api_url
                ),
            params = args
            )    
        return response.json()

    def get_summoner_by_name(self, name):
        api_url = Consts.URL['summoner_by_name'].format(
            version = Consts.API_VERSIONS['summoner'],
            name = name
            )
        return self._request(api_url)

    def get_match_history(self, name):
        rankedQueues = {'rankedQueues': 'RANKED_SOLO_5x5'}
        summoner_id = self.get_summoner_by_name(name)
        api_url = Consts.URL['match_history'].format(
            version = Consts.API_VERSIONS['match_history'],
            summoner_id =  summoner_id[name]['id']
            )
        return self._request(api_url, rankedQueues)

    def get_champion_name(self, champsList):
        dataChamp =  requests.get('http://ddragon.leagueoflegends.com/cdn/5.20.1/data/en_US/champion.json')
        dataChamp = dataChamp.json() 
        lista = []
        for matches in champsList['matches']:
            aux = matches['champion']
            for champ in dataChamp['data'].items():
                if int(champ[1]['key']) == aux:
                    lista.append(champ[0])
        """for x in champsList['matches']:
            for champ in dataChamp['data']:
                pass
        """
        return lista
       
        
        """
        dataChamp = Champions.data
        print dataChamp['data']['Aatrox']['image']
        return 0
        """