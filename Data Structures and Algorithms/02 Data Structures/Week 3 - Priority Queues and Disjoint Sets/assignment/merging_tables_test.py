from merging_tables import Database

db = Database(row_counts=[1, 1, 1, 1, 1])
db.merge(3-1, 5-1)
print(db.max_row_count)
db.merge(2-1, 4-1)
print(db.max_row_count)
db.merge(1-1, 4-1)
print(db.max_row_count)
db.merge(5-1, 4-1)
print(db.max_row_count)
db.merge(5-1, 3-1)
print(db.max_row_count)