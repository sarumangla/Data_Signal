# Generated by Django 4.1.7 on 2023-08-10 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_loan_amount', models.BigIntegerField()),
                ('annual_income', models.BigIntegerField()),
                ('monthly_debt', models.BigIntegerField()),
                ('number_of_open_accounts', models.BigIntegerField()),
                ('maximum_open_credit', models.BigIntegerField()),
                ('term', models.CharField(max_length=30)),
                ('home_ownership', models.CharField(max_length=30)),
                ('bankruptcies', models.IntegerField()),
                ('years_in_current_job', models.CharField(max_length=30)),
                ('pdf_file', models.FileField(upload_to='pdfs/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
