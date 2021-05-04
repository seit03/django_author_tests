from django.db import models


YES = 'YES'
NO = 'NO'
ALIVE = (
    (YES, ' YES'),
    (NO, 'NO')
)


class Author(models.Model):
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Author'
    name = models.CharField(max_length=250)
    alive_or_not = models.CharField(choices=ALIVE,
                                    default='YES',
                                    max_length=200)

    def __str__(self):
        return f'{self.name}'


FANTASY = 'FANTASY'
ADVENTURE = 'ADVENTURE'
COMEDY = 'COMEDY'
HORROR = 'HORROR'
DRAMA = 'DRAMA'
SACRED = 'SACRED'
NO = 'NO'
GENRE = (
    (FANTASY, 'FANTASY'),
    (ADVENTURE, 'ADVENTURE'),
    (COMEDY, 'COMEDY'),
    (HORROR, 'HORROR'),
    (DRAMA, 'DRAMA'),
    (SACRED, 'SACRED'),
    (NO, 'NO')
)


class Books(models.Model):
    class Meta:
        verbose_name = 'Books'
        verbose_name_plural = 'Books'
    author = models.ForeignKey(Author,
                               on_delete=models.CASCADE,
                               related_name='author_books')
    title = models.CharField(max_length=235)
    description = models.TextField()
    published_date = models.DateField()
    genre = models.CharField(choices=GENRE,
                             default='NO',
                             max_length=200)
    rating = models.FloatField()

    def __str__(self):
        return f'{self.title}'