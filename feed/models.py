from django.db import models

# Create your models here.
class Hashtag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Article(models.Model):
    DEVELOPMENT = "dv"
    PERSONAL = "ps"
    CATEGORY_CHOICES = (
        (DEVELOPMENT, "development"),
        (PERSONAL, "personal"),
    )

    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default=DEVELOPMENT,
        )
    hashtag = models.ManyToManyField(Hashtag)

    def __str__(self):
        return self.title

class Comment(models.Model):
    # PERMISSION = "pm"
    # DEFAULT="df"
    # COMMENT_CHOICES = (
    #     (PERMISSION, "permission"),
    #     (DEFAULT, "default"),
    # )

    article = models.ForeignKey(
        Article,
        related_name="article_comments",
        on_delete=models.CASCADE,
    )
    username = models.CharField(max_length=50)
    content = models.CharField(
        max_length=200,
        # choices=COMMENT_CHOICES,
        # default=DEFAULT,
        )

    def __str__(self):
        return "{}에 작성됨 - {} : {} ".format(self.article.title, self.username, self.content)
