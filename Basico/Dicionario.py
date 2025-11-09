#testando alguns metodos
meu_dicio = {'nome' : 'Sara', 'idade' : 19, 'faculdade' : 'eng comp'}
print(meu_dicio) 
print(meu_dicio.get('nome'))
print(meu_dicio.pop('idade'))
print(meu_dicio.keys())
print(meu_dicio.values())
print(meu_dicio.clear())
print(meu_dicio)

#melhorando as coisas
pessoa = {
    'nome' : 'Sara',
    'idade' : 20,
    'status' : 'viva',
    'interesses' : ['python', 'javascript', 'java'],
    'mascote' : {
        'gatas' : {
            'nome' : ['Maria', 'polly', 'Leia'],
        },
        'cachorros' : {
            'nome' : ['Tobi', 'Rosa'],
        }
    }
}
print(pessoa.get('interesses')[0])
print(pessoa.get('mascote').get('gatas').get('nome'))
pessoa['ano nascimento'] = 2006
pessoa['mae'] = {
    'nome' : 'Elizete',
    'idade' : 42
}
print(pessoa)