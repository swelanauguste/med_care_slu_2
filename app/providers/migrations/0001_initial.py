# Generated by Django 4.1.3 on 2022-11-01 23:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("address1", models.CharField(max_length=255)),
                ("address2", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "postal_code",
                    models.CharField(
                        help_text="<em><a target='_blank' href='https://stluciapostal.com/postal-codes-2/'>Post Codes</a></em>",
                        max_length=8,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tel1", models.CharField(max_length=50)),
                ("tel2", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "email",
                    models.EmailField(
                        blank=True,
                        max_length=254,
                        null=True,
                        verbose_name="alternative email, if any?",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="District",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("district_name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Provider",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "provider",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Relationship",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Shift",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Vaccination",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="WorkSchedule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="WorkType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="WorkInterest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "other_commitments",
                    models.BooleanField(
                        default=False, verbose_name="Do you have other commitments?"
                    ),
                ),
                ("preferred_shift", models.ManyToManyField(to="providers.shift")),
                (
                    "provider",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="providers.provider",
                    ),
                ),
                (
                    "work_schedule",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="providers.workschedule",
                    ),
                ),
                ("work_type", models.ManyToManyField(to="providers.worktype")),
            ],
        ),
        migrations.CreateModel(
            name="OtherDetail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "driver_license",
                    models.BooleanField(
                        default=False,
                        verbose_name="Do you have a current driving license?",
                    ),
                ),
                (
                    "transport",
                    models.BooleanField(
                        default=False, verbose_name="Do you have transport?"
                    ),
                ),
                (
                    "language",
                    models.BooleanField(
                        default=False,
                        verbose_name="Do you speak any foreign languages?",
                    ),
                ),
                ("languages", models.TextField(blank=True)),
                (
                    "provider",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="providers.provider",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NextOfKin",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nok_name", models.CharField(max_length=200)),
                (
                    "nok_address",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="providers.address",
                    ),
                ),
                (
                    "nok_contact",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="providers.contact",
                    ),
                ),
                (
                    "provider",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="providers.provider",
                    ),
                ),
                (
                    "relationship",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="providers.relationship",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ImmunisationStatement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "i_date",
                    models.DateField(
                        blank=True, null=True, verbose_name="injection date"
                    ),
                ),
                (
                    "b_date",
                    models.DateField(blank=True, null=True, verbose_name="booster due"),
                ),
                (
                    "provider",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="providers.provider",
                    ),
                ),
                (
                    "vaccination",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="providers.vaccination",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Education",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("course", models.CharField(max_length=100, null=True)),
                ("date", models.DateField(blank=True, null=True)),
                (
                    "provider",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="providers.provider",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="contact",
            name="provider",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="providers.provider",
            ),
        ),
        migrations.AddField(
            model_name="address",
            name="district",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="providers.district"
            ),
        ),
        migrations.AddField(
            model_name="address",
            name="provider",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="providers.provider",
            ),
        ),
    ]
