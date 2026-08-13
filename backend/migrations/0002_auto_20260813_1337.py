from tortoise import fields, migrations
from tortoise.migrations import operations as ops


class Migration(migrations.Migration):
    dependencies = [("models", "0001_initial")]

    initial = False

    operations = [
        ops.CreateModel(
            name="RoleModel",
            fields=[
                (
                    "name",
                    fields.CharField(
                        primary_key=True,
                        unique=True,
                        db_index=True,
                        max_length=16,
                    ),
                ),
                ("description", fields.CharField(max_length=512)),
            ],
            options={"table": "ag_roles", "app": "models", "pk_attr": "name"},
            bases=["Model"],
        ),
    ]
