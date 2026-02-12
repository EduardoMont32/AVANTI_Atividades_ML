# Curso: Básico em Machine Learning
## Atividade 01 (ATIV-01) - Diagnóstica

**Aluno:** Eduardo Nogueira  
**Instituição:** Atlântico Avanti  
**Tema:** Conceitos básicos de Machine Learning  

---

### 1. O que é Machine Learning?
Machine Learning é um campo da inteligência artificial focado no desenvolvimento de algoritmos que permitem aos computadores aprender padrões a partir de dados. Em vez de seguir instruções estáticas, o modelo melhora seu desempenho à medida que é exposto a mais informações.
* **Exemplo:** Sistemas de recomendação (como Netflix ou Spotify) que aprendem seus gostos musicais e sugerem novos conteúdos com base no que você ouviu anteriormente.

### 2. Conjunto de Treinamento, Validação e Teste
Para garantir que um modelo funcione bem, os dados são divididos em:
* **Treinamento:** Dados usados para "ensinar" o modelo a identificar padrões.
* **Validação:** Conjunto usado para ajustar parâmetros e evitar o *overfitting* (quando o modelo decora o treino mas não generaliza).
* **Teste:** Dados que o modelo nunca viu, usados para medir a eficácia real antes de colocá-lo em produção.

### 3. Como lidar com dados ausentes?
Existem diversas estratégias dependendo do contexto:
* **Exclusão:** Remover registros que possuam dados faltantes (útil se a perda for pequena).
* **Imputação:** Substituir os valores ausentes por medidas estatísticas como a média, mediana ou moda da coluna.
* **Modelagem:** Usar algoritmos de regressão para prever e preencher o valor que deveria estar ali.

### 4. O que é uma Matriz de Confusão?
É uma ferramenta de visualização para modelos de classificação. Ela mostra a contagem de acertos e erros cruzando o que o modelo previu com o resultado real.
* **Utilidade:** Permite identificar se o modelo está confundindo uma classe específica com outra, ajudando a calcular métricas como Precisão e Revocação (Recall).

### 5. Áreas de aplicação interessantes
A aplicação de Machine Learning é vasta, mas vejo grande potencial em áreas que lidam com grandes volumes de dados em tempo real:

* **Telecomunicações (Exemplo Prático):** Utilização de modelos para **Alocação Dinâmica de Recursos** e **Manutenção Preditiva de Redes**. Algoritmos podem analisar o tráfego em tempo real para prever congestionamentos em células de rede (estilo 5G) e redistribuir a carga automaticamente, garantindo a Qualidade de Serviço (QoS) sem intervenção humana constante.
* **Saúde:** Diagnóstico auxiliado por computador, onde modelos de visão computacional analisam exames de imagem para detectar anomalias com precisão milimétrica.
* **Manufatura:** Implementação de sensores em linhas de produção que, através de Machine Learning, identificam padrões de vibração ou calor que antecedem falhas mecânicas, permitindo o conserto antes da parada total.
