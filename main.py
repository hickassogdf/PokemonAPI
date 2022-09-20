import requests 

def PokeAPI():
  
  poke_name = input('Digite o nome do pokemon: ')

  request = requests.get('https://pokeapi.co/api/v2/pokemon/{}' .format(poke_name)) 
  adress_data = request.json() 

  request_evolution = requests.get('https://pokeapi.co/api/v2/pokemon-species/{}' .format(poke_name))
  adress_data2 = request_evolution.json() 
  
  
  
  print("\n")
  print("Abilitys of {}  : " "\n" .format(poke_name))
  abilities(adress_data)
  print("\n" "Types of {}  : " "\n".format(poke_name))
  type(adress_data)
  evolution(adress_data2)


   
def abilities(adress_data):
  
  for i in adress_data['abilities']:
    print(i['ability']['name'])
  
  
def type(adress_data):
  for j in adress_data['types']:
    print(j['type']['name'])

def evolution(adress_data2):
  url_evolution = (adress_data2['evolution_chain']['url'])
  request_chain = requests.get('{}' .format(url_evolution))
  adress_evolution = request_chain.json()
  print("\nEvolve from :")
  pokemon_ev = print(adress_evolution['chain']['species']['name']) 
  print("\nTo: ")
  pokemon_to = print(adress_evolution['chain']['evolves_to'][0]['species']['name'])
  
 
   
  
    
  

if __name__ == '__main__':
  PokeAPI()
  