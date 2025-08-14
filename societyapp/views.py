from django.shortcuts import render,redirect
from societyapp.models import *
from django.core.files.storage import FileSystemStorage
from datetime import *
import calendar
# Create your views here.
def index(request):
    return render(request,"index.html")

def index1(request):
    return render(request,"index1.html")

def index2(request):
    if request.session.has_key('id')==False:
        return redirect('/alogin/')
    members=Member.objects.all()
    occupants=Occupant.objects.all()
    advertisements=Advertisement.objects.all()
    bookings=Booking.objects.all()
    committees=Committee.objects.all()
    deposits=Deposit.objects.all()
    expenses=Expense.objects.all()
    functions=Function.objects.all()
    items=Items.objects.all()
    complaints=Complaint.objects.all()
    incomes=Income.objects.all()
    maintenances=Maintenance.objects.all()
    notices=Notice.objects.all()
    mcnt=0
    ocnt=0
    acnt=0
    bcnt=0
    ccnt=0
    dcnt=0
    ecnt=0
    fcnt=0
    icnt=0
    cocnt=0
    incnt=0
    macnt=0
    ncnt=0
    for i in members:
        mcnt=mcnt+1
    for i in occupants:
        ocnt=ocnt+1
    for i in advertisements:
        if i.status == 'pending':
            acnt=acnt+1
    for i in bookings:
        bcnt=bcnt+1
    for i in committees:
        ccnt=ccnt+1
    for i in deposits:
        dcnt=dcnt+i.deposit_amount
    for i in expenses:
        ecnt=ecnt+i.amount
    for i in functions:
        fcnt=fcnt+1
    for i in items:
        icnt=icnt+1
    for i in complaints:
        cocnt=cocnt+1
    for i in incomes:
        incnt=incnt+i.amount
    for i in maintenances:
        macnt=macnt+i.amount_required
    for i in notices:
        ncnt=ncnt+1
    return render(request,"admin/index2.html",{"mcnt":mcnt,"ocnt":ocnt,"acnt":acnt,"bcnt":bcnt,"ccnt":ccnt,"dcnt":dcnt,"ecnt":ecnt,"fcnt":fcnt,"icnt":icnt,"cocnt":cocnt,"incnt":incnt,"macnt":macnt,"ncnt":ncnt})
    
        
def dashboard(request):
    if request.session.has_key('id')==False:
        return redirect('/alogin/')
    return render(request,"admin/dashboard.html")

def aprofile(request):
    if request.session.has_key('id')==False:
        return redirect('/alogin/')
    member=Member.objects.get(member_id=request.session.get('id'))
    return render(request,"admin/profile.html",{"member":member})

def updateaprofile(request,id):
    if request.method=="POST":
        members=Member.objects.get(member_id=id)
        name=request.POST.get('txtname')
        # dob=request.POST.get('dob')
        email=request.POST.get('txtemail')
        pwd=request.POST.get('txtps')
        con=request.POST.get('con')
        fn=request.POST.get('txtfn')
        bn=request.POST.get('block')
        gender=request.POST.get('gender')
        religion=request.POST.get('txtreligion')
        hstatus=request.POST.get('hstatus')
        mstatus=request.POST.get('mstatus')
        cdate=request.POST.get('cdate')
        ldate=request.POST.get('ldate')
        fm=request.POST.get('txtfm')
        pr=request.POST.get('pr')
        # profile=request.POST.get('profile')
        
        if pr!='':
            pro=request.FILES['pr']
            fss=FileSystemStorage()
            sfl=fss.save(pro,pro)
            sfss=fss.url(sfl)
            members.profile=sfss
        
        # members.name=name
        # members.email=email
        # members.password=pwd
        # members.contact_no_field=con
        members.flat_no_field=fn
        members.name=name
        members.email=email
        members.contact_no_field=con
        members.block_no_field=bn
        members.gender=gender
        members.religion=religion
        members.house_status=hstatus
        members.member_status=mstatus
        members.comming_date=cdate
        if ldate!='':
            members.leaving_date=ldate
        members.family_member=fm
        # members.date_of_birth=dob
        
        members.save()
        return redirect('/aprofile/')
        
    members=Member.objects.get(member_id=id)
    return render(request,"admin/updateaprofile.html",{"members":members})

def alogin(request):
    if request.method=='POST':
        em=request.POST.get('email')
        pwd=request.POST.get('pwd')
        
        members=Member.objects.filter(email=em,password=pwd)
        com=Committee.objects.filter(work_of_committee='chairman')
        for member in members:
            committeedetails=CommitteeDetails.objects.filter(member=member,committee=com[0])
            
            for com in committeedetails:
                request.session['id']=member.member_id
                return redirect('/index2/')
        return redirect('/alogin/')
    return render(request,"login.html")


def changepassword(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('pass')
        cpassword=request.POST.get('cpass')
        member=Member.objects.all()
        for m in member:
            if m.name==name and m.email==email:
                if password!=cpassword:
                    # m.password=password
                    return redirect('/changepassword/')
                elif password==cpassword:
                    m.password=password
                    m.save()
                    return redirect('/alogin')
        
    return render(request,"admin/changepassword.html")

def advertisement(request):
    if request.session.has_key('id')==False:
        return redirect('/alogin/')
    advertisements=Advertisement.objects.all()
    return render(request,"admin/advertisement.html",{"advertisements":advertisements})

def editadvertisement(request,id):
    if request.method=='POST':
        advertisements=Advertisement.objects.get(advertise_id=id)
        nm=request.POST.get('nm')
        
        st=request.POST.get('st')
        add=Member.objects.get(member_id=nm)
        
        advertisements.member=add
       
        advertisements.status=st
        advertisements.save()
        return redirect('/advertisement/')
    advertisement=Advertisement.objects.get(advertise_id=id)
    members=Member.objects.all()
    return render(request,"admin/editadvertisement.html",{"advertisement":advertisement,"members":members})

def deleteadvertisement(request,id):
    advertisements=Advertisement.objects.get(advertise_id=id)
    advertisements.delete()
    return redirect('/advertisement/') 

def booking(request):
    if request.session.has_key('id')==False:
        return redirect('/alogin/')
    bookings=Booking.objects.all()
    return render(request,"admin/booking.html",{"bookings":bookings})

def editbooking(request,id):
    if request.method=='POST':
        mname=request.POST.get('mname')
      
        st=request.POST.get('st')
        to=request.POST.get('total')
        mnm=Member.objects.get(member_id=mname)
        booking=Booking.objects.get(booking_id=id)
        booking.member=mnm
        
        booking.status=st
        booking.total=to
        booking.save()        
        return redirect('/one_booking/')
    members=Member.objects.all()
    booking=Booking.objects.get(booking_id=id)
    return render(request,'admin/editbooking.html',{"booking":booking,"members":members})

def bookingdetail(request,id):
    if request.session.has_key('id')==False:
        return redirect('/alogin/')
    members=Member.objects.all()
    booking=Booking.objects.get(booking_id=id)
    bookingdetails=BookingDetail.objects.filter(booking=id)
    return render(request,"admin/bookingdetail.html",{"bookingdetails":bookingdetails,"booking":booking,"members":members})

def editbookingdetail(request,id):
    if request.method=='POST':
        bid=request.POST.get('bname')
        iid=request.POST.get('iname')
       
        amt=request.POST.get('amt')
        bkid=Booking.objects.get(booking_id=bid)
        items=Items.objects.get(item_id=iid)
        bookingdetail=BookingDetail.objects.get(booking_detail_id=id)
        bookingdetail.booking=bkid
        bookingdetail.item=items
       
        bookingdetail.amount=amt
        bookingdetail.save()
 
        return redirect('/bookingdetail/')
    
    bookingdetails=BookingDetail.objects.get(booking_detail_id=id)
    items=Items.objects.all()
    bookings=Booking.objects.all()
    return render(request,'admin/editbookingdetail.html',{"bookingdetails":bookingdetails,"items":items,"bookings":bookings})

def committee(request):
    if request.session.has_key('id')==False:
        return redirect('/alogin/')
    committees=Committee.objects.all()
    return render(request,"admin/committee.html",{"committees":committees})

def addcommittee(request):
    if request.method=='POST':
        work=request.POST.get('txtnm')
        nom=request.POST.get('no')
        date=request.POST.get('dt')
        committee=Committee(work_of_committee=work,no_of_members=nom,committee_creation_date=date)
        committee.save()
        return redirect('/committee/')
    return render(request,"admin/addcommittee.html")

def editcommittee(request,id):
    if request.method=='POST':
        work=request.POST.get('txtnm')
        nom=request.POST.get('no')
        date=request.POST.get('dt')
        committee=Committee.objects.get(committee_id=id)
        committee.work_of_committee = work   
        committee.no_of_members =  nom      
        committee.committee_creation_date=date
        committee.save()
        return redirect('/one_committee/')
    committees=Committee.objects.get(committee_id=id)
    return render(request,"admin/editcommittee.html",{"committees":committees})

def deletecommittee(request,id):
    committee=Committee.objects.get(committee_id=id)
    committee.delete()
    return redirect("/committee/")

def committeedetail(request,id):
    if request.session.has_key('id')==False:
        return redirect('/alogin/')
    committees=Committee.objects.get(committee_id=id)
    committeedetails=CommitteeDetails.objects.filter(committee=id)
    return render(request,"admin/committeedetail.html",{"committeedetails":committeedetails,"committees":committees})

def addcommitteedetail(request):
    if request.method=='POST':
        cname=request.POST.get('cname')
        mname=request.POST.get('mname')
        jdt=request.POST.get('jdt')
        
        cnm=Committee.objects.get(committee_id=cname)
        
        mnm=Member.objects.get(member_id=mname)
        committeedetail=CommitteeDetails(committee=cnm,member=mnm,member_joining_date=jdt)
        committeedetail.save()
        return redirect('/committee/')
    committees=Committee.objects.all()
    members=Member.objects.all()
    return render(request,'admin/addcommitteedetail.html',{"committees":committees,"members":members})

def editcommitteedetail(request,id):
    if request.method=='POST':
        cname=request.POST.get('cname')
        mname=request.POST.get('mname')
        jdt=request.POST.get('jdt')
        ldt=request.POST.get('ldt')
        cnm=Committee.objects.get(committee_id=cname)
        mnm=Member.objects.get(member_id=mname)
        committeedetail=CommitteeDetails.objects.get(committee_detail_id=id)
        committeedetail.committee=cnm
        committeedetail.member=mnm
        committeedetail.member_joining_date=jdt
        committeedetail.member_leaving_date=ldt
        committeedetail.save()
        return redirect('/committee/')
    
    committeedetail=CommitteeDetails.objects.get(committee_detail_id=id)
    committees=Committee.objects.all()
    members=Member.objects.all()
    return render(request,'admin/editcommitteedetail.html',{"committeedetail":committeedetail,"committees":committees,"members":members})

def deletecommitteedetail(request,id):
    committeedetails=CommitteeDetails.objects.get(committee_detail_id=id)
    committeedetails.delete()
    return redirect('/committee/') 

def complaint(request):
    if request.session.has_key('id')==False:
        return redirect('/alogin/')
    complaints=Complaint.objects.all()
    return render(request,"admin/complaint.html",{"complaints":complaints})

def editcomplaint(request,id):
    if request.method=='POST':
        mname=request.POST.get('mname')
        desc=request.POST.get('desc')
        cdt=request.POST.get('cdt')
        st=request.POST.get('st')
        sdt=request.POST.get('sdt')
        cname=request.POST.get('cname')
        mnm=Member.objects.get(member_id=mname)
        cnm=CommitteeDetails.objects.get(committee_detail_id=cname)
        complaint=Complaint.objects.get(complaint_id=id)
        complaint.member=mnm
        complaint.description=desc
        complaint.complaint_date=cdt
        complaint.status=st
        complaint.solution_date=sdt
        complaint.committee_detail=cnm
        complaint.save()
        return redirect('/complaint/')

    complaint=Complaint.objects.get(complaint_id=id)
    members=Member.objects.all()
    committees=Committee.objects.all()
    committeedetails=CommitteeDetails.objects.all()
    return render(request,'admin/editcomplaint.html',{"complaint":complaint,"members":members,"committeedetails":committeedetails,"committees":committees})

def deposit(request):
    if request.session.has_key('id')==False:
        return redirect('/alogin/')
    deposits=Deposit.objects.all()
    return render(request,"admin/deposit.html",{"deposits":deposits})

def adddeposit(request):
    if request.method=='POST':
        txtnm=request.POST.get('txtnm')
        desc=request.POST.get('desc')
        rate=request.POST.get('rate')
        amount=request.POST.get('amount')
        ddt=request.POST.get('ddt')
        mdt=request.POST.get('mdt')
        deposit=Deposit(bank_name=txtnm,description=desc,rate=rate,deposit_amount=amount,deposit_date=ddt,maturity_date=mdt)
        deposit.save()
        return redirect('/deposit/')  
    return render(request,"admin/adddeposit.html")

def editdeposit(request,id):
    if request.method=='POST':
        txtnm=request.POST.get('txtnm')
        desc=request.POST.get('desc')
        rate=request.POST.get('rate')
        amount=request.POST.get('amount')
        ddt=request.POST.get('ddt')
        mdt=request.POST.get('mdt')
        deposit=Deposit.objects.get(deposit_id=id)
        deposit.bank_name=txtnm
        deposit.description =desc
        deposit.rate = rate
        deposit.deposit_amount=amount
        deposit.deposit_date =ddt
        deposit.maturity_date =mdt
        deposit.save()
        return redirect('/deposit/')  
    deposits=Deposit.objects.get(deposit_id=id)
    return render(request,"admin/editdeposit.html",{"deposits":deposits})

def deletedeposit(request,id):
    deposit=Deposit.objects.get(deposit_id=id)
    deposit.delete()
    return redirect("/deposit/")

def expense(request):
    if request.session.has_key('id')==False:
        return redirect('/alogin/')
    expenses=Expense.objects.all()
    return render(request,"admin/expense.html",{"expenses":expenses})

def addexpense(request):
    if request.method=="POST":
        etype=request.POST.get('etype')
        dt=request.POST.get('dt')
        amt=request.POST.get('amt')
        if (etype=='function'):
            fname=request.POST.get('fn')
            fnm=Function.objects.get(function_id=fname)
            expense=Expense(function=fnm,date=dt,amount=amt)
            expense.save()
            return redirect('/expense/')
        elif (etype=='other'):
            ot=request.POST.get('ot')
            expense=Expense(description=ot,date=dt,amount=amt)
            expense.save()
            return redirect('/expense/')
        elif (etype=='both'):
            bfn=request.POST.get('bfn')
            bdesc=request.POST.get('bdesc')
            fnm=Function.objects.get(function_id=bfn)
            expense=Expense(function=fnm,description=bdesc,date=dt,amount=amt)
            expense.save()
            return redirect('/expense/')
    others=['working staff salary','repairing cost','renovation cost']
    functions=Function.objects.all()
    return render(request,'admin/addexpense.html',{"functions":functions,"others":others})

def editexpense(request,id):
    if request.method=='POST':
        expense=Expense.objects.get(expence_id=id)
        etype=request.POST.get('etype')
        dt=request.POST.get('dt')
        amt=request.POST.get('amt')
        
        if etype=='fun':
            fname=request.POST.get('fn')
            fnm=Function.objects.get(function_id=fname)
            expense.function=fnm
            expense.date=dt
            expense.amount=amt
            expense.save()
            return redirect('/expense/')
        if etype=='other':
            desc=request.POST.get('ot')
            expense.description=desc
            expense.date=dt
            expense.amount=amt
            expense.save()
            return redirect('/expense/')
        if etype=='both':
            fn=request.POST.get('bfn')
            desc=request.POST.get('bdesc')
            fnm=Function.objects.get(function_id=fn)
            expense.function=fnm
            expense.description=desc
            expense.date=dt
            expense.amount=amt
            expense.save()
            return redirect('/expense/')
        
        
    others=['working staff salary','repairing cost','renovation cost','lift repairing cost']
    
    functions=Function.objects.all()
    expense=Expense.objects.get(expence_id=id)
    return render(request,'admin/editexpense.html',{"functions":functions,"expense":expense,"others":others})

def deleteexpense(request,id):
    expenses=Expense.objects.get(expence_id=id)
    expenses.delete()
    return redirect('/expense/')

def function(request):
    if request.session.has_key('id')==False:
        return redirect('/alogin/')
    functions=Function.objects.all()
    return render(request,"admin/function.html",{"functions":functions})

def cfunction(request):
    if request.session.has_key('id')==False:
        return redirect('/alogin/')
    dt=date.today()
    functions=Function.objects.filter(fdate__gt=dt)
    return render(request,"admin/cfunction.html",{"functions":functions})

def addfunction(request):
    if request.method=='POST':
        fnm=request.POST.get('fn')
        fp=request.POST.get('fp')
        apm=request.POST.get('apm')
        dt=request.POST.get('dt')
        function=Function(function_name=fnm,function_place=fp,amount_per_member=apm,date=dt)
        function.save()
        return redirect('/function/')
    return render(request,"admin/addfunction.html")

def editfunction(request,id):
    if request.method=='POST':
        fnm=request.POST.get('fn')
        fp=request.POST.get('fp')
        apm=request.POST.get('apm')
        dt=request.POST.get('dt')
        function=Function.objects.get(function_id=id)
        function.function_name = fnm   
        function.function_place =  fp      
        function.amount_per_member=apm
        function.date=dt
        function.save()
        return redirect('/one_function/')
    functions=Function.objects.get(function_id=id)
    return render(request,"admin/editfunction.html",{"functions":functions})

def deletefunction(request,id):
    function=Function.objects.get(function_id=id)
    function.delete()
    return redirect("/function/")

def item(request):
    if request.session.has_key('id')==False:
        return redirect('/alogin/')
    items=Items.objects.all()
    return render(request,"admin/item.html",{"items":items})

def additem(request):
    if request.method=='POST':
        nm=request.POST.get('txtnm')
        qt=request.POST.get('qt')
        pr=request.POST.get('amount')
        item=Items(item_name=nm,total_quantity=qt,price_per_unit=pr)
        item.save()
        return redirect('/item/')
    return render(request,'admin/additem.html')

def edititem(request,id):
    if request.method=='POST':
        nm=request.POST.get('txtnm')
        qt=request.POST.get('qt')
        pr=request.POST.get('amount')
        pimg=request.POST.get('img')
        # profile=request.POST.get('profile')
        item=Items.objects.get(item_id=id)
        if pimg!='':
            pro=request.FILES['img']
            fss=FileSystemStorage()
            sfl=fss.save(pro,pro)
            sfss=fss.url(sfl)
            item.image=sfss
        
        
        item.item_name=nm
        item.total_quantity=qt
        item.price_per_unit=pr
        item.save()
        return redirect('/item/')
    items=Items.objects.get(item_id=id)
    return render(request,"admin/edititem.html",{"items":items})

def deleteitem(request,id):
    item=Items.objects.get(item_id=id)
    item.delete()
    return redirect("/item/")

def income(request):
    if request.session.has_key('id')==False:
        return redirect('/alogin/')
    incomes=Income.objects.all()
    return render(request,"admin/income.html",{"incomes":incomes})

def addincome(request):
    if request.method=="POST":
        itype=request.POST.get('itype')
        dt=request.POST.get('dt')
        amt=request.POST.get('amt')
        if (itype=='maintenance'):
            mname=request.POST.get('mname')
            mnm=MemberMaintenance.objects.get(member_maintenance_id=mname)
            mn=Maintenance.objects.get(maintenance_id=mnm.maintenance_id)
            incomes=Income(member_maintenance=mn,date=dt,amount=amt)
            incomes.save()
            return redirect('/income/')
        elif (itype=='deposit'):
            dname=request.POST.get('dname')
            deposit=Deposit.objects.get(deposit_id=dname)
            incomes=Income(deposit=deposit,date=dt,amount=amt)
            incomes.save()
            return redirect('/income/')
        elif (itype=='booking'):
            bname=request.POST.get('bname')
            booking=Booking.objects.get(booking_id=bname)
            incomes=Income(booking=booking,date=dt,amount=amt)
            incomes.save()
            return redirect('/income/')
        elif (itype=='other'):
            event=request.POST.get('ot')
            incomes=Income(society_event_fund=event,date=dt,amount=amt)
            incomes.save()
            return redirect('/income/')
    membermaintenances=MemberMaintenance.objects.all()
    bookings=Booking.objects.all()
    deposits=Deposit.objects.all()
    lst1=["1(Holi celebration)","2(navratri celebration)","3(diwali celebration)","4(uttrayaan celebration)"]
    
    return render(request,"admin/addincome.html",{"membermaintenances":membermaintenances,"bookings":bookings,"deposits":deposits,"lst1":lst1})

def editincome(request,id):
    if request.method=="POST":
        income=Income.objects.get(income_id=id)
        dt=request.POST.get('dt')
        amt=request.POST.get('amt')
        itype=request.POST.get('itype')
        if itype == 'maintenance':
            mname=request.POST.get('mname')
            mnm=MemberMaintenance.objects.get(member_maintenance_id=mname)
            nm=Maintenance.objects.get(maintenance_id=mnm.maintenance_id)
            income.member_maintenance=nm
            income.date=dt
            income.amount=amt
            income.save()
            return redirect('/income/')
        if itype == 'booking':
            bname=request.POST.get('bname')
            bnm=Booking.objects.get(booking_id=bname)
            income.booking=bnm
            income.date=dt
            income.amount=amt
            income.save()
            return redirect('/income/')
                # bookings=Booking.objects.get(booking_id=itype)

        if itype == 'deposit':
            dname=request.POST.get('bname')
            dnm=Deposit.objects.get(deposit_id=dname)
            income.deposit=dnm
            income.date=dt
            income.amount=amt
            income.save()
            return redirect('/income/') 
            

        if itype == 'other':
            other=request.POST.get('ot')  
            income.society_event_fund=other
            income.date=dt
            income.amount=amt
            income.save()
            return redirect('/income/')  
        return redirect('/income/')
    income=Income.objects.get(income_id=id)
    membermaintenances=MemberMaintenance.objects.all()
    bookings=Booking.objects.all()
    deposits=Deposit.objects.all()
    lst1=["1(Holi celebration)","2(navratri celebration)","3(diwali celebration)","4(uttrayaan celebration)"]
    return render(request,'admin/editincome.html',{"income":income,"membermaintenances":membermaintenances,"bookings":bookings,"deposits":deposits,"lst1":lst1})

def deleteincome(request,id):
    incomes=Income.objects.get(income_id=id)
    incomes.delete()
    return redirect('/income/')

def maintenance(request):
    if request.session.has_key('id')==False:
        return redirect('/alogin/')
    maintenances=Maintenance.objects.all()
    return render(request,"admin/maintenance.html",{"maintenances":maintenances})

def addmaintenance(request):
    if request.method=='POST':
        month=request.POST.get('month')
        mn=request.POST.get('mn')
        income=request.POST.get('txtincome')
        expense=request.POST.get('txtexpense')
        ramount=request.POST.get('amt')
        member=request.POST.get('totalmembers')
        amount=request.POST.get('mamt')
        date=request.POST.get('ldate')
        charge=request.POST.get('lcharges')
        maintenance=Maintenance(month_year=mn,total_income=income,total_expence=expense,amount_required=ramount,no_of_member=member,maintenance_amount=amount,last_date=date,late_charges=charge)
        maintenance.save()
        return redirect('/maintenance/')
    # return render(request,"admin/addmaintenance.html")

def editmaintenance(request,id):
    if request.method=='POST':
        month=request.POST.get('txtmy')
        income=request.POST.get('txtincome')
        expense=request.POST.get('txtexpense')
        ramount=request.POST.get('txtramount')
        member=request.POST.get('txtmem')
        amount=request.POST.get('txtmamount')
        date=request.POST.get('txtdate')
        charge=request.POST.get('txtcharge')
        
        maintenance=Maintenance.objects.get(maintenance_id=id)
        maintenance.month_year=month
        maintenance.total_income=income
        maintenance.total_expence=expense
        maintenance.no_of_member =ramount
        maintenance.maintenance_amount=member
        maintenance.last_date=amount
        maintenance.last_date=date
        maintenance.late_charges=charge
        maintenance.save()
        return redirect('/maintenance/')
    maintenances=Maintenance.objects.get(maintenance_id=id)
    return render(request,"admin/editmaintenance.html",{"maintenances":maintenances})

def deletemaintenance(request,id):
    maintenance=Maintenance.objects.get(maintenance_id=id)
    maintenance.delete()
    return redirect("/maintenance/")

def member(request):
    if request.session.has_key('id')==False:
        return redirect('/alogin/')
    members=Member.objects.all()
    return render(request,"admin/member.html",{"members":members})

def addmember(request):
    if request.method=='POST':
        txtname=request.POST.get('txtname')
        txtemail=request.POST.get('txtemail')
        txtps=request.POST.get('txtps')
        con=request.POST.get('con')
        txtfn=request.POST.get('txtfn')
        txtbn=request.POST.get('block')
        gender=request.POST.get('gender')
        txtreligion=request.POST.get('txtreligion')
        txths=request.POST.get('hstatus')
        txtms=request.POST.get('mstatus')
        cdate=request.POST.get('cdate')
        txtfm=request.POST.get('txtfm')
        dob=request.POST.get('dob')
        ctxtprofile=request.FILES['txtprofile']
        fss=FileSystemStorage()
        sfss=fss.save(ctxtprofile,ctxtprofile)
        surl=fss.url(sfss)
        if (txtfm!='' and txtreligion!=''):
            member=Member(name =txtname ,email =txtemail,date_of_birth=dob ,password =txtps ,contact_no_field=con,flat_no_field =txtfn,block_no_field =txtbn,
                    gender =gender ,religion = txtreligion,house_status =txths ,member_status =txtms,
                    comming_date = cdate,family_member =txtfm, profile =surl)
            member.save()
        elif (txtfm=='' and txtreligion==''):
            member=Member(name =txtname ,email =txtemail ,date_of_birth=dob,password =txtps ,contact_no_field=con,flat_no_field =txtfn,block_no_field =txtbn,
                    gender =gender ,house_status =txths ,member_status =txtms,
                    comming_date = cdate, profile =surl)
            member.save()
        return redirect('/member/')
    return render(request,"admin/addmember.html")

def memberdetail(request,id):
    if request.method=="POST":
        members=Member.objects.get(member_id=id)
        name=request.POST.get('txtname')
        # dob=request.POST.get('dob')
        email=request.POST.get('txtemail')
        pwd=request.POST.get('txtps')
        con=request.POST.get('con')
        fn=request.POST.get('txtfn')
        bn=request.POST.get('block')
        gender=request.POST.get('gender')
        religion=request.POST.get('txtreligion')
        hstatus=request.POST.get('hstatus')
        mstatus=request.POST.get('mstatus')
        cdate=request.POST.get('cdate')
        ldate=request.POST.get('ldate')
        fm=request.POST.get('txtfm')
        pr=request.POST.get('pr')
        # profile=request.POST.get('profile')
        
        if pr!='':
            pro=request.FILES['pr']
            fss=FileSystemStorage()
            sfl=fss.save(pro,pro)
            sfss=fss.url(sfl)
            members.profile=sfss
        
        # members.name=name
        # members.email=email
        # members.password=pwd
        # members.contact_no_field=con
        members.flat_no_field=fn
        members.block_no_field=bn
        members.gender=gender
        members.religion=religion
        members.house_status=hstatus
        members.member_status=mstatus
        members.comming_date=cdate
        if ldate!='':
            members.leaving_date=ldate
        members.family_member=fm
        # members.date_of_birth=dob
        
        members.save()
        return redirect('/member/')
        
    members=Member.objects.get(member_id=id)
    return render(request,"admin/memberdetail.html",{"members":members})

def ememberdetail(request,id):
    if request.method=="POST":
        members=Member.objects.get(member_id=id)
        name=request.POST.get('txtname')
        email=request.POST.get('txtemail')
        pwd=request.POST.get('txtps')
        con=request.POST.get('txtcontactno')
        fn=request.POST.get('txtfn')
        bn=request.POST.get('txtbn')
        gender=request.POST.get('txtgender')
        religion=request.POST.get('txtreligion')
        hstatus=request.POST.get('txths')
        mstatus=request.POST.get('txtms')
        cdate=request.POST.get('txtcdate')
        ldate=request.POST.get('txtldate')
        fm=request.POST.get('txtfm')
        profile=request.FILES['profile']
        
        fss=FileSystemStorage()
        sfss=fss.save(profile,profile)
        surl=fss.url(sfss)
        
        members.name=name
        members.email=email
        members.password=pwd
        members.contact_no_field=con
        members.flat_no_field=fn
        members.block_no_field=bn
        members.gender=gender
        members.religion=religion
        members.house_status=hstatus
        members.member_status=mstatus
        members.comming_date=cdate
        members.leaving_date=ldate
        members.family_member=fm
        members.profile=surl
        members.save()
        return redirect('/member/')
        
    members=Member.objects.get(member_id=id)
    return render(request,"admin/memberdetail.html",{"members":members})

def deletemember(request,id):
    member=Member.objects.get(member_id=id)
    member.delete()
    return redirect("/member/")

def memberfunction(request,id):
    if request.session.has_key('id')==False:
        return redirect('/alogin/')
    functions=Function.objects.get(function_id=id)
    memberfunctions=MemberFunction.objects.filter(member=id)
    return render(request,"admin/memberfunction.html",{"memberfunctions":memberfunctions,"functions":functions})

def editmemberfunction(request,id):

    if request.method=="POST":
        fid=request.POST.get('txtfid')
        mid=request.POST.get('txtmid')
        # amount=request.POST.get('txtamount')
        # pdate=request.POST.get('txtdate')
        # passes=request.POST.get('txtpass')
        fstatus=request.POST.get('fstatus')
        fnm=Function.objects.get(function_id=fid)
        mnm=Member.objects.get(member_id=mid)
        memberfunction=MemberFunction.objects.get(member_function_id=id)
        # memberfunction.function=fnm
        # memberfunction.member=mnm
        # memberfunction.amount=amount
        # memberfunction.pay_date=pdate
        # memberfunction.no_of_pass=passes 
        memberfunction.status=fstatus 
        memberfunction.save()
        return redirect('/one_function/')
    memberfunctions=MemberFunction.objects.get(member_function_id=id)
    functions=Function.objects.all()
    members=Member.objects.all()
    return render(request,"admin/editmemberfunction.html",{'memberfunctions':memberfunctions,"members":members,"functions":functions})

def membermaintenance(request,id):
    if request.session.has_key('id')==False:
        return redirect('/alogin/')
    maintenances=Maintenance.objects.get(maintenance_id=id)
    members=Member.objects.all()
    membermaintenances=MemberMaintenance.objects.filter(maintenance=id)
    return render(request,"admin/membermaintenance.html",{"membermaintenances":membermaintenances,"maintenances":maintenances,'members':members})

def addmembermaintenance(request):
    if request.method=='POST':
        mnid=request.POST.get('txtmnid')
        mid=request.POST.get('txtmid')
        pdate=request.POST.get('txtdate')
        amount=request.POST.get('txtamount')
        lcharges=request.POST.get('txtlcharges')
        total=request.POST.get('txttotal')
        mnobj=Maintenance.objects.get(maintenance_id=mnid)
        mobj=Member.objects.get(member_id=mid)
        mm=MemberMaintenance(maintenance=mnobj,member=mobj,pay_date=pdate,amount=amount,late_charges=lcharges,total=total)
        mm.save()
        return redirect('/membermaintenance/')
    maintenances=Maintenance.objects.all()
    members=Member.objects.all()
    return render(request,'admin/addmembermaintenance.html',{"maintenances":maintenances,"members":members})

def editmembermaintenance(request,id):
    if request.method=="POST":
        mm=MemberMaintenance.objects.get(member_maintenance_id=id)
        mnid=request.POST.get('txtmnid')
        mid=request.POST.get('txtmid')
        pdate=request.POST.get('txtdate')
        amount=request.POST.get('txtamount')
        lcharges=request.POST.get('txtlcharges')
        total=request.POST.get('txttotal')
        mn=Maintenance.objects.get(maintenance_id=mnid)
        members=Member.objects.get(member_id=mid)
        mm.maintenance=mn
        mm.member=members
        mm.pay_date=pdate
        mm.amount=amount
        mm.late_charges=lcharges
        mm.total=total
        mm.save()
        return redirect('/membermaintenance/')
    membermaintenances=MemberMaintenance.objects.get(member_maintenance_id=id)
    members=Member.objects.all()
    maintenances=Maintenance.objects.all()
    return render(request,"admin/editmembermaintenance.html",{"membermaintenances":membermaintenances,"members":members,"maintenances":maintenances})

def deletemembermaintenance(request,id):
    membermaintenances=MemberMaintenance.objects.get(member_maintenance_id=id)
    membermaintenances.delete()
    return redirect('/membermaintenance/') 

def notice(request):
    if request.session.has_key('id')==False:
        return redirect('/alogin/')
    notices=Notice.objects.all()
    return render(request,"admin/notice.html",{"notices":notices})

def addnotice(request):
    if request.method=='POST':
        txtcommittee=request.POST.get('txtcommittee')
        txtdesc=request.POST.get('txtdesc')
        txtdate=request.POST.get('txtdate')
        cm=Committee.objects.get(committee_id=txtcommittee)
        notice=Notice(committee=cm,description=txtdesc,date=txtdate)
        notice.save()
        return redirect('/notice/')
    committees=Committee.objects.all()
    return render(request,"admin/addnotice.html",{"committees":committees})

def editnotice(request,id):
    if request.method=="POST":
        notice=Notice.objects.get(notice_id=id)
        committee=request.POST.get('txtcommittee')
        desc=request.POST.get('desc')
        date=request.POST.get('dt')
        status=request.POST.get('st')
        cobj=Committee.objects.get(committee_id=committee)
        
        notice.committee=cobj
        notice.description=desc
        notice.date=date
        notice.status=status
        notice.save()
        return redirect('/notice/')
    notices=Notice.objects.get(notice_id=id)
    committees=Committee.objects.all()
    return render(request,"admin/editnotice.html",{"notices":notices,"committees":committees})

def deletenotice(request,id):
    notice=Notice.objects.get(notice_id=id)
    notice.delete()
    return redirect('/notice/') 

def occupant(request):
    if request.session.has_key('id')==False:
        return redirect('/alogin/')
    occupants=Occupant.objects.all()
    return render(request,"admin/occupant.html",{"occupants":occupants})

def occupantdetail(request,id):
    if request.session.has_key('id')==False:
        return redirect('/alogin/')
    members=Member.objects.all()
    occupants=Occupant.objects.get(occupant_id=id)
    return render(request,"admin/occupantdetail.html",{"occupants":occupants,"members":members})

def one_committee(request):
    if request.session.has_key('id')==False:
        return redirect('/alogin/')
    committees=Committee.objects.all()
    committeedetails=CommitteeDetails.objects.all()
    members=Member.objects.all()
    return render(request,'admin/one_committee.html',{'members':members,"committeedetails":committeedetails,'committees':committees})

def edit_one_committee(request,id):
    if request.method=='POST':
        cname=request.POST.get('cname')
        mname=request.POST.get('mname')
        jdt=request.POST.get('jdt')
        ldt=request.POST.get('ldt')
        cnm=Committee.objects.get(committee_id=cname)
        mnm=Member.objects.get(member_id=mname)
        committeedetail=CommitteeDetails.objects.get(committee_detail_id=id)
        committeedetail.committee=cnm
        committeedetail.member=mnm
        committeedetail.member_joining_date=jdt
        committeedetail.member_leaving_date=ldt
        committeedetail.save()
        return redirect('/one_committee/')
    committees=Committee.objects.all()
    committeedetails=CommitteeDetails.objects.get(committee_detail_id=id)
    members=Member.objects.all()
    return render(request,'admin/edit_one_committee.html',{'members':members,"committeedetails":committeedetails,'committees':committees})

def one_booking(request):
    if request.session.has_key('id')==False:
        return redirect('/alogin/')
    bookings=Booking.objects.all()
    bookingdetails=BookingDetail.objects.all()
    items=Items.objects.all()
    return render(request,'admin/one_booking.html',{'items':items,"bookingdetails":bookingdetails,'bookings':bookings})

def edit_one_booking(request,id):
    bookings=Booking.objects.all()
    bookingdetails=BookingDetail.objects.get(booking_detail_id=id)
    items=Items.objects.all()
    return render(request,'admin/edit_one_booking.html',{'items':items,"bookingdetails":bookingdetails,'bookings':bookings})

def one_function(request):
    if request.session.has_key('id')==False:
        return redirect('/alogin/')
    functions=Function.objects.all()
    members=Member.objects.all()
    memberfunctions=MemberFunction.objects.all()
    return render(request,'admin/one_function.html',{"functions":functions,'members':members,"memberfunctions":memberfunctions})

def edit_one_function(request,id):

    functions=Function.objects.all()
    members=Member.objects.all()
    memberfunctions=MemberFunction.objects.all()
    return render(request,'admin/edit_one_function.html',{"functions":functions,'members':members,"memberfunctions":memberfunctions})

def one_maintenance(request):
    if request.session.has_key('id')==False:
        return redirect('/alogin/')
    maintenances=Maintenance.objects.all()
    membermaintenances=MemberMaintenance.objects.all()
    members=Member.objects.all()
    return render(request,'admin/one_function.html',{"maintenances":maintenances,'members':members,"membermaintenances":membermaintenances})

def edit_one_maintenance(request,id):
    maintenances=Maintenance.objects.all()
    membermaintenances=MemberMaintenance.objects.all()
    members=Member.objects.all()
    return render(request,'admin/edit_one_function.html',{"maintenances":maintenances,'members':members,"membermaintenances":membermaintenances})

def new_main(request):
    if request.session.has_key('id')==False:
        return redirect('/alogin/')
    if request.method=='POST':
        sdt=request.POST.get('month')
        stdt=datetime.strptime(sdt+"-"+"01", '%Y-%m-%d').date()
        
        print(stdt)
        ldt=calendar.monthrange(stdt.year,stdt.month)
        print(ldt[1])

        ltdt=datetime.strptime(sdt+"-"+str(ldt[1]), '%Y-%m-%d').date()
        
        incomes=Income.objects.filter(date__range=(str(stdt),str(ltdt)))
        totalincome=0
        for income in incomes:
            totalincome=totalincome+income.amount

        # print(totalincome)
        return redirect('/admin/new_main1/',{"totalincome":totalincome,'sdt':sdt}) 

    return render(request,"admin/new_main.html")

def new_main1(request):
    if request.session.has_key('id')==False:
        return redirect('/alogin/')
    if request.method=='POST':
        my=request.POST.get('month')
       
        sdt=request.POST.get('month')
        stdt=datetime.strptime(sdt+"-"+"01", '%Y-%m-%d').date()
        
        print(stdt)
        ldt=calendar.monthrange(stdt.year,stdt.month)
        print(ldt[1])

        ltdt=datetime.strptime(sdt+"-"+str(ldt[1]), '%Y-%m-%d').date()
        
        incomes=Income.objects.filter(date__range=(str(stdt),str(ltdt)))
        totalincome=0
        for income in incomes:
            totalincome=totalincome+income.amount

        sedt=request.POST.get('month')
        setdt=datetime.strptime(sedt+"-"+"01", '%Y-%m-%d').date()
        
        print(setdt)
        ledt=calendar.monthrange(setdt.year,setdt.month)
        print(ldt[1])

        letdt=datetime.strptime(sedt+"-"+str(ledt[1]), '%Y-%m-%d').date()
        
        expenses=Expense.objects.filter(date__range=(str(setdt),str(letdt)))
        totalexpense=0
        for expense in expenses:
            totalexpense=totalexpense+expense.amount
        amt=0
        if totalexpense>totalincome:
            amt=totalexpense-totalincome
        return render(request,"admin/new_main1.html",{"my":my,"totalincome":totalincome,"totalexpense":totalexpense,"amt":amt})
def new_main2(request):
    
    if request.method=='POST':
        pass
    month=request.POST.get('month')
    mn=request.POST.get('txtnm')
    expense=request.POST.get('txtincome')
    income=request.POST.get('txtexpense')
    amount=request.POST.get('txtamt')
    aamount=request.POST.get('aamount')
    members=Member.objects.all()
    cnt=0
    for member in members:
        cnt=cnt+1
    amt=int(amount)+int(aamount)
    mamt=int(int(amt)/int(cnt))
    return render(request,"admin/new_main2.html",{'mamt':mamt,'amt':amt,'cnt':cnt,'income':income,'expense':expense,'month':month,"mn":mn})

       #member side

def mindex(request):
    if request.session.has_key('id')==False:
        return redirect('/mlogin/')
    else:
        members=Member.objects.filter(member_id=request.session.get('id'))
        return render(request,"member/mindex.html",{"members":members})
    
def mindex1(request):
    if request.session.has_key('id')==False:
        return redirect('/mlogin/')
    members=Member.objects.filter(member_id=request.session.get('id'))
    return render(request,"member/mindex1.html",{"members":members})
        
def mindex2(request):
    if request.session.has_key('id')==False:
        return redirect('/mlogin/')
    members=Member.objects.filter(member_id=request.session.get('id'))
    return render(request,"member/mindex2.html",{"members":members})

def mlogin(request):
    if request.method=='POST':
        em=request.POST.get('email')
        pwd=request.POST.get('pwd')
        members=Member.objects.filter(email=em,password=pwd)
        for member in members:
            request.session['id']=member.member_id
            return redirect('/home/')
        # return redirect('/mlogin/')
        msg="invalid Username and Password"
        return render(request,"member1/login.html",{"msg":msg})
    msg=""
    return render(request,"member1/login.html",{"msg":msg})

def search(request):
    pass

def madvertisement(request):
    if request.session.has_key('id')==False:
        return redirect('/mlogin/')
    advertisements=Advertisement.objects.filter(member_id=request.session.get('id'))
    return render(request,'member1/advertisement.html',{"advertisements":advertisements})

def addmadvertisement(request):
    if request.method=='POST':
        desc=request.POST.get('desc')
        dt=request.POST.get('dt')
        mm=request.session.get('id')
        member=Member.objects.get(member_id=mm)
        advertisement=Advertisement(description=desc,date=dt,status='pending',member=member)
        advertisement.save()
        return redirect('/madvertisement/')

    members=Member.objects.all()
    return render(request,'member1/addadvertisement.html',{"members":members})

def editmadvertisement(request,id):
    if request.method=='POST':
        advertisements=Advertisement.objects.get(advertise_id=id)
        nm=request.POST.get('dt')
       
        st=request.POST.get('desc')
        # add=Member.objects.get(member_id=nm)
        
        advertisements.date=nm
       
        advertisements.description=st
        advertisements.save()
        return redirect('/madvertisement/')
    if request.session.has_key('id')==False:
        return redirect('/mlogin/')
    members=Member.objects.filter(member_id=request.session.get('id'))

    advertisement=Advertisement.objects.get(advertise_id=id)
    return render(request,"member1/editadvertisement.html",{"advertisement":advertisement,"members":members})



def mbooking(request):
    if request.session.has_key('id')==False:
        return redirect('/mlogin/')
    items=Items.objects.all()
    bookings=Booking.objects.filter(member_id=request.session.get('id'))
    bookingsdetails=BookingDetail.objects.all()
    return render(request,'member1/booking.html',{"bookings":bookings,"bookingsdetails":bookingsdetails,"items":items})

def addmbooking(request):
    members=Member.objects.all()
    return render(request,'member/addbooking.html',{"members":members})

def editmbooking(request,id):
    if request.method=='POST':
        mname=request.POST.get('mname')
       
        st=request.POST.get('st')
        to=request.POST.get('total')
        mnm=Member.objects.get(member_id=mname)
        booking=Booking.objects.get(booking_id=id)
        booking.member=mnm
        
        booking.status=st
        booking.total=to
        booking.save()        
        return redirect('/one_booking/')
    members=Member.objects.all()
    booking=Booking.objects.get(booking_id=id)
    return render(request,'member/editbooking.html',{"booking":booking,"members":members})


def deletembooking(request,id):
    bookings=Booking.objects.get(booking_id=id)
    bookings.delete()
    return redirect('/mbooking/') 

# def mbookingdetail(request,id):
#     if request.session.has_key('id')==False:
#         return redirect('/mlogin/')
#     bookings=Booking.objects.filter(member_id=request.session.get('id'))
#     bookingdetails=BookingDetail.objects.filter(booking=id)    
#     return render(request,'member1/bookingdetail.html',{"bookingdetails":bookingdetails,"bookings":bookings})

def mbookingdetail(request,id):
    if request.session.has_key('id')==False:
        return redirect('/mlogin/')
    bookings=Booking.objects.filter(member_id=request.session.get('id'))
    bookingdetails=BookingDetail.objects.filter(booking=id)
    # bookings=Booking.objects.all()
    
    return render(request,'member1/bookingdetail.html',{"bookingdetails":bookingdetails,"bookings":bookings})

def addmbookingdetail(request):
    members=Member.objects.all()
    items=Items.objects.all()
    return render(request,'member/addbookingdetail.html',{"members":members,"items":items})

def editmbookingdetail(request,id):
    if request.method=='POST':
        bid=request.POST.get('bname')
        iid=request.POST.get('iname')
       
        amt=request.POST.get('amt')
        bkid=Booking.objects.get(booking_id=bid)
        items=Items.objects.get(item_id=iid)
        bookingdetail=BookingDetail.objects.get(booking_detail_id=id)
        bookingdetail.booking=bkid
        bookingdetail.item=items
       
        bookingdetail.amount=amt
        bookingdetail.save()
 
        return redirect('/bookingdetail/')
    
    bookingdetails=BookingDetail.objects.get(booking_detail_id=id)
    items=Items.objects.all()
    bookings=Booking.objects.all()
    return render(request,'member/editbookingdetail.html',{"bookingdetails":bookingdetails,"items":items,"bookings":bookings})


def deletembookingdetail(request,id):
    bookingdetails=BookingDetail.objects.get(booking_detail_id=id)
    bookingdetails.delete()
    return redirect('/mbookingdetail/') 

def mcommittee(request):
    if request.session.has_key('id')==False:
        return redirect('/mlogin/')
    committees=Committee.objects.all()
    return render(request,'member1/committee.html',{"committees":committees})

def mcommitteedetail(request):
    if request.session.has_key('id')==False:
        return redirect('/mlogin/')
    committeedetails=CommitteeDetails.objects.filter(member_id=request.session.get('id'))
    return render(request,'member1/committeedetail.html',{"committeedetails":committeedetails})

def mcomplaint(request):
    if request.session.has_key('id')==False:
        return redirect('/mlogin/')
    complaints=Complaint.objects.filter(member_id=request.session.get('id'))
    return render(request,'member1/complaint.html',{"complaints":complaints})

def addmcomplaint(request):
    if request.session.has_key('id')==False:
        return redirect('/mlogin/')
    if request.method=='POST':
        mn=request.session.get('id')
        mname=Member.objects.get(member_id=mn)
        
        desc=request.POST.get('desc')
        cdt=request.POST.get('cdt')
       
        complaint=Complaint(member=mname,description=desc,complaint_date=cdt,status='pending')
        complaint.save()
        return redirect('/mcomplaint/')
    committees=Committee.objects.all()
    members=Member.objects.all()
    return render(request,'member1/addcomplaint.html',{"members":members,"committees":committees})

def editmcomplaint(request,id):
    if request.method=='POST':
        
        desc=request.POST.get('desc')
        cdt=request.POST.get('dt')
       
        complaint=Complaint.objects.get(complaint_id=id)
        
        complaint.description=desc
        complaint.complaint_date=cdt
        
        complaint.save()
        return redirect('/mcomplaint/')
    if request.session.has_key('id')==False:
        return redirect('/mlogin/')
    complaint=Complaint.objects.get(complaint_id=id)
    members=Member.objects.filter(member_id=request.session.get('id'))
    committeedetails=CommitteeDetails.objects.all()
    committees=Committee.objects.all()
    return render(request,'member1/editcomplaint.html',{"complaint":complaint,"members":members,"committeedetails":committeedetails,"committees":committees})


def mdeposit(request):
    if request.session.has_key('id')==False:
        return redirect('/mlogin/')
    deposits=Deposit.objects.all()
    return render(request,'member1/deposit.html',{"deposits":deposits})

def mexpense(request):
    if request.session.has_key('id')==False:
        return redirect('/mlogin/')
    expenses=Expense.objects.all()
    return render(request,'member1/expense.html',{"expenses":expenses})

def mfunction(request):
    if request.session.has_key('id')==False:
        return redirect('/mlogin/')
    dt=date.today()
    functions=Function.objects.filter(fdate__gt=dt)
    return render(request,'member1/function.html',{"functions":functions,'dt':dt})  
        

   

def mincome(request):
    if request.session.has_key('id')==False:
        return redirect('/mlogin/')
    incomes=Income.objects.all()
    return render(request,'member1/income.html',{"incomes":incomes})

def mitem(request):
    if request.session.has_key('id')==False:
        return redirect('/mlogin/')
    items=Items.objects.all()
    return render(request,'member1/item.html',{"items":items})

def cart(request):
    if request.session.has_key('id')==False:
        return redirect('/mlogin/')
   
    item=Items.objects.all()
    member=Member.objects.get(member_id=request.session.get('id'))
    cart=Cart.objects.filter(member_id=request.session.get('id'))
    total=0
    for i in cart:
        total=total+i.total
    return render(request,"member1/cart.html",{"item":item,"member":member,"cart":cart,"total":total})

def cartsave(request,id):
    if request.session.has_key('id')==False:
        return redirect('/mlogin/')
    
    price=request.POST.get('price')
    
    qty=request.POST.get('qty')
   
    items=Items.objects.get(item_id=id)
    q=items.total_quantity
    if (int(qty) > int(q)):
        return redirect('/itemdetail/'+str(id)+"/")
    else:
        im=Items.objects.get(item_id=id)
        mn=Member.objects.get(member_id=request.session.get('id'))
        cart=Cart(member=mn,item=im,quantity=qty,rate=price,total=(int(price)*int(qty)))
        cart.save()
    return redirect('/cart/')

def deletecart(request,id):
    cart=Cart.objects.get(cart_id=id)
    cart.delete()
    return redirect('/cart/')

def invoice1(request):
    booking=Booking.objects.filter(member=request.session.get('id'))
    return render(request,'member/invoice.html',{'booking':booking})
    
def checkout(request):
    if request.session.has_key('id')==False:
        return redirect('/mlogin/')
   
    mn=Member.objects.get(member_id=request.session.get('id'))
    event=request.POST.get('event')
    sdt=request.POST.get('sdt')
    edt=request.POST.get('edt')
    
    sdt=request.POST.get('sdt')
    cart=Cart.objects.filter(member_id=request.session.get('id'))
    total=0
    for i in cart:
        total=total+i.total
    #--- booking insert
    booking=Booking(member=mn,starting_date=sdt,ending_date=edt,event_name=event,booking_date=date.today(),status='pending',total=total)
    booking.save()
    income=Income(booking=booking,date=date.today(),amount=total)
    income.save()
    for i in cart:
        itemid=i.item
        qty=i.quantity
        amt=i.total
        bookingdetail=BookingDetail(booking=booking,item=itemid,quantity=qty,amount=amt)
        bookingdetail.save()
    for i in cart:
        i.delete()
    return redirect("/mbooking/")

def itemdetail(request,id):
    if request.session.has_key('id')==False:
        return redirect('/mlogin/')
    items=Items.objects.get(item_id=id)
    member=Member.objects.get(member_id=request.session.get('id'))
    return render(request,'member1/itemdetail.html',{"items":items,"member":member})

def mmaintenance(request):
    if request.session.has_key('id')==False:
        return redirect('/mlogin/')
    maintenances=MemberMaintenance.objects.filter(member=request.session.get('id'))
    return render(request,'member1/maintenance.html',{"maintenances":maintenances})

def mmmaintenance(request):
    if request.session.has_key('id')==False:
        return redirect('/mlogin/')
    maintenances=Maintenance.objects.all()
    return render(request,'member1/mmaintenance.html',{"maintenances":maintenances})


def mmember(request):
    if request.session.has_key('id')==False:
        return redirect('/mlogin/')
    members=Member.objects.filter(member_id=request.session.get('id'))
    return render(request,'member1/member.html',{"members":members})

def editmmember(request,id):
    if request.method=="POST":
        members=Member.objects.get(member_id=id)
        name=request.POST.get('txtname')
        dob=request.POST.get('dob')
        email=request.POST.get('txtemail')
        pwd=request.POST.get('txtps')
        con=request.POST.get('con')
        pr=request.POST.get('profile')
        
        
        if pr!='':
            pro=request.FILES['pr']
            fss=FileSystemStorage()
            sfl=fss.save(pro,pro)
            sfss=fss.url(sfl)
            members.profile=sfss
        
        members.name=name
        members.email=email
        members.password=pwd
        members.contact_no_field=con
        
        
        members.save()
        return redirect('/mmember/')
    members=Member.objects.get(member_id=id)
    return render(request,'member/editmember.html',{"members":members})


def mmemberfunction(request):
    if request.session.has_key('id')==False:
        return redirect('/mlogin/')
    memberfunctions=MemberFunction.objects.filter(member=request.session.get('id'))
    return render(request,'member1/memberfunction.html',{"memberfunctions":memberfunctions})

def addmmemberfunction(request,id):
    if request.session.has_key('id')==False:
        return redirect('/mlogin/')
    if request.method=='POST':
        functions=Function.objects.get(function_id=id)
        name=request.POST.get('name')
        total=request.POST.get('total')
        p=request.POST.get('p')
        # dt=request.POST.get('dt')
        amt=int(total)*int(p)
        member=request.session.get('id')
        m=Member.objects.get(member_id=member)

        memberfunction=MemberFunction(function=functions,member=m,amount=amt,no_of_pass=p,status='unpaid')
        memberfunction.save()
        return redirect('/mmemberfunction/')
    functions=Function.objects.get(function_id=id)
    members=Member.objects.all()
    return render(request,'member1/addmemberfunction.html',{"functions":functions,"members":members})

def editmmemberfunction(request,id):
    if request.session.has_key('id')==False:
        return redirect('/mlogin/')
    if request.method=="POST":
        
        passes=request.POST.get('txtpass')
        
        memberfunction=MemberFunction.objects.get(member_function_id=id)
       
        memberfunction.no_of_pass=passes 
        np=int(passes)*int(memberfunction.function.amount_per_member)
        memberfunction.amount=np
        memberfunction.save()
        return redirect('/mmemberfunction/')
    memberfunctions=MemberFunction.objects.get(member_function_id=id)
    functions=Function.objects.all()
    members=Member.objects.all()
    return render(request,"member1/editmemberfunction.html",{'memberfunctions':memberfunctions,"members":members,"functions":functions})

def mmembermaintenance(request):
    if request.session.has_key('id')==False:
        return redirect('/mlogin/')
    membermaintenances=MemberMaintenance.objects.filter(member=request.session.get('id'))
    return render(request,'member/membermaintenance.html',{"membermaintenances":membermaintenances})

def mnotice(request):
    if request.session.has_key('id')==False:
        return redirect('/mlogin/')
    notices=Notice.objects.all()
    return render(request,'member1/notice.html',{"notices":notices})

def moccupant(request):
    if request.session.has_key('id')==False:
        return redirect('/mlogin/')
   
    occupants=Occupant.objects.filter(member_id=request.session.get('id'))
    return render(request,'member1/occupant.html',{"occupants":occupants})

def addmoccupant(request):
    if request.session.has_key('id')==False:
        return redirect('/mlogin/')
    if request.method=='POST':
        mn=request.POST.get('name')
        nm=request.POST.get('txtreligion')
        mnm=Member.objects.get(member_id=request.session.get('id'))
       
        rg=request.POST.get('gender')
        cdt=request.POST.get('cdt')
        ramt=request.POST.get('txtramount')
        fno=request.POST.get('txtno')
        
        profile=request.FILES['profile']
        fss=FileSystemStorage()
        sfss=fss.save(profile,profile)
        sf=fss.url(sfss)

        occupant=Occupant(member=mnm,name=mn,   religion=nm,gender=rg ,  comming_date=cdt , rent_amount=ramt, no_of_family_member=fno ,profile=sf)
        occupant.save()
        return redirect('/moccupant/')
    members=Member.objects.all()
    return render(request,'member1/addoccupant.html',{"members":members})

def editmoccupant(request,id):
    if request.method=='POST':
        occupants=Occupant.objects.get(occupant_id=id)
        name=request.POST.get("txtname")
        religion=request.POST.get("txtreligion")
        gender=request.POST.get("txtgender")
        cdate=request.POST.get("txtcdate")
        ramount=request.POST.get("txtramount")
        txtno=request.POST.get("txtno")
        txtldate=request.POST.get("txtldate")
        pr=request.POST.get("profile")
        mn=request.session.has_key('id')
        mnm=Member.objects.get(member_id=mn)
        occupants.member=mnm
        occupants.gender=gender
        occupants.religion=religion
        occupants.comming_date=cdate
        occupants.rent_amount=ramount
        occupants.no_of_family_member=txtno
        if txtldate == ' ':
            occupants.leaving_date=''
        else:
            occupants.leaving_date=txtldate

        if pr!='':
            pro=request.FILES['pr']
            fss=FileSystemStorage()
            sfl=fss.save(pro,pro)
            sfss=fss.url(sfl)
            occupants.profile=sfss

        occupants.save()
        return redirect ('/moccupant/')
    occupants=Occupant.objects.get(occupant_id=id)
    return render(request,'member1/editoccupant.html',{"occupants":occupants})

def deletemoccupant(request,id):
    occupants=Occupant.objects.get(occupant_id=id)
    occupants.delete()
    return redirect('/moccupant/') 

def mloggedin(request):
    members=Member.objects.all()
    return render(request,'member/loggedinmember.html',{"members":members})

def nindex(request):
   
    return render(request,'member1/index.html')

def home(request):
    return render(request,'member1/home.html')

def about(request):
    return render(request,'member1/about.html')

def contact(request):
    return render(request,'member1/contact.html')

def invoice(request,id):
    if request.session.has_key('id')==False:
        return redirect('/mlogin/')
    bookings=Booking.objects.get(booking_id=id)
    
    if bookings.status == 'Pending':
        msg='status is pending'
        bookings=Booking.objects.filter(member=request.session.get('id'))
        return render(request,'member1/booking.html',{"msg":msg,"bookings":bookings})
    else:
        msg=''
        bookingdetails=BookingDetail.objects.filter(booking=bookings)
    # bookings=Booking.objects.filter(booking_id=bookingdetails.booking.booking_id)
        return render(request,'member1/invoice.html',{"bookingdetails":bookingdetails,"bookings":bookings,"msg":msg})

def payment(request):
    if request.session.has_key('id')==False:
        return redirect('/mlogin/')
    bookings=Booking.objects.filter(member=request.session.get('id'))
    maintenances=MemberMaintenance.objects.filter(member=request.session.get('id'))
    functions=MemberFunction.objects.filter(member=request.session.get('id'))
    return render(request,'member1/payment.html',{"bookings":bookings,"maintenances":maintenances,"functions":functions})

# visitor side

def vindex(request):
    return render(request,'visitor/index.html')

def vabout(request):
    return render(request,'visitor/about.html')

def vcontact(request):
    return render(request,'visitor/contact.html')

def vhome(request):
    return render(request,'visitor/home.html')

def vadvertisement(request):
    advertisements=Advertisement.objects.filter(status='approve')
    return render(request,'visitor/advertisement.html',{'advertisements':advertisements})

def vmember(request):
    members=Member.objects.all()
    committees=CommitteeDetails.objects.all()
    return render(request,'visitor/member.html',{'members':members,"committees":committees})



#report
def memberrpt(request):
    if request.method=='POST':
        block=request.POST.get('search')
        members=Member.objects.filter(block_no_field=block)
        return render(request,"report/memberrpt.html",{"members":members})
    members=Member.objects.all()
    return render(request,"report/memberr.html",{"members":members})

def occupantrpt(request):
    if request.method=='POST':
        st=request.POST.get('search')
        members=Member.objects.all()
        for m in members:
            if m.name==st:
                occupants=Occupant.objects.filter(member=m.member_id)
                return render(request,"report/occupantrpt.html",{"occupants":occupants})
    occupants=Occupant.objects.all()
    members=Member.objects.all()
    return render(request,"report/occupantr.html",{"occupants":occupants,"members":members})

def advertisementrpt(request):
    if request.method=='POST':
        st=request.POST.get('search')
        members=Member.objects.all()
        for m in members:
            if m.name==st:
                advertisements=Advertisement.objects.filter(member=m.member_id)
        # advertisements=Advertisement.objects.filter()
                return render(request,"report/advertisementrpt.html",{"advertisements":advertisements})
    advertisements=Advertisement.objects.all()
    return render(request,"report/advertisementr.html",{"advertisements":advertisements})

def bookingrpt(request):
    if request.method=='POST':
        id=request.POST.get('search')
        bookingdetails=BookingDetail.objects.filter(booking=id)
        bookings=Booking.objects.get(booking_id=id)
        return render(request,"report/bookingrpt.html",{"bookingdetails":bookingdetails,"bookings":bookings})
    bookings=Booking.objects.all()
    return render(request,"report/bookingr.html",{"bookings":bookings})

def bookingdetailrpt(request):
    # if request.method=='POST':
    #     id=request.POST.get('search')
    #     bookingdetails=BookingDetail.objects.all()
    #     return render(request,"report/bookingdetailr.html",{"bookingdetails":bookingdetails})
    bookingdetails=BookingDetail.objects.all()
    return render(request,"report/bookingdetailr.html",{"bookingdetails":bookingdetails})

def committeerpt(request):
    if request.method=='POST':
        id=request.POST.get('search')
        committeedetails=CommitteeDetails.objects.filter(committee=id)
        return render(request,"report/committeerpt.html",{"committeedetails":committeedetails})
    committees=Committee.objects.all()
    return render(request,"report/committeer.html",{"committees":committees})

def committeedetailrpt(request):
    committeedetails=CommitteeDetails.objects.all()
    return render(request,"report/committeedetailr.html",{"committeedetails":committeedetails})

def depositrpt(request):
    if request.method=='POST':
        bank=request.POST.get('search')
        deposits=Deposit.objects.filter(bank_name=bank)
        amt=0
        for i in deposits:
            amt=amt+i.deposit_amount
        return render(request,"report/depositrpt.html",{"deposits":deposits,"amt":amt})
    deposits=Deposit.objects.all()
    return render(request,"report/depositr.html",{"deposits":deposits})

def expenserpt(request):
    if request.method=='POST':
        my=request.POST.get('search')
    
        sdt=request.POST.get('search')
        stdt=datetime.strptime(sdt+"-"+"01", '%Y-%m-%d').date()
        
        print(stdt)
        ldt=calendar.monthrange(stdt.year,stdt.month)
        print(ldt[1])

        ltdt=datetime.strptime(sdt+"-"+str(ldt[1]), '%Y-%m-%d').date()
        
        expenses=Expense.objects.filter(date__range=(str(stdt),str(ltdt)))
        amt=0
        for e in expenses:
            amt=amt+e.amount
        return render(request,"report/expenserpt.html",{"expenses":expenses,'amt':amt})

    expenses=Expense.objects.all()
    return render(request,"report/expenser.html",{"expenses":expenses})

def functionrpt(request):
    if request.method=='POST':
        dt=request.POST.get('search')
        functions=Function.objects.get(fdate=dt)
        memberfunctions=MemberFunction.objects.filter(function=functions.function_id)
        return render(request,"report/memberfunctionrpt.html",{"memberfunctions":memberfunctions})
    functions=Function.objects.all()
    return render(request,"report/functionr.html",{"functions":functions})

def memberfunctionrpt(request):
    memberfunctions=MemberFunction.objects.all()
    return render(request,"report/memberfunctionr.html",{"memberfunctions":memberfunctions})


def itemrpt(request):
    if request.method=='POST':
        name=request.POST.get('search')
        items=Items.objects.filter(item_name=name)
        return render(request,"report/itemrpt.html",{"items":items})
    items=Items.objects.all()
    return render(request,"report/itemr.html",{"items":items})

def complaintrpt(request):
    if request.method=='POST':
        st=request.POST.get('search')
        complaints=Complaint.objects.filter(status=st)
        return render(request,"report/complaintrpt.html",{"complaints":complaints})
    complaints=Complaint.objects.all()
    return render(request,"report/complaintr.html",{"complaints":complaints})

def incomerpt(request):
    if request.method=='POST':
        my=request.POST.get('search')
    
        sdt=request.POST.get('search')
        stdt=datetime.strptime(sdt+"-"+"01", '%Y-%m-%d').date()
        
        print(stdt)
        ldt=calendar.monthrange(stdt.year,stdt.month)
        print(ldt[1])

        ltdt=datetime.strptime(sdt+"-"+str(ldt[1]), '%Y-%m-%d').date()
        
        incomes=Income.objects.filter(date__range=(str(stdt),str(ltdt)))
        amt=0
        for e in incomes:
            amt=amt+e.amount
        return render(request,"report/incomerpt.html",{"incomes":incomes,"amt":amt})
    incomes=Income.objects.all()
    return render(request,"report/incomer.html",{"incomes":incomes})

def maintenancerpt(request):
    if request.method=='POST':
        name=request.POST.get('search')
        name=str(name)
        maintenances=Maintenance.objects.get(month_year=name)
        members=Member.objects.all()
        membermaintenances=MemberMaintenance.objects.filter(maintenance=maintenances)
        amt=0
        lst=[]
        for e in membermaintenances:
            lst.append(e.member.member_id)
            amt=amt+e.total
        members=Member.objects.all()
        lst1=[]
        for m in members:
            cnt=0
            for e in lst:
                if m.member_id==e:
                    cnt=cnt+1
            if cnt==0:
                lst1.append(m)
        print(lst1)
        
        return render(request,"report/membermaintenancerpt.html",{"membermaintenances":membermaintenances,"amt":amt,"lst1":lst1})
    maintenances=Maintenance.objects.all()
    return render(request,"report/maintenancer.html",{"maintenances":maintenances})

def membermaintenancerpt(request):
    membermaintenances=MemberMaintenance.objects.all()
    return render(request,"report/membermaintenancer.html",{"membermaintenances":membermaintenances})

def noticerpt(request):
    if request.method=='POST':
        st=request.POST.get('search')
        committees=Committee.objects.all()
        for m in committees:
            if m.work_of_committee==st:
                notices=Notice.objects.filter(committee=m.committee_id)
                return render(request,"report/noticerpt.html",{"notices":notices})
    notices=Notice.objects.all()
    committees=Committee.objects.all()
    return render(request,"report/noticer.html",{"notices":notices,'committees':committees})
def searchbyblock(request):
    block=request.POST.get('search')
    members=Member.objects.filter(block_no_field=block)
    return render(request,"report/memberrpt.html",{"members":members})