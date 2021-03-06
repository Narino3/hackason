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

class PType(models.Model):
    pty = models.CharField('職種',max_length=300, unique=True)

    def __str__(self):
        return self.pty

#募集が親、応募が子
class Recruit(models.Model):
    """募集"""
    #recruit_IDは自動取得
    recruit_ID = models.AutoField('募集ID',primary_key=True)
    shop_ID = models.CharField('店舗名',max_length=40)
    #TimeField⇒AutoFieldに変更
    #投稿時刻自動取得
    recruit_title = models.CharField('募集タイトル',max_length=500,default='NOT TITLE')
    post_time = models.DateTimeField('投稿時刻',auto_now=True)
    finish_time = models.DateTimeField('募集締め切り時刻')
    person_type = models.ManyToManyField(PType, blank=True)
    person_number = models.PositiveIntegerField('人数', blank=True, default=1)
    work_start_time = models.DateTimeField('開始時刻')
    work_last_time = models.DateTimeField('終了時刻')
    comment = models.CharField('コメント',max_length=1000)
    finish_flag = models.BooleanField('マッチング前後', default=0)
    password = models.CharField('パスワード',max_length=40)

    def __str__(self):
        return self.comment


class Entry(models.Model):
    """応募"""
    #recruit = models.ForeignKey(Recruit,verbose_name='応募',related_name='entry', on_delete=models.CASCADE)
    recruit_ID = models.PositiveIntegerField('募集ID', default=1)
    #entry_IDは自動取得
    entry_ID = models.AutoField('応募ID',primary_key=True)
    shop_ID = models.CharField('店舗名', blank=True, max_length=40)
    #TimeField⇒AutoFieldに変更
    #投稿時刻自動取得
    post_time = models.DateTimeField('投稿時刻',auto_now=True)
    person_type = models.ManyToManyField(PType, blank=True)
    person_number = models.PositiveIntegerField('人数', blank=True, default=1)
    comment = models.CharField('コメント',max_length=1000)
    finish_flag = models.BooleanField('マッチング判定', default=0)

    def __str__(self):
        return self.comment