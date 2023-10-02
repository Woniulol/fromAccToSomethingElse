// this script can be runned directly the mongosh interface using the load("<filePath>") method
// if try to run in NoSQL booster, replace `db.getSiblingDB()` method with `use <database>`

// import data
// mongoimport --db="boxoffice" --collection="moviestarts" --drop --file="week10BoxOffice.json" --jsonArray

db = db.getSiblingDB( "boxoffice" )
print("\n set db as boxoffice")
print("--------------------")

// Q1
// display the first document
print("\n Q1. display the first document")
print("--------------------")
printjson(db.moviestarts.findOne())

// Q2
// search all movies that have a rating higher than 9.2 and a runtime lower than 100 minutes
print("\n Q2. search all movies that have a rating higher than 9.2 and a runtime lower than 100 minutes")
print("--------------------")
q2 = db.moviestarts.find(
    {
        $and: [
            {"meta.rating": {$gt: 9.2}},
            {"meta.runtime": {$lt: 100}}
        ]
    }
)
printjson(q2)

// Q3
// search all movies that have a genre of "drama" and "action". 
print("\n Q3. search all movies that have a genre of 'drama' and 'action'.")
print("--------------------")
q3 = db.moviestarts.find(
    {
        $and: [
            {"genre": "drama"},
            {"genre": "action"}
        ]
    }
)
printjson(q3)

// Q4
// search all movies that have a genre of "drama" and "action". You must not use $and
print("\n Q4. search all movies that have a genre of 'drama' and 'action'. You must not use $and")
print("--------------------")
q4 = db.moviestarts.find(
    {
        "genre": {
            $all: ["drama", "action"]
        }
    }
)
printjson(q4)
/*
db.moviestarts.find(
    {
        "genre": "drama",
        "genre": "actioan"
    }
)
this won't work as the the second condition of `genre` will overwirte the first condition
*/

// Q5
// search all movies where visitors exceeded expected visitors
print("\n Q5. search all movies where visitors exceeded expected visitors")
print("--------------------")
q5 = db.moviestarts.find(
    {
        $expr: {
            $gt: ["$visitors", "$expectedVisitors"]
        }
    }
)
printjson(q5)

// Q6
// search all movies that have a title contains the letter "Su".
print("\n Q6. search all movies that have a title contains the letter 'Su'")
print("--------------------")
q6 = db.moviestarts.find(
    {
        "title": {$regex: /.*Su.*/}
    }
)
printjson(q6)

// Q7
// search all movies that either have a genre of "action" and "thriller" or have a genre of "drama", 
// and at the same time, have more than 300000 visitors with a rating between 8 and 9.5 (inclusive).
print("\n Q7")
print("--------------------")
q7 = db.moviestarts.find(
    { $and: [
            { $or: [
                {$and: [{"genre": "action"}, {"genre": "thriller"}]},
                {"genre": "drama"}
            ]},
            {"visitors": {$gt: 300000}},
            { $and: [
                {"meta.rating": {$gte: 8}}, 
                {"meta.rating": {$lte: 9.5}},
            ]}
        ]
    }
)
printjson(q7)