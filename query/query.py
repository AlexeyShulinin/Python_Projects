from datetime import datetime

from django.db.models import Q, Count, Avg

from pytz import UTC

from db.models import User, Blog, Topic


def create():
    u1 = User(first_name='u1', last_name='u1')
    u1.save()
    u2 = User(first_name='u2', last_name='u2')
    u2.save()
    u3 = User(first_name='u3', last_name='u3')
    u3.save()
    blog1 = Blog(title='blog1', author=u1)
    blog1.save()
    blog2 = Blog(title='blog2', author=u1)
    blog2.save()
    blog1.subscribers.add(u1, u2)
    blog1.save()
    blog2.subscribers.add(u2)
    blog2.save()
    topic1 = Topic(title='topic1', blog=blog1, author=u1)
    topic1.save()
    topic2 = Topic(title='topic2_content', blog=blog1, author=u3, created=datetime(year=2017, month=1, day=1, tzinfo=UTC))
    topic2.save()
    topic1.likes.add(u1, u2, u3)
    topic1.save()


def edit_all():
    User.objects.all().update(first_name='uu1')


def edit_u1_u2():
    User.objects.filter(Q(first_name='u1') | Q(first_name='u2')).update(first_name='uu1')


def delete_u1():
    User.objects.get(first_name='u1').delete()


def unsubscribe_u2_from_blogs():
    user = User.objects.filter(first_name='u2')[0]
    for blog in Blog.objects.all():
        blog.subscribers.remove(user)

def get_topic_created_grated():
    return Topic.objects.filter(created__gt='2018-01-01')


def get_topic_title_ended():
    return Topic.objects.filter(title__endswith="content")


def get_user_with_limit():
    return User.objects.order_by('-id')[:2]


def get_topic_count():
    return Blog.objects.all().annotate(topic_count=Count('topic')).order_by('topic_count')


def get_avg_topic_count():
    return Blog.objects.annotate(topic_count=Count('topic')).aggregate(avg=Avg('topic_count'))


def get_blog_that_have_more_than_one_topic():
    return Blog.objects.all().annotate(topic_count=Count('topic')).filter(topic_count__gt=1)


def get_topic_by_u1():
    return Topic.objects.filter(author__first_name='u1')


def get_user_that_dont_have_blog():
    return User.objects.filter(blog__isnull=True).order_by('pk')


def get_topic_that_like_all_users():
    return Topic.objects.filter(likes=User.objects.all())


def get_topic_that_dont_have_like():
    return Topic.objects.filter(likes__isnull=True)
