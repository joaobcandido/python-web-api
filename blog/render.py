from pathlib import Path
from database import conn

cursor = conn.cursor()
fields = ['id', 'title', 'content', 'author']
results = cursor.execute('SELECT * FROM posts;')
posts = [dict(zip(fields, result)) for result in results]
print(posts)


site_dir = Path('site')
site_dir.mkdir(exist_ok=True)

def get_post_url(post):
    slug = post['title'].lower().replace(' ', '-')
    return f'{slug}.html'

index_template = Path('list.template.html').read_text()
index_page = site_dir / Path('index.html')
post_list = [
    f'<li><a href="{get_post_url(post)}">{post["title"]}</a></li>' for post in posts
    ]

index_page.write_text(index_template.format(post_list='\n'.join(post_list)))

for post in posts:
    post_template = Path('post.template.html').read_text()
    post_page = site_dir / Path(get_post_url(post))
    post_page.write_text(post_template.format(post=post))

print('Site generated successfully!') 

conn.close()