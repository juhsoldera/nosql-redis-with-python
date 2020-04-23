import redis

#IMPORTANTE: Startar o docker com a imagem do Redis antes de rodar. Recomendado: redis:3.2.5-alpine
#Sistema de votação: key: eleitor, value: candidato em que votou

r = redis.StrictRedis(host='localhost', port=6379, decode_responses=True, db=0)

r.set('A', 'candidato1')
r.set('B', 'candidato1')
r.set('C', 'candidato2')
r.set('D', 'candidato1')
r.set('E', 'candidato2')
r.set('F', 'candidato2')
r.set('G', 'candidato1')
r.set('H', 'candidato1')
r.set('I', 'candidato1')

value= r.get('C')
print(value)
value = r.get('A')
print(value)

#To-do: verificar se é possível utilizar listas
#To-do: verificar casos de uso mais complexos

