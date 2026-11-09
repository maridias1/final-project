# Django-ს ადმინ-პანელის მარშრუტიზაციისთვის საჭირო მოდული
from django.contrib import admin

# path გამოიყენება კონკრეტული URL-ის გასაწერად,
# ხოლო include - სხვა აპლიკაციის (მაგ: shop) urls.py ფაილის მთლიანად შემოსატანად
from django.urls import path, include

# პროექტის პარამეტრების (settings.py) შემოტანა, საიდანაც გვჭირდება DEBUG, MEDIA_URL და MEDIA_ROOT
from django.conf import settings

# static ფუნქცია გამოიყენება დეველოპმენტის დროს მედია ფაილების (სურათების) URL-ებთან დასაკავშირებლად
from django.conf.urls.static import static


# პროექტის მთავარი მარშრუტები (URL patterns)
urlpatterns = [
    # 1. Django-ს ჩაშენებული ადმინისტრაციული პანელის მისამართი (http://127.0.0.1:8000/admin/)
    path('admin/', admin.site.urls),

    # 2. მთავარ დომენზე ('') ვაკავშირებთ shop აპლიკაციის შიგნით არსებულ urls.py ფაილს.
    # ეს ნიშნავს, რომ მაღაზიის ყველა გვერდი (კატალოგი, კალათა, ავტორიზაცია) გაეშვება პირდაპირ მთავარ მისამართზე
    path('', include('shop.urls')),
]

# ==============================================================================
# ატვირთული ფოტოების (Media Files) ჩვენება ბრაუზერში
# ==============================================================================
# settings.DEBUG ამოწმებს, ვართ თუ არა დეველოპმენტის (ტესტირების) რეჟიმში.
# თუ DEBUG=True არის, Django თვითონ მოემსახურება media/ საქაღალდეში ატვირთულ სურათებს
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)