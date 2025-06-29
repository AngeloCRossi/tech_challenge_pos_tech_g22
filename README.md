# tech_challenge_pos_tech_g22

- link da base de dados: https://www.kaggle.com/datasets/mathchi/diabetes-data-set/data

- Tiraremos o campo 'Outcome', para poder treinar.
- o DS tem 768 linhas e 9 colunas, onde são:

     0   Pregnancies               768 non-null    int64
     1   Glucose                   768 non-null    int64
     2   BloodPressure             768 non-null    int64
     3   SkinThickness             768 non-null    int64
     4   Insulin                   768 non-null    int64
     5   BMI                       768 non-null    float64
     6   DiabetesPedigreeFunction  768 non-null    float64
     7   Age                       768 non-null    int64
     8   Outcome                   768 non-null    int64

    Number of times pregnant
    Plasma glucose concentration a 2 hours in an oral glucose tolerance test
    Diastolic blood pressure (mm Hg)
    Triceps skin fold thickness (mm)
    2-Hour serum insulin (mu U/ml)
    Body mass index (weight in kg/(height in m)^2)
    Diabetes pedigree function
    Age (years)
    Class variable (0 or 1)

- Todas as pessoas são mulheres indígena(Pina), maiores de 21 anos.
- Faremos gráficos com cada coluna relacionando em ter ou não diabetes, faremos analise e discutiremos posteriormente.
- Removeremos linhas inteiras onde houver dado como 'null'
- Buscaremos tipos distintos dos dados.
- Não tem variavel categórica. Já temos o dado como 0 e 1
- Análise de correlação, conforme aula e modelo que o Groff mandou no grupo de discord (https://www.kaggle.com/code/ohseokkim/diabetes-three-ensemble-models/notebook#Checking-features-before-modeling)
- Modelos preditivos Regressão logística, Árvore de Decisão, KNN
- Separação clara entre treino, validação e teste.

- 85% dos dados para treino e 15% para teste
- Interpretação dos resultados à decidir
-Discuta os resultados de maneira crítica. O seu modelo pode ser utilizado na prática? Como?  Falaremos que sim, se houvesse mais dados para testar, e que se fosse o caso haveria uma interface, como um chatbot.
