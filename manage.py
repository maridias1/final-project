#!/usr/bin/env python
"""Django-ს ბრძანებების მართვის უტილიტა ტერმინალიდან სამუშაოდ."""

# os მოდული გამოიყენება ოპერაციულ სისტემასთან და გარემოს ცვლადებთან (Environment Variables) სამუშაოდ
import os

# sys მოდული გამოიყენება ტერმინალში აკრეფილი არგუმენტების (ბრძანებების) წასაკითხად (მაგ: sys.argv)
import sys


def main():
    """ადმინისტრაციული დავალებებისა და ბრძანებების გამშვები მთავარი ფუნქცია."""

    # გარემოს ცვლადებში უთითებს, სად მდებარეობს პროექტის მთავარი პარამეტრების ფაილი (settings.py).
    # პროექტში ეს არის conf/settings.py
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

    try:
        # Django-ს ბირთვიდან შემოაქვს ბრძანებების შემსრულებელი ფუნქცია execute_from_command_line
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # თუ Django დაინსტალირებული არ არის ან ვირტუალური გარემო (.venv) არაა გააქტიურებული,
        # ამოაგდებს გასაგებ შეცდომას (Error Message-ს)
        raise ImportError(
            "Django ვერ მოიძებნა. დარწმუნდით, რომ ის დაინსტალირებულია "
            "და გააქტიურებული გაქვთ ვირტუალური გარემო (.venv)."
        ) from exc

    # sys.argv არის ტერმინალში აკრეფილი ბრძანებების სია (მაგ: ['manage.py', 'runserver']).
    # execute_from_command_line იღებს ამ ბრძანებას და უშვებს შესაბამის პროცესს
    execute_from_command_line(sys.argv)


# Python-ის სტანდარტული ჩანაწერი:
# ამოწმებს, ფაილი პირდაპირ ტერმინალიდან გაეშვა თუ სხვა ფაილიდან დაიმპორტდა.
# თუ პირდაპირ გაეშვა (python manage.py ...), მაშინ გამოიძახებს main() ფუნქციას
if __name__ == '__main__':
    main()