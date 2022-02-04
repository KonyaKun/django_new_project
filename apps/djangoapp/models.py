from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Account (models.Model):
    ACCOUNT_FULL_NAME_MAX_LENTGTH = 20
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=ACCOUNT_FULL_NAME_MAX_LENTGTH)
    description = models.TextField()

    def __str__(self) -> str:
        return f'Account {self.user.id} / {self.full_name}'

    class Meta:
        ordering = ('full_name',)
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'

class Group(models.Model):
    GROUP_NAME_MAX_LENGTH = 10
    name = models.CharField(
        max_length=GROUP_NAME_MAX_LENGTH
    )
    def __str__(self) -> str:
        return f'Group {self.name}'
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

class Student(models.Model):
    # 1 Account = много Студентов
    account = models.OneToOneField(
        Account,
        on_delete=models.CASCADE
    )
    group = models.ForeignKey(
        Group,
        on_delete = models.PROTECT
    )
    age = models.IntegerField(
        'Возраст студента'
    )
    GPA = models.FloatField(
        'Среднее значение GPA'
    )
    
    def __str__(self) -> str:
        return f'Student: {self.account} \
        age: {self.age} group: {self.group} GPA: {self.GPA}'

    class Meta:
        ordering = (
            'account',
            'age',
            'group',
            'GPA'
        )
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'