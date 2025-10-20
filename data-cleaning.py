import pandas as pd


df = pd.read_csv("customer_personality_analysis.csv")


print(df.info())
print(df.head())


print(df.isnull().sum())

df = df.dropna()

# df["Income"] = df["Income"].fillna(df["Income"].median())


df = df.drop_duplicates()


df["Education"] = df["Education"].str.strip().str.lower()
df["Marital_Status"] = df["Marital_Status"].str.strip().str.title()


df["Dt_Customer"] = pd.to_datetime(df["Dt_Customer"], errors='coerce')


df.columns = df.columns.str.lower().str.replace(" ", "_")

df["income"] = df["income"].astype(int)
df["year_birth"] = df["year_birth"].astype(int)


df.to_csv("cleaned_customer_personality.csv", index=False)

print("✅ Data cleaning done! Cleaned file saved.")
