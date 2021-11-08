import json
import re
import requests

ADVANCED =\
  "This is the result for the highest paying salary for a spefic club and position.------- ENTER 1\n\n"\
  
ADVANCED_TO_QUESTION = {
  1: "Select a club: \n\n1. - for CHI.\n2. - for CHV. \n3. - for CLB. \n4. - for COL.\n\n ",
}

BASIC = "\nSelect a year btw 2007 - 2012:\n"

YEARS = [
  {
   "Year": "2007",
   #team
   "Club": "CHI", 
   #position
   "CHI club, D position": "900000", 
   "CHI club, D-M position": "270000", 
   "CHI club, F position": "1500000",
   "CHI club, GK position": "872736", 
   "CHI club, M position": "5500000", 

   #team
   "Club": "CHV", 
   #position
   "CHV club, D position": "195000", 
   "CHV club, F position": "195000", 
   "CHV club, F-D position": "192000", 
   "CHV club, GK position": "190008", 
   "CHV club, M position": "180000",
   
   #team
   "Club":"CLB", 
   #position
   "CLB club, D position": "142000", 
   "CLB club, D-M position": "138000", 
   "CLB club, F position": "147500", 
   "CLB club, F-M position": "120000", 
   "CLB club, GK position": "144000",
   "CLB club, M position": "142500", 
   
  "Club":"COL", 
   #position
   "COL club, D position": "100000", 
   "COL club, F position": "110000", 
   "COL club, GK position": "100008",
   "COL club,  M position": "110000", 
   "COL club, M-D position": "90000",
   "COL club, M position": "142500",
},
  {
   "Year": "2008",
   #team
   "Club": "CHI",
    #position
   "CHI club, D position": "156000", 
   "CHI club, D-M position": "70000", 
   "CHI club, F position": "198000",
   "CHI club, GK position": "80000", 
   "CHI club, M position": "2492316", 

    #team
   "Club": "CHV", 
   #position
   "CHV club, D position": "125000", 
   "CHV club, F position": "255000", 
   "CHV club, F-D position": "272000", 
   "CHV club, GK position": "88974", 
   "CHV club, M position": "151250",

    #team
   "Club":"CLB", 
   #position
   "CLB club, D position": "150000", 
   "CLB club, D-M position": "258000", 
   "CLB club, F position": "250000", 
   "CLB club, F-M position": "160000", 
   "CLB club, GK position": "70000",
   "CLB club, M position": "165000", 

   "Club":"COL", 
   #position
   "COL club, D position": "133000", 
   "COL club, F position": "190008", 
   "COL club, GK position": "100008",
   "COL club,  M position": "385000", 
   "COL club, M-D position": "160000",
   "COL club, M position": "125800",
},
  {
    "Year": "2009",
   #team
   "Club": "CHI",
    #position
   "CHI club, D position": "168000", 
   "CHI club, D-M position": "20100", 
   "CHI club, F position": "360000",
   "CHI club, GK position": "135000", 
   "CHI club, M position": "2769240", 

  #team
   "Club": "CHV", 
   #position
   "CHV club, D position": "125000", 
   "CHV club, F position": "255000", 
   "CHV club, F-D position": "272000", 
   "CHV club, GK position": "88974", 
   "CHV club, M position": "151250",

   #team
   "Club":"CLB", 
   #position
   "CLB club, D position": "250000", 
   "CLB club, D-M position": "650000", 
   "CLB club, F position": "132300", 
   "CLB club, F-M position": "650000", 
   "CLB club, GK position": "77000",
   "CLB club, M position": "133875", 

   "Club":"COL", 
   #position
   "COL club, D position": "156000", 
   "COL club, F position": "200000", 
   "COL club, GK position": "125000",
   "COL club,  M position": "159600", 
   "COL club, M-D position": "255000",
   "COL club, M position": "210000",
},
  {
    "Year": "2010",
   #team
   "Club": "CHI",
    #position
   "CHI club, D position": "184000", 
   "CHI club, D-M position": "40100", 
   "CHI club, F position": "580000",
   "CHI club, GK position": "254000", 
   "CHI club, M position": "45681230", 

   #team
   "Club": "CHV", 
   #position
   "CHV club, D position": "145000", 
   "CHV club, F position": "366000", 
   "CHV club, F-D position": "458000", 
   "CHV club, GK position": "10974", 
   "CHV club, M position": "200250",

   #team
   "Club":"CLB", 
   #position
   "CLB club, D position": "780000", 
   "CLB club, D-M position": "450000", 
   "CLB club, F position": "157300", 
   "CLB club, F-M position": "890000", 
   "CLB club, GK position": "75000",
   "CLB club, M position": "166875",

    "Club":"COL", 
   #position
   "COL club, D position": "145000", 
   "COL club, F position": "400000", 
   "COL club, GK position": "165000",
   "COL club,  M position": "148600", 
   "COL club, M-D position": "155000",
   "COL club, M position": "310000",
},
  {
   "Year": "2011",
   #team
   "Club": "CHI",
    #position
   "CHI club, D position": "165000", 
   "CHI club, D-M position": "50100", 
   "CHI club, F position": "280000",
   "CHI club, GK position": "454000", 
   "CHI club, M position": "45685640", 

   #team
   "Club": "CHV", 
   #position
   "CHV club, D position": "245000", 
   "CHV club, F position": "166000", 
   "CHV club, F-D position": "128000", 
   "CHV club, GK position": "60974", 
   "CHV club, M position": "500250",

   #team
   "Club":"CLB", 
   #position
   "CLB club, D position": "440000", 
   "CLB club, D-M position": "650000", 
   "CLB club, F position": "254300", 
   "CLB club, F-M position": "190000", 
   "CLB club, GK position": "95000",
   "CLB club, M position": "166254",

    "Club":"COL", 
   #position
   "COL club, D position": "788000", 
   "COL club, F position": "50000", 
   "COL club, GK position": "415000",
   "COL club,  M position": "168600", 
   "COL club, M-D position": "255000",
   "COL club, M position": "500000", 
},
  {
     "Year": "2012",
   #team
   "Club": "CHI",
    #position
   "CHI club, D position": "105000", 
   "CHI club, D-M position": "60100", 
   "CHI club, F position": "480000",
   "CHI club, GK position": "861000", 
   "CHI club, M position": "78655640", 

   #team
   "Club": "CHV", 
   #position
   "CHV club, D position": "562000", 
   "CHV club, F position": "166045", 
   "CHV club, F-D position": "145000", 
   "CHV club, GK position": "48074", 
   "CHV club, M position": "100850",

    #team
   "Club":"CLB", 
   #position
   "CLB club, D position": "660000", 
   "CLB club, D-M position": "750000", 
   "CLB club, F position": "255900", 
   "CLB club, F-M position": "190026", 
   "CLB club, GK position": "950098",
   "CLB club, M position": "556254",

    "Club":"COL", 
   #position
   "COL club, D position": "665000", 
   "COL club, F position": "90074", 
   "COL club, GK position": "615000",
   "COL club,  M position": "256600", 
   "COL club, M-D position": "153690",
   "COL club, M position": "100000", 
}]

METADATA = [["2007", "CHI", "CHI club, D position - $900000","CHI club, D-M positioN - $270000", "CHI club, F position - $1500000", "CHI club, GK position - $872736", "CHI club, M position - $5500000", 

"CHV",  
   "CHV club, D position - 195000", 
   "CHV club, F position - 195000", 
   "CHV club, F-D position - 192000", 
   "CHV club, GK position - 190008", 
   "CHV club, M position - 180000",

"CLB",
   "CLB club, D position - 142000", 
   "CLB club, D-M position - 138000", 
   "CLB club, F position - 147500", 
   "CLB club, F-M position - 120000", 
   "CLB club, GK position - 144000",
   "CLB club, M position - 142500"

"COL", 
 "COL club, D position - 100000", 
   "COL club, F position - 110000", 
   "COL club, GK position - 100008",
  "COL club,  M position - 110000", 
   "COL club, M-D position - 90000",
   "COL club, M position - 142500" 

],["2008","CHI", "CHI club, D position -$156000",
"CHI club, D-M position-$70000","CHI club, F position - $198000","CHI club, GK position - $80000", 
"CHI club, M position - $2492316",

"CHV",
  "CHV club, D position - 125000", 
   "CHV club, F position - 255000", 
   "CHV club, F-D position - 272000", 
   "CHV club, GK position - 88974", 
   "CHV club, M position - 151250",

"CLB",
  "CLB club, D position - 150000", 
   "CLB club, D-M position - 258000", 
   "CLB club, F position - 250000", 
   "CLB club, F-M position - 160000", 
   "CLB club, GK position - 70000",
   "CLB club, M position - 165000", 

"COL",
   "COL club, D position - 133000", 
   "COL club, F position - 190008", 
   "COL club, GK position - 100008",
   "COL club,  M position - 385000", 
   "COL club, M-D position - 160000",
   "COL club, M position - 125800",
],["2009","CHI","CHI club, D position - $168000","CHI club, D-M position - $20100","CHI club, F position - $360000",   "CHI club, GK position - $135000", 
"CHI club, M position - $2769240", 

"CHV",
"CHI club, D position - 168000", 
"CHI club, D-M position - 20100", 
"CHI club, F position - 360000",
"CHI club, GK position - 135000", 
"CHI club, M position - 2769240", 

"CLB",
"CLB club, D position - 250000", 
"CLB club, D-M position - 650000", 
"CLB club, F position - 132300", 
"CLB club, F-M position - 650000", 
"CLB club, GK position - 77000",
"CLB club, M position - 133875", 

"COL",
"COL club, D position - 156000", 
"COL club, F position - 200000", 
"COL club, GK position - 125000",
"COL club,  M position - 159600", 
"COL club, M-D position - 255000",
"COL club, M position - 210000",
],[
"2010","CHI","CHI club, D position - $184000","CHI club, D-M position - $40100","CHI club, F position - $580000",
   "CHI club, GK position - $254000","CHI club, M position - $45681230", 

"CHV",
  "CHV club, D position - 145000", 
   "CHV club, F position - 366000", 
   "CHV club, F-D position - 458000", 
   "CHV club, GK position - 10974", 
   "CHV club, M position - 200250",

"CLB",
  "CLB club, D position - 780000", 
   "CLB club, D-M position - 450000", 
   "CLB club, F position - 157300", 
   "CLB club, F-M position - 890000", 
   "CLB club, GK position - 75000",
   "CLB club, M position - 166875",

"COL",
   "COL club, D position - 145000", 
   "COL club, F position - 400000", 
   "COL club, GK position - 165000",
   "COL club,  M position - 148600", 
   "COL club, M-D position - 155000",
   "COL club, M position - 310000",
],["2011","CHI", "CHI club, D position - $165000","CHI club, D-M position - $50100","CHI club, F position - $280000",
   "CHI club, GK position - $454000","CHI club, M position - $45685640", 

"CHV",
  "CHV club, D position - 245000", 
   "CHV club, F position - 166000", 
   "CHV club, F-D position - 128000", 
   "CHV club, GK position - 60974", 
   "CHV club, M position - 500250",

"CLB",
  "CLB club, D position - 440000", 
   "CLB club, D-M position - 650000", 
   "CLB club, F position - 254300", 
   "CLB club, F-M position - 190000", 
   "CLB club, GK position - 95000",
   "CLB club, M position - 166254",

"COL",
   "COL club, D position - 788000", 
   "COL club, F position - 50000", 
   "COL club, GK position - 415000",
   "COL club,  M position - 168600", 
   "COL club, M-D position - 255000",
   "COL club, M position - 500000", 
],["2012","CHI",  "CHI club, D position - $105000","CHI club, D-M position - $60100","CHI club, F position - $480000",
   "CHI club, GK position - $861000","CHI club, M position - $78655640", 

"CHV",
  "CHV club, D position - 562000", 
   "CHV club, F position - 166045", 
   "CHV club, F-D position - 145000", 
   "CHV club, GK position - 48074", 
   "CHV club, M position - 100850",

"CLB",
  "CLB club, D position - 660000", 
   "CLB club, D-M position - 750000", 
   "CLB club, F position - 255900", 
   "CLB club, F-M position - 190026", 
   "CLB club, GK position - 950098",
   "CLB club, M position - 556254",

"COL",
   "COL club, D position - 665000", 
   "COL club, F position - 90074", 
   "COL club, GK position - 615000",
   "COL club,  M position - 256600", 
   "COL club, M-D position - 153690",
   "COL club, M position - 100000",
]]





