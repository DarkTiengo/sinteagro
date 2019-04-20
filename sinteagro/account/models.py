from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserManager(BaseUserManager):

    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError(_('Nome de usuario deve ser informado'))
        if not password:
            raise ValueError(_('Senha deve ser fornecida.'))
        if not email:
            raise ValueError(_('E-Mail deve ser informado.'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, is_staff=is_staff, is_active=True, is_superuser=is_superuser, last_login=now, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        user=self._create_user(username, email, password, True, True, **extra_fields)
        user.is_active=True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(_('Nome de Usuário'), max_length=30,unique=True)

    first_name = models.CharField(_('Nome'), max_length=30)

    last_name = models.CharField(_('Sobrenome'), max_length=30)

    email = models.EmailField(_('E-Mail'), max_length=255, unique=True)

    sexo = models.CharField(_('Sexo'),max_length=1,default="m")

    nascimento = models.DateField(_('Data de Nascimento'),default= "2000-01-01")

    cidade = models.CharField(_('Cidade'),max_length= 60, default= "")

    estado = models.CharField(_('Estado'),max_length=2, default= "")

    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Usuarios que podem logar no admin site.'))

    is_active = models.BooleanField(_('active'), default=True, help_text=_(
        'Designado para usuarios ativos. Desmarcado sao contas deletadas.'))

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    is_trusty = models.BooleanField(_('trusty'), default=False,
                                    help_text=_('Confirmacao de conta via e-mail.'))

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UserManager()

    class Meta:
        verbose_name = _('usuario')
        verbose_name_plural = _('usuarios')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def get_sexo(self):
        return self.sexo

    def get_cidade_estado(self):
        cidade_estado = '%s / %s' % (self.cidade,self.estado)
        return cidade_estado.strip()

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])

    def altera_senha(self,novasenha):
        self.set_password(novasenha)
        return True