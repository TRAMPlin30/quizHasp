from django.contrib import admin
from django.contrib.auth.models import User
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget

from questions.models import Test
from result.models import Result


class ResultResource(resources.ModelResource):
    user = fields.Field(column_name='user', attribute='user', widget=ForeignKeyWidget(User, 'username'))
    test = fields.Field(column_name='test', attribute='test', widget=ForeignKeyWidget(Test, 'name'))

    class Meta:
        model = Result


@admin.register(Result)
class ResultAdmin(ImportExportModelAdmin):
    list_display = ('user', 'test', 'score')
    resource_class = ResultResource
    pass

# admin.site.register(Result)
