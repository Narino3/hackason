from django.db import models


#データベースのモデル作る
#クラスの前は２行空けないと怒られる。どして・・・
# Create your models here.


class Book(models.Model):
    """書籍"""
    name = models.CharField('書籍名', max_length=255)
    publisher = models.CharField('出版社', max_length=255, blank=True)
    page = models.IntegerField('ページ数', blank=True, default=0)

    def __str__(self):
        return self.name



class Impression(models.Model):
    """感想"""
    book = models.ForeignKey(Book, verbose_name='書籍', related_name='impressions', on_delete=models.CASCADE)
    comment = models.TextField('コメント', blank=True)

    def __str__(self):
        return self.comment



class Recruit(models.Model):
    """募集"""
    recruit_ID = models.IntegerField('募集ID', blank=True, default=0)
    shop_ID = models.IntegerField('店舗ID', blank=True, default=0)
    post_time = models.TimeField('投稿時刻')
    finish_time = models.TimeField('募集締め切り時刻')
    person_type = models.IntegerField('職種', blank=True, default=0)
    person_number = models.IntegerField('人数', blank=True, default=1)
    work_start_time = models.TimeField('開始時刻')
    work_last_time = models.TimeField('終了時刻')
    comment = models.CharField('コメント')
    finish_flag = models.BooleanField('マッチング前後')
    password = models.CharField('パスワード')
    entry_ID = models.IntegerField('応募ID')

    def __str__(self):
        return self.comment



class Recruit(models.Model):
    """募集"""
    recruit_ID = models.IntegerField('募集ID', blank=True, default=0)
    shop_ID = models.IntegerField('店舗ID', blank=True, default=0)
    post_time = models.TimeField('投稿時刻')
    finish_time = models.TimeField('募集締め切り時刻')
    person_type = models.IntegerField('職種', blank=True, default=0)
    person_number = models.IntegerField('人数', blank=True, default=1)
    work_start_time = models.TimeField('開始時刻')
    work_last_time = models.TimeField('終了時刻')
    comment = models.CharField('コメント',max_length=1000)
    finish_flag = models.BooleanField('マッチング前後')
    password = models.CharField('パスワード',max_length=400)
    entry_ID = models.IntegerField('応募ID')

    def __str__(self):
        return self.comment