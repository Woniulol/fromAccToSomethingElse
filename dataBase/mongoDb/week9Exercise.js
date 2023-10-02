// this script can be runned directly the mongosh interface using the load("<filePath>") method
// if try to run in NoSQL booster, replace `db.getSiblingDB()` method with `use <database>`

// Q1
db = db.getSiblingDB( "simpleClinic" )
db.dropDatabase()
db.patients.drop()

// create the above database and colletion
// insert the above document into the collection
db.patients.insertOne({
    firstName: "Ben",
    lastName: "Choi",
    age: 18,
    history: [
        {disease: "cold", treatment: "pain killer"},
        {checkup: "annual", output: "OK"},
        {disease: "sore throat", treatment: "antibodies"},
        ]
})

// insert 3 additional patient records (documents) with at least 1 history entry per patient.
db.patients.insertMany([
    {
        firstName: "C",
        lastName: "D",
        age: 20,
        history: [
            {disease: "flu", treatment: "pain killer_2"},
            {disease: "sore throattt_2", treatment: "antibodies_2"},
        ]
    },
    {
        firstName: "E",
        lastName: "F",
        age: 22,
        history: [
            {disease: "cold_3", treatment: "pain killer_3"},
            {disease: "sore throattt_3", treatment: "antibodies_3"},
        ]
    },
    {
        firstName: "G",
        lastName: "H",
        age: 28,
        history: [
            {disease: "cold_4", treatment: "pain killer_4"},
            {disease: "flu", treatment: "antibodies_4"},
        ]
    }
])

// test out your database with find()
print("\n\n\n find all documents in patients collection")
print("------------------------------------------")
printjson(db.patients.find())

// find all patients who are older than 25 years old
print("\n\n\n find all patients who are older than 25 years old")
print("--------------------------------------------------")
printjson(db.patients.find( {"age": {$gt: 25} } ))

// delete all patients who got a flu as a disease
print("\n\n\n find all patients who got a flu as a disease")
print("---------------------------------------------")
printjson(db.patients.find( {"history.disease": "flu"} ))

// Q2
// Create a MongoDB to capture the above records (database name = amazonPrime). 
// You can use a maximum of 3 collections.
db = db.getSiblingDB( "amazonPrime" )
db.dropDatabase()
db.customers.drop()
db.orders.drop()
db.products.drop()

// insert the records in the above tables into documents in each collection
// You must observe the relationships depicted in the ERD, either by reference or embedded documents.
db.customers.insertMany([
    {
        "_id": "1000",
        "customerName": "Ben Choi",
        "customerOrder": ['1880001', '1880002', '1880003']
    },
    {
        "_id": "1001",
        "customerName": "Jayden Choi",
        "customerOrder": ['1880004', '1880005']
    },
    {
        "_id": "1002",
        "customerName": "Cammy Soh",
        "customerOrder": null
    },
    {
        "_id": "1004",
        "customerName": "Mason Greenwood",
        "customerOrder": ['1880006']
    },
    {
        "_id": "1005",
        "customerName": "Dean Henderson",
        "customerOrder": ['1880007']
    }
])

db.orders.insertMany([
    {
        "_id": "1880001",
        "orderDate": "2020/01/21",
        "customerID": "1000",
        "productInfors": [
            {'prodcutID': '50001', 'quantity': 2, 'price': 4.25}, 
            {'prodcutID': '50003', 'quantity': 1, 'price': 14.9}
        ]
    },
    {
        "_id": "1880002",
        "orderDate": "2020/01/22",
        "customerID": "1000",
        "productInfors": [
            {'prodcutID': '50002', 'quantity': 2, 'price': 11.8}
        ]
    },
    {
        "_id": "1880003",
        "orderDate": "2020/01/23",
        "customerID": "1000",
        "productInfors": [
            {'prodcutID': '50004', 'quantity': 4, 'price': 9.9}, 
            {'prodcutID': '50005', 'quantity': 2, 'price': 22.0}
        ]
    },
    {
        "_id": "1880004",
        "orderDate": "2020/01/22",
        "customerID": "1001",
        "productInfors": [
            {'prodcutID': '50003', 'quantity': 1, 'price': 14.9}, 
            {'prodcutID': '50004', 'quantity': 1, 'price': 9.9}
        ]
    },
    {
        "_id": "1880005",
        "orderDate": "2020/01/23",
        "customerID": "1001",
        "productInfors": [
            {'prodcutID': '50002', 'quantity': 2, 'price': 11.8}
        ]
    },
    {
        "_id": "1880006",
        "orderDate": "2020/01/24",
        "customerID": "1004",
        "productInfors": [
            {'prodcutID': '50004', 'quantity': 1, 'price': 9.9}, 
            {'prodcutID': '50005', 'quantity': 1, 'price': 22.0}
        ]
    },
    {
        "_id": "1880007",
        "orderDate": "2020/01/25",
        "customerID": "1005",
        "productInfors": [
            {'prodcutID': '50002', 'quantity': 2, 'price': 11.8}, 
            {'prodcutID': '50003', 'quantity': 1, 'price': 14.9}, 
            {'prodcutID': '50001', 'quantity': 2, 'price': 4.25}
        ]
    }
])

db.products.insertMany([
    {
        "_id": "50001",
        "productName": "Scott Pick A Size Multi Purpose Towels",
        "standardPrice": 4.25
    },
    {
        "_id": "50002",
        "productName": "Japanese Super Crispy Chicken",
        "standardPrice": 11.8
    },
    {
        "_id": "50003",
        "productName": "Vegan Beyond Burger Plant Based Patties Beef",
        "standardPrice": 14.9
    },
    {
        "_id": "50004",
        "productName": "Korean Honey Sweet Potato",
        "standardPrice": 9.9
    },
    {
        "_id": "50005",
        "productName": "Premium Atlantic Salmon 1Kg",
        "standardPrice": 22.0
    }
])

print("\n\n\n show all documents in customers collection")
print("-------------------------------------------")
printjson(db.customers.find())

print("\n\n\n show all documents in orders collection")
print("----------------------------------------")
printjson(db.orders.find())

print("\n\n\n show all documents in products collection")
print("------------------------------------------")
printjson(db.products.find())











