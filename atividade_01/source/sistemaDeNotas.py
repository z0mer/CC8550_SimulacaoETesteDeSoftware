def validar_nota(nota):
    return 0 <= nota <= 10

def calcular_media(notas):
    if not notas:
        raise ValueError("Lista de notas vazia")
    
    notas_validas = [nota for nota in notas if validar_nota(nota)]
    
    if not notas_validas:
        raise ValueError("Nenhuma nota valida")
    
    return sum(notas_validas) / len(notas_validas)

def obter_situacao(media):    
    if not validar_nota(media):
        raise ValueError("Media invalida")
    
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperacao"
    else:
        return "Reprovado"

def calcular_estatisticas(notas):    
    if not notas:
        raise ValueError("Lista de notas vazia")
    
    notas_validas = [nota for nota in notas if validar_nota(nota)]
    
    if not notas_validas:
        raise ValueError("Nenhuma nota valida")
    
    media = sum(notas_validas) / len(notas_validas)
    maior = max(notas_validas)
    menor = min(notas_validas)
    
    aprovados = sum(1 for nota in notas_validas if nota >= 7.0)
    recuperacao = sum(1 for nota in notas_validas if 5.0 <= nota < 7.0)
    reprovados = sum(1 for nota in notas_validas if nota < 5.0)
    
    return {
        "media": media,
        "maior": maior,
        "menor": menor,
        "aprovados": aprovados,
        "reprovados": reprovados,
        "recuperacao": recuperacao
    }

def normalizar_notas(notas, nota_maxima=10):
    if not notas:
        raise ValueError("Lista de notas vazia")
    
    if nota_maxima <= 0:
        raise ValueError("Nota maxima deve ser positiva")
    
    return [(nota / nota_maxima) * 10 for nota in notas]