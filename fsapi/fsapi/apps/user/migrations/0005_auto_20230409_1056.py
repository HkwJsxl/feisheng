# Generated by Django 3.2.18 on 2023-04-09 10:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_auto_20230408_1656'),
        ('user', '0004_credit'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='study_time',
            field=models.IntegerField(default=0, verbose_name='总学习时长'),
        ),
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='姓名/名称/标题')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否显示')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('orders', models.SmallIntegerField(default=0, verbose_name='序号')),
                ('study_time', models.IntegerField(default=0, verbose_name='学习时长')),
                ('chapter', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_chapter', to='course.coursechapter', verbose_name='章节信息')),
                ('course', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='course_users', to='course.course', verbose_name='课程名称')),
                ('lesson', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_lesson', to='course.courselesson', verbose_name='课时信息')),
                ('user', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='user_courses', to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户课程购买记录',
                'verbose_name_plural': '用户课程购买记录',
                'db_table': 'fs_user_course',
            },
        ),
    ]
