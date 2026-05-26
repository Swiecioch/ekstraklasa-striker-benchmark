import pandas as pd
 
df_standard = pd.read_excel('standard_stats.xlsx', header=1) 
df_shooting = pd.read_excel('shooting_stats.xlsx', header=1)
 
df = pd.merge(df_standard, df_shooting[['Player','Squad', 'Sh']], on=['Player', 'Squad'], how='left')
 
df = df[df['Player'].notna()]
df = df[df['Player'] != 'Player'].copy()
 
df['Min'] = df['Min'].astype(str).str.replace('.', '', regex=False).str.replace(',', '', regex=False)
 
cols = ['Min', '90s', 'Gls', 'Ast', 'Sh']
for col in cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')
 
df_strikers = df[df['Pos'].astype(str).str.strip() == 'FW'].copy()
df_strikers = df_strikers[df_strikers['Min'] >= 500].copy()
 
df_strikers['G+A'] = df_strikers['Gls'].fillna(0) + df_strikers['Ast'].fillna(0)
df_strikers['G+A_per_90'] = (df_strikers['G+A'] / df_strikers['90s']).round(2)
 
df_strikers['Shot_conversion_rate'] = (df_strikers['Gls'] / df_strikers['Sh']) * 100
df_strikers['Shot_conversion_rate'] = df_strikers['Shot_conversion_rate'].fillna(0).round(2)
 
final_columns = ['Player', 'Squad', 'Age', 'Min', 'Gls', 'Ast', 'G+A', 'Sh', 'G+A_per_90', 'Shot_conversion_rate']
df_final_data = df_strikers[final_columns]
 
output = 'ekstraklasa_strikers.csv'
df_final_data.to_csv(output, index=False, sep=',')
 
print(f"Data for strikers with at least 500 minutes has been saved to {output}.")
 