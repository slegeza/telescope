import time
import math
import jdcal
from math import cos,sin,tan,acos,asin,atan
from datetime import datetime
from IPython.display import clear_output

#Initial conditions
im_still_presenting=True
longitude= 83.6123 #W
latitude= 41.6624 #N
tstep=1/5 #timestep between time calculations
utc_time=datetime.utcnow()
New_T=False #New Target
alpha=0 #angle off meridian

class converted_DMS:
    '''For values converted TO DMS from some other unit'''
    newd=0
    newm=0
    news=0
    snewd=''
    snewm=''
    snews=''

class converted_HMS:
    '''The same as above but for HMS.'''
    newh=0
    newm=0
    news=0
    snewh=''
    snewm=''
    snews=''

class Coordinates:
    lon=83.6123
    E=1
    W=0
    lat=41.6624
    N=1
    S=0
    
class current_DEC:
    degree=0
    minute=0
    second=0
    sdegree=''
    sminute=''
    ssecond=''

class current_GST:
    '''Current Greenwich Sidereal Time'''
    hour=0
    minute=0
    second=0
    shour=''
    sminute=''
    ssecond=''

class current_HA:
    hour=0
    minute=0
    second=0
    shour='0'
    sminute='0'
    ssecond='0'  

class current_LST:
    hour=0
    minute=0
    second=0
    shour=''
    sminute=''
    ssecond=''  
    
class current_RA:
    hour=0
    minute=0
    second=0
    shour=current_LST.shour
    sminute=current_LST.sminute
    ssecond=current_LST.ssecond

class equinox:
    '''Defining point where RA is zero (vernal equinox at Greenwich at noon)'''
    year=utc_time.year
    month=3
    day=21
    hour=12
    minute=0
    second=0

class sday:
    '''1 solar day=this many sidreal days.'''
    year=1.
    month=1.
    day=1.
    hour=23.
    minute=56.
    second=4.091   
    
class target_DEC:
    degree=0
    minute=0
    second=0
    sdegree='0'
    sminute='0'
    ssecond='0'

class target_RA:
    hour=0
    minute=0
    second=0
    shour='0'
    sminute='0'
    ssecond='0'
    
class target_temp:
    hour=0
    minute=0
    second=0
    shour='0'
    sminute='0'
    ssecond='0'
    degree=0
    dminute=0
    dsecond=0
    dsdegree='0'
    dsminute='0'
    dssecond='0'
        
def airmass():
    '''Airmass
    
    x=altitude of telescope above horizon.'''
   # z=90-altitude()
    return 
  
def altitude():
    '''Finds angle between telescope and ground.'''
    #theta=abs(HMS_Degrees(current_HA)) #theta=decimal degree value for hour angle.
    #delta=abs(DMS_Degrees(current_DEC))
    #90-theta=the angle between the telescope and the ground
    #x=90-abs(asin((sin(latitude)*sin(delta))+(cos(latitude)*cos(delta)*cos(theta))))
    #alt=abs(round(x,2))
    return 

def DecimalYear(x):
    '''Converts dates into decimal years'''
    year_num=x-datetime(year=x.year, month=1, day=1,hour=0,minute=0,second=0)
    year_den=datetime(year=x.year+1, month=1, day=1,hour=0,minute=0,second=0) - datetime(year=x.year, \
            month=1, day=1,hour=0,minute=0,second=0)
    return x.year + year_num/year_den

def DEC(x,theta):
    '''this is useless why did I make this function'''
    return 0

def Degrees_DMS(x):
    '''Similar to Degrees_DMS, but converts decimal degrees into degress minutes seconds.'''
    while x>=360.:
        x-=360
    dec,int_=math.modf(x)
    degree=int(int_)
    
    minute=dec*60
    dec,int_=math.modf(minute)
    second=dec*60
    minute=int(int_)
    second=round(second,3)
    sdegree=str(degree)
    sminute=str(minute)
    ssecond=str(second)
    
    converted_DMS.newd=degree
    converted_DMS.newm=minute
    converted_DMS.news=second
    converted_DMS.snewd=sdegree
    converted_DMS.snewm=sminute
    converted_DMS.snews=ssecond
    return #sdegree+' h '+ sminute +' m '+ssecond+'s'
    
def Degrees_HMS(x):
    '''Does the exact opposite of HMS_Degrees.'''
    while x>=360.:
        x-=360
    dec,int_=math.modf(x)
    hour=int(int_)
    #minute,int_=math.modf(hour)
    minute=dec*60
    dec,int_=math.modf(minute)
    second=dec*60
    minute=int(int_)
    second=round(second,3)
    shour=str(hour)
    sminute=str(minute)
    ssecond=str(second)
    
    converted_HMS.newh=hour
    converted_HMS.newm=minute
    converted_HMS.news=second
    converted_HMS.snewh=shour
    converted_HMS.snewm=sminute
    converted_HMS.snews=ssecond
    return

def DMS_Degrees(x):
    '''Similar to HMS_Degrees, but accepts an argument of degrees minutes seconds and puts it into decimal degrees.'''
    degree,minute,second=x.degree,x.minute,x.second
    a=degree
    b=minute/60.
    c=second/3600
    return a+b+c

def HA(x):
    '''Instantaneous hour angle, or angle from meridian in DMS.
    x=alpha=RA in HMS'''
    phi=HMS_Degrees(x)
    l=HMS_Degrees(current_LST)
    phi-=l
    Degrees_HMS(phi)
    if phi>0:
        current_HA.hour=converted_HMS.newh*-1
        current_HA.minute=abs(converted_HMS.newm)
        current_HA.second=abs(converted_HMS.news)
        current_HA.shour='-'+str(converted_HMS.snewh)
        current_HA.sminute=str(current_HA.minute)
        current_HA.ssecond=str(current_HA.second)
    else:
        current_HA.hour=converted_HMS.newh*-1
        current_HA.minute=converted_HMS.newm*-1
        current_HA.second=converted_HMS.news*-1
        current_HA.shour='+'+str(current_HA.hour)
        current_HA.sminute=str(current_HA.minute)
        current_HA.ssecond=str(current_HA.second)
    
    return 0

def HMS_Degrees(x):
    '''Converts HMS measurements (sidereal time, RA) to decimal degrees.'''
    hour,minute,second=x.hour,x.minute,x.second
    a=hour
    b=minute/60.
    c=second/3600
    return a+b+c

def JD(x):
    ''' Converts UTC time into Julian date
    http://129.79.46.40/~foxd/cdrom/musings/formulas/formulas.htm
    
    The above website contains all kinds of useful formulae for
    this type of stuff :)'''
    return sum(jdcal.gcal2jd(x.year,x.month,x.day))

def LST(x):
    '''This gives us Greenwich LST and local LST as a function of longitude.'''
    #Greenwich Sidereal Time
    #JD @ 0 hours GMT
    julian=sum(jdcal.gcal2jd(x.year,x.month,x.day))
    #print(julian)
    
    h,m,s=x.hour,x.minute,x.second
    ctime=h+m/60.+s/3600. #UTC time in decimal hours
    T=(julian-2451545.0)/36525.0
    #Current Sidereal Time in Greenwich:
    T0=6.697374558+(2400.051336*T)+(0.000025862*(T**2))+(ctime*1.0027379093)
    
    while T0>=24:
        T0-=24 #GST in decimal hours
    
    if Coordinates.W==1:
        lon=longitude*-1
        E=1
        W=0
    else:
        lon=longitude
    
    dec1,int_=math.modf(T0) #int=hours, dec1=frac. of hours
    #print(int_,dec1)
    hour=int_ #h=value for hour
    #print(hour,'hours!')
    dec2,int_=math.modf(T0)
    #print(dec2,int_)
    dec2*=60. #dec2=value for minutes
    #print(dec2,'minutes!')
    dec3,int_=math.modf(dec2)
    dec3*=60 #dec3=value for seconds.  NOT an integer.
    dec3=round(dec3,3) #rounding off the seconds value
    dec2=int(dec2) #rounding off the minutes value.  The extra bit was passed to the seconds.
    #print(dec3,'seconds!')
    temp=hour
    hour=int(temp) #rounding off for hours
    
    
    #Hour, Dec2, and Dec3 at this point are LST at Greenwich in HMS
    current_GST.hour=hour
    while current_GST.hour>=24:
        current_GST.hour-=24
    current_GST.minute=dec2
    while current_GST.minute>=60.:
        current_GST.hour+=1
        current_GST.minute-=60
    current_GST.second=dec3
    while current_GST.second>=60.:
        current_GST.minute+=1
        current_GST.second-=60
    #print(hour,dec2,dec3)
    s_hour,s_dec2,s_dec3=str(hour),str(dec2),str(dec3)
    current_GST.shour=s_hour+'h '
    current_GST.sminute=s_dec2+'m '
    current_GST.ssecond=s_dec3+'s '
    
    #Now the class current_GST contains up to date values for the Greenwich LST :)
    
    #Now, for the local LST depending on longitude:
    lst=T0-(longitude/15.)
    while lst<0:
        lst+=24.
    #As above:
    #print(lst)
    dec1,int_=math.modf(lst) #int=hours, dec1=frac. of hours
    #print(int_,dec1)
    hour=int_ #h=value for hour
    #print(hour,'hours!')
    dec2,int_=math.modf(lst)
    #print(dec2,int_)
    dec2*=60. #dec2=value for minutes
    #print(dec2,'minutes!')
    dec3,int_=math.modf(dec2)
    dec3*=60 #dec3=value for seconds.  NOT an integer.
    dec3=round(dec3,3) #rounding off the seconds value
    dec2=int(dec2) #rounding off the minutes value.  The extra bit was passed to the seconds.
    #print(dec3,'seconds!')
    temp=hour
    hour=int(temp) #rounding off for hours
    
    current_LST.hour=hour
    while current_LST.hour>=24.:
        current_LST.hour-=24
    current_LST.minute=dec2
    while current_LST.minute>=60.:
        current_LST.hour+=1
        current_LST.minute-=60.
    current_LST.second=dec3
    while current_LST.second>=60.:
        current_LST.minute+=1
        currenet_LST.second-=60.
    s_hour2,s_dec2,s_dec3=str(hour),str(dec2),str(dec3)
    current_LST.shour=s_hour2
    current_LST.sminute=s_dec2
    current_LST.ssecond=s_dec3  
    return 
    
def NewTarget():
    '''Gets target info from user, and updates hour angle from that.'''
    target_RA.hour=   int(input('Enter RA hour   : '))
    while target_RA.hour>=24:
        target_RA.hour-=24
    target_RA.minute= int(input('Enter RA minute : '))
    while target_RA.minute>=60.:
        target_RA.hour+=1
        target_RA.minute-=60
    target_RA.second= float(input('Enter RA second : '))
    while target_RA.second>=60:
        target_RA.minute+=1
        target_RA.second-=60
    target_DEC.degree=int(input('Enter DEC degree: '))
    while target_DEC.degree>=90:
        target_DEC.degree-=90
    target_DEC.minute= int(input('Enter DEC minute: '))
    while target_DEC.minute>=60.:
        target_DEC.degree+=1
        target_DEC.minute-=60
    target_DEC.second=float(input('Enter DEC second: '))
    while target_DEC.second>=60:
        target_DEC.minute+=1
        target_DEC.second-=60
    target_RA.shour,target_RA.sminute,target_RA.ssecond=str(target_RA.hour), \
                str(target_RA.minute),str(target_RA.second)
    target_DEC.sdegree,target_DEC.sminute,target_DEC.ssecond=str(target_DEC.degree), \
                str(target_DEC.minute),str(target_DEC.second) 
    if target_DEC.degree<-90 or target_DEC.degree>90:
        zeroTarget()
        IsTracking=False
    return

def RA(x,ha):
    '''Returns instantaneous RA, which is a function of time and hour angle.
    x=current_LST
    ha=hour angle in decimal degrees'''
    if IsTracking==False:
        d=HMS_Degrees(x)+ha
        Degrees_HMS(d)
        current_RA.hour=converted_HMS.newh
        current_RA.minute=converted_HMS.newm
        current_RA.second=converted_HMS.news
        current_RA.shour=converted_HMS.snewh
        current_RA.sminute=converted_HMS.snewm
        current_RA.ssecond=converted_HMS.snews
    
    return 

def RA_Change(x):
    '''Calculates difference in right ascension from current position and target.'''
    current_pos=DMS_Degrees(current_RA)
    target_pos =DMS_Degrees(target_RA)
    diff=target_pos-current_pos
    return Degrees_HMS(diff)

def Track():
    '''Tracks a target, specified by target classes.'''
    current_RA.hour=target_RA.hour
    current_RA.minute=target_RA.minute
    current_RA.second=target_RA.second
    current_DEC.degree=target_DEC.degree
    current_DEC.minute=target_DEC.minute
    current_DEC.second=target_DEC.second
    current_RA.shour=str(target_RA.hour)
    current_RA.sminute=str(target_RA.minute)
    current_RA.ssecond=str(target_RA.second)
    current_DEC.sdegree=str(target_DEC.degree)
    current_DEC.sminute=str(target_DEC.minute)
    current_DEC.ssecond=str(target_DEC.second)
    global IsTracking
    IsTracking=True
    return

def Status():
    if IsTracking==False:
        return 'Locked'
    else:
        return 'Tracking!'
    return

def StopTrack():
    global IsTracking
    IsTracking=False
    return

def zero_All():
    '''Zeros telescope!'''
    zero_DEC()
    zero_RA()
    return

def zero_DEC():
    Degrees_DMS(latitude)
    current_DEC.degree=converted_DMS.newd
    current_DEC.minute=converted_DMS.newm
    current_DEC.second=converted_DMS.news
    current_DEC.sdegree=converted_DMS.snewd
    current_DEC.sminute=converted_DMS.snewm
    current_DEC.ssecond=converted_DMS.snews
    return 
    
def zero_RA():
    if IsTracking==False:
        current_RA.hour=current_LST.hour
        current_RA.minute=current_LST.minute
        current_RA.second=current_LST.second
        current_RA.shour=current_LST.shour
        current_RA.sminute=current_LST.sminute
        current_RA.ssecond=current_LST.ssecond
    return 

def zero_Target():
    '''Zeros the values for target...do I really have to write that?'''
    target_RA.hour=0
    target_RA.minute=0
    target_RA.second=0
    target_RA.shour='0'
    target_RA.sminute='0'
    target_RA.ssecond='0'
    target_DEC.degree=0
    target_DEC.minute=0
    target_DEC.second=0
    target_DEC.sdegree='0'
    target_DEC.sminute='0'
    target_DEC.ssecond='0'
    return

IsTracking=False
zero_RA() #sets RA to meridian
zero_DEC()
zero_Target()

go=0 #condition for program to prompt for target position

if go==1:
    NewTarget()
else:
    StopTrack()
    
while im_still_presenting==True:
    utc_time,loc_time=datetime.utcnow(),time.ctime()
    LST(utc_time)
    RA(current_LST,alpha)
    if IsTracking==False:
        HA(current_RA)
    else:
        HA(target_RA)
    if go==1: Track()
    print('Coordinates: ', latitude, ' N',longitude, ' W',flush=True)
    print('',flush=True)
    
    print('UTC        :',utc_time,'     Julian Day:',JD(utc_time),flush=True)
    print('Local time :',loc_time,'       Air Mass  :','....',flush=True)
    #print(DateToDecimal(utc_time))     
    print('LST        :',current_LST.shour+'h',current_LST.sminute+'m',current_LST.ssecond+'s','               Altitude  :','....',\
          'degrees',flush=True)
    print('Hour Angle :',current_HA.shour+'h',current_HA.sminute+'m',current_HA.ssecond+'s',flush=True)
    print('--------------------------------------------------------------------',flush=True)
    print('Target Data:','                  Current Status: ',Status(),flush=True)
    print('',flush=True)
    print('Target RA  :',target_RA.shour+'h',target_RA.sminute+'m',target_RA.ssecond+'s',
          '          Current RA:',current_RA.shour+'h',current_RA.sminute+'m',current_RA.ssecond+'s',flush=True)
    print('Target DEC :',target_DEC.sdegree+'\xb0',target_DEC.sminute+'m',target_DEC.ssecond+'s',
          '          Current DEC:',current_DEC.sdegree+'\xb0',current_DEC.sminute+'m',current_DEC.ssecond+'s',flush=True)
    time.sleep(tstep)
    clear_output(wait=True)
