
# 커스텀 필터를 만들것
# 1. content 를 받아와 해시태그만 a 태그로 변경

# 필수 정의 영영

from django import template
from articles.models import Hashtag
from django.shortcuts import resolve_url # a태그를 클릭했을때 해당 url로 이동해야하니까
from django.utils.safestring import mark_safe
# name > url 로 볼 수 있는것


register = template.Library()


# 내가 만든 커스텀 함수
# value : content가 넘어온거고
# arg : 뒤에 작성한 내용
def set_hashtag(value):
    contents = value.replace('\r\n', ' ').split(' ')
    for i in range(len(contents)):
        if contents[i].startswith('#'):
            hashtag = contents[i][1:]
            # 문제점 : #으로 시작하는 모든 단어는 무조건 해시태그다 !!!! 라는 확신이있어야함
            try:
                hashtag_obj = Hashtag.objects.get(content=hashtag)
                # a 태그로 변경 (index를 참조해서 보기위해)
                contents[i] = f'<a href="{resolve_url("articles:hashtag", hashtag_obj.pk)}">#{hashtag}</a>'
            except Hashtag.DoesNotExist:
                # #으로시작하지만 해시태그에 없으면 pass처리
                pass
            # 공백으로 합쳐서 종료
    return mark_safe(' '.join(contents))

    """Removes all values of arg from the given string"""
    return "필터적용후"
    # return value.replace(arg, '')

# 커스텀 함수를 filter에 등록
register.filter('set_hashtag', set_hashtag)