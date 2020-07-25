from django.shortcuts import render,HttpResponse
import requests
import json



# Create your views here.
def home(request):
    return render(request,'search.html')
def state(request):
    return render(request,'searchstate.html')


    
def search(request):
    query1 = request.GET['query']
    
        
    url = "https://covid-193.p.rapidapi.com/statistics"
   
    querystring = {"country":query1}
    headers = {
         'x-rapidapi-host': "covid-193.p.rapidapi.com",
         'x-rapidapi-key': "4fdebbade4msh8568e7f28f6d9acp1d7b97jsn66f10976032e"
         }

    response = requests.request("GET", url, headers=headers,params = querystring).json()

    data = response['response']

    d = data[0]
    

    print(d)
    context = {
        'all': d['cases']['total'],
        'recovered': d['cases']['recovered'],
        'deaths': d['deaths']['total'],
        'new': d['cases']['new'],
        'critical': d['cases']['critical'],
        'tests':d['tests']['total'],
        'country':d['country']
        
        }


    

    return render(request,'index.html',context)
def searchstate(request):
    return render(request,"temp.html")
def searchstate3(request):
    query2 = request.GET['query2']
    

    

    url = "https://covid-19-india.p.rapidapi.com/state_data"
    

    headers = {
    'x-rapidapi-host': "covid-19-india.p.rapidapi.com",
    'x-rapidapi-key': "4fdebbade4msh8568e7f28f6d9acp1d7b97jsn66f10976032e"
    }

    response = requests.request("GET", url, headers=headers).json()
    data= response['state_data']

    if query2=="Andaman and Nicobar" or query2=="andaman and nicobar":
        d = data[0]
    


    if query2=="Andhra pradesh" or query2=="andhra pradesh":
        d = data[1]
    if query2=="Arunachal pradesh" or query2=="arunachal pradesh":
        d = data[2]
    if query2=="Assam" or query2=="assam":
        d = data[3]
    if query2=="Bihar" or query2=="bihar":
        d = data[4]
    if query2=="Chandigarh" or query2=="chandigarh":
        d = data[5]
    if query2=="Chattisgarh" or query2=="chattisgarh":
        d = data[6]
    if query2=="Dadra and Nagarhaveli" or query2=="dadra and nagarhaveli":
        d = data[7]
    if query2=="daman and diu" or query2=="Daman and Diu":
        d = data[8]
    if query2=="Delhi" or query2=="delhi":
        d = data[9]
    if query2=="Goa" or query2=="goa":
        d = data[10]
    if query2=="Gujarat" or query2=="gujarat":
        d = data[11]
    if query2=="Haryana" or query2=="haryana":
        d = data[12]
    if query2=="himachal pradesh" or query2=="Himachal Pradesh":
        d = data[13]
    if query2=="Jammu and Kashmir" or query2=="jammu and kashmir":
        d = data[14]
    if query2=="Jharkhand" or query2=="jharkhand":
        d = data[15]
    if query2=="Kartnataka" or query2=="karnataka":
        d = data[16]
    if query2=="Kerala" or query2=="kerala":
        d = data[17]
    if query2=="Ladakh" or query2=="ladakh":
        d = data[18]
    if query2=="Lakshadweep" or query2=="lakshadeep":
        d = data[19]
    if query2=="Maharashtra" or query2=="maharashtra":
        d = data[20]
    if query2=="Manipur" or query2=="manipur":
        d = data[21]
    if query2=="Meghalaya" or query2=="meghalaya" or query2=="meghalay":
        d = data[22]
    if query2=="Mizoram" or query2=="mizoram":
        d = data[23]
    if query2=="Madhya pradesh" or query2=="madhya pradesh":
        d = data[24]
    if query2=="Nagaland" or query2=="nagaland":
        d = data[25]
    if query2=="Odisha" or query2=="odisha":
        d = data[26]
    if query2=="Puducherry" or query2=="puducherry" or query2=="punduchery":
        d = data[27]
    if query2=="Punjab" or query2=="punjab":
        d = data[28]
    if query2=="Rajasthan" or query2=="rajasthan":
        d = data[29]
    if query2=="Sikkim" or query2=="sikkim":
        d = data[30]
    if query2=="Tamil nadu" or query2=="tamil nadu" or query2=="tamilnadu":
        d = data[31]
    if query2=="Telengana" or query2=="telengana":
        d = data[32]
    if query2=="Tripura" or query2=="tripura":
        d = data[33]
    if query2=="Uttar pradesh" or query2=="uttar pradesh":
        d = data[34]
    if query2=="Uttarakhand" or query2=="uttrakhand":
        d = data[35]
    if query2=="West bengal" or query2=="west bengal" or query2=="West Bengal":

        d = data[36]
    




    

    context = {
        'total': d['confirmed'],
        'recovered': d['recovered'],
        'deaths': d['deaths'],
        'active': d['active'],
        'death_rate':d['death_rate'],
        'state':d['state'],
        'recovered_rate':d['recovered_rate']
        
        
        }

    print(d)

  
    return render(request,'index2.html',context)
   


    
    
    
    
    
    
    
     