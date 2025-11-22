'''Назначение файлов
train.csv — обучающий набор данных с множеством факторов (признаков) и целевой переменной FloodProbability (вероятность затопления).
Используется для построения и обучения модели. Каждая строка — наблюдение с разными факторами.
test.csv — тестовый набор с теми же факторами, но без значения FloodProbability. По этим данным нужно сделать прогнозы с помощью обученной модели.
sample_submission.csv — пример формата для отправки результатов (submission), содержит id строк из test.csv и колонки FloodProbability,
которые нужно заполнить прогнозами из модели.

Описание столбцов train и test
Каждый столбец — фактор, влияющий на вероятность затопления:

id — уникальный идентификатор записи

MonsoonIntensity — интенсивность муссонных дождей

TopographyDrainage — особенности рельефа и водоотведения

RiverManagement — управление реками

Deforestation — вырубка лесов

Urbanization — уровень урбанизации

ClimateChange — влияние изменения климата

DamsQuality — качество плотин

Siltation — зарастание осадками

AgriculturalPractices — сельскохозяйственные практики

Encroachments — захват территорий

IneffectiveDisasterPreparedness — неэффективность подготовки к ЧС

DrainageSystems — состояние дренажных систем

CoastalVulnerability — уязвимость прибрежных зон

Landslides — оползни

Watersheds — состояние водосборных бассейнов

DeterioratingInfrastructure — ухудшение инфраструктуры

PopulationScore — показатели населения (плотность, рост)

WetlandLoss — потеря водно-болотных угодий

InadequatePlanning — недостаточное планирование территорий

PoliticalFactors — политические факторы

FloodProbability — целевая переменная (только в train.csv), вероятность затопления'''
import os
dir_path = os.path.dirname(os.path.abspath(__file__))