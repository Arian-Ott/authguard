from tortoise import fields, migrations
from tortoise.fields.base import OnDelete
from tortoise.migrations import operations as ops


class Migration(migrations.Migration):
    dependencies = [("models", "0002_auto_20260813_1337")]

    initial = False

    operations = [
        ops.CreateModel(
            name="UserRoleMapping",
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
                (
                    "user",
                    fields.ForeignKeyField(
                        "models.UserModel",
                        source_field="user_id",
                        db_constraint=True,
                        to_field="id",
                        on_delete=OnDelete.CASCADE,
                    ),
                ),
                (
                    "role",
                    fields.ForeignKeyField(
                        "models.RoleModel",
                        source_field="role_id",
                        db_constraint=True,
                        to_field="name",
                        on_delete=OnDelete.CASCADE,
                    ),
                ),
                (
                    "created_at",
                    fields.DatetimeField(auto_now=False, auto_now_add=True),
                ),
            ],
            options={
                "table": "ag_user_role_mapping",
                "app": "models",
                "unique_together": [("user_id", "role_id")],
                "pk_attr": "id",
            },
            bases=["Model"],
        ),
    ]
