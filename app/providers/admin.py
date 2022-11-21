from django.contrib import admin

from .models import (
    Address,
    Contact,
    District,
    Education,
    ImmunisationStatement,
    NextOfKin,
    OtherDetail,
    Relationship,
    Shift,
    Vaccination,
    WorkInterest,
    WorkSchedule,
    WorkType,
    Provider
)

admin.site.register(Address)
admin.site.register(Contact)
admin.site.register(District)
admin.site.register(Education)
admin.site.register(ImmunisationStatement)
admin.site.register(NextOfKin)
admin.site.register(OtherDetail)
admin.site.register(Relationship)
admin.site.register(Shift)
admin.site.register(Vaccination)
admin.site.register(WorkInterest)
admin.site.register(WorkSchedule)
admin.site.register(WorkType)
admin.site.register(Provider)
