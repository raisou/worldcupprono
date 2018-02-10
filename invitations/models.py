from django.db import models
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.utils.crypto import get_random_string

from boards.models import Board


class Invitation(models.Model):
    STATUS_PENDING = 0
    STATUS_ACCEPTED = 1
    STATUS_REFUSED = 2
    STATUS_CANCELED = 3
    STATUS_CHOICES = (
        (STATUS_PENDING, 'En attente'),
        (STATUS_ACCEPTED, 'Acceptée'),
        (STATUS_REFUSED, 'Refusée'),
        (STATUS_CANCELED, 'Annulée'))

    source = models.ForeignKey(User, related_name="invitations_sent")
    destination = models.ForeignKey(
        User, related_name="invitations_received", blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    board = models.ForeignKey(Board)
    status = models.IntegerField(
        choices=STATUS_CHOICES, default=STATUS_PENDING)
    token = models.CharField(max_length=32, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        if is_new:
            unique = False
            while not unique:
                token = get_random_string(length=32)
                unique = not Invitation.objects.filter(token=token).exists()
            self.token = token
        super(Invitation, self).save(*args, **kwargs)

        if is_new:
            self.send_invitation_mail()

    def send_invitation_mail(self):
        plaintext = get_template('email/invitation.txt')
        site = Site.objects.get_current()

        context = {
            'protocol': 'https' if settings.ENABLE_HTTPS else 'http',
            'invitation': self,
            'site': site
        }

        subject = "{} vous invite à pronostiquer la coupe du monde".format(
            self.source.username)
        from_email = settings.DEFAULT_FROM_EMAIL
        to = [self.destination.email] if self.destination else [self.email]
        text_content = plaintext.render(context)
        msg = EmailMessage(subject, text_content, from_email, to)
        msg.send()
