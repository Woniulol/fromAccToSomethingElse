// this script can be runned directly the mongosh interface using the load("<filePath>") method
// if try to run in NoSQL booster, replace `db.getSiblingDB()` method with `use <database>`

// case 1 Box Office 2
// import data
// mongoimport --db=boxoffice2 --collection=boxofficeExtended --drop --file="week11BoxOffice2.json" --jsonArray
db = db.getSiblingDB( "boxoffice2" )

// Q1
// Find all movies with exactly two genres
print("\n case1_Q1. Find all movies with exactly two genres")
print("--------------------")
q1 = db.boxofficeExtended.aggregate([
    {$addFields: {
        "genreSize": {$size: "$genre"}
    }},
    {$match: {"genreSize": 2}},
    {$project: {"genreSize": 0}}
])
printjson(q1)

// Q2
// Find all movies with exactly two genres
print("\n case1_Q2. Find all movies which aired in 2018")
print("--------------------")
q2 = db.boxofficeExtended.aggregate([{
    $match: {
        "meta.aired": 2018
    }
}])
printjson(q2)

// Q3
// Find all movies which have ratings greater than 8 but lower than 10
print("\n case1_Q3. Find all movies which have ratings greater than 8 but lower than 10")
print("--------------------")
q3 = db.boxofficeExtended.aggregate([{
    $match: {
        $and: [
            {"ratings": {$gt: 8}},
            {"ratings": {$lt: 10}}
        ]
    }
}])
printjson(q3)

// case 2: Sports Teams

// Q1
// Insert the following documents using upsert, not insert()
db = db.getSiblingDB( "sports" )
db.dropDatabase()

print("\n case2_Q1. Insert the following documents using upsert, not insert()")
print("--------------------")

db.teams.updateOne( 
    { "title": "Nanyang United" }, 
    { $set: { "requiresTeam": true } }, 
    { upsert: true } 
)

db.teams.updateOne( 
    { "title": "Sengkang One" }, 
    { $set: { "requiresTeam": false } }, 
    { upsert: true } 
)

printjson(
    db.teams.find()
)

// Q2
// Update all documents which do require a team by adding a new field with the minimum amount of players required
print("\n case2_Q2. Update all documents which do require a team by adding a new field with the minimum amount of players required")
print("--------------------")

db.teams.updateMany(
    {"requiresTeam": true},
    {$set: {"minNumPlayers": 0}},
    {upsert: true } 
)

printjson(
    db.teams.find()
)

// Q3
// Update all documents that require a team by increasing the number of required players by 10
print("\n case2_Q3. Update all documents that require a team by increasing the number of required players by 10")
print("--------------------")
db.teams.updateMany(
    {"requiresTeam": true},
    {$inc: {"minNumPlayers": 10}}
)

printjson(
    db.teams.find()
)

// case 3 Persons
// import data
// mongoimport --db=analytics --collection=persons --drop --file="week11Persons.json" --jsonArray
db = db.getSiblingDB( "analytics" )

// Q1
// Build a pipeline to find the number of peron(s) older than 50. 
// Group these people by gender. 
// For each group, compute the average age and count the total number of person(s) in the group.  
// Order the output by the total amount of person(s) per group in a descending order.
print("\n case3_Q1. apply in aggregation")
print("--------------------")
q1 = db.persons.aggregate([
    {
        $match: {"dob.age": {$gt: 50}}
    },
    {
        $group: {
            "_id": "$gender",
            "personCount": {$sum: 1},
            "ageAverage": {$avg: "$dob.age"},
        }
    },
    {
        $sort: {"personCount": -1}
    },
    {
        $project: {
            "_id": 0,
            "gender": "$_id",
            "personCount": 1,
            "roundedAvgAge": {$round: ['$ageAverage', 2]}
        }
    }
])

printjson(q1)