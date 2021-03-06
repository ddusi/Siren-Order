import django.db.models.deletion
import django_extensions.db.fields
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Merchant",
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
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "Inactive"), (1, "Active")],
                        default=1,
                        verbose_name="status",
                    ),
                ),
                (
                    "activate_date",
                    models.DateTimeField(
                        blank=True,
                        help_text="keep empty for an immediate activation",
                        null=True,
                    ),
                ),
                (
                    "deactivate_date",
                    models.DateTimeField(
                        blank=True,
                        help_text="keep empty for indefinite activation",
                        null=True,
                    ),
                ),
                (
                    "merchant_number",
                    models.IntegerField(
                        db_index=True, unique=True, verbose_name="매장번호"
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="매장이름")),
                (
                    "type",
                    models.CharField(
                        default="store", max_length=30, verbose_name="매장유형"
                    ),
                ),
                (
                    "merchant_contract",
                    models.CharField(blank=True, max_length=50, verbose_name="매장연락처"),
                ),
                (
                    "addr",
                    models.CharField(blank=True, max_length=200, verbose_name="매장주소"),
                ),
                (
                    "addr_detail",
                    models.CharField(blank=True, max_length=100, verbose_name="상세주소"),
                ),
                ("addr_city", models.CharField(max_length=30, verbose_name="시,도")),
                ("addr_province", models.CharField(max_length=30, verbose_name="구,동")),
            ],
            options={
                "verbose_name": "매장",
                "verbose_name_plural": "매장 목록",
                "ordering": ["merchant_number"],
            },
        ),
        migrations.CreateModel(
            name="Partner",
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
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "Inactive"), (1, "Active")],
                        default=1,
                        verbose_name="status",
                    ),
                ),
                (
                    "activate_date",
                    models.DateTimeField(
                        blank=True,
                        help_text="keep empty for an immediate activation",
                        null=True,
                    ),
                ),
                (
                    "deactivate_date",
                    models.DateTimeField(
                        blank=True,
                        help_text="keep empty for indefinite activation",
                        null=True,
                    ),
                ),
                (
                    "employee_number",
                    models.IntegerField(
                        db_index=True, unique=True, verbose_name="사원번호"
                    ),
                ),
                (
                    "employment_date",
                    models.DateTimeField(null=True, verbose_name="입사날짜"),
                ),
                (
                    "rank",
                    models.CharField(blank=True, max_length=30, verbose_name="직급"),
                ),
                (
                    "is_store_manager",
                    models.BooleanField(default=False, verbose_name="매장관리자"),
                ),
                (
                    "nick_name",
                    models.CharField(blank=True, max_length=50, verbose_name="호칭"),
                ),
                (
                    "department",
                    models.CharField(blank=True, max_length=30, verbose_name="부서"),
                ),
                (
                    "merchant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="merchant_set",
                        to="client.merchant",
                        verbose_name="매장",
                    ),
                ),
            ],
            options={
                "verbose_name": "파트너",
                "verbose_name_plural": "파트너 목록",
                "ordering": ["employee_number"],
            },
        ),
        migrations.CreateModel(
            name="HistoricalPartner",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "Inactive"), (1, "Active")],
                        default=1,
                        verbose_name="status",
                    ),
                ),
                (
                    "activate_date",
                    models.DateTimeField(
                        blank=True,
                        help_text="keep empty for an immediate activation",
                        null=True,
                    ),
                ),
                (
                    "deactivate_date",
                    models.DateTimeField(
                        blank=True,
                        help_text="keep empty for indefinite activation",
                        null=True,
                    ),
                ),
                (
                    "employee_number",
                    models.IntegerField(db_index=True, verbose_name="사원번호"),
                ),
                (
                    "employment_date",
                    models.DateTimeField(null=True, verbose_name="입사날짜"),
                ),
                (
                    "rank",
                    models.CharField(blank=True, max_length=30, verbose_name="직급"),
                ),
                (
                    "is_store_manager",
                    models.BooleanField(default=False, verbose_name="매장관리자"),
                ),
                (
                    "nick_name",
                    models.CharField(blank=True, max_length=50, verbose_name="호칭"),
                ),
                (
                    "department",
                    models.CharField(blank=True, max_length=30, verbose_name="부서"),
                ),
                ("history_change_reason", models.TextField(null=True)),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "merchant",
                    models.ForeignKey(
                        blank=True,
                        db_constraint=False,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="+",
                        to="client.merchant",
                        verbose_name="매장",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical 파트너",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalMerchant",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        auto_created=True, blank=True, db_index=True, verbose_name="ID"
                    ),
                ),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                (
                    "status",
                    models.IntegerField(
                        choices=[(0, "Inactive"), (1, "Active")],
                        default=1,
                        verbose_name="status",
                    ),
                ),
                (
                    "activate_date",
                    models.DateTimeField(
                        blank=True,
                        help_text="keep empty for an immediate activation",
                        null=True,
                    ),
                ),
                (
                    "deactivate_date",
                    models.DateTimeField(
                        blank=True,
                        help_text="keep empty for indefinite activation",
                        null=True,
                    ),
                ),
                (
                    "merchant_number",
                    models.IntegerField(db_index=True, verbose_name="매장번호"),
                ),
                ("name", models.CharField(max_length=50, verbose_name="매장이름")),
                (
                    "type",
                    models.CharField(
                        default="store", max_length=30, verbose_name="매장유형"
                    ),
                ),
                (
                    "merchant_contract",
                    models.CharField(blank=True, max_length=50, verbose_name="매장연락처"),
                ),
                (
                    "addr",
                    models.CharField(blank=True, max_length=200, verbose_name="매장주소"),
                ),
                (
                    "addr_detail",
                    models.CharField(blank=True, max_length=100, verbose_name="상세주소"),
                ),
                ("addr_city", models.CharField(max_length=30, verbose_name="시,도")),
                ("addr_province", models.CharField(max_length=30, verbose_name="구,동")),
                ("history_change_reason", models.TextField(null=True)),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField()),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical 매장",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
