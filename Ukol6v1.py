import sqlite3


try:
    conn = sqlite3.connect('knihy.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute("""CREATE TABLE knihy (
                            ISBN TEXT PRIMARY KEY,
                            nazev TEXT NOT NULL,
                            vyadatel TEXT NOT NULL,
                            rok_vydani INTEGER,
                            pocet_stran INTEGER,
                            zanr TEXT,
                            typ TEXT)""")
    except sqlite3.Error as e:
        print(f'Chyba při vytváření tabulky: {e}')

    try:
        cursor.execute("""INSERT INTO knihy
                            (ISBN, nazev, vyadatel, rok_vydani, pocet_stran, zanr, typ)
                            VALUES 
                            ('K003', 'Stopařův průvodce po galaxii', 'MF', 1985, 214, 'scifi', 'kniha'),
                            ('K045', 'Pán prstenů - Dvě věže', 'MF', 1948, 251, 'fantasy', 'kniha'),
                            ('K051', 'Kedrigern a hlas pro princeznu', 'MF', 1996, 321, 'fantasy', 'kniha'),
                            ('K043', 'Hobit', 'MF', 1950, 410, 'fantasy', 'kniha'),
                            ('K025', 'Barva kouzel', 'Talpress', 1989, 221, 'fantasy', 'ebook'),
                            ('K026', 'Stráže! Stráže!', 'Talpress', 2000, 341, 'fantasy', 'ebook'),
                            ('K027', 'Lehké fantastično', 'Talpress', 1999, 154, 'fantasy', 'ebook')""")
        
        conn.commit()
    except sqlite3.Error as e:
        print(f'Chyba při vkládání dat: {e}')

    try:
        cursor.execute("SELECT * FROM knihy WHERE pocet_stran > 300")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(f'Chyba při výběru dat: {e}')

except sqlite3.Error as e:
    print(f'Chyba při připojení k databázi: {e}')

finally:
    conn.close()
