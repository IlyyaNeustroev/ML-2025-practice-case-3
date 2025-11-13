import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# Загрузка тренировочных данных с целевой переменной
train_df = pd.read_csv('C:\\Users\\NeustroevIL\\Documents\\проекты\\ML-2025-practice-case-3\\DA\\PythonProject8\\train_01.csv')

# Разделение признаков и целевой переменной
X_train = train_df.drop(columns=['FloodProbability'])
y_train = train_df['FloodProbability']

# Загрузка тестовых данных (без столбца FloodProbability)
test_df = pd.read_csv('C:\\Users\\NeustroevIL\\Documents\\проекты\\ML-2025-practice-case-3\\DA\\PythonProject8\\test.csv')

# Проверка, что тестовый набор содержит те же признаки
assert all(X_train.columns == test_df.columns), "Столбцы теста и обучения не совпадают"

# Стандартизация признаков (fit на тренировочных, transform на обоих)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(test_df)

# Обучение модели линейной регрессии
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Предсказание на тестовых данных
y_test_pred = model.predict(X_test_scaled)

# Вывод результатов
print("Предсказания вероятности затопления на тестовых данных:")
print(y_test_pred)