#!/usr/bin/env python
# coding: utf-8

# In[1]:


# IMPORTING LIBRARIES

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:

### BUSINESS UNDERSTANDING


# In[3]:
"""
In this notebook we'll be exploring the data from AirBnb Barcelona dataset http://insideairbnb.com/get-the-data.html published in year 2019. Datasets involves insights of interest related to prices, neigbourhoods, avalability or room types in the city.

In recent years, I came across people who plans to go Toronto with various reasons. This reasons are mostly for studying, settling, working. And some of them was travelling or short term seminars or training courses. So there are people who wants to choose where to stay for long or short terms. And I am also in the group for long term staying. So I decided to analyze Toronto data for everyone and tried to answer mostly general questions below which everyone wants to know about before renting Airbnb house.


1) Which districts have most alternative for different style of houses, where are the Airbnb guests clusters?

2) Where the clients mostly looking a house for renting, what are the most popular districts for users?

3) What is the map looks like when seperating the districts? Is it possible to see which locations of most popular 2 districts have the most reviews? Which locations of most popular 2 districts are cheaper then the rest? (On City Map)

4) What is the distribution of room types by districts, and how is it looks in map? 

5) Can we analyze all mean prices according to room types seperatly and district by district?

6) Which moths are the most expensive months? When clients startes to search their target Airbnb, what are the most popular months for clients, and can we compare it for 2 years?


For answering these questions, I created this notebook with visualizations.. If Airbnb publishs new data or update the data below, you can still use this notebook to analyse new/updated dataset.

Let's start with loading datas..

"""

# In[4]:

# LOADING DATAS

calendar=pd.read_csv('calendar.csv')
listing=pd.read_csv('listings.csv')
reviews=pd.read_csv('reviews.csv')
neighbourhoods=pd.read_csv('neighbourhoods.csv')



# In[5]:

listing.head()

# In[6]:


calendar.head()


# In[7]:


calendar.shape


# I want to make 'neighbourhood classification' for enable to see all in one map. 
# So, because of the data is missing for what I wanna see, I needed to import district names manually.
# I took region names from wikipedia

# In[9]:


Downtown_Core = [
'Alexandra Park','Annex','Baldwin Village',
'Cabbagetown','CityPlace','Chinatown','Church and Wellesley','Corktown','Discovery District','Distillery District',
'The Entertainment District','East Bayfront','Fashion District','Financial District','Garden District',
'Grange Park','Harbord Village','Harbourfront','Kensington Market','Little Japan','Moss Park','Old Town',
'Quayside','Queen Street West','Regent Park','South Core','St. James Town','St. Lawrence','Toronto Islands',
'Trefann Court','University (includes Huron–Sussex)','Yorkville',
'Waterfront Communities-The Island',
'Church-Yonge Corridor','Kensington-Chinatown','Cabbagetown-South St.James Town','University',
'North St.James Town'
    
]

East_End = [
'The Beaches','The Beach','East Chinatown','East Danforth',
'Gerrard Street East', 'Gerrard India Bazaar', 'Little India','Greektown','Danforth',
'Leslieville','Main Square','Playter Estates','Port Lands', 'Villiers Island','Riverdale','Upper Beaches',
'Bay Street Corridor','Woodbine Corridor','South Riverdale','East Riverdale','Danforth East York',
'Playter Estates-Danforth','North Riverdale','Blake-Jones','East End-Danforth'
]

North_End = [
'Bedford Park','Casa Loma','Chaplin Estates','Davisville Village','Deer Park', 'Yonge', 'St. Clair',
'Forest Hill', 'Forest Hill Village', 'Upper Village','Lawrence Park','Lytton Park','Midtown','Moore Park',
'North Toronto','Rosedale','South Hill', 'Rathnelly','Summerhill','Uptown','Wanless Park','Wychwood Park',
'Yonge–Eglinton', 'Midtown Toronto',
'Rosedale-Moore Park','Yonge–Eglinton','Wychwood Park','Wychwood Park','Mount Pleasant West',
'Mount Pleasant East','Lawrence Park South','Lawrence Park North','Forest Hill South','Forest Hill North',
'Wychwood','Bedford Park-Nortown'
]


# In[10]:


West_End = [
'Beaconsfield Village','Bloor West Village','Bracondale Hill','Brockton Village','Carleton Village',
'Corso Italia','Davenport','Dovercourt Park','Dufferin Grove','Earlscourt','Fort York','High Park',
'The Junction', 'West Toronto', 'Dundas Street', 'Little Malta','Junction Triangle',
'Koreatown','Liberty Village','Little Italy','Little Portugal','Little Tibet','Mirvish Village',
'Niagara','Palmerston','Parkdale','Queen Street West','Regal Heights',
'Roncesvalles','Runnymede','Seaton Village','Swansea','Trinity–Bellwoods','Wallace Emerson',
'South Parkdale','Palmerston-Little Italy',
'Dovercourt-Wallace Emerson-Junction','Corso Italia-Davenport','High Park-Swansea','Trinity-Bellwoods',
'Weston-Pellam Park','Runnymede-Bloor West Village','Junction Area'
]

East_York = [
'Broadview North','Crescent Town','East Danforth','Pape Village','Woodbine Heights',
'Bermondsey','Governor s Bridge','Leaside','O Connor–Parkview','Thorncliffe Park',
'Greenwood-Coxwell','Woodbine Heights','Woodbine-Lumsden','Taylor-Massey','Old East York',
"O'Connor-Parkview",'Leaside-Bennington'
]

Etobicoke = [
'Alderwood','Centennial Park','Clairville','Eatonville', 'Etobicoke West Mall','The Elms',
'Eringate','Humber Bay','Humber Heights – Westmount','Humber Valley Village','Humberwood',
'Islington–City Centre West','Kingsview Village', 'The Westway','The Kingsway','Long Branch',
'Markland Wood','Mimico','New Toronto','Princess Gardens','Rexdale','Richview','Smithfield',
'Stonegate-Queensway','Sunnylea','Thistletown','Thorncrest Village','West Humber-Clairville',
'West Deane Park','Willowridge',
'Islington-City Centre West','Elms-Old Rexdale','Rexdale-Kipling','Yonge-Eglinton','Yonge-St.Clair',
'Willowridge-Martingrove-Richview','Thistletown-Beaumond Heights','Princess-Rosethorn',
'Mount Olive-Silverstone-Jamestown','Mimico (includes Humber Bay Shores)','Kingsway South',
'Kingsview Village-The Westway','Humber Heights-Westmount','Humber Heights-Westmount',
'Eringate-Centennial-West Deane','Humber Heights-Westmount','Edenbridge-Humber Valley'
]


# In[11]:


North_York= [
'Amesbury','Armour Heights','Bathurst Manor','Bayview Village','Bayview Woods-Steeles','Bermondsey',
'Black Creek','The Bridle Path','Clanton Park', 'Wilson Heights','Don Mills','Don Valley Village',
'Downsview','Flemingdon Park','Glen Park', 'Yorkdale', 'Glen Park', 'Englemount', 'Marlee Village',
'Henry Farm','Hillcrest Village','Hoggs Hollow','Humber Summit','Humbermede', 'Emery',
'Jane and Finch', 'University Heights', 'Elia','Lansing','Lawrence Heights','Lawrence Manor',
'Ledbury Park','Maple Leaf','Newtonbrook','North York City Centre','Parkway Forest','Parkwoods',
'The Peanut','Pelmo Park', 'Humberlea','Pleasant View','Uptown Toronto','Victoria Village','Westminster–Branson',
'Willowdale','York Mills','York University Heights', 'Village at York','Banbury-Don Mills' ,'Yorkdale-Glen Park',
'Willowdale East','Willowdale West','Westminster-Branson','St.Andrew-Windfields','Pelmo Park-Humberlea',
'Parkwoods-Donalda','Newtonbrook West','Newtonbrook East','Lansing-Westgate','Glenfield-Jane Heights',
'Glenfield-Jane Heights','Englemount-Lawrence','Glenfield-Jane Heights','Willowdale West','Willowdale East',
'Westminster-Branson','St.Andrew-Windfields','Rustic','Pelmo Park-Humberlea','Parkwoods-Donalda',
'Bridle Path-Sunnybrook-York Mills','Brookhaven-Amesbury','Downsview-Roding-CFB'

]

Scarborough= [
'Agincourt','Armadale','Bendale', 'Cedarbrae','Birch Cliff','Birch Cliff Heights','Brown s Corners',
'Clairlea','Cliffside','Cliffcrest','Dorset Park','Eglinton East','Golden Mile','Guildwood','Highland Creek',
'Ionview', "L'Amoreaux" ,'Malvern','Maryvale','Milliken','Morningside','Morningside Heights','Oakridge',
'Port Union', 'Centennial Scarborough','Rouge','Scarborough City Centre','Scarborough Junction',
'Scarborough Village','Steeles','Tam O Shanter','Sullivan','West Hill','West Rouge','Wexford','Woburn',
'Wexford/Maryvale','Agincourt North','Agincourt South-Malvern West','Agincourt','Agincourt North',
'Tam OShanter-Sullivan','Kennedy Park','Birchcliffe-Cliffside','Clairlea-Birchmount'

]

York= [
'Baby Point',
'Briar Hill','Belgravia',
'Eglinton West', 'Little Jamaica',
'Fairbank', 'Caledonia','Fairbank',
'Humewood–Cedarvale',  'Upper Village', 'Forest Hill',
'Lambton',
'Mount Dennis',
'Oakwood–Vaughan', 'Oakwood Village', 'Five Points', 'Northcliffe',
'Old Mill',
'Rockcliffe–Smythe',
'Silverthorn' ,'Keelesdale',
'Tichester',
'Weston',
'Briar Hill-Belgravia',
'Rockcliffe-Smythe',
'High Park North','Rustic',
'Lambton Baby Point',
'Keelesdale-Eglinton West','Humewood-Cedarvale','Beechborough-Greenbrook','Caledonia-Fairbank'
]


# In[13]:


dictDowntown=dict()
dictEastend=dict()
dictNorthend=dict()

dictWestend=dict()
dictEastyork=dict()
dictEtobicoke=dict()

dictNorthyork=dict()
dictScarborough=dict()
dictYork=dict()


for i in Downtown_Core:
    dictDowntown[i]="Downtown_Core"

for i in East_End:
    dictEastend[i]="East_End"

for i in North_End:
    dictNorthend[i]="North_End"
    
for i in West_End:
    dictWestend[i]="West_End"

for i in East_York:
    dictEastyork[i]="East_York"

for i in Etobicoke:
    dictEtobicoke[i]="Etobicoke"
    
for i in North_York:
    dictNorthyork[i]="North_York"
    
for i in Scarborough:
    dictScarborough[i]="Scarborough"
    
for i in York:
    dictYork[i]="York"
    
    
for i in range(len(listing)):
    
    if listing["neighbourhood"][i] in dictDowntown:
        listing["neighbourhood_group"][i] = "Downtown Core"
    elif listing["neighbourhood"][i] in dictEastend:
        listing["neighbourhood_group"][i] = "East End"
    elif listing["neighbourhood"][i] in dictNorthend:
        listing["neighbourhood_group"][i] = "North End"
        
        
    elif listing["neighbourhood"][i] in dictWestend:
        listing["neighbourhood_group"][i] = "West End"
    elif listing["neighbourhood"][i] in dictEastyork:
        listing["neighbourhood_group"][i] = "East York"
    elif listing["neighbourhood"][i] in dictEtobicoke:
        listing["neighbourhood_group"][i] = "Etobicoke"
        
    elif listing["neighbourhood"][i] in dictNorthyork:
        listing["neighbourhood_group"][i] = "North York"
    elif listing["neighbourhood"][i] in dictScarborough:
        listing["neighbourhood_group"][i] = "Scarborough"
    elif listing["neighbourhood"][i] in dictYork:
        listing["neighbourhood_group"][i] = "York"
        
        
    else:
        listing["neighbourhood_group"][i] = 0


# In[ ]:





# # DATA PREPARING

# In[ ]:





# In[15]:



for i in range(len(neighbourhoods)):
    
    if neighbourhoods["neighbourhood"][i] in dictDowntown:
        neighbourhoods["neighbourhood_group"][i] = "Downtown Core"
    elif neighbourhoods["neighbourhood"][i] in dictEastend:
        neighbourhoods["neighbourhood_group"][i] = "East End"
    elif neighbourhoods["neighbourhood"][i] in dictNorthend:
        neighbourhoods["neighbourhood_group"][i] = "North End"  
        
    elif neighbourhoods["neighbourhood"][i] in dictWestend:
        neighbourhoods["neighbourhood_group"][i] = "West End"
    elif neighbourhoods["neighbourhood"][i] in dictEastyork:
        neighbourhoods["neighbourhood_group"][i] = "East York"
    elif neighbourhoods["neighbourhood"][i] in dictEtobicoke:
        neighbourhoods["neighbourhood_group"][i] = "Etobicoke"
        
    elif neighbourhoods["neighbourhood"][i] in dictNorthyork:
        neighbourhoods["neighbourhood_group"][i] = "North York"
    elif neighbourhoods["neighbourhood"][i] in dictScarborough:
        neighbourhoods["neighbourhood_group"][i] = "Scarborough"
    elif neighbourhoods["neighbourhood"][i] in dictYork:
        neighbourhoods["neighbourhood_group"][i] = "York"
        
    else:
        neighbourhoods["neighbourhood_group"][i] = 0


# In[ ]:





# In[19]:


# District Scarborough data is broken, so we will change it manually.


# In[16]:


neighbourhoods['neighbourhood_group'].isin([0]).sum()


# In[17]:


neighbourhoods['neighbourhood_group'][114:115]="Scarborough"


# In[18]:


neighbourhoods['neighbourhood_group'].isin([0]).sum()


# In[20]:


# Now it's ok!
# But there are still some districts where not be assigned!
# Let's see them..


# In[21]:


listing['neighbourhood_group'].isin([0]).sum()


# In[22]:


listing[listing['neighbourhood_group'].isin([0])]


# In[23]:


# We changed 0 values to NaN values with .mask then filled NaN values with 'Scarborough'

listing['neighbourhood_group']=listing.neighbourhood_group.mask(listing.neighbourhood_group==0).fillna("Scarborough")


# In[25]:


listing['neighbourhood_group'].isin([0]).sum()


# In[26]:


# NOW WE ALL CLEAR WITH 'NEIGHBOURHOOD GROUP' COLUMN..


# In[ ]:





# # DATA WRANGLING

# In[28]:



#First will rename neigbourhood_group column to district in both datatsets to enable to match them up..
neighbourhoods = neighbourhoods.rename(columns={"neighbourhood_group": "district"})
listing = listing.rename(columns={"neighbourhood_group": "district"})

#There are not necessary id columns(id, host_id) neither for description columns (name, host_name)
listing = listing.drop(['name', 'host_name'], axis=1)

#Print all columns without NA values
no_nulls = set(listing.columns[listing.isnull().mean()==0])
print(no_nulls)


# In[29]:


listing.head()


# In[30]:


listing.isnull().sum()


# In[31]:


nan_values=listing['last_review'].isnull().sum()/listing.shape[0]


print(nan_values)


# This is our perentage of NaN values for 'last_review' and 'reviews_per_month' on listing dataset..
# 
# We have approximately %19 missing values on'last_review' and 'reviews_per_month' columns on listing dataset..

# In[32]:


listing.number_of_reviews


# In[33]:


# Let's make some parsing and cleaning..

# I don't wanna see adverts which 'number of reviews' less than 2..


# In[36]:


listing=listing[listing.number_of_reviews >=2]
listing.shape


# In[37]:


# We will create new columns from date column, we need to seperate date column to day-month-year columns.


# In[38]:


listing['year'] = pd.DatetimeIndex(listing['last_review']).year
listing['month'] = pd.DatetimeIndex(listing['last_review']).month
listing['day'] = pd.DatetimeIndex(listing['last_review']).day


# NOTE: As we know, there are few adverts before 2016, there are few adverts before 2016. So it might be miscalculation with few data.
# 
# So I decided to delete datas before 2016 for better analysis

# In[40]:


listing=listing[listing.year>2015]


# In[42]:


listing.shape


# In[ ]:





# In[43]:


# Let's check how many of airbnb advert not available even one day..
listing[listing.availability_365==0]


# In[44]:


# And let's check the availability list for each airbnb advert.

listing.availability_365


# In[ ]:





# In[45]:


# And now we will plot numver of districts by airbnb adv.


# In[47]:


#Show number of adverts by district

plt.figure(figsize = (10, 5))
ax = sns.countplot(x='district', data=listing, order = listing.district.value_counts().sort_values(ascending=False).index)
ax.set_xlabel('Districts', weight='normal', size=15)
ax.set_ylabel('Number of AirBnb', weight='normal', size=15)
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right", size=12)
plt.title('The number of Airbnb in Toronto', fontsize=18)

plt.show()

listing.district.value_counts().sort_values(ascending=False)


# So, from 2016 to 2020 we can see most popular(most adverts) districts for airbnb hosts.

# In[ ]:





# In[49]:



#Visualization of bookings in the Toronto map (according on latitude and longitude columns)


plt.figure(figsize=(10,6))
sns.scatterplot(listing.longitude,listing.latitude,hue=listing.district)
plt.ioff()


# And we can see the advert maps for 9 regions in the map (with a few deviation)

# In[50]:


# Now lets loot at adverts with most clicks and visualize it by district to catch up more productive search 

# First, we will groupby by district and create new dataset..


# In[52]:



#Visualization of bookings in the Toronto map (according on latitude and longitude columns)
# We can't see weighted map for full toronto easily

plt.figure(figsize=(10,6))
sns.scatterplot(listing.longitude,listing.latitude,data=listing,size=listing.number_of_reviews,hue=listing.district)
plt.ioff()


# Now here we can see adverts by their popularity with number of reviews weights..

# In[53]:


# Relplot is easier library to see it.. But still not enough!

sns.relplot(x="longitude", y="latitude", hue="district", size="number_of_reviews",
            sizes=(1, 1000), alpha=.8, palette="muted",
            height=10, data=listing)


# It will be better if we will look closely to the map by district since we have most of the intencity on 1 or 2 districts..
# 
# For this, we need to specify-explore which districts have more demand compering to the others.

# In[58]:


numreviews=listing.groupby('district').sum()
numreviews.index.name=None
numreviews.index


# In[56]:


# I want to boxplot the data to see the distribution of reviews


# In[59]:


#Show number of adverts by district
plt.figure(figsize = (10, 5))
ax = sns.barplot(x=numreviews.index, y='number_of_reviews', data=numreviews)
ax.set_xlabel('Districts', weight='normal', size=15)
ax.set_ylabel('Number of Review', weight='normal', size=15)
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right", size=12)
plt.title('The number of Reviews by District in Toronto', fontsize=18)

plt.show()


# As we see, more than %75 percent of reviews belongs to Downtown Core & West End regions.
# 
# Lets visualize it on map for see district popular area more closely..

# In[60]:


downtown=listing[(listing['district'] == "Downtown Core" )]

westend=listing[(listing['district'] == "West End" )]


# In[ ]:





# In[66]:


# DOWNTOWN MAP BY ROOM TYPE - PRICE

sns.relplot(x="longitude", y="latitude", hue="room_type", size="price",
            sizes=(1 , 1000), alpha=.6, palette="muted",
            height=8, data=downtown)


# For Downtown, it seems southern west is more popular area.. We can assume that most activities centered around here. 

# ### WEST END MAP BY ROOM TYPE - PRICE
# 

# In[67]:



sns.relplot(x="longitude", y="latitude", hue="room_type", size="price",
            sizes=(1 , 1000), alpha=.6, palette="muted",
            height=8, data=westend)


# For Westend, south seems more solid.. You can consider this information when you choose your flat.  

# This two districts we looked at are the most popular districts.
# 
# For me it is good to see popular areas of specific regions since we have options to choose place with searching on map.
# 
# 

# In[ ]:





# Now lets look at the room type data and use it with height map.
# 
# We can also see distribution by room type on height map.

# In[ ]:





# ### Show number and type of rooms by neighbourhood

# In[70]:



plt.figure(figsize = (15, 6))
ax = sns.countplot(x='district', hue='room_type', data=listing)

#set the axes
ax.set_xlabel('Districts', weight='normal', size=15)
ax.set_ylabel('Number of Room types', weight='normal', size=15)
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")

plt.title('Room type by district', fontsize=18)

plt.show()


# In[71]:


westend_entire=listing[(listing["room_type"]=="Entire home/apt") & (listing['district'] == "West End" )]
westend_private=listing[(listing["room_type"]=="Private room") & (listing['district'] == "West End" )]
downtown_entire=listing[(listing["room_type"]=="Entire home/apt") & (listing['district'] == "Downtown Core" )]
downtown_private=listing[(listing["room_type"]=="Private room") & (listing['district'] == "Downtown Core" )]


# In[ ]:



sns.relplot(x="longitude", y="latitude", hue="year", size="price",
            sizes=(1 , 1000), alpha=.6, palette="YlGnBu",
            height=8, data=downtown_private)


# In[ ]:





# In[72]:


westend_entire=listing[(listing["room_type"]=="Entire home/apt") & (listing['district'] == "West End" )]
downtown_entire=listing[(listing["room_type"]=="Entire home/apt") & (listing['district'] == "Downtown Core" )]


# In[80]:


sns.relplot(x="longitude", y="latitude", hue="room_type", size="price",
            sizes=(50 , 1000), alpha=.6, palette="muted",
            height=8, data=downtown_entire)

# This map shows 'Entire Home/Apt by price' for Downtown Core..


# In[113]:


listing.head()


# In[115]:


zz=listing.groupby('district').mean()


# In[119]:


zz


# # Prices According to Room Type

# In[81]:


plt.figure(figsize = (10, 6))
#Draw plot
ax = sns.barplot('price', 'district',data=listing, ci=80,hue='room_type')
#Set the axes
ax.set_xlabel('Price in $', weight='normal', size=15)
ax.set_ylabel('Districts', weight='normal', size=15)
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right", size= 12)
#Set tittle
plt.title('Price according the district', fontsize=18)
#Show plot
plt.show()


# In[ ]:





# ### Mean Prices by Room Type for Entire City

# In[102]:


mean_prices_by_room_type=listing.groupby('room_type').mean()
mean_prices_by_room_type.index.name=None
mean_prices_by_room_type


# In[ ]:


prices_by_room_type


# In[111]:


#Show number of adverts by district
plt.figure(figsize = (10, 5))
ax = sns.barplot(x=mean_prices_by_room_type.index, y='price', data=mean_prices_by_room_type)
ax.set_xlabel('Room Type', weight='normal', size=15)
ax.set_ylabel('Mean Price in ($)', weight='normal', size=15)
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right", size=12)
plt.title('Mean Price by Room Type in Toronto', fontsize=18)

plt.show()


# In[ ]:





# In[112]:


fig = plt.figure(figsize = (12, 10))

plt.subplot(2, 2, 1)
ax = sns.barplot(x=mean_prices_by_room_type.index, y='price', data=mean_prices_by_room_type)
ax.set_xlabel('Room Type', weight='normal', size=15)
ax.set_ylabel('Mean Price in ($)', weight='normal', size=15)
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right", size=12)
plt.title('Mean Price by Room Type in Toronto', fontsize=18)


plt.subplot(2, 2, 2)
ax = sns.barplot('price', 'district',data=listing, ci=80,hue='room_type')
#Set the axes
ax.set_xlabel('Price in $', weight='normal', size=15)
ax.set_ylabel('Districts', weight='normal', size=15)
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right", size= 12)
#Set tittle
plt.title('Price according the district', fontsize=18)
#Show plot

plt.tight_layout()
plt.show()


# In[113]:

# We also can define this subplot as a function since they have common parts. We can this functions for further data wranglings

def create_subplot(data1, data2,figsize=(12,10), size=12, fontsize=15 ):
    
    fig = plt.figure(figsize = (12, 10))
    list1=[1,2]
    
    for i in list1:
        plt.subplot(2,2,i)
        
        if i==1:
            ax=sns.barplot(x=data1.index, y='price', data=data1)
            #Set the axes            
            ax.set_xlabel('Room Type',size=size, weight='normal')
            ax.set_ylabel('Mean Price in ($)',size=size, weight='normal')
            #Set tittle
            plt.title('Mean Price by Room Type in Toronto', fontsize=fontsize)
            continue
            
        if i==2:
            ax = sns.barplot('price', 'district',data=data2, ci=80,hue='room_type')
            #Set the axes
            ax.set_xlabel('Price in $', size=size, weight='normal')
            ax.set_ylabel('Districts', size=size, weight='normal')
            #Set tittle
            plt.title('Price according the district', fontsize=fontsize)
            
        ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right", size=size)
        plt.tight_layout()
        plt.show()


# In[115]:

create_subplot(mean_prices_by_room_type,listing)

# # Prices & Reviews Comperition by Month for 2018-2019

# In[82]:


year2019=listing[listing['year']==2019]
year2018=listing[listing['year']==2018]


# In[94]:


month_sum_2019=year2019.groupby('month').sum()
month_mean_2019=year2019.groupby('month').mean()
month_sum_2018=year2018.groupby('month').sum()
month_mean_2018=year2018.groupby('month').mean()


# In[96]:


month_sum_2019


# In[121]:



fig = plt.figure(figsize = (12, 10))

plt.subplot(3, 2, 1)
ax = sns.barplot(x=month_mean_2018.index, y='price', data=month_mean_2018)
ax.set_xlabel('Months 2018', weight='normal', size=15)
ax.set_ylabel('Price', weight='normal', size=15)
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right", size=12)


plt.subplot(3, 2, 2)
ax = sns.barplot(x=month_sum_2018.index, y='number_of_reviews', data=month_mean_2018)
ax.set_xlabel('Months 2018', weight='normal', size=15)
ax.set_ylabel('Mean Review by Room', weight='normal', size=15)
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right", size=12)



plt.subplot(3, 2, 3)
ax = sns.barplot(x=month_mean_2019.index, y='price', data=month_mean_2019)
ax.set_xlabel('Months 2019', weight='normal', size=15)
ax.set_ylabel('Price', weight='normal', size=15)
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right", size=12)


plt.subplot(3, 2, 4)
ax = sns.barplot(x=month_sum_2019.index, y='number_of_reviews', data=month_mean_2019)
ax.set_xlabel('Months 2019', weight='normal', size=15)
ax.set_ylabel('Mean Review by Room', weight='normal', size=15)
ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right", size=12)


plt.tight_layout()
plt.show()


# In[ ]:




