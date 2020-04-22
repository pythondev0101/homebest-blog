from app.admin.forms import AdminIndexForm

class PostForm(AdminIndexForm):
    index_headers = ['Title', 'Created at', 'updated at']
    index_title = "Posts"
    index_message = "Message"
    title = index_title