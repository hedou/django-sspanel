# Generated by Django 2.0.5 on 2018-06-18 21:17

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

import apps.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [("auth", "0009_alter_user_last_name_max_length")]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=30, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("invitecode", models.CharField(max_length=40, verbose_name="邀请码")),
                (
                    "invited_by",
                    models.PositiveIntegerField(default=1, verbose_name="邀请人id"),
                ),
                (
                    "balance",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=0,
                        max_digits=10,
                        null=True,
                        verbose_name="余额",
                    ),
                ),
                (
                    "invitecode_num",
                    models.PositiveIntegerField(default=5, verbose_name="可生成的邀请码数量"),
                ),
                (
                    "level",
                    models.PositiveIntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MaxValueValidator(9),
                            django.core.validators.MinValueValidator(0),
                        ],
                        verbose_name="用户等级",
                    ),
                ),
                (
                    "level_expire_time",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="等级有效期"
                    ),
                ),
                (
                    "theme",
                    models.CharField(
                        choices=[
                            ("default", "default"),
                            ("darkly", "darkly"),
                            ("flatly", "flatly"),
                            ("journal", "journal"),
                            ("materia", "materia"),
                            ("minty", "minty"),
                            ("spacelab", "spacelab"),
                            ("superhero", "superhero"),
                        ],
                        default="superhero",
                        max_length=10,
                        verbose_name="主题",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "用户",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[("objects", django.contrib.auth.models.UserManager())],
        ),
        migrations.CreateModel(
            name="Announcement",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("time", models.DateTimeField(auto_now_add=True, verbose_name="时间")),
                ("body", models.TextField(verbose_name="主体")),
            ],
            options={"verbose_name_plural": "系统公告", "ordering": ("-time",)},
        ),
        migrations.CreateModel(
            name="Donate",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("time", models.DateTimeField(auto_now_add=True, verbose_name="捐赠时间")),
                (
                    "money",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=0,
                        max_digits=10,
                        null=True,
                        verbose_name="捐赠金额",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="捐赠人",
                    ),
                ),
            ],
            options={"verbose_name_plural": "捐赠记录", "ordering": ("-time",)},
        ),
        migrations.CreateModel(
            name="Goods",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        default="待编辑", max_length=128, verbose_name="商品名字"
                    ),
                ),
                (
                    "content",
                    models.CharField(
                        default="待编辑", max_length=256, verbose_name="商品描述"
                    ),
                ),
                (
                    "transfer",
                    models.BigIntegerField(default=1073741824, verbose_name="增加的流量"),
                ),
                (
                    "money",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=0,
                        max_digits=10,
                        null=True,
                        verbose_name="金额",
                    ),
                ),
                (
                    "level",
                    models.PositiveIntegerField(
                        default=0,
                        validators=[
                            django.core.validators.MaxValueValidator(9),
                            django.core.validators.MinValueValidator(0),
                        ],
                        verbose_name="设置等级",
                    ),
                ),
                (
                    "days",
                    models.PositiveIntegerField(
                        default=1,
                        validators=[
                            django.core.validators.MaxValueValidator(365),
                            django.core.validators.MinValueValidator(1),
                        ],
                        verbose_name="设置等级时间(天)",
                    ),
                ),
                (
                    "status",
                    models.SmallIntegerField(
                        choices=[(1, "上架"), (-1, "下架")], default=1, verbose_name="商品状态"
                    ),
                ),
                (
                    "order",
                    models.PositiveSmallIntegerField(default=1, verbose_name="排序"),
                ),
            ],
            options={"verbose_name_plural": "商品", "ordering": ["order"]},
        ),
        migrations.CreateModel(
            name="InviteCode",
            fields=[
                (
                    "code_type",
                    models.IntegerField(
                        choices=[(1, "公开"), (0, "不公开")], default=0, verbose_name="类型"
                    ),
                ),
                (
                    "code_id",
                    models.PositiveIntegerField(default=1, verbose_name="邀请人ID"),
                ),
                (
                    "code",
                    models.CharField(
                        blank=True,
                        default=apps.utils.get_long_random_string,
                        max_length=40,
                        primary_key=True,
                        serialize=False,
                        verbose_name="邀请码",
                    ),
                ),
                (
                    "time_created",
                    models.DateTimeField(auto_now_add=True, verbose_name="创建时间"),
                ),
                ("isused", models.BooleanField(default=False, verbose_name="是否使用")),
            ],
            options={
                "verbose_name_plural": "邀请码",
                "ordering": ("isused", "-time_created"),
            },
        ),
        migrations.CreateModel(
            name="MoneyCode",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "user",
                    models.CharField(
                        blank=True, max_length=128, null=True, verbose_name="用户名"
                    ),
                ),
                ("time", models.DateTimeField(auto_now_add=True, verbose_name="捐赠时间")),
                (
                    "code",
                    models.CharField(
                        blank=True,
                        default=apps.utils.get_long_random_string,
                        max_length=40,
                        unique=True,
                        verbose_name="充值码",
                    ),
                ),
                (
                    "number",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=10,
                        max_digits=10,
                        null=True,
                        verbose_name="捐赠金额",
                    ),
                ),
                ("isused", models.BooleanField(default=False, verbose_name="是否使用")),
            ],
            options={"verbose_name_plural": "充值码", "ordering": ("isused",)},
        ),
        migrations.CreateModel(
            name="PayRecord",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=64, verbose_name="用户名")),
                (
                    "info_code",
                    models.CharField(max_length=64, unique=True, verbose_name="流水号"),
                ),
                ("time", models.DateTimeField(auto_now_add=True, verbose_name="时间")),
                (
                    "amount",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=0,
                        max_digits=10,
                        null=True,
                        verbose_name="金额",
                    ),
                ),
                (
                    "money_code",
                    models.CharField(max_length=64, unique=True, verbose_name="充值码"),
                ),
                (
                    "charge_type",
                    models.CharField(
                        default=1,
                        help_text="1：支付宝 2：QQ钱包 3：微信支付",
                        max_length=10,
                        verbose_name="充值类型",
                    ),
                ),
            ],
            options={"verbose_name_plural": "支付转账记录", "ordering": ("-time",)},
        ),
        migrations.CreateModel(
            name="PayRequest",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=64, verbose_name="用户名")),
                (
                    "info_code",
                    models.CharField(max_length=64, unique=True, verbose_name="流水号"),
                ),
                ("time", models.DateTimeField(auto_now_add=True, verbose_name="时间")),
                (
                    "amount",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=0,
                        max_digits=10,
                        null=True,
                        verbose_name="金额",
                    ),
                ),
                (
                    "charge_type",
                    models.CharField(
                        default=1,
                        help_text="1：支付宝 2：QQ钱包 3：微信支付",
                        max_length=10,
                        verbose_name="充值类型",
                    ),
                ),
            ],
            options={"verbose_name_plural": "支付申请记录", "ordering": ("-time",)},
        ),
        migrations.CreateModel(
            name="PurchaseHistory",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user", models.CharField(max_length=128, verbose_name="购买者")),
                (
                    "money",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=0,
                        max_digits=10,
                        null=True,
                        verbose_name="金额",
                    ),
                ),
                (
                    "purchtime",
                    models.DateTimeField(auto_now_add=True, verbose_name="购买时间"),
                ),
                (
                    "good",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="sspanel.Goods",
                        verbose_name="商品名",
                    ),
                ),
            ],
            options={"verbose_name_plural": "购买记录", "ordering": ("-purchtime",)},
        ),
        migrations.CreateModel(
            name="RebateRecord",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "user_id",
                    models.PositiveIntegerField(default=1, verbose_name="返利人ID"),
                ),
                (
                    "rebatetime",
                    models.DateTimeField(auto_now_add=True, verbose_name="返利时间"),
                ),
                (
                    "money",
                    models.DecimalField(
                        blank=True,
                        decimal_places=2,
                        default=0,
                        max_digits=10,
                        null=True,
                        verbose_name="金额",
                    ),
                ),
            ],
            options={"ordering": ("-rebatetime",)},
        ),
        migrations.CreateModel(
            name="Ticket",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("time", models.DateTimeField(auto_now_add=True, verbose_name="时间")),
                ("title", models.CharField(max_length=128, verbose_name="标题")),
                ("body", models.TextField(verbose_name="内容主体")),
                (
                    "status",
                    models.SmallIntegerField(
                        choices=[(1, "开启"), (-1, "关闭")], default=1, verbose_name="状态"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="用户",
                    ),
                ),
            ],
            options={"verbose_name_plural": "工单", "ordering": ("-time",)},
        ),
    ]
