import kagglehub
import pandas as pd

path = kagglehub.dataset_download("mathchi/diabetes-data-set")

print("Path to dataset files:", path)

df = pd.read_csv(path + "/diabetes.csv")

print(df.shape) #(768, 9)

