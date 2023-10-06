// we use mongoimport to import all the json file to mongodb
// improvement: how to detect the folder path automatically? . ..?
// importing using mongoimport cannot avoid the \r in the very end of each filem, see how to improve

/*
mongoimport --db="ev" --collection="co2_emissions_canada" --drop --file="/Users/jiananwang/ob_library/StoriesofYourLifeandOthers/Others/MediaNote/DocumentNote/nosql/group_project.co2_emissions_canada.json"
mongoimport --db="ev" --collection="electric_vehicle_population" --drop --file="/Users/jiananwang/ob_library/StoriesofYourLifeandOthers/Others/MediaNote/DocumentNote/nosql/group_project.electric_vehicle_population.json"
mongoimport --db="ev" --collection="ev_stations_v1" --drop --file="/Users/jiananwang/ob_library/StoriesofYourLifeandOthers/Others/MediaNote/DocumentNote/nosql/group_project.ev_stations_v1.json"
mongoimport --db="ev" --collection="evByState" --drop --file="/Users/jiananwang/ob_library/StoriesofYourLifeandOthers/Others/MediaNote/DocumentNote/nosql/group_project.evByState.json"
mongoimport --db="ev" --collection="evStationByState" --drop --file="/Users/jiananwang/ob_library/StoriesofYourLifeandOthers/Others/MediaNote/DocumentNote/nosql/group_project.evStationByState.json"
mongoimport --db="ev" --collection="evByPostalCode" --drop --file="/Users/jiananwang/ob_library/StoriesofYourLifeandOthers/Others/MediaNote/DocumentNote/nosql/group_project.evByPostalCode.json"
mongoimport --db="ev" --collection="evStationByZIP" --drop --file="/Users/jiananwang/ob_library/StoriesofYourLifeandOthers/Others/MediaNote/DocumentNote/nosql/group_project.evStationByZIP.json"
mongoimport --db="ev" --collection="nei_2017_full_data" --drop --file="/Users/jiananwang/ob_library/StoriesofYourLifeandOthers/Others/MediaNote/DocumentNote/nosql/group_project.nei_2017_full_data.json"
*/

db = db.getSiblingDB( "ev" )

/*
1.	[ev_stations_v1] For each zip code, display the number of stations located between 
latitudes (33.20 to 34.70) and longitudes (-118.40 and -117.20). 
*/
print("\n query 1")
print("--------------------")

q1 = db.ev_stations_v1.aggregate([
    { $addFields: {
        "LatitudeDouble": { $convert: {
                input: "$Latitude",
                to: "double"
            }},
        "LongitudeDouble": { $convert: {
                input: "$Longitude",
                to: "double"
            }},
    }},
    { $match: { $and: [ 
        { "LatitudeDouble": { 
            $gt: 33.20, 
            $lt: 34.70 
        }},
        { "LongitudeDouble": { 
            $gt: -118.40, 
            $lt: -117.20 
        }}
    ]}},
    { $group: {
        "_id": { "ZIP": "$ZIP" },
        "countOfStations": { $count: { } }
    }},
    { $sort: {"countOfStations": -1}}
])

printjson(q1)

/*
2.	[ev_stations_v1] Let’s find out where we can find the most Telsa cars. 
For each state and model, display the number of Telsa cars in descending order.

note: why this one should use ev_stations_v1??? should be electric_vehicle_population?
*/
print("\n query 2")
print("--------------------")
q2 = db.electric_vehicle_population.aggregate([
    { $match: { "Make": "TESLA" }}, // there is no other way to epxress word TESLA
    { $group: {
        "_id": {
            "State": "$State",
            "Model": "$Model"
        },
        "vehicleCount": { $count: { }}
    }},
    { $sort: { "vehicleCount": -1 }},
    // { $group: {
    //     "_id": null,
    //     "total": { $sum: "$vehicleCount" }
    // }}
])

printjson(q2)

/*
3.	[ev_stations_v1] For each electric vehicle type and each clean alternative fuel vehicle eligibility, 
display the average electric range value.

note: why this one should use ev_stations_v1??? should be electric_vehicle_population?
*/
print("\n query 3")
print("--------------------")
q3 = db.electric_vehicle_population.aggregate([
    { $addFields: { "ElectricRangeDouble": {
        $convert: {
            input: "$ElectricRange",
            to: "double"
        }
    }}},
    { $group: {
        "_id": {
            "EVType": "$ElectricVehicleType",
            "Eligibility": "$CleanAlternativeFuelVehicleEligibility"
        },
        "avgERange": { $avg: "$ElectricRangeDouble" }
    }},
    { $sort: { "avgERange": -1 }},
    { $project: {
        "_id": 1,
        "avgERangeRounded": { $round: [ "$avgERange", 2 ] }
    }}
])

printjson(q3)

/*
4.	[co2_emissions_canada] and [electric_vehicle_population] Estimate the CO2 emission of vehicles using alternative fuel in the states. 
For each make and each model, in each state, display the number of vehicles and the CO2 emissions in grams per km.
*/

/*
in [electric_vehicle_population], group by make and model, count the number
join
in [co2_emissions_canada], group by make and model (the co2 emssion may be different event thought the make and model are same)
get the CO2Emissions_g_km for each make and model
*/

print("\n query 4")
print("--------------------")
q4 = db.electric_vehicle_population.aggregate([
    { $group: {
        "_id": {
            "State": "$State",
            "Make": "$Make",
            "Model": "$Model"
        },
        "count_": { $count: { }}
    }},
    { $lookup: {
        from: "co2_emissions_canada",
        let: {
            make_veh: "$_id.Make",
            model_veh: "$_id.Model",
        },
        pipeline: [
            { $addFields: { "CO2Emissions_g_kmDouble": {
                $convert: {
                    input: { $trim: { input: "$CO2Emissions_g_km" }},
                    to: "double"
                }
            }}},
            { $group: {
                "_id": {
                    "Make": "$Make",
                    "Model": "$Model"
                },
                "avgCO2Emissions_g_km": { $avg: "$CO2Emissions_g_kmDouble" },
                "minCO2Emissions_g_km": { $min: "$CO2Emissions_g_kmDouble" },
                "maxCO2Emissions_g_km": { $max: "$CO2Emissions_g_kmDouble" }
            }},
            { $match: { $expr: {
                $and: [
                    { $eq: [ "$_id.Make", "$$make_veh" ]},
                    { $eq: [ "$_id.Model", "$$model_veh" ]}
                ]
            }}},
            { $project: {
                "_id": 0,
                "avgCO2Emissions_g_km": 1,
                "minCO2Emissions_g_km": 1,
                "maxCO2Emissions_g_km": 1,
            }}
        ],
        as: "dataFromco2"
    }},
    { $unwind: {
        path: "$dataFromco2",
        preserveNullAndEmptyArrays: true // defaulte value is false, null value document after unwind will not show up
    }},
    { $sort: { "count_": -1 }}
])

printjson(q4)

/*
5.	[ev_stations_v1] and [electric_vehicle_population] Does the number of EV stations matter? There are two parts to this query:
i)	For each state, display the number of electric vehicles, the number of EV stations, and the vehicle:station ratio in descending ratio order.
ii)	For each postalcode(zip), display the number of electric vehicles, the number of EV stations, and the vehicle:station ratio in descending ratio order.
*/
print("\n query 5_1")
print("--------------------")

q5_1 = db.electric_vehicle_population.aggregate([
    { $group: {
        "_id": { "State": "$State" },
        "vehicleCount": { $count: { }}
    }}, 
    { $lookup: {
        from: "ev_stations_v1",
        let: { vp_state: "$_id.State" },
        pipeline: [
            { $group: {
                "_id": { "StateGroup": "$State" },
                "EVStationCount": { $count: { }}
            }}, 
            { $match: { $expr: {
                $eq: [ "$_id.StateGroup", "$$vp_state" ]
            }}},
            { $project: {
                "_id": 0,
                "EVStationCount": 1
            }}
        ],
        as: "dataFromEVStations"
    }},
    { $unwind: {
        path: "$dataFromEVStations",
        preserveNullAndEmptyArrays: true // there should be no missing value
    }},
    { $project: {
        "_id": 0,
        "State": "$_id.State",
        "vehicleCount": 1,
        "dataFromEVStations": 1,
        "vehicleToStations": { $divide: [ "$vehicleCount", "$dataFromEVStations.EVStationCount" ]}, 
    }},
    { $sort: { "vehicleToStations": -1 }}
])

printjson(q5_1)
// 44records are returned as we are using evByState(44) to join evStationByState(53)

print("\n query 5_2")
print("may be slow as we are using the [electric_vehicle_population] and the [ev_stations_v1] dataset")
print("--------------------")

q5_2 = db.electric_vehicle_population.aggregate([
    { $group: {
        "_id": { "PostalCode": "$PostalCode" },
        "vehicleCount": { $count: { }}
    }}, 
    { $lookup: {
        from: "ev_stations_v1",
        let: { vp_PostalCode: "$_id.PostalCode" },
        pipeline: [
            { $group: {
                "_id": { "ZipGroup": "$ZIP" },
                "EVStationCount": { $count: { }}
            }}, 
            { $match: { $expr: {
                $eq: [ "$_id.ZipGroup", "$$vp_PostalCode" ]
            }}},
            { $project: {
                "_id": 0,
                "EVStationCount": 1
            }}
        ],
        as: "dataFromEVStations"
    }},
    { $unwind: {
        path: "$dataFromEVStations",
        preserveNullAndEmptyArrays: true // there should be no missing value
    }},
    { $project: {
        "_id": 0,
        "PostalCode": "$_id.PostalCode",
        "vehicleCount": 1,
        "dataFromEVStations": 1,
        "vehicleToStations": { $divide: [ "$vehicleCount", "$dataFromEVStations.EVStationCount" ]}, 
    }},
    { $sort: { "vehicleToStations": -1 }}
])

printjson(q5_2)
// 764 records are returned as we are using evByPostalCode(764) to join evStationByZIP(9472)

// test state with the provided evByState
db.electric_vehicle_population.aggregate([
    { $group: {
        "_id": { "State": "$State" },
        "vehicleCount": { $count: { } }
    }},
    { $lookup: { 
        from: "evByState",
        localField: "_id.State",
        foreignField: "groupByState",
        as: "dataFromEVByState"
    }},
    { $unwind: {
        path: "$dataFromEVByState",
        preserveNullAndEmptyArrays: true // there should be no missing value
    }},
    { $addFields: { "trueOrFalse": { 
        $cond: {
            if: { $eq: [ "$vehicleCount", "$dataFromEVByState.vehicleCount" ]}, 
            then: true, 
            else: false 
        }
    }}},
    { $group: {
        "_id": { "trueOrFalse": "$trueOrFalse" },
        "count": { $count: { }}
    }}
])

// test state with the provided evStationByState
db.ev_stations_v1.aggregate([
    { $group: {
        "_id": { "State": "$State" },
        "EVStationCount": { $count: { }}
    }},
    { $lookup: { 
        from: "evStationByState",
        localField: "_id.State",
        foreignField: "groupByState",
        as: "dataFromEVStationByState"
    }},
    { $unwind: {
        path: "$dataFromEVStationByState",
        preserveNullAndEmptyArrays: true // there should be no missing value
    }},
    { $addFields: { "trueOrFalse": { 
        $cond: {
            if: { $eq: [ "$EVStationCount", "$dataFromEVStationByState.stationCount" ]}, 
            then: true, 
            else: false 
        }
    }}},
    { $group: {
        "_id": { "trueOrFalse": "$trueOrFalse" },
        "count": { $count: { }}
    }}
])

// test zip with the provided evByPostalCode
db.electric_vehicle_population.aggregate([
    { $group: {
        "_id": { "PostalCode": "$PostalCode" },
        "vehicleCount": { $count: { } }
    }},
    { $lookup: { 
        from: "evByPostalCode",
        localField: "_id.PostalCode",
        foreignField: "groupByPostalCode",
        as: "dataFromEVByPostalCode"
    }},
    { $unwind: {
        path: "$dataFromEVByPostalCode",
        preserveNullAndEmptyArrays: true // there should be no missing value
    }},
    { $addFields: { "trueOrFalse": { 
        $cond: {
            if: { $eq: [ "$vehicleCount", "$dataFromEVByPostalCode.vehCount" ]}, 
            then: true, 
            else: false 
        }
    }}},
    { $group: {
        "_id": { "trueOrFalse": "$trueOrFalse" },
        "count": { $count: { }}
    }}
])

// test zip with the provided evStationByZIP
db.ev_stations_v1.aggregate([
    { $group: {
        "_id": { "ZIP": "$ZIP" },
        "EVStationCount": { $count: { }}
    }},
    { $lookup: { 
        from: "evStationByZIP",
        localField: "_id.ZIP",
        foreignField: "groupByZIP",
        as: "dataFromEVStationByZIP"
    }},
    { $unwind: {
        path: "$dataFromEVStationByZIP",
        preserveNullAndEmptyArrays: true // there should be no missing value
    }},
    { $addFields: { "trueOrFalse": { 
        $cond: {
            if: { $eq: [ "$EVStationCount", "$dataFromEVStationByZIP.stationCount" ]}, 
            then: true, 
            else: false 
        }
    }}},
    { $group: {
        "_id": { "trueOrFalse": "$trueOrFalse" },
        "count": { $count: { }}
    }}
])

/*
6.	[nei_2017_full_data] For each NACIS description that contained “auto” or “motor”, 
display the sum of total emissions. 
Note: For details on NACIS codes, see https://www.standardtechnology.us/services/nacis-codes
*/
print("\n query 6")
print("--------------------")

q6 = db.nei_2017_full_data.aggregate([
    { $match: { $and: [   
        { $or: [
            { "naicsDescription": { $regex: /auto/, $options: "i" }},
            { "naicsDescription": { $regex: /motor/, $options: "i" }},
        ]},
        {"naicsDescription": { $not: { $regex: /except/, $options: "i" }}},
        // some description is like "except motor vehicle"
    ]}},
    { $addFields: { "totalEmissionsDouble": {
        $convert: {
            input: "$totalEmissions",
            to: "double"
        }
    }}},
    { $group: {
        "_id": { "naicsDescription": "$naicsDescription" },
        "count_": { $count: { }},
        "sumEmissions": { $sum: "$totalEmissionsDouble"},
        "avgEmissions": { $avg: "$totalEmissionsDouble"},
        "minEmissions": { $min: "$totalEmissionsDouble"},
        "maxEmissions": { $max: "$totalEmissionsDouble"}
    }},
    { $project: {
        "_id": 0,
        "naicsDescription": "$_id.naicsDescription",
        "count_": 1,
        "sumEmissions": 1,
        "avgEmissions": 1,
        "minEmissions": 1,
        "maxEmissions": 1
    }},
    { $sort: { "sumEmissions": -1 }}
])

printjson(q6)

/*
7.	[nei_2017_full_data]. Who are the key suppliers of Telsa (a major EV producer)? 
For each state, display the total emissions for the following suppliers: 
dana, emerson, nucor, micron, allegheny, albemarle, schneider, and veatch.
*/

print("\n query 7")
print("--------------------")

q7 = db.nei_2017_full_data.aggregate([
    { $match: { $or: [
        { "companyName": { $regex: /dana/, $options: "i" }},
        { "companyName": { $regex: /emerson/, $options: "i" }},
        { "companyName": { $regex: /nucor/, $options: "i" }},
        { "companyName": { $regex: /micron/, $options: "i" }},
        { "companyName": { $regex: /allegheny/, $options: "i" }},
        { "companyName": { $regex: /albemarle/, $options: "i" }},
        { "companyName": { $regex: /schneider/, $options: "i" }},
        { "companyName": { $regex: /veatch/, $options: "i" }},
        { "siteName": { $regex: /dana/, $options: "i" }},
        { "siteName": { $regex: /emerson/, $options: "i" }},
        { "siteName": { $regex: /nucor/, $options: "i" }},
        { "siteName": { $regex: /micron/, $options: "i" }},
        { "siteName": { $regex: /allegheny/, $options: "i" }},
        { "siteName": { $regex: /albemarle/, $options: "i" }},
        { "siteName": { $regex: /schneider/, $options: "i" }},
        { "siteName": { $regex: /veatch/, $options: "i" }},
    ]}},
    { $addFields: { "totalEmissionsDouble": {
        $convert: {
            input: "$totalEmissions",
            to: "double"
        }
    }}},
    { $group: {
        "_id": { "State": "$state" },
        "count_": { $count: { }},
        "sumEmissions": { $sum: "$totalEmissionsDouble" },
        "avgEmissions": { $avg: "$totalEmissionsDouble" },
        "minEmissions": { $min: "$totalEmissionsDouble" },
        "maxEmissions": { $max: "$totalEmissionsDouble" }
    }},
    { $sort: { "sumEmissions": -1 }}
])

printjson(q7)
// the last supplier veatch is still not captured








