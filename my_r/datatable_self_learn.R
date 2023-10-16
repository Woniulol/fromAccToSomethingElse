# install.packages("data.table")
library(data.table)

# https://cran.r-project.org/web/packages/data.table/vignettes/

# fundemental logic:
# DT[         i,                  j,          by. ]
# SQL:  where | order by   select | update  group by

# why would they even bother to put j in the first place?
    # in two dimension tables, i generally equals to the row but it happens to be the where in sql
# very similar to sql

# read data
setwd("/Users/jiananwang/ob_library/StoriesofYourLifeandOthers/Others/MediaNote/DocumentNote/AC6006 Course Materials/Unit 3 - Data Exploration and Summaries")
flights.dt <- fread("flights14.csv")
flights.dt
    # there is a parameter called na.strings which you can specify what kind of 
    # value within the data set should be interpreted as NA

# conditioning (select all) data
ans <- flights.dt[origin == 'JFK' & month == 6]
    # just like sql, you can directly use origin and month as variable
    # but you could use $ to get the corresponding columns and 
    # you could add a comma in the very end to do data frame style
ans <- flights.dt[flights.dt$origin == 'JFK' & flights.dt$month == 6, ]
identical(flights.dt[origin == 'JFK' & month == 6],
          flights.dt[flights.dt$origin == 'JFK' & flights.dt$month == 6])
    # data table support something like this
ans <- flights.dt[origin %in% c("JFK", "LGA")]

ans <- flights.dt[1:3]
    # equals to
ans <- flights.dt[1:3, ]

identical(flights.dt[1:3], flights.dt[1:3, ])


# sort (order by in sql)
ans <- flights.dt[order(origin, -dest)]
    # by defualt it is ascending ordering, with - then it is descending


# select columns
ans <- flights.dt[, arr_delay]
class(ans)
    # this will only return a vector
    # to get a sub data table, you need to pass a list in j sector
ans <- flights.dt[, list(arr_delay)]
    # within the list, columns name are not enclosed by "
    # .() is the alias of .list()
ans <- flights.dt[, .(arr_delay)]
identical(flights.dt[, list(arr_delay)], flights.dt[, .(arr_delay)])
    # As long as j-expression returns a list, 
    # each element of the list will be converted to a column in the resulting data.table.

# select multiple columns
ans <- flights.dt[, .(arr_delay, dep_delay)]
ans <- flights.dt[, c('arr_delay', 'dep_delay')]
    # if you pass a vector in j, you need to enclose the columne name with ""
identical(flights.dt[, .(arr_delay, dep_delay)], flights.dt[, c('arr_delay', 'dep_delay')])
    # if you store the vector of selection out side the clauses
select_cols = c('arr_delay', 'dep_delay') 
ans <- flights.dt[, ..select_cols]
ans <- flights.dt[, select_cols, with = F]
identical(flights.dt[, ..select_cols], flights.dt[, select_cols, with = F])
    # you get same result
    # For those familiar with the Unix terminal, 
    # the .. prefix should be reminiscent of the “up-one-level” command
    # basically means go to the global variables to find select_cols
    # even tough string type is more complex, you can use it to deselect
ans <- flights.dt[, -c('arr_delay', 'dep_delay')]
ans <- flights.dt[, !c('arr_delay', 'dep_delay')]
identical(flights.dt[, -c('arr_delay', 'dep_delay')], flights.dt[, !c('arr_delay', 'dep_delay')])
# also support
ans <- flights.dt[, year:day]
ans <- flights.dt[, day:year]
ans <- flights.dt[, -(year:day)]
ans <- flights.dt[, !(year:day)]

####################################
# select and rename
ans <- flights.dt[, .(delay_arr = arr_delay, delay_dep = dep_delay)]
# consider it a list operation, with give the element of the list (columns here) an name
####################################

# functions in j
# just like in sql we allow select columnA * columnB as a*b
ans <- flights.dt[, sum( (arr_delay + dep_delay) < 0 )]


# combined operation
# Calculate the average arrival and departure delay for all flights 
# with “JFK” as the origin airport in the month of June.
ans <- flights.dt[origin == 'JFK' & month == 6,
                 .(m_arr = mean(arr_time), m_dep = mean(dep_delay))]
ans <- flights.dt[origin == 'JFK' & month == 6,
                  lapply(.(m_arr = arr_time, m_dep = dep_delay), mean)]
# some times you cannot type every mean to all the variabels within a list
# as long as it returns a list, it is leagal in j
identical(flights.dt[origin == 'JFK' & month == 6,
                     .(m_arr = mean(arr_time), m_dep = mean(dep_delay))],
          flights.dt[origin == 'JFK' & month == 6,
                     lapply(.(m_arr = arr_time, m_dep = dep_delay), mean)])
# within single statement, we do conditioning, selection, calculation and rename
# Because the three main components of the query (i, j and by) are together 
# inside [...], data.table can see all three and optimize the query altogether 
# before evaluation, not each separately. We are able to therefore avoid the 
# entire subset (i.e., subsetting the columns besides arr_delay and dep_delay), 
# for both speed and memory efficiency.
# – How many trips have been made in 2014 from “JFK” airport in the month of June?
ans <- flights.dt[origin == 'JFK' & year == 2014,
                  .(count = length(dest))]
# equal to 
# Special symbol .N:
ans <- flights.dt[origin == 'JFK' & year == 2014,
                  .(count = .N)]
# with .(), we get a data table here
ans <- flights.dt[origin == 'JFK' & year == 2014, .N]
# here we get a vector

# chained operation
# firstly, we have this
ans <- flights.dt[carrier == "AA", .N, by = .(origin, dest)]
# then how can we order ans using the columns origin in ascending order, 
# and dest in descending order?
ans <- flights.dt[carrier == "AA", .N, by = .(origin, dest)][order(origin, -dest)]
# by using a chain operation, we avoid the space and time in creating something new



# aggregation (group by)
# when excuting a statement, by is ways carried out first and other is carried out based on the result of groups of by
ans <- flights.dt[, .(.N), by = .(origin)]
# When there’s only one column or expression to refer to in j and by, 
# we can drop the .() notation.
ans <- flights.dt[, .N, by = origin]
# for sql: select origin, count(origin) from flights.dt group by origin
# How can we calculate the number of trips for each origin airport for carrier code "AA"?
ans <- flights.dt[carrier == 'AA', .N, by = origin]
# Once again no columns are actually materialized here, 
# because the j-expression does not require any columns to be actually 
# subsetted and is therefore fast and memory efficient.
# How can we get the total number of trips for each origin, dest pair for carrier code "AA"?
ans <- flights.dt[carrier == 'AA', .N, by = .(origin, dest)]
# equals to
ans <- flights.dt[carrier == "AA", .N, by = c("origin", "dest")]
identical(flights.dt[carrier == 'AA', .N, by = .(origin, dest)], 
          flights.dt[carrier == "AA", .N, by = c("origin", "dest")])
# similarly, once use want to use the string type column names, pass a vector
# How can we get the average arrival and departure delay for 
# each orig, dest pair for each month for carrier code "AA"?
ans <- flights.dt[carrier == 'AA', 
                  .(m_arrtime = mean(arr_time), m_depdelay = mean(dep_delay)), 
                  by = .(origin, dest, month)]
# note that the input order of grouping columns is preserved in the result.
  # we could sort the group by pairs using key word keyby
ans <- flights.dt[carrier == 'AA', 
                  .(m_arrtime = mean(arr_time), m_depdelay = mean(dep_delay)), 
                  keyby = .(origin, dest, month)]
# the default is in increasing order
# keyby is typically faster than by because it doesn't require this second step.
# Keys: Actually keyby does a little more than just ordering. 
# It also sets a key after ordering by setting an attribute called sorted.
# expressions in by
# e.g. find out how many flights started late but arrived early
ans <- flights.dt[, .N, .(dep_delay <= 0, arr_delay <= 0)]
# could also be achieved by
ans <- flights.dt[, .N, .(dep_delay > 0, arr_delay > 0)]
# equals to
ans <- flights.dt[, .N, by = .(dep_delay > 0, arr_delay > 0)]
# you can also combine expression with non expression in by


# .SD
# It by itself is a data.table that holds the data for the current group defined using by.
# Recall that a data.table is internally a list as well with all its columns of equal length.
# which means a data table is actually a long list so that .SD could be passed to j
ans <- flights.dt[, .SD]
identical(flights.dt, flights.dt[, .SD])
# this help us to do multicolumn calculationc fast and we could use .SDcol to get rid of columns that we dont want
ans <- flights.dt[carrier == "AA", 
                  lapply(.SD, mean), 
                  by = .(origin, dest, month), 
                  .SDcols = c("arr_delay", "dep_delay")]
# just consider .SD as a full length data table which you can perform any action
ans <- flights.dt[, 
                  head(.SD, 2), 
                  by = month]
# group by month first and show the first two row of SD in each group


# concatenate
DT = data.table(
  ID = c("b","b","b","a","a","c"),
  a = 1:6,
  b = 7:12,
  c = 13:18
)

ans <- DT[, .(val = c(a, b)), by = ID]
# attention, here, even though it is in a vector, but a and b are not encloused with ""
# c(a, b) within the [ ] equal to c(DT$a, DT$b)
DT[, .(val = list(c(a,b))), by = ID]
# remember, we always do group by first!

# j
# j part is possibily the most powerful part of data table
# use print to play around
DT[, print(c(a,b)), by = ID]
DT[, print(list(c(a,b))), by = ID]


# With data.table’s := operator, absolutely no copies are made in 
# both (1) and (2), irrespective of R version you are using. 
# This is because := operator updates data.table columns in-place (by reference).

# add / update / delete

    # operator := in j part
        # form 1
        # DT[, c("colA", "colB", ...) := list(valA, valB, ...)]
        # when you have only one column to assign to you
        # can drop the quotes and list(), for convenience
        # DT[, colA := valA]
        # similarly, the right hand side is only need to be a list
    
        # form 2
        # DT[, `:=`(colA = valA, # valA is assigned to colA
        #           colB = valB, # valB is assigned to colB
        # ...
        # )]

    # add
        # How can we add columns speed and total delay of each flight to 
        # flights data.table?
        # speed = distance / (air_time / 60)
        # delay = arr_delay + dep_delay
flights.dt[, `:=`(
                speed = distance / (air_time / 60),
                delay = arr_delay + dep_delay
                )
           ]
        # we dont have to reassign the value as the change in by reference
    
    # update
        # replace those rows where hour == 24 with the value 0
flights.dt[hour == 24, hour := 0]
        # update tables set hour = 0 where hour == 24
        # all the add / update / delete will be finished without returning anything
        # if you want to see something, add a [] at the end of the statement
flights.dt[hour == 24, hour := 0][]
        # the difference between 
        # a --- flights.dt[hour == 24, hour := 0]
        # and
        # b --- flights.dt[hour == 24][, hour := 0]
        # for a, the update in j is made to flights.dt directly and invisibly
        # for b, the update in j is made to flights.dt[hour == 24], not flights.dt
ans <- flights.dt[hour == 24][, hour := 0]

    # delete
        # the logic the to assign NULL to specific columns
flights.dt[, `:=`( delay = NULL )]
        # equals to
flight.dt[, c('delay') := NULL]
        # When there is just one column to delete, we can drop the c() 
        # and double quotes and just use the column name unquoted, for convenience. 
        # That is:
flights.dt[, delay := NULL]

    # := along with by
        # How can we add a new column which contains for 
        # each orig, dest pair the maximum speed?
flights.dt[, max_speed := round(max(speed)), by = .(origin, dest)]
        # That value is recycled to fit the length of the group. Once again, 
        # no copies are being made at all.
flights.dt[, max(max_speed), by = .(origin, dest)]

    # multiple columns
        # How can we add two more columns computing max() of dep_delay 
        # and arr_delay for each month, using .SD?
in_cols  = c("dep_delay", "arr_delay")
out_cols = c("max_dep_delay", "max_arr_delay")
flights.dt[, c(out_cols) := lapply(.SD, max), by = month, .SDcols = in_cols]
        # ote that since we allow assignment by reference without quoting column 
        # names when there is only one column as explained in Section 2c, we can 
        # not do out_cols := lapply(.SD, max). That would result in adding one 
        # new column named out_col. Instead we should do either c(out_cols) or 
        # simply (out_cols). Wrapping the variable name with ( is enough to 
        # differentiate between the two cases.

# copy
    # When we store the column names on to a variable, e.g., DT_n = names(DT), 
    # and then add/update/delete column(s) by reference. It would also modify 
    # DT_n, unless we do copy(names(DT)).
DT = data.table(x = 1L, y = 2L)
DT_n = names(DT)
DT_n
    # "x" "y"
    # add a new column by reference
DT[, z := 3L]
    ## DT_n also gets updated
DT_n
    # "x" "y" "z"
    # use `copy()` deepcopy
DT_n = copy(names(DT))
DT[, w := 4L]
    # DT_n doesn't get updated
DT_n
    # "x" "y" "z"


# key and row names
    # If you would like to preserve the row names, use keep.rownames = TRUE in as.data.table() 
    # this will create a new column called rn and assign row names to this column.


