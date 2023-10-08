// this script can be runned directly in the mongosh interface using the load("<filePath>") method
// if try to run in NoSQL booster, replace `db = db.getSiblingDB()` method with `use <database>`

//import all the data
/*
mongoimport --db=ac6005_ia --collection=complainttbl --drop --file="/Users/jiananwang/ob_library/StoriesofYourLifeandOthers/Others/MediaNote/DocumentNote/AC6005_ia/complainttbl.json"
mongoimport --db=ac6005_ia --collection=customertbl --drop --file="/Users/jiananwang/ob_library/StoriesofYourLifeandOthers/Others/MediaNote/DocumentNote/AC6005_ia/customertbl.json"
mongoimport --db=ac6005_ia --collection=vehicletbl --drop --file="/Users/jiananwang/ob_library/StoriesofYourLifeandOthers/Others/MediaNote/DocumentNote/AC6005_ia/ia.vehicletbl.json"
mongoimport --db=ac6005_ia --collection=incidenttbl --drop --file="/Users/jiananwang/ob_library/StoriesofYourLifeandOthers/Others/MediaNote/DocumentNote/AC6005_ia/incidenttbl.json"
mongoimport --db=ac6005_ia --collection=incidenttypetbl --drop --file="/Users/jiananwang/ob_library/StoriesofYourLifeandOthers/Others/MediaNote/DocumentNote/AC6005_ia/incidenttypetbl.json"
mongoimport --db=ac6005_ia --collection=ordertbl --drop --file="/Users/jiananwang/ob_library/StoriesofYourLifeandOthers/Others/MediaNote/DocumentNote/AC6005_ia/ordertbl.json"
mongoimport --db=ac6005_ia --collection=postalcodetbl --drop --file="/Users/jiananwang/ob_library/StoriesofYourLifeandOthers/Others/MediaNote/DocumentNote/AC6005_ia/postalcodetbl.json"
mongoimport --db=ac6005_ia --collection=vehicletypetbl --drop --file="/Users/jiananwang/ob_library/StoriesofYourLifeandOthers/Others/MediaNote/DocumentNote/AC6005_ia/vehicletypetbl.json"
*/

db = db.getSiblingDB( "ac6005_ia" )

/* Question 1
1) Table considered: <postalCodeTBL>
What are the unique [generalLoc]?
*/

print("\n query 1")
print("--------------------")

q1 = db.postalcodetbl.aggregate([
    { $group: { "_id": {
            "generalLoc": "$generalLoc"
    }}},
    { $project: {
        "_id": 0,
        "generalLoc": { $trim: { input: "$_id.generalLoc" }}
    }}
    // { $group: {
    //     "_id": null,
    //     "count": { $count: { }}
    // }}
])

printjson(q1)

/* Question 2
2) Table considered: <incidentTypeTBL>
How many incident types are related to speed limit issues?
*/

print("\n query 2")
print("--------------------")

q2 = db.incidenttypetbl.aggregate([
    { $match: { "detail": {
            $regex: /speed limit/,
            $options: "i"
    }}},
    { $group: {
        "_id": null,
        "count": { $count: { }}
    }}
])

printjson(q2)

/* Question 3
3) Table considered: <incidentTBL>
For each [year], on each [incidentType], how many incidents are recorded?
*/

print("\n query 3")
print("--------------------")

q3 = db.incidenttbl.aggregate([
    { $addFields: { "year_": {
        $year: { $dateFromString: { dateString: "$date" }}
    }}},
    { $group: {
            "_id": {
                "year": "$year_",
                "incidentType": "$incidentType"
            },
            "count": { $count: { }}
    }}
    // { $group: {
    //         "_id": null,
    //         "count": { $count: { }}
    //     }}
])

printjson(q3)

/* Question 4
4) Tables considered: <complaintTBL> + <customerTBL>
For each year (2010 to 2018), on each issue category, 
display the total number of complaints, and the respective breakdowns between females and males
*/

print("\n query 4")
print("--------------------")

q4 = db.complainttbl.aggregate([
    { $addFields: { "complaintYear": {
        $year: { $dateFromString: { dateString: "$date" }}
    }}},
    { $lookup: {
        from: "customertbl",
        localField: "customerID",
        foreignField: "customerID",
        as: "dataFromCustomertbl"
    }},
    { $unwind: "$dataFromCustomertbl" },
    { $group: {
        "_id": {
            "year": "$complaintYear",
            "issue": "$issue",
            "gender": "$dataFromCustomertbl.gender"
        },
        "count": { $count: { }}
    }}
    // { $group: {
    //     "_id": null,
    //     "count": { $count: { }}
    // }}
])

printjson(q4)

/* Question 5
5) Tables considered: <vehicleTBL> + <orderTBL> + <customerTBL> + <postalcodeTBL>
For each year, on each generalLoc, display the total customer value 
(i.e., total rental fees recorded for the year).
Note: You need to sum up the values for the same generalLoc (under different postalCode).
*/

// we can prove that all the orders starts and ends in the same day
db.ordertbl.aggregate([
    { $match: { $expr: { 
        $eq: ["$startDate", "$endDate" ]}
    }},
    { $group: {
        "_id": null,
        "count": { $count: { }}
    }}
])

print("\n query 5")
print("--------------------")

q5 = db.ordertbl.aggregate([
    // get startLoc = endLoc
    {$match: {$expr: {
        $eq: ["$startLoc", "$endLoc"]
    }}},
    { $addFields: { "year_": {
        $year: { $dateFromString: { dateString: "$startDate" }}
    }}},
    // calculate oder duration hours
    { $addFields: { "orderDuration(hr)": {
        $subtract: [
            { $round: [ 
                { $add: [
                    { $add: [
                        { $convert: { input: "$endTime_hr", to: "int" }}, 
                        { $divide: [{ $convert: { input: '$endTime_min', to: "int" }}, 60 ]}
                    ]},
                    0.001
                    // $round in mongodb will give some unexpected result, e.g. 12.5 --> 12
                    // so we add a very small number to avoid such condition
                ]}, 
                0
            ]},
            { $round: [ 
                { $add: [
                    { $add: [
                        { $convert: { input: "$startTime_hr", to: "int" }}, 
                        { $divide: [{ $convert: { input: '$startTime_min', to: "int" }}, 60 ]}
                    ]},
                    0.001
                    // $round in mongodb will give some unexpected result, e.g. 12.5 --> 12
                    // so we add a very small number to avoid such condition
                ]}, 
                0
            ]},
        ],
    }}},
    { $lookup: {
        from: "vehicletbl",
        localField: "vehicleID",
        foreignField: "vehicleID",
        as: "dataFromVehicletbl"
      }},
    { $unwind: "$dataFromVehicletbl" },
    { $addFields: { "orderFee": { 
        $multiply: [ 
            "$orderDuration(hr)", 
            {$round: [ 
                {$add: [
                    { $convert: { 
                        input: { $trim: { input: "$dataFromVehicletbl.fee_per_hour" }}, 
                        to: "double"
                    }},
                    0.001
                    // $round in mongodb will give some unexpected result, e.g. 12.5 --> 12
                    // so i add a very small number to avoid such condition
                ]},
                0
            ]}
        ]},
    }},
    { $lookup: {
        from: "postalcodetbl",
        localField: "startLoc",
        foreignField: "postalCode",
        as: "dataFromPostalcodetbl"
    }},
    { $unwind: "$dataFromPostalcodetbl"},
    { $group: {
        "_id": {
            "year": "$year_",
            "generalLoc": { $trim: { input: "$dataFromPostalcodetbl.generalLoc"}}
        },
        "fee": { $sum: "$orderFee" }
    }},
    { $sort: { "fee": -1 }}
])

printjson(q5)