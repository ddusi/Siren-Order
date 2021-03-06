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
                        db_index=True, unique=True, verbose_name="????????????"
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="????????????")),
                (
                    "type",
                    models.CharField(
                        default="store", max_length=30, verbose_name="????????????"
                    ),
                ),
                (
                    "merchant_contract",
                    models.CharField(blank=True, max_length=50, verbose_name="???????????????"),
                ),
                (
                    "addr",
                    models.CharField(blank=True, max_length=200, verbose_name="????????????"),
                ),
                (
                    "addr_detail",
                    models.CharField(blank=True, max_length=100, verbose_name="????????????"),
                ),
                ("addr_city", models.CharField(max_length=30, verbose_name="???,???")),
                ("addr_province", models.CharField(max_length=30, verbose_name="???,???")),
            ],
            options={
                "verbose_name": "??????",
                "verbose_name_plural": "?????? ??????",
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
                        db_index=True, unique=True, verbose_name="????????????"
                    ),
                ),
                (
                    "employment_date",
                    models.DateTimeField(null=True, verbose_name="????????????"),
                ),
                (
                    "rank",
                    models.CharField(blank=True, max_length=30, verbose_name="??????"),
                ),
                (
                    "is_store_manager",
                    models.BooleanField(default=False, verbose_name="???????????????"),
                ),
                (
                    "nick_name",
                    models.CharField(blank=True, max_length=50, verbose_name="??????"),
                ),
                (
                    "department",
                    models.CharField(blank=True, max_length=30, verbose_name="??????"),
                ),
                (
                    "merchant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="merchant_set",
                        to="client.merchant",
                        verbose_name="??????",
                    ),
                ),
            ],
            options={
                "verbose_name": "?????????",
                "verbose_name_plural": "????????? ??????",
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
                    models.IntegerField(db_index=True, verbose_name="????????????"),
                ),
                (
                    "employment_date",
                    models.DateTimeField(null=True, verbose_name="????????????"),
                ),
                (
                    "rank",
                    models.CharField(blank=True, max_length=30, verbose_name="??????"),
                ),
                (
                    "is_store_manager",
                    models.BooleanField(default=False, verbose_name="???????????????"),
                ),
                (
                    "nick_name",
                    models.CharField(blank=True, max_length=50, verbose_name="??????"),
                ),
                (
                    "department",
                    models.CharField(blank=True, max_length=30, verbose_name="??????"),
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
                        verbose_name="??????",
                    ),
                ),
            ],
            options={
                "verbose_name": "historical ?????????",
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
                    models.IntegerField(db_index=True, verbose_name="????????????"),
                ),
                ("name", models.CharField(max_length=50, verbose_name="????????????")),
                (
                    "type",
                    models.CharField(
                        default="store", max_length=30, verbose_name="????????????"
                    ),
                ),
                (
                    "merchant_contract",
                    models.CharField(blank=True, max_length=50, verbose_name="???????????????"),
                ),
                (
                    "addr",
                    models.CharField(blank=True, max_length=200, verbose_name="????????????"),
                ),
                (
                    "addr_detail",
                    models.CharField(blank=True, max_length=100, verbose_name="????????????"),
                ),
                ("addr_city", models.CharField(max_length=30, verbose_name="???,???")),
                ("addr_province", models.CharField(max_length=30, verbose_name="???,???")),
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
                "verbose_name": "historical ??????",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": "history_date",
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
