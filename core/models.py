# coding=utf-8
import os
from random import randint
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


__author__ = 'alexy'


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')

        if not password:
            password = User.objects.make_random_password()

        kwargs.update({'email': self.normalize_email(email)})
        user = self.model(**kwargs)
        user.set_password(password)
        user.original_password = password
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, first_name=None, last_name=None, patronymic=None):
        user = self.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            patronymic=patronymic,
        )

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def normalize_email(self, email):
        email = super(MyUserManager, self).normalize_email(email)
        return email.lower()


class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = u'Пользователь'
        verbose_name_plural = u'Пользователи'
        ordering = ['-date_joined']
        app_label = 'core'

    # def get_photo_image_path(self, filename):
    #     extension = filename.split('.')[-1]
    #     filename = "%s.%s" % (uuid.uuid4(), extension)
    #     return os.path.join('core_auth', "avatars", filename)

    email = models.EmailField(_('email address'), unique=True)

    first_name = models.CharField(_('first name'), max_length=30, blank=True, null=True, default=u'')
    last_name = models.CharField(_('last name'), max_length=30, blank=True, null=True, default=u'')
    patronymic = models.CharField(u'Отчество', max_length=50, blank=True, null=True, default=u'')
    phone = models.CharField(max_length=250, verbose_name=u'Телефон', null=True, blank=True, default=u'')

    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin site.'))

    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    delivery_address = models.CharField(verbose_name=u'адрес доставки', max_length=512, blank=True, default=u'')

    # avatar = models.ImageField(verbose_name=u'Аватар', upload_to=get_photo_image_path, null=True, blank=True)
    # avatar_small = ImageSpecField([SmartResize(*settings.AVATAR_SMALL)], source='avatar',
    #                               format='JPEG', options={'quality': 94})

    objects = MyUserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return u'%s %s %s' % (self.last_name, self.first_name or '', self.patronymic or '')

    def get_short_name(self):
        return u'%s' % self.first_name

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Setup(models.Model):
    class Meta:
        verbose_name = u'Настройки сайта'
        verbose_name_plural = u'Настройки сайта'
        app_label = 'core'

    def __unicode__(self):
        if self.meta_title:
            return self.meta_title
        else:
            return u'Настройки'

    meta_title = models.CharField(verbose_name=u'Заголовок <TITLE>...</TITLE>', max_length=256, blank=True)
    email = models.EmailField(verbose_name=u'e-mail для приёма заявок', blank=True)
    # video = models.TextField(verbose_name=u'HTML-код видео', blank=True, null=True)
    meta_key = models.TextField(verbose_name=u'Ключевые слова META_KEYWORDS', blank=True)
    meta_desc = models.TextField(verbose_name=u'Описание META_DESCRIPTION', blank=True)
    top_js = models.TextField(verbose_name=u'Скрипты в <HEAD>..</HEAD>', blank=True)
    bottom_js = models.TextField(verbose_name=u'Скрипты перед закрывающим </BODY>', blank=True)
    robots_txt = models.TextField(verbose_name=u'robots.txt', blank=True, null=True)
