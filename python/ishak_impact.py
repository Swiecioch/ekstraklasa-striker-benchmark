import pandas as pd
 
df_ishak = pd.read_excel('ishak_matches.xlsx', header=2)
df_ishak = df_ishak[df_ishak['Date'].notna()]
df_ishak = df_ishak[df_ishak['Date'] != 'Date']
df_ishak['Date'] = pd.to_datetime(df_ishak['Date']).dt.date
df_ishak = df_ishak[df_ishak['Comp'] == 'Ekstraklasa'][['Date', 'Start', 'Min']]
df_ishak['Min'] = pd.to_numeric(df_ishak['Min'], errors='coerce').fillna(0)
df_ishak['Ishak_started'] = df_ishak['Start'].astype(str).str.startswith('Y')
 
df_lech = pd.read_excel('lech_fixtures.xlsx', header=1)
df_lech = df_lech[df_lech['Date'].notna()]
df_lech = df_lech[df_lech['Date'] != 'Date']
df_lech['Date'] = pd.to_datetime(df_lech['Date']).dt.date
df_lech = df_lech[df_lech['Comp'] == 'Ekstraklasa'][['Date', 'Result', 'GF', 'GA', 'Opponent', 'Venue']]
df_lech['GF'] = pd.to_numeric(df_lech['GF'], errors='coerce')
df_lech['GA'] = pd.to_numeric(df_lech['GA'], errors='coerce')
 
df = pd.merge(df_lech, df_ishak[['Date', 'Start', 'Min', 'Ishak_started']], on='Date', how='left')
df['Ishak_started'] = df['Ishak_started'].fillna(False)
df['Min'] = df['Min'].fillna(0)
 
def get_points(r):
    if r == 'W': return 3
    if r == 'D': return 1
    return 0
 
df['Points'] = df['Result'].apply(get_points)
df['Ishak_status'] = df['Ishak_started'].apply(lambda x: 'With Ishak' if x else 'Without Ishak')
 
output = 'lech_ishak_impact.csv'
df.to_csv(output, index=False)
 
print(f"Data saved to {output}.")
 