# Projeto de Previsão de Diabetes

## Descrição do Projeto

Este projeto tem como objetivo principal desenvolver e avaliar modelos de Machine Learning para prever o diagnóstico de diabetes com base em dados de medições diagnósticas. O trabalho foca na identificação do modelo mais eficaz e robusto, capaz de atuar como uma ferramenta de apoio para a triagem e o diagnóstico precoce da doença, sem substituir a avaliação médica profissional.


## Preparando o ambiente

- Clone o projeto para sua máquina


    >git clone https://github.com/AngeloCRossi/tech_challenge_pos_tech_g22
    
    >cd tech_challenge_pos_tech_g22

- Crie e ative o ambiente virtual Python

    Instalação
    >python -m pip install --user virtualenv

    Criação
    >virtualenv venv

    Ativação Linux
    >source venv/bin/activate

    Ativação Windows
    >venv\Scripts\activate


- Instale as depedências

    >pip install -r requirements.txt



## Conjunto de Dados

O conjunto de dados, originalmente do *National Institute of Diabetes and Digestive and Kidney Diseases (NIDDK)*, inclui informações de pacientes do sexo feminino, com pelo menos 21 anos de idade e de herança Pima-indígena. As colunas de dados incluem:

| Nome da Coluna             | Tipo de Dado | Descrição                                  |
| -------------------------- | ------------ | ------------------------------------------ |
| `gravidez`                 | `int64`      | Número de gestações.                       |
| `glicose`                  | `int64`      | Concentração de glicose no plasma.         |
| `pressao_arterial`         | `int64`      | Pressão arterial diastólica (mm Hg).       |
| `espessura_pele`           | `int64`      | Espessura da dobra da pele do tríceps (mm).|
| `insulina`                 | `int64`      | Insulina sérica de 2 horas (mu U/ml).      |
| `imc`                      | `float64`    | Índice de Massa Corporal (peso em kg/(altura em m)^2).|
| `historico_familiar_diabetes` | `float64`    | Função de histórico familiar de diabetes.  |
| `idade`                    | `int64`      | Idade em anos.                             |
| `diagnostico`              | `int64`      | Variável de saída (0 = não diabético, 1 = diabético). |

## Metodologia

A metodologia do projeto seguiu um pipeline estruturado para garantir a confiabilidade dos resultados:

1.  **Pré-processamento de Dados**: As colunas foram traduzidas para português e valores inválidos (representados por zero) nas features de `glicose`, `pressao_arterial`, `espessura_pele`, `insulina` e `imc` foram substituídos pela mediana da respectiva coluna para evitar distorções.
2.  **Balanceamento de Classes**: A técnica **SMOTE (Synthetic Minority Over-sampling Technique)** foi utilizada para lidar com o desequilíbrio entre as classes de diagnóstico, criando amostras sintéticas da classe minoritária.
3.  **Avaliação de Múltiplos Modelos**: Foram comparados seis algoritmos de classificação: `KNN`, `Regressão Logística`, `Decision Tree`, `Random Forest`, `SVM (RBF Kernel)` e `Naive Bayes`.
4.  **Otimização de Modelos**:
    * **Ajuste de Hiperparâmetros**: `GridSearchCV` foi aplicado para encontrar a melhor combinação de parâmetros para cada modelo.
    * **Ajuste de Limiar (`Threshold`)**: `TunedThresholdClassifierCV` foi utilizado para otimizar o ponto de corte de classificação, maximizando o `F1-Score` de forma robusta com validação cruzada.
5.  **Validação Cruzada**: A técnica de `StratifiedKFold` (5 folds) foi empregada para avaliar o desempenho dos modelos em diferentes subconjuntos de dados, garantindo que os resultados fossem representativos e não viesados.
