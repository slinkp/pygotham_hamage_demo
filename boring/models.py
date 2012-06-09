from django.db import models
from django.contrib.comments.moderation import CommentModerator, moderator

# Create your models here.


class Entry(models.Model):
    "Blog-ish demo content. Yes, boring."
    author = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    body = models.TextField()


class EntryModerator(CommentModerator):

    """Wire up django.contrib.comments moderation
    to a particular model.

    This is not a particularly good idea, because if allow() returns False
    (don't allow the object), Django gives the user a not very useful
    'security has been tampered with' message, and you apparently have
    no influence over what it says.
    """

    def allow(self, comment, content_object, request):
        from hamage.backends.django_hamage.models import DjangoFilterSystem
        from hamage.backends.django_hamage.models import RejectContent
        filtersys = DjangoFilterSystem()
        if comment.user_name:
            author = comment.user_name
        elif comment.user:
            author = comment.user.name
        else:
            author = ''
        if comment.user_email:
            author = '%s <%s>' % (author, comment.user_email)
            author = author.strip()
        changes = [(u'', comment.comment),
                   (u'', comment.url),
                   (u'', comment.email),
                   ]
        try:
            filtersys.test(request, author, changes)
            return True
        except RejectContent:
            return False

#moderator.register(Entry, EntryModerator)
