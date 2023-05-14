import os 
import pandas as pd 
import numpy
from numpy import genfromtxt

wikidata_entities = ["97570923","974144","96","87866152","85000195","846570","8333","83267","82955","817393","8148","806798","7748","76793","766866","76074","7314586","7188","65087482","6279","6266","610018","58968","5043","47913","467","462","458","455011","43229","428148","420474","41171","40231","3918","37230","3624078","3612401","340169","3365273","331483","317","309","3089570","30","2979","29552","29468","289891","28136847","241588","2386606","2368859","23505","22687","22686","2167348","2151621","207","192797","192692","180774","18028810","178790","167037","1658150","164597","160381","159810","1553390","15228","1464994","1403016","133346","12908","12377291","1211427","11698","11696","1124","11231","11042","11033","110315740","105764136","1057263","102232426","926348"]
wikidata_entities = [int(entity) for entity in wikidata_entities] 

statements_df = pd.DataFrame(columns=['source_item_id', 'edge_property_id', 'target_item_id'])
for filename in os.listdir("statements"):
    f = os.path.join("statements", filename)
    # checking if it is a file
    print(f)
    if os.path.isfile(f):
        my_data = genfromtxt(f, delimiter=',')
        df = pd.DataFrame(my_data, columns=['source_item_id', 'edge_property_id', 'target_item_id']).dropna()

        for col in df.columns:
            df[col] = df[col].astype(int)
            print(df[col])    
        df = df.where(df['source_item_id'].isin(wikidata_entities) | df['target_item_id'].isin(wikidata_entities)).dropna()
        print(df.head(100))
        statements_df = statements_df.append(df)
statements_df.to_csv("statements-entities.csv")   




statements_df = pd.read_csv("statements-entities.csv")[['source_item_id', 'edge_property_id', 'target_item_id']]
statements_df['source_item_id'] = statements_df['target_item_id'].astype(int) 
items_df = pd.DataFrame(columns=['item_id', 'en_alias', 'en_description'])
for filename in os.listdir("items-csv-split"):
    f = os.path.join("items-csv-split", filename)
    # checking if it is a file
    print(f)
    if os.path.isfile(f):
        df = pd.read_csv(f)
        df = df.where(df['item_id'] != "item_id").dropna()
        df['item_id'] = df['item_id'].astype(int) 
        df = df.where(df['item_id'].isin(statements_df['source_item_id']) | df['item_id'].isin(statements_df['target_item_id'])).dropna()
        print(df.head(100))
        items_df = items_df.append(df)
        
items_df[['item_id','en_label','en_description']].to_csv("items-entities.csv")



statements_df = pd.read_csv("statements-entities.csv")[['source_item_id', 'edge_property_id', 'target_item_id']]
statements_df['source_item_id'] = statements_df['target_item_id'].astype(int) 
items_df = pd.DataFrame(columns=['item_id', 'en_alias'])
for filename in os.listdir("items-alias-csv-split"):
    f = os.path.join("items-alias-csv-split", filename)
    # checking if it is a file
    print(f)
    if os.path.isfile(f):
        df = pd.read_csv(f)
        df = df.where(df['item_id'] != "item_id").dropna()
        df['item_id'] = df['item_id'].astype(int) 
        df = df.where(df['item_id'].isin(statements_df['source_item_id']) | df['item_id'].isin(statements_df['target_item_id'])).dropna()
        print(df.head(100))
        items_df = items_df.append(df)
        
items_df.to_csv("items-alias-entities.csv")   

statements_df = pd.read_csv("statements-entities.csv")[['source_item_id', 'edge_property_id', 'target_item_id']]
statements_df['source_item_id'] = statements_df['target_item_id'].astype(int) 
items_df = pd.DataFrame(columns=['page_id','item_id','title', 'views'])
for filename in os.listdir("items-alias-csv-split"):
    f = os.path.join("page-csv-split", filename)
    # checking if it is a file
    print(f)
    if os.path.isfile(f):
        df = pd.read_csv(f)
        df = df.where(df['item_id'] != "item_id").dropna()
        df['item_id'] = df['item_id'].astype(int) 
        df = df.where(df['item_id'].isin(statements_df['source_item_id']) | df['item_id'].isin(statements_df['target_item_id'])).dropna()
        print(df.head(100))
        items_df = items_df.append(df)
        
items_df.to_csv("page-entities.csv")   

item_df = pd.read_csv("items-entities.csv")
item_df['item_id'] = item_df['item_id'].astype(int)
page_df = pd.read_csv("page-entities.csv")
page_df['item_id'] = page_df['item_id'].astype(int)
df = pd.merge(item_df,page_df,left_on='item_id',right_on='item_id')
df["inlinks"] = pd.Series(0)
df.rename(columns={"Unnamed: 0_x": "index"},inplace=True)
df.head(10)

df["inlinks"] = df["inlinks"].fillna(1)
df[["index","item_id","page_id","en_label","en_description","title","views","inlinks"]].to_csv("joined.csv")

item_df = pd.read_csv("items-alias-entities.csv")
item_df['item_id'] = item_df['item_id'].astype(int)
item_df["en_alias_lowercase"] = item_df["en_alias"].str.lower()
item_df.reset_index()
item_df.rename(columns={"Unnamed: 0": "index"},inplace=True)
item_df.head(10)
item_df.to_csv("aliases.csv")

statements_df = pd.read_csv("statements-entities.csv")
statements_df.reset_index()
statements_df.rename(columns={"Unnamed: 0": "index"},inplace=True)
statements_df.head(10)
statements_df.to_csv("statements.csv")



   