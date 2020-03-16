from django.db import models


class Team(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True,
        help_text='Name of team'
    )

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        return self.name


class Role(models.Model):

    name = models.CharField(
        max_length=50,
        unique=True,
        help_text='Name of role'
    )

    class Meta:
        ordering = ['name', ]

    def __str__(self):
        return self.name


class Employee(models.Model):

    first_name = models.CharField(
        max_length=30,
        help_text='First name'
    )
    last_name = models.CharField(
        max_length=30,
        help_text='Last name'
    )
    team = models.ForeignKey(
        Team,
        related_name='members',
        null=True,
        on_delete=models.SET_NULL,
        help_text='Member of team'
    )
    role = models.ForeignKey(
        Role,
        null=True,
        on_delete=models.SET_NULL,
        help_text='Employee role on team'
    )
    on_call_order = models.IntegerField(
        help_text='On call order'
    )

    class Meta:
        unique_together = ['team', 'on_call_order']
        ordering = ['last_name', 'first_name', ]

    def __str__(self):
        return '{}, {}'.format(self.last_name, self.first_name)
