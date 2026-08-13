from tortoise import fields, migrations
from tortoise.migrations import operations as ops


class Migration(migrations.Migration):
    initial = True

    operations = [
        ops.CreateModel(
            name="UserModel",
            fields=[
                (
                    "id",
                    fields.BigIntField(
                        generated=True,
                        primary_key=True,
                        unique=True,
                        db_index=True,
                    ),
                ),
                ("username", fields.CharField(unique=True, max_length=32)),
                ("email", fields.CharField(unique=True, max_length=255)),
                ("password", fields.CharField(max_length=255)),
                ("first_name", fields.CharField(max_length=65)),
                ("last_name", fields.CharField(max_length=65)),
                ("is_active", fields.BooleanField(default=True)),
                (
                    "created_at",
                    fields.DatetimeField(auto_now=False, auto_now_add=True),
                ),
                (
                    "updated_at",
                    fields.DatetimeField(auto_now=True, auto_now_add=False),
                ),
            ],
            options={"table": "ag_users", "app": "models", "pk_attr": "id"},
            bases=["Model"],
        ),
    ]
