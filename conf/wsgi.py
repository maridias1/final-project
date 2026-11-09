"""
WSGI კონფიგურაცია conf პროექტისთვის.
WSGI (Web Server Gateway Interface) წარმოადგენს სტანდარტულ ხიდს ვებ-სერვერსა (მაგ: Nginx, Gunicorn) 
და Python-ის Django აპლიკაციას შორის საკომუნიკაციოდ.
"""

# os მოდული გამოიყენება ოპერაციული სისტემის გარემოს ცვლადების დასაყენებლად
import os

# Django-ს WSGI აპლიკაციის შემქმნელი მთავარი ფუნქცია
from django.core.wsgi import get_wsgi_application

# Django-ს გარემოს ცვლადებში მივუთითებთ, სად მდებარეობს პროექტის პარამეტრების ფაილი (conf.settings)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

# application არის მთავარი WSGI ობიექტი, რომელსაც უკავშირდება გარე ვებ-სერვერი
application = get_wsgi_application()