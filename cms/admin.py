from django.contrib import admin

# Register your models here.
from django.contrib import admin
from cms.models import Book, Impression, Recruit,Entry



class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'publisher', 'page',)  # 一覧に出したい項目
    list_display_links = ('id', 'name',)  # 修正リンクでクリックできる項目


admin.site.register(Book, BookAdmin)


class ImpressionAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment',)
    list_display_links = ('id', 'comment',)
    raw_id_fields = ('book',)   # 外部キーをプルダウンにしない（データ件数が増加時のタイムアウトを予防）


admin.site.register(Impression, ImpressionAdmin)


class EntryAdmin(admin.ModelAdmin):
    list_display = ('entry_ID', 'shop_ID', 'post_time', 'person_type', 'person_number', 'comment', 'finish_flag',)
    list_display_links =('entry_ID', 'shop_ID', 'post_time', 'person_type', 'person_number', 'comment', 'finish_flag',)
    
admin.site.register(Entry, EntryAdmin)

