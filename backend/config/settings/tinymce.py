'''定义了 Django 中 TinyMCE 编辑器的一些配置选项，以便在网页上实现富文本编辑功能。'''
# Django TinyMCE Settings

TINYMCE_JS_URL = "tinymce/tinymce.min.js"
# TINYMCE_COMPRESSOR = True
TINYMCE_DEFAULT_CONFIG = {
    "theme": "silver",
    "height": 500,
    "menubar": True,
    "plugins": "advlist,autolink,lists,link,image,charmap,print,preview,anchor,"
    "searchreplace,visualblocks,code,fullscreen,insertdatetime,media,table,paste,"
    "code,help,wordcount",
    "toolbar": "undo redo | formatselect | "
    "bold italic backcolor | alignleft aligncenter "
    "alignright alignjustify | bullist numlist outdent indent | "
    "removeformat | help",
}
