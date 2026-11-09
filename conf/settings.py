"""
Django-ს მთავარი კონფიგურაციისა და პარამეტრების ფაილი (conf project).
აქ ინახება მთელი სისტემის პარამეტრები: ბაზის ტიპი, აპლიკაციები, შაბლონები, უსაფრთხოება და მედია ფაილები.
"""

from pathlib import Path
import os

# BASE_DIR განსაზღვრავს პროექტის ძირეულ (root) დირექტორიას (სადაც manage.py მდებარეობს).
# ამ ცვლადით დგება ფაილების აბსოლუტური მისამართები
BASE_DIR = Path(__file__).resolve().parent.parent


# ==============================================================================
# 1. უსაფრთხოება და დეველოპმენტის რეჟიმი
# ==============================================================================

# SECRET_KEY გამოიყენება კრიპტოგრაფიული ხელმოწერებისთვის (სესიები, CSRF ტოკენები, პაროლები).
# პროდაქშენში (რეალურ სერვერზე) ის აუცილებლად დაფარული უნდა იყოს
SECRET_KEY = 'django-insecure-)aluv11zk&zqltiys1%y1q)(&4h5x9_=4z2iv8i*e--!na@a)9'

# DEBUG=True ნიშნავს დეველოპმენტის რეჟიმს: ერორის დროს ბრაუზერში გამოდის დეტალური შეცდომის ტექსტი.
# რეალურ სერვერზე აუცილებლად იცვლება False-ით უსაფრთხოებისთვის!
DEBUG = True

# დომენების ან IP მისამართების სია, საიდანაც საიტი გაეშვება (დეველოპმენტში ცარიელია [])
ALLOWED_HOSTS = []


# ==============================================================================
# 2. რეგისტრირებული აპლიკაციები (INSTALLED_APPS)
# ==============================================================================
#პროექტს აცნობს ჩვენ მიერ შექმნილ shop აპლიკაციას
INSTALLED_APPS = [
    # Django-ს ჩაშენებული მოდულები:
    'django.contrib.admin',         # ადმინ-პანელი
    'django.contrib.auth',          # მომხმარებლების ავთენტიფიკაცია/ავტორიზაცია
    'django.contrib.contenttypes',  # მონაცემთა მოდელების მეტა-ინფორმაცია
    'django.contrib.sessions',      # ბრაუზერის სესიები (კალათისთვის აუცილებელი!)
    'django.contrib.messages',      # სისტემური შეტყობინებები
    'django.contrib.staticfiles',   # სტატიკური ფაილების (CSS/JS) მართვა
    
    # ჩვენი შექმნილი მაღაზიის აპლიკაცია:
    'shop',
]


# ==============================================================================
# 3. შუამავალი ფენები (MIDDLEWARE)
# ==============================================================================
# Middleware ამუშავებს ყველა Request-სა და Response-ს (მაგ: ამოწმებს CSRF-ს, სესიებს, იუზერს)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',       # სესიების მენეჯერი (კალათისთვის)
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',                 # CSRF შეტევებისგან დაცვა
    'django.contrib.auth.middleware.AuthenticationMiddleware',   # იუზერის იდენტიფიცირება (request.user)
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',     # Clickjacking-ისგან დაცვა
]

# პროექტის მთავარი მარშრუტების (URL-ების) ფაილის მისამართი
ROOT_URLCONF = 'conf.urls'


# ==============================================================================
# 4. HTML შაბლონების (Templates) კონფიგურაცია
# ==============================================================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #  Django-ს ეუბნება, რომ HTML ფაილები ეძებოს პროექტის templates/ საქაღალდეში
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True, # ეძებს templates ფოლდერებს აპლიკაციებშიც
        'OPTIONS': {
            'context_processors': [
                # კონტექსტ-პროცესორები, რომელთა მონაცემებიც ყველა HTML-ში ავტომატურად ხელმისაწვდომია:
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',      # {{ user }} HTML-ში გამოსაჩენად
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI აპლიკაციის მისამართი
WSGI_APPLICATION = 'conf.wsgi.application'


# ==============================================================================
# 5. მონაცემთა ბაზა (DATABASE)
# ==============================================================================
# აკონფიგურირებს მონაცემთა ბაზად db.sqlite3 ფაილს
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ==============================================================================
# 6. პაროლის ვალიდაცია (უსაფრთხოების წესები)
# ==============================================================================
# ამოწმებს, რომ რეგისტრაციისას პაროლი არ იყოს ძალიან მარტივი, მოკლე ან მხოლოდ ციფრები
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', # მინიმალური სიგრძე
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', # გავრცელებული პაროლები
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', # მხოლოდ ციფრები
    },
]


# ==============================================================================
# 7. ინტერნაციონალიზაცია და დროის სარტყელი
# ==============================================================================
LANGUAGE_CODE = 'en-us' # ნაგულისხმევი ენა
TIME_ZONE = 'UTC'       # დროის სარტყელი
USE_I18N = True
USE_TZ = True


# ==============================================================================
# 8. სტატიკური და მედია ფაილები (CSS, JS, ატვირთული ფოტოები)
# ==============================================================================

# ბრაუზერში სტატიკის URL პრეფიქსი
STATIC_URL = 'static/'

# კონსოლის მეილ-სერვერი ტესტირებისთვის
MAILERS = {
    'default': {
        'BACKEND': 'django.core.mail.backends.console.EmailBackend',
    },
}

# MEDIA_URL - მისამართი, რომლითაც ბრაუზერი მიმართავს ატვირთულ ფოტოს (მაგ: /media/products/shirt.jpg)
MEDIA_URL = '/media/'

# MEDIA_ROOT - ზუსტი ფიზიკური საქაღალდე კომპიუტერზე (პროექტის media/ ფოლდერი), სადაც ფაილები ინახება
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')