def edit_user(id:int, diccionario: dict):
    print(f"Editando {id}:")
    for key, value in diccionario.items():
        print(f"{key} : {value}")

    return 4

def make_person(name, **kwargs):
    result = name + ': '
    for key, value in kwargs.items():
        result += f'{key} = {value}, '
    return result



if __name__=="__main__":
    print(make_person('Melissa', id=12112, location='london', net_worth=12000))
    
    dic = {"prueba":"hola", "de": "hola", "sonido":"hola"}
    edit_user(4, dic)