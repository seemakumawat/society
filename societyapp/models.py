# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Admin(models.Model):
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'admin'


class Advertisement(models.Model):
    advertise_id = models.AutoField(db_column='ADVERTISE_ID', primary_key=True)  # Field name made lowercase.
    member = models.ForeignKey('Member', models.DO_NOTHING, db_column='MEMBER_ID', blank=True, null=True)  # Field name made lowercase.     
    date = models.DateField(db_column='DATE')  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=50)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'advertisement'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Booking(models.Model):
    booking_id = models.AutoField(db_column='BOOKING_ID', primary_key=True)  # Field name made lowercase.
    member = models.ForeignKey('Member', models.DO_NOTHING, db_column='MEMBER_ID')  # Field name made lowercase.
    starting_date = models.DateTimeField(db_column='STARTING_DATE')  # Field name made lowercase.
    ending_date = models.DateTimeField(db_column='ENDING_DATE')  # Field name made lowercase.
    event_name = models.CharField(db_column='EVENT_NAME', max_length=15)  # Field name made lowercase.
    booking_date = models.DateField(db_column='BOOKING_DATE', blank=True, null=True)  # Field name made lowercase.       
    status = models.CharField(db_column='STATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.    
    total = models.IntegerField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'booking'


class BookingDetail(models.Model):
    booking_detail_id = models.AutoField(db_column='BOOKING_DETAIL_ID', primary_key=True)  # Field name made lowercase.  
    booking = models.ForeignKey(Booking, models.DO_NOTHING, db_column='BOOKING_ID')  # Field name made lowercase.
    item = models.ForeignKey('Items', models.DO_NOTHING, db_column='ITEM_ID')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='QUANTITY')  # Field name made lowercase.
    amount = models.IntegerField(db_column='AMOUNT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'booking_detail'


class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    member = models.ForeignKey('Member', models.DO_NOTHING)
    item = models.ForeignKey('Items', models.DO_NOTHING)
    quantity = models.IntegerField()
    rate = models.IntegerField()
    total = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cart'

class Committee(models.Model):
    committee_id = models.AutoField(db_column='COMMITTEE_ID', primary_key=True)  # Field name made lowercase.
    work_of_committee = models.CharField(db_column='WORK_OF_COMMITTEE', max_length=30)  # Field name made lowercase.
    no_of_members = models.IntegerField(db_column='NO._OF_MEMBERS')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    committee_creation_date = models.DateField(db_column='COMMITTEE_CREATION_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'committee'


class CommitteeDetails(models.Model):
    committee_detail_id = models.AutoField(db_column='COMMITTEE_DETAIL_ID', primary_key=True)  # Field name made lowercase.
    committee = models.ForeignKey(Committee, models.DO_NOTHING, db_column='COMMITTEE_ID', blank=True, null=True)  # Field name made lowercase.
    member = models.ForeignKey('Member', models.DO_NOTHING, db_column='MEMBER_ID', blank=True, null=True)  # Field name made lowercase.     
    member_joining_date = models.DateField(db_column='MEMBER_JOINING_DATE')  # Field name made lowercase.
    member_leaving_date = models.DateField(db_column='MEMBER_LEAVING_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'committee_details'


class Complaint(models.Model):
    complaint_id = models.AutoField(db_column='COMPLAINT_ID', primary_key=True)  # Field name made lowercase.
    member = models.ForeignKey('Member', models.DO_NOTHING, db_column='MEMBER_ID', blank=True, null=True)  # Field name made lowercase.     
    description = models.CharField(db_column='DESCRIPTION', max_length=50)  # Field name made lowercase.
    complaint_date = models.DateField(db_column='COMPLAINT_DATE')  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    solution_date = models.DateField(db_column='SOLUTION_DATE', blank=True, null=True)  # Field name made lowercase.
    committee_detail = models.ForeignKey(CommitteeDetails, models.DO_NOTHING, db_column='COMMITTEE_DETAIL_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'complaint'


class Deposit(models.Model):
    deposit_id = models.AutoField(db_column='DEPOSIT_ID', primary_key=True)  # Field name made lowercase.
    bank_name = models.CharField(db_column='BANK_NAME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=30)  # Field name made lowercase.
    rate = models.IntegerField(db_column='RATE')  # Field name made lowercase.
    deposit_amount = models.IntegerField(db_column='DEPOSIT_AMOUNT')  
# Field name made lowercase.
    deposit_date = models.DateField(db_column='DEPOSIT_DATE')  # Field name made lowercase.
    maturity_date = models.DateField(db_column='MATURITY_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'deposit'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)   
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Expense(models.Model):
    expence_id = models.AutoField(db_column='EXPENCE_ID', primary_key=True)  # Field name made lowercase.
    function = models.ForeignKey('Function', models.DO_NOTHING, db_column='FUNCTION_ID', blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='DATE')  # Field name made lowercase.
    amount = models.IntegerField(db_column='AMOUNT')  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'expense'


class Function(models.Model):
    function_id = models.AutoField(db_column='FUNCTION_ID', primary_key=True)  # Field name made lowercase.
    function_name = models.CharField(db_column='FUNCTION_NAME', max_length=30)  # Field name made lowercase.
    function_place = models.CharField(db_column='FUNCTION_PLACE', max_length=15)  # Field name made lowercase.
    amount_per_member = models.IntegerField(db_column='AMOUNT_PER_MEMBER')  # Field name made lowercase.
    fdate = models.DateField(db_column='FDATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'function'


class Income(models.Model):
    income_id = models.AutoField(db_column='INCOME_ID', primary_key=True)  # Field name made lowercase.
    member_maintenance = models.ForeignKey('MemberMaintenance', models.DO_NOTHING, db_column='MEMBER_MAINTENANCE_ID', blank=True, null=True)  # Field name made lowercase.
    deposit = models.ForeignKey(Deposit, models.DO_NOTHING, db_column='DEPOSIT_ID', blank=True, null=True)  # Field name made lowercase.    
    booking = models.ForeignKey(Booking, models.DO_NOTHING, db_column='BOOKING_ID', blank=True, null=True)  # Field name made lowercase.    
    society_event_fund = models.CharField(db_column='SOCIETY_EVENT_FUND', max_length=30, blank=True, null=True)  # Field name made lowercase.
    date = models.DateField(db_column='DATE', blank=True, null=True)  
# Field name made lowercase.
    amount = models.IntegerField(db_column='AMOUNT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'income'


class Items(models.Model):
    item_id = models.AutoField(db_column='ITEM_ID', primary_key=True) 
 # Field name made lowercase.
    item_name = models.CharField(db_column='ITEM_NAME', max_length=20)  # Field name made lowercase.
    total_quantity = models.IntegerField(db_column='TOTAL_QUANTITY')  
# Field name made lowercase.
    price_per_unit = models.IntegerField(db_column='PRICE_PER_UNIT')  
# Field name made lowercase.
    image = models.CharField(db_column='IMAGE', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'items'

    class Meta:
        managed = False
        db_table = 'items'


class Maintenance(models.Model):
    maintenance_id = models.AutoField(db_column='MAINTENANCE_ID', primary_key=True)  # Field name made lowercase.
    month_year = models.CharField(db_column='MONTH/YEAR', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_income = models.IntegerField(db_column='TOTAL_INCOME')  # Field name made lowercase.
    total_expence = models.IntegerField(db_column='TOTAL_EXPENCE')  # Field name made lowercase.
    amount_required = models.IntegerField(db_column='AMOUNT_REQUIRED')  # Field name made lowercase.
    no_of_member = models.IntegerField(db_column='NO._OF_MEMBER')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    maintenance_amount = models.IntegerField(db_column='MAINTENANCE_AMOUNT')  # Field name made lowercase.
    last_date = models.DateField(db_column='LAST_DATE')  # Field name made lowercase.
    late_charges = models.IntegerField(db_column='LATE_CHARGES', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'maintenance'


class Member(models.Model):
    member_id = models.AutoField(db_column='MEMBER_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=20)  # Field name made lowercase.
    date_of_birth = models.DateField(db_column='DATE_OF_BIRTH', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=25)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=15)  
# Field name made lowercase.
    contact_no_field = models.BigIntegerField(db_column='CONTACT_NO.')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    flat_no_field = models.IntegerField(db_column='FLAT_NO.')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    block_no_field = models.CharField(db_column='BLOCK_NO.', max_length=1)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    gender = models.CharField(db_column='GENDER', max_length=6)  # Field name made lowercase.
    religion = models.CharField(db_column='RELIGION', max_length=10, blank=True, null=True)  # Field name made lowercase.
    house_status = models.CharField(db_column='HOUSE_STATUS', max_length=10)  # Field name made lowercase.
    member_status = models.CharField(db_column='MEMBER_STATUS', max_length=10)  # Field name made lowercase.
    comming_date = models.DateField(db_column='COMMING_DATE')  # Field name made lowercase.
    leaving_date = models.DateField(db_column='LEAVING_DATE', blank=True, null=True)  # Field name made lowercase.
    family_member = models.IntegerField(db_column='FAMILY_MEMBER', blank=True, null=True)  # Field name made lowercase.
    profile = models.CharField(db_column='PROFILE', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'member'


class MemberFunction(models.Model):
    member_function_id = models.AutoField(db_column='MEMBER_FUNCTION_ID', primary_key=True)  # Field name made lowercase.
    function = models.ForeignKey(Function, models.DO_NOTHING, db_column='FUNCTION_ID')  # Field name made lowercase.
    member = models.ForeignKey(Member, models.DO_NOTHING, db_column='MEMBER_ID')  # Field name made lowercase.
    amount = models.IntegerField(db_column='AMOUNT')  # Field name made lowercase.
    pay_date = models.DateField(db_column='PAY_DATE')  # Field name made lowercase.
    no_of_pass = models.IntegerField(db_column='NO._OF_PASS')  # Field name made lowercase. Field renamed to remove unsuitable characters.  
    status = models.CharField(db_column='STATUS', max_length=10)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'member_function'


class MemberMaintenance(models.Model):
    member_maintenance_id = models.AutoField(db_column='MEMBER_MAINTENANCE_ID', primary_key=True)  # Field name made lowercase.
    maintenance = models.ForeignKey(Maintenance, models.DO_NOTHING, db_column='MAINTENANCE_ID')  # Field name made lowercase.
    member = models.ForeignKey(Member, models.DO_NOTHING, db_column='MEMBER_ID')  # Field name made lowercase.
    pay_date = models.DateField(db_column='PAY_DATE')  # Field name made lowercase.
    amount = models.IntegerField(db_column='AMOUNT')  # Field name made lowercase.
    late_charges = models.IntegerField(db_column='LATE_CHARGES', blank=True, null=True)  # Field name made lowercase.
    total = models.IntegerField(db_column='TOTAL')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'member_maintenance'


class Notice(models.Model):
    notice_id = models.AutoField(db_column='NOTICE_ID', primary_key=True)  # Field name made lowercase.
    committee = models.ForeignKey(Committee, models.DO_NOTHING, db_column='COMMITTEE_ID')  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=50)  # Field name made lowercase.
    date = models.DateField(db_column='DATE')  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'notice'


class Occupant(models.Model):
    occupant_id = models.AutoField(db_column='OCCUPANT_ID', primary_key=True)  # Field name made lowercase.
    member = models.ForeignKey(Member, models.DO_NOTHING, db_column='MEMBER_ID')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=20)  # Field name made lowercase.
    gender = models.CharField(db_column='GENDER', max_length=6)  # Field name made lowercase.
    religion = models.CharField(db_column='RELIGION', max_length=15, blank=True, null=True)  # Field name made lowercase.
    comming_date = models.DateField(db_column='COMMING_DATE')  # Field name made lowercase.
    rent_amount = models.IntegerField(db_column='RENT_AMOUNT', blank=True, null=True)  # Field name made lowercase.
    no_of_family_member = models.IntegerField(db_column='NO._OF_FAMILY_MEMBER', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    profile = models.CharField(db_column='PROFILE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    leaving_date = models.DateField(db_column='LEAVING_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'occupant'
