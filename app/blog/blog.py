from .models import Post


class BlogModule:
    module_name = 'blog'
    module_icon = 'fa-rss-square'
    module_link = 'bp_blog.index'
    module_description = 'Blog'
    models = [Post]