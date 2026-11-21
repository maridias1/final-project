from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-)aluv11zk&zqltiys1%y1q)(&4h5x9_=4z2iv8i*e--!na@a)9'


DEBUG = True


ALLOWED_HOSTS = []


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


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',       # სესიების მენეჯერი (კალათისთვის)
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',                 # CSRF შეტევებისგან დაცვა
    'django.contrib.auth.middleware.AuthenticationMiddleware',   # იუზერის იდენტიფიცირება (request.user)
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',     # Clickjacking-ისგან დაცვა
]

ROOT_URLCONF = 'conf.urls'



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True, 
        'OPTIONS': {
            'context_processors': [
                
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',      
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'conf.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', 
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', 
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', 
    },
]



LANGUAGE_CODE = 'en-us' 
TIME_ZONE = 'UTC'       
USE_I18N = True
USE_TZ = True



STATIC_URL = 'static/'


MAILERS = {
    'default': {
        'BACKEND': 'django.core.mail.backends.console.EmailBackend',
    },
}

MEDIA_URL = '/media/'


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')