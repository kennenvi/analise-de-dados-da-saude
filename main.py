df_novo = df_usaveis.sample(7)
pd.concat([df_novo, df_usaveis.loc[['29 Bahia']]], axis=0)