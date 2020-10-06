import functools

def removeUnuseless(arr):
    # Remove null or zero elements. Note than filter require to be saved on list initializtion
    # Challenge of Hola Mundo Channel on https://www.youtube.com/watch?v=MXmQM_Uehtk&t=584s
    lista = list(filter(lambda x: x ,arr))
    return lista

if __name__ == "__main__":
    print(removeUnuseless([5,3,66,False,76,None,45,0,False,0]))