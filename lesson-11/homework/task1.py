import sqlite3

conn = sqlite3.connect("roster.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

cursor.executemany("""
INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)
""", [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
])
conn.commit()
cursor.execute("""
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
""")
conn.commit()

cursor.execute("""
SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'
""")
print("Bajoran Characters:", cursor.fetchall())

cursor.execute("""
DELETE FROM Roster WHERE Age > 100
""")
conn.commit()


cursor.execute("""
ALTER TABLE Roster ADD COLUMN Rank TEXT
""")
conn.commit()


ranks = {
    "Benjamin Sisko": "Captain",
    "Ezri Dax": "Lieutenant",
    "Kira Nerys": "Major"
}
for name, rank in ranks.items():
    cursor.execute("""
    UPDATE Roster SET Rank = ? WHERE Name = ?
    """, (rank, name))
conn.commit()

cursor.execute("""
SELECT * FROM Roster ORDER BY Age DESC
""")
print("Sorted Characters:", cursor.fetchall())


conn.close()
