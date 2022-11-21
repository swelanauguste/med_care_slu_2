from django.conf import settings
from django.db import models
from django.urls import reverse

User = settings.AUTH_USER_MODEL


class Provider(models.Model):
    provider = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.provider.profile}"


class District(models.Model):
    district_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.district_name} ({self.pk})"


class Address(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, null=True)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True)
    postal_code = models.CharField(
        max_length=8,
        help_text="<em><a target='_blank' href='https://stluciapostal.com/postal-codes-2/'>Post Codes</a></em>",
    )

    # def get_postal_code(self):
    #     return self.postal_code.upper()

    def __str__(self):
        if self.address1 and self.address2 and self.district and self.postal_code:
            return f"{self.address1}, {self.address2}, {self.district.district_name}, {self.postal_code}"
        return f"{self.provider} address"


class Contact(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, null=True)
    tel1 = models.CharField(max_length=50, help_text="eg: 758-489-4565")
    tel2 = models.CharField(
        max_length=50, help_text="eg: 758-489-4565", blank=True, null=True
    )
    email1 = models.EmailField("alternative email, if any?", blank=True, null=True)

    def __str__(self):
        if self.tel1 or self.tel2:
            if self.email1:
                return f"{self.provider}, {self.tel1} {self.tel2}, {self.email1}"
            return f"{self.provider}, {self.tel1} {self.tel2}"
        return f"{self.provider} nas no additional contact information"


class OtherDetail(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, null=True)
    driver_license = models.BooleanField(
        "Do you have a current driving license?", default=False
    )
    transport = models.BooleanField("Do you have transport?", default=False)
    language = models.BooleanField("Do you speak any foreign languages?", default=False)
    languages = models.TextField(blank=True)

    def __str__(self):
        return f"{self.provider} ({self.driver_license})"


class Education(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, null=True)
    course = models.CharField(max_length=100, null=True)
    date = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.course}, {self.date}"


class Relationship(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name


class NextOfKin(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, null=True)
    nok_name = models.CharField(max_length=200)
    nok_address = models.ForeignKey("Address", on_delete=models.SET_NULL, null=True)
    nok_contact = models.ForeignKey("Contact", on_delete=models.SET_NULL, null=True)
    relationship = models.ForeignKey(
        "Relationship", on_delete=models.SET_NULL, null=True
    )

    def __str__(self) -> str:
        return f"{self.provider}'s KON {self.nok_name}"


class WorkType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Shift(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class WorkSchedule(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class WorkInterest(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.SET_NULL, null=True)
    work_type = models.ManyToManyField(WorkType)
    preferred_shift = models.ManyToManyField(Shift)
    other_commitments = models.BooleanField(
        "Do you have other commitments?", default=False
    )
    work_schedule = models.ForeignKey(
        WorkSchedule, on_delete=models.SET_NULL, null=True
    )

    def __str__(self) -> str:
        return f"{self.provider} work interest {self.work_type.values_list()}"


class Vaccination(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class ImmunisationStatement(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, null=True)
    vaccination = models.ForeignKey(Vaccination, on_delete=models.SET_NULL, null=True)
    i_date = models.DateField("injection date", blank=True, null=True)
    b_date = models.DateField("booster due", blank=True, null=True)

    def __str__(self):
        return f"{self.provider} vaccinations"
