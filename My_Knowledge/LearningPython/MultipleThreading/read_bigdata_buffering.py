import pandas as pd

drinks = pd.read_csv('http://bit.ly/drinksbycountry')

drinks.head()

drinks.info() # get more detail from dataframe

drinks.info(memory_usage='deep') # memory usage
print('----------Memory usage: ', drinks.memory_usage(deep=True))
print('----------Sum memory usage: ', drinks.memory_usage(deep=True).sum())
print('Sorted: ', sorted(drinks.continent.unique()))

drinks['continent'] = drinks.continent.astype('category')
drinks.dtypes

drinks.continent.head()

drinks.continent.cat.codes.head()

drinks['country'] = drinks.country.astype('category')
drinks.country.cat.categories

df = pd.DataFrame({'ID': [100, 101, 102, 103], 'quality': ['bad', 'good', 'very good','excellent']})
df.sort_values('quality')

df['quality'] = df.quality.astype('category', categories=['good', 'very good', 'excellent'], ordered=True)
df.loc[df.quality > 'good', :]
