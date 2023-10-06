use `ac6005_gp`;

-- q1
/*
1.	[ev_stations_v1] For each zip code, display the number of stations 
located between latitudes (33.20 to 34.70) and longitudes (-118.40 and -117.20).
*/

select 
	ZIP,
	count(*) as countOfStations
from `ev_stations_v1`
where
	(convert(latitude, decimal(16, 8)) > 33.20)
    and
    (convert(latitude, decimal(16, 8)) < 34.70)
    and
    (convert(longitude, decimal(16, 8)) > -118.40)
    and 
    (convert(longitude, decimal(16, 8)) < -117.20)
group by ZIP
order by countOfStations desc;

-- q2
/*
2.	[ev_stations_v1] Let’s find out where we can find the most Telsa cars. 
For each state and model, display the number of Telsa cars in descending order.
*/

select 
	state, 
    model, 
    count(*) as countOfVehicle
from electric_vehicle_population
where make like "%TESLA%"
group by state, model
order by countOfVehicle desc;

-- q3
/*
3.	[ev_stations_v1] For each electric vehicle type and each clean alternative fuel vehicle eligibility, 
display the average electric range value.
*/

select 
	ElectricVehicleType,
    CleanAlternativeFuelVehicleEligibility,
    avg(convert(ElectricRange, decimal(16, 2))) as avgElectricRange
from electric_vehicle_population
group by ElectricVehicleType, CleanAlternativeFuelVehicleEligibility
order by avgElectricRange desc;

-- q4
/*
4.	[co2_emissions_canada] and [electric_vehicle_population] 
Estimate the CO2 emission of vehicles using alternative fuel in the states. 
For each make and each model, in each state, display 
the number of vehicles and the CO2 emissions in grams per km.
*/

select * 
from (
	select
		make,
		model, 
		round(avg(convert(CO2Emissions_g_km, decimal(16, 8))),2) as avgCO2Emissions_g_km,
		max(convert(CO2Emissions_g_km, decimal(16, 2))) as maxCO2Emissions_g_km,
		min(convert(CO2Emissions_g_km, decimal(16, 2))) as minCO2Emissions_g_km
	from co2_emissions_canada
	group by make, model
	order by avgCO2Emissions_g_km desc
) as groupCO2
right join (
	select
		state,
		make,
		model,	
		count(*) as countOfVehicle
	from electric_vehicle_population
	group by state, make, model
) as groupEVP
using (make, model)
order by countOfVehicle desc;



-- q5
/*
5.	[ev_stations_v1] and [electric_vehicle_population] Does the number of EV stations matter? There are two parts to this query:
i)	For each state, display 
the number of electric vehicles, the number of EV stations, 
and the vehicle:station ratio in descending ratio order.
ii)	For each postalcode(zip), display 
the number of electric vehicles, the number of EV stations, 
and the vehicle:station ratio in descending ratio order.
*/

select state, countofStations, countOfVehicle, round((countOfVehicle/countofStations),5) as vehicleToStations
from (
	select state, count(*) as countofStations
	from ev_stations_v1
	group by state
) as groupEVStation
join (
	select state, count(*) as countOfVehicle
	from electric_vehicle_population
	group by state
) as groupEVP
using (state)
order by vehicleToStations desc;

select ZIP, countofStations, countOfVehicle, round((countOfVehicle/countofStations),5) as vehicleToStations
from (
	select ZIP, count(*) as countofStations
	from ev_stations_v1
	group by ZIP
) as groupEVStation
join (
	select postalcode, count(*) as countOfVehicle
	from electric_vehicle_population
	group by postalcode
) as groupEVP
on (ZIP = postalcode)
order by vehicleToStations desc;

-- q6
/*
6.	[nei_2017_full_data] For each NACIS description that contained “auto” or “motor”, 
display the sum of total emissions. 
Note: For details on NACIS codes, see https://www.standardtechnology.us/services/nacis-codes
*/

select 
	naicsDescription, 
	count(*) as count_, 
    sum(convert(totalEmissions, decimal(16, 8))) as sumEmissions,
    avg(convert(totalEmissions, decimal(16, 8))) as avgEmissions,
    min(convert(totalEmissions, decimal(16, 8))) as minEmissions,
    max(convert(totalEmissions, decimal(16, 8))) as maxEmissions
from nei_2017_full_data
where
	((naicsDescription like "%auto%") or (naicsDescription like "%motor%"))
    and
    (naicsDescription not like "%except%") 
group by naicsDescription
order by sumEmissions desc;

-- q6
/*
7.	[nei_2017_full_data]. Who are the key suppliers of Telsa (a major EV producer)? 
For each state, display the total emissions for the following suppliers: 
dana, emerson, nucor, micron, allegheny, albemarle, schneider, and veatch.
*/

select 
	state, 
	count(*) as count_, 
    sum(convert(totalEmissions, decimal(16, 8))) as sumEmissions,
    avg(convert(totalEmissions, decimal(16, 8))) as avgEmissions,
    min(convert(totalEmissions, decimal(16, 8))) as minEmissions,
    max(convert(totalEmissions, decimal(16, 8))) as maxEmissions
from nei_2017_full_data
where
	(companyName like "%dana%") or (siteName like "%dana%") or
    (companyName like "%emerson%") or (siteName like "%emerson%") or
    (companyName like "%nucor%") or (siteName like "%nucor%") or
    (companyName like "%micron%") or (siteName like "%micron%") or
    (companyName like "%allegheny%") or (siteName like "%allegheny%") or
    (companyName like "%albemarle%") or (siteName like "%albemarle%") or
    (companyName like "%schneider%") or (siteName like "%schneider%") or
    (companyName like "%veatch%") or (siteName like "%veatch%")
group by state
order by sumEmissions desc;