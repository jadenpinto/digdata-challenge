# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 14:44:49 2021

@author: DELL
"""


import csv


def printContents():
    with open ('DataSet.csv',"r",newline="") as f:
        print("Contents of file")
        ReadObj= csv.reader(f)
        for line in ReadObj:
            print(line)

def CountEach():
    with open ('DataSet.csv',"r",newline="") as f:
        global AdsCount
        global InfluencerCount        
        AdsCount=0
        InfluencerCount=0
        ReadObj= csv.reader(f)
        for line in ReadObj:
            if line[1]=='Ads_only':
                AdsCount=AdsCount+1
            elif line[1]=='Influencer':
                InfluencerCount=InfluencerCount+1
        print("Ads Count=",AdsCount)
        print("Influencer Count=", InfluencerCount)

def EffectiveAds():
    with open ('DataSet.csv',"r",newline="") as f:
        global EffectiveAdsCount        
        EffectiveAdsCount=0
        ReadObj= csv.reader(f)
        for line in ReadObj:
            if line[1]=='Ads_only':
                if float(line[7].replace("%","")) > float(line[8].replace("%","")):                   
                    EffectiveAdsCount = EffectiveAdsCount+1
        print("The successful number of Ads only=",EffectiveAdsCount)

def EffectiveInfluencers():
    with open ('DataSet.csv',"r",newline="") as f:
        global EffectiveInfluencersCount       
        EffectiveInfluencersCount=0
        ReadObj= csv.reader(f)
        for line in ReadObj:
            if line[1]=='Influencer':
                if float(line[7].replace("%","")) > float(line[8].replace("%","")):
                    EffectiveInfluencersCount = EffectiveInfluencersCount+1
        print("The successful number of ads by influencers=",EffectiveInfluencersCount)
        
def ComparePercentage():
    percent_ads_only = (EffectiveAdsCount/AdsCount) * 100
    percent_influencers = (EffectiveInfluencersCount/InfluencerCount) * 100 
    print("Percentage of Effective Ads=", percent_ads_only, "%")
    print("Percentage of Effective Ads by influencers=", percent_influencers, "%")
    if percent_ads_only > percent_influencers:
        print("Therefore Ads only is better and more effective")
    else:
        print("Therefore Ads by influencers are better and more effective")

def BrandAwareness():
    with open ('DataSet.csv',"r",newline="") as f:       
        BrandAdsCount=0
        BrandInfluencerCount=0
        EffectiveBrandAdsCount=0
        EffectiveBrandInfluencerCount=0
        ReadObj= csv.reader(f)
        for line in ReadObj:
            if line[6] == 'brand_awareness':
                if line[1]=='Ads_only':
                    BrandAdsCount=BrandAdsCount+1
                    if float(line[7].replace("%","")) > float(line[8].replace("%","")):
                        EffectiveBrandAdsCount= EffectiveBrandAdsCount+1
                elif line[1]=='Influencer':
                    BrandInfluencerCount=BrandInfluencerCount+1
                    if float(line[7].replace("%","")) > float(line[8].replace("%","")):
                        EffectiveBrandInfluencerCount= EffectiveBrandInfluencerCount+1
        print("Ads Count=",BrandAdsCount)
        print("Influencer Count=", BrandInfluencerCount)
        print("Number of effective standard ads=", EffectiveBrandAdsCount)
        print("Number of effective influencer ads=", EffectiveBrandInfluencerCount)
        percent_brand_ads_only= (EffectiveBrandAdsCount/BrandAdsCount) * 100
        percent_brand_influencer= (EffectiveBrandInfluencerCount/BrandInfluencerCount) * 100
        print("Percentage of effective standard ads=", percent_brand_ads_only,"%")
        print("Percentage of effective influencer ads=", percent_brand_influencer,"%")
        if percent_brand_ads_only > percent_brand_influencer:
            print("Therefore Standard Ads better are better for Brand Awareness")
        else:
            print("Therefore Influencer Ads better are better for Brand Awareness")

def BrandAwarenessMedia():
    with open ('DataSet.csv',"r",newline="") as f:       
        Image=0
        Video=0
        EffectiveImage=0
        EffectiveVideo=0
        ReadObj= csv.reader(f)
        for line in ReadObj:
            if line[6] == 'brand_awareness':
                if line[4]=='Image':
                    Image=Image+1
                    if float(line[7].replace("%","")) > float(line[8].replace("%","")):
                        EffectiveImage= EffectiveImage+1
                elif line[4]=='Video':
                    Video=Video+1
                    if float(line[7].replace("%","")) > float(line[8].replace("%","")):
                        EffectiveVideo= EffectiveVideo+1
        print("Number of image ads=",Image)
        print("Number of video ads=", Video)
        print("Number of effective iamge ads=", EffectiveImage)
        print("Number of effective video ads=", EffectiveVideo)
        percent_image= (EffectiveImage/Image) * 100
        percent_video= (EffectiveVideo/Video) * 100
        print("Percentage of effective image ads=", percent_image,"%")
        print("Percentage of effective influencer ads=", percent_video,"%")
        if percent_image > percent_video:
            print("Therefore Ads with images are better for Brand Awareness")
        else:
            print("Therefore Ads with videos are better for Brand Awareness")

def BrandWithinThree():
    with open ('DataSet.csv',"r",newline="") as f:       
        InThree=0
        NotInThree=0
        EffectiveInThree=0
        EffectiveNotInThree=0
        ReadObj= csv.reader(f)
        for line in ReadObj:
            if line[6] == 'brand_awareness':
                if line[2]=='1':
                    InThree=InThree+1
                    if float(line[7].replace("%","")) > float(line[8].replace("%","")):
                        EffectiveInThree= EffectiveInThree+1
                elif line[2]=='0':
                    NotInThree=NotInThree+1
                    if float(line[7].replace("%","")) > float(line[8].replace("%","")):
                        EffectiveNotInThree= EffectiveNotInThree+1
        print("Number of ads in which brand was shown within 3s=",InThree)
        print("Number of ads in which brand was shown after 3s=", NotInThree)
        print("Number of effective ads in which brand was shown within 3s=", EffectiveInThree)
        print("Number of effective ads in which brand was shown after 3s=", EffectiveNotInThree)
        percent_in_three= (EffectiveInThree/InThree) * 100
        percent_after_three= (EffectiveNotInThree/NotInThree) * 100
        print("Percentage of effective ads in which brand was shown within 3s=", percent_in_three,"%")
        print("Percentage of effective ads in which brand was shown after 3s=", percent_after_three,"%")
        if percent_in_three > percent_after_three:
            print("Therefore Ads in which brand was shown within 3s are better for Brand Awareness")
        else:
            print("Therefore Ads in which brand was shown after 3s are better for Brand Awareness")

printContents()
CountEach()
EffectiveAds()
EffectiveInfluencers()
ComparePercentage()
BrandAwareness()
BrandAwarenessMedia()
BrandWithinThree()

