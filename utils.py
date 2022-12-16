import json

def load_json(file_name):
    """Загружает посты из файла в список."""
    """Если файл не найден или в неподходящем формате, происходит логирование ошибки и
    возвращается пустой список"""
    with open(file_name, encoding='UTF-8') as file:
        return json.load(file)

def load_posts():
    """загружает все наши посты"""
    data = load_json("data/posts.json")
    for post in data:
        post['short'] = post['content'][:post['content'].find(" ", 100)]
    return data

def load_comments(post_pk):
    """возвращаем комментарии"""
    data = load_json('data/comments.json')
    return [comment for comment in data if comment['post_id'] == post_pk]

def load_posts_user_id(pk):
    """загружает все наши посты"""
    data = load_posts()
    for post in data:
        if post['pk'] == pk:
            return post
    return 'нет поста с таким номером!'

def get_comments_by_post_id(post_id):
     """возвращает комментарии определенного поста. """
     for comment in load_posts():
         if comment["post_id"] in post_id:
             return comment
     return 'у поста нет комментария!'

def search_for_posts(text):
    """ возвращает список постов по ключевому слову"""
    data = load_posts()
    post_filter = []
    for post in data:
        if text.lower() in post['content'].lower():
            post_filter.append(post)
    return post_filter

def search_for_name(name):
    """ возвращает список имени и что написал этот человек"""
    data = load_posts()
    post_filter = []
    for post in data:
        if name.lower() == post['poster_name'].lower():
            post_filter.append(post)
    return post_filter

