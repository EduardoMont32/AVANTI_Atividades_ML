# =================================================================
# CURSO: BÁSICO EM MACHINE LEARNING
# ATIVIDADE 02 (ATIV-02) - RESOLUÇÃO DETALHADA
# Aluno: Eduardo Nogueira
# =================================================================

import pandas as pd
import numpy as np

# --- PARTE 1: ALGORITMOS EM PYTHON ---

# 1. Filtro de números ímpares
def filtrar_impares(lista):
    """
    Utiliza o operador de módulo (%). Se o resto da divisão por 2 
    for diferente de zero, o número é classificado como ímpar.
    """
    return [num for num in lista if num % 2 != 0]

# 2. Identificação de números primos
def filtrar_primos(lista):
    """
    Um número primo é divisível apenas por 1 e por ele mesmo.
    A lógica de busca vai até a raiz quadrada do número para otimizar o processamento,
    visto que se não houver divisor até a raiz, o número é primo.
    """
    def eh_primo(n):
        if n < 2: return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    return [num for num in lista if eh_primo(num)]

# 3. Diferença Simétrica entre listas
def elementos_exclusivos(lista1, lista2):
    """
    Transforma as listas em conjuntos (sets) para realizar a operação de 
    diferença simétrica (^). Retorna apenas os elementos que não são comuns às duas.
    """
    return list(set(lista1) ^ set(lista2))

# 4. Segundo maior valor da lista
def segundo_maior(lista):
    """
    Remove duplicatas com set() para garantir que, se o maior valor estiver repetido,
    o algoritmo ainda encontre o valor imediatamente abaixo dele. 
    Após ordenar, acessamos o índice -2 (penúltimo).
    """
    unicos = list(set(lista))
    if len(unicos) < 2: return None
    unicos.sort()
    return unicos[-2]

# 5. Ordenação alfabética de tuplas
def ordenar_por_nome(lista_pessoas):
    """
    Utiliza a função sorted com uma chave lambda apontando para o índice [0] 
    da tupla, garantindo a ordenação pelo campo 'Nome'.
    """
    return sorted(lista_pessoas, key=lambda pessoa: pessoa[0])


# --- PARTE 2: ANÁLISE DE DADOS COM PANDAS ---

# 6. Tratamento de Outliers (Teoria aplicada)
# Identificamos outliers usando o Intervalo Interquartil (IQR).
# O limite superior é (Q3 + 1.5 * IQR) e o inferior (Q1 - 1.5 * IQR). 
# Em telecomunicações, isso ajuda a filtrar ruídos de sensores ou picos anômalos de sinal.

# 7. Concatenar DataFrames (Dica técnica)
# O comando pd.concat() com axis=0 empilha dados verticalmente. 
# Quando as colunas divergem, o Pandas cria uma união das colunas e 
# preenche os valores faltantes com NaN (Not a Number)[cite: 53].

# 8. Leitura e Inspeção Inicial
# O método pd.read_csv() carrega os dados e o .head() exibe as 5 primeiras 
# linhas para validar se a estrutura de colunas e tipos de dados está correta[cite: 54].

# 9. Filtragem de Dados
# A filtragem é feita por indexação booleana (ex: df[df['sinal'] > -70]). 
# Isso permite isolar subconjuntos de dados que atendam a critérios específicos.

# 10. Lidar com Valores Ausentes (NaN)
# Pode-se usar df.dropna() para remover dados corrompidos ou df.fillna() 
# para imputar valores como a média da coluna, evitando a perda de amostras importantes[cite: 56].
