'''import json, requests
class Sorteio:
    def __init__(self, args):
        self.concurso = int(args["sorteio"])
        #self.name = u' '.join((agent_contact, agent_telno)).encode('utf-8').strip()
        #self.data = str(args["nome"].encode('utf-8'))
        #self.nick = str(args["abreviacao"])
        #self.position = int(args["posicao"] if "posicao" in args else -1)

response = requests.get("https://www.lotodicas.com.br/api/lotomania")
teams = json.loads(response.content)
#print teams.values()
teams = teams.values()
teams = [Sorteio(team) for team in teams]
teams_dict = {}
#print teams.values()
for team in teams:
	print team
	#teams_dict[team.numero] = team
'''