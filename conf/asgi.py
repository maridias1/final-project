"""
ASGI კონფიგურაცია conf პროექტისთვის.
ASGI (Asynchronous Server Gateway Interface) არის WSGI-ის თანამედროვე, ასინქრონული მემკვიდრე.
ის გამოიყენება მაშინ, როდესაც პროექტს სჭირდება ასინქრონული ფუნქციონალი (მაგალითად: WebSockets, ჩატი, Real-time შეტყობინებები).
"""

# os მოდული გამოიყენება სისტემის გარემოს ცვლადებთან სამუშაოდ
import os

# Django-ს ASGI აპლიკაციის შემქმნელი მთავარი ფუნქციის შემოტანა
from django.core.asgi import get_asgi_application

# მივუთითებთ პროექტის პარამეტრების ფაილის მისამართს (conf.settings)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

# application არის ასინქრონული სერვერის მთავარი ობიექტი (მაგალითად Daphne ან Uvicorn სერვერებისთვის)
application = get_asgi_application()