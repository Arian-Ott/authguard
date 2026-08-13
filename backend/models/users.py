from tortoise import Model, fields


class UserModel(Model):
    id = fields.BigIntField(primary_key=True)
    username = fields.CharField(max_length=32, unique=True)
    email = fields.CharField(max_length=255, unique=True)
    password = fields.CharField(max_length=255)

    first_name = fields.CharField(max_length=65)
    last_name = fields.CharField(max_length=65)

    is_active = fields.BooleanField(default=True)
    created_at = fields.DateTimeField(auto_now_add=True)
    updated_at = fields.DateTimeField(auto_now=True)

    class Meta:
        table = "ag_users"


class UserRoleMapping(Model):
    id = fields.BigIntField(primary_key=True)
    user = fields.ForeignKeyField("models.UserModel")
    role = fields.ForeignKeyField("models.RoleModel")
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "ag_user_role_mapping"
        unique_together = [("user_id", "role_id")]


class RoleModel(Model):
    name = fields.CharField(primary_key=True, max_length=16)
    description = fields.CharField(max_length=512)

    class Meta:
        table = "ag_roles"
