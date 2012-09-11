import hashlib

from django.db import models


class Tier(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name


class Level(models.Model):
    tier = models.ForeignKey('Tier')
    hash = models.CharField(max_length=40, unique=True, db_index=True)
    name = models.CharField(max_length=64)
    content = models.TextField()
    points = models.IntegerField()
    maxsize = models.IntegerField()

    speech = models.TextField(blank=True)

    class Meta:
        ordering = ['tier', 'pk']

    def __init__(self, *args, **kwargs):
        super(Level, self).__init__(*args, **kwargs)
        self.lines = [map(str, line) for line in self.content.split()]

    def get(self, x, y):
        if all([x >= 0, x < len(self.lines),
               y >= 0, y < len(self.lines[0])]):
            return self.lines[x][y]
        return None

    @property
    def start(self):
        for i, line in enumerate(self.lines):
            try:
                index = line.index("u")
                return (i, index)
            except ValueError:
                pass

    @property
    def dots(self):
        dots = []
        for y, line in enumerate(self.lines):
            for x, element in enumerate(line):
                if element == "o":
                    dots.append((y, x))
        return dots

    @property
    def next(self):
        n = False
        for level in Level.objects.all():
            if n == True:
                return level
            if level == self:
                n = True
        return None

    def all_previous(self):
        return Level.objects.filter(id__lte=self.pk)

    @models.permalink
    def get_absolute_url(self):
        return ('level', [self.hash])

    def save(self, *args, **kwargs):
        if not self.pk:
            self.hash = hashlib.sha1(self.content).hexdigest()[:10]
        super(Level, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    def best_result(self):
        try:
            return Result.objects.filter(level=self).order_by("program_length", "commited")[0]
        except IndexError:
            return None


class Result(models.Model):
    level = models.ForeignKey('Level')
    program = models.TextField()
    program_length = models.IntegerField()

    username = models.CharField(max_length=16, blank=True)
    session = models.CharField(max_length=32, blank=True)
    email = models.EmailField(blank=True)
    commited = models.DateTimeField(auto_now_add=True)

    def gravatar(self):
        if self.email:
            return hashlib.md5(self.email).hexdigest()
        return ""

    def __unicode__(self):
        return "%s:%s" % (self.level.name, self.program_length)
