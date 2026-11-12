import pandas as pd


def f(age):
    if pd.isna(age):
        return None
    elif age < 18:
        return '18-'
    elif age <= 60:
        return '18-60'
    else:
        return '60+'


df = pd.read_csv("http://python.mipt.ru/lpr/extra/lab09/Titanic.csv")
df['Age group'] = df['Age'].apply(f)
df = df[df['Age group'].notna()]
answer = (df.groupby('Age group').agg({'Survived': 'mean'}))
answer2 = df.groupby(['Pclass']).agg({'Age':'mean'})
print(answer)


