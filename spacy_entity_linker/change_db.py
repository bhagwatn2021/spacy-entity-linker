# https://stackoverflow.com/questions/2887878/importing-a-csv-file-into-a-sqlite3-database-table-using-python
# https://www.sqlitetutorial.net/sqlite-python/delete/ 

import csv, sqlite3

DB_DEFAULT_PATH = os.path.abspath("/anaconda/envs/azureml_py38/lib/python3.8/site-packages/data_spacy_entity_linker/wikidb_filtered.db")

conn = sqlite3.connect(DB_DEFAULT_PATH, check_same_thread=False)
cur = conn.cursor()

cur.execute("DELETE FROM joined")
cur.execute("DELETE FROM aliases")
cur.execute("DELETE FROM statements")

with open('joined.csv','r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['item_id'], i['en_label'], i['en_description'], i['page_id'], i['views'], i['inlinks']) for i in dr]

cur.executemany("INSERT INTO joined(item_id,en_label,en_description,page_id,views,inlinks) VALUES (?, ?, ?, ?, ?, ?);", to_db)

with open('aliases.csv','r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['item_id'], i['en_alias'], i['en_alias_lowercase']) for i in dr]

cur.executemany("INSERT INTO aliases(item_id,en_alias,en_alias_lowercase) VALUES (?, ?, ?);", to_db)

with open('statements-entities.csv','r') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['source_item_id'], i['edge_property_id'], i['target_item_id']) for i in dr]
cur.executemany("INSERT INTO statements(source_item_id,edge_property_id,target_item_id) VALUES (?, ?, ?);", to_db)

conn.commit()
conn.close()
