from django.db import models
from datetime import datetime


class Category(models.Model):
    LIFE = 'life'
    INSURANCE = 'IN'
    APPLEID = 'APPLE'
    STAFF = 'STA'
    GAME = 'GA'
    WORK = 'WO'
    BANK = 'BA'
    PHONE = 'PH'
    GIT = 'GIT'
    MACHINE = 'MA'
    OTHERS = 'OT'
    PWD_CAT = (
        (LIFE, 'life'),
        (INSURANCE, 'insurance'),
        (APPLEID, 'appleid'),
        (STAFF, 'staff'),
        (GAME, 'game'),
        (WORK, 'work'),
        (BANK, 'bank'),
        (PHONE, 'phone'),
        (GIT, 'git'),
        (MACHINE, 'machine'),
        (OTHERS, 'others'),
    )
    pwd_category = models.CharField(
        max_length=20,
        choices=PWD_CAT,
        default=LIFE,
        unique=True
    )

    def __str__(self):
        return self.pwd_category


class Password(models.Model):

    def __str__(self):
        return self.name + ' and user id is ' + self.user_id

    def save(self, *args, **kwargs):
        if self.text != self.text_repeat:
            raise ValueError("two password value is inconsistent, please check")
        else:
            super().save(*args, **kwargs)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, choices=Category.PWD_CAT, default=Category.PWD_CAT[0])
    name = models.CharField(max_length=200)
    user_id = models.CharField(max_length=200, blank=True)
    text = models.CharField(max_length=200)
    middle_comments = models.CharField(max_length=200, blank=True)
    text_repeat = models.CharField(max_length=200)
    email = models.CharField(max_length=200, blank=True)
    url = models.URLField(blank=True)
    first_comments = models.CharField(max_length=200, blank=True)
    second_comments = models.CharField(max_length=200, blank=True)
    third_comments = models.CharField(max_length=200, blank=True)
    pub_date = models.DateTimeField('date published', blank=True, default=datetime.today())
    validation = models.BooleanField(default=True, blank=True)
