# conection to the database
from sqlite3 import connect
conn = connect('blog.db')
cursor = conn.cursor()

# create the table
conn.execute(
    """\
    CREATE TABLE IF NOT EXISTS posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        author TEXT NOT NULL
    );
    """
)
conn.commit()
print('Database initialized successfully.')

post = [{
    'title': 'My First Post',
    'content': 'This is the content of my first post.',
    'author': 'John Doe'
},
{
    'title': 'My Second Post',
    'content': 'This is the content of my second post.',
    'author': 'Jane Doe'
},
{
    'title': 'My Third Post',
    'content': 'This is the content of my third post.',
    'author': 'John Doe'
}]

# insert the posts into the database
count = cursor.execute('SELECT * FROM posts').fetchall()
if not count:
    cursor.executemany(
        """\
        INSERT INTO posts (title, content, author)
        VALUES (:title, :content, :author);
        """,
        post,
    )
    conn.commit()
    print('Sample posts inserted successfully.')
        
