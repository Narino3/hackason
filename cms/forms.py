from django.forms import ModelForm
from cms.models import *
from django import forms
from django.utils import timezone

# input欄の見栄え良くするwidget, 変更したいフォームで追加
widget_textarea = forms.Textarea(
    attrs={
        "class": "form-control"
    }
)
widget_textinput = forms.TextInput(
    attrs={
        "class": "form-control"
    }
)
comment = forms.CharField(
    widget=widget_textarea
)
recruit_title = forms.CharField(
    widget=widget_textinput, label="募集タイトル"
)

# 時間をカレンダーから入力
class BosyuForm(ModelForm):
    work_start_time = forms.DateTimeField(
        label='開始時刻',
        widget=forms.DateTimeInput(attrs={"type": "datetime-local", "value": timezone.datetime.now().strftime('%Y-%m-%dT%H:%M')}),
        input_formats=['%Y-%m-%d']
    )
    work_last_time = forms.DateTimeField(
        label='終了時刻',
        widget=forms.DateTimeInput(attrs={"type": "datetime-local", "value": timezone.datetime.now().strftime('%Y-%m-%dT%H:%M')}),
        input_formats=['%Y-%m-%dT%H:%M']
    )
    finish_time = forms.DateTimeField(
        label='募集締め切り時刻',
        widget=forms.DateTimeInput(attrs={"type": "datetime-local", "value": timezone.datetime.now().strftime('%Y-%m-%dT%H:%M')}),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    """書籍のフォーム"""
    class Meta:
        model = Recruit
        fields = ('recruit_title', 'shop_ID', 'person_type', 'person_number', 'work_start_time', 'work_last_time', 'finish_time', 'comment', 'password' )
        #fields = '__all__'
        widgets = {
            'person_type': forms.CheckboxSelectMultiple
        }

