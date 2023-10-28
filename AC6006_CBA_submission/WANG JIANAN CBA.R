# ----------
# NAME: Jianan Wang
# Matriculation Number: G2200496L
# For AC6006 CBA
# ----------

library(data.table)
library(car)
library(caTools)
library(rpart)
library(rpart.plot)
library(randomForest)
set.seed(1)
setwd("/Users/jiananwang/ob_library/StoriesofYourLifeandOthers/Others/MediaNote/DocumentNote/AC6006 Course Materials/AY23 CBA")

# import, clean and factor the data
# ----------
marun_table <- fread("marun_sample2.csv")  # read the csv data
summary(marun_table)

sum(is.na(marun_table))  # four NAs are identified
which(rowSums(is.na(marun_table)) > 0)  # four NA are concentrated in two rows

marun_table_clean <- na.omit(marun_table)  # remove the observation with any NA
summary(marun_table_clean)  # 2668 -2 = 2666 obs remains
sum(is.na(marun_table_clean))

marun_table <- marun_table_clean
rm(marun_table_clean)  # release the memory

# reset some names so that Random Forest can recognize
setnames(marun_table, 'Depth (ft)', 'DepthFT')
setnames(marun_table, 'Pore pressure', 'PorePressure')
setnames(marun_table, 'Fracture pressure', 'FracturePressure')
setnames(marun_table, 'Mud pressure (psi)', 'MudPressurePSI')
setnames(marun_table, 'Hole size (in)', 'HoleSizeIN')
setnames(marun_table, 'Pump flow rate', 'PumpFlowRate')
setnames(marun_table, 'Pump pressure', 'PumpPressure')

names(marun_table)

marun_table$Formation <- factor(marun_table$Formation)  # factor the categorical feature
marun_table$HoleSizeIN <- factor(marun_table$HoleSizeIN)  # factor the categorical feature

summary(marun_table)

# data exploration
# ----------
# please refer to the python script WANG JIANAN CBA_data_exploration.ipynb

# train-test split
train <- sample.split(Y = marun_table$MUDLOSSU, SplitRatio = 0.7)
trainset <- subset(marun_table, train == T)
testset <- subset(marun_table, train == F)
# it is noticed that the split does not follow exactly the Split Ratio, 
# as the distribution of target Y is imbalanced

# Liner Regression
# ----------
# build a LM based on full information, to test VIF, complexity and p-value
LM_1 <- lm(MUDLOSSU ~ ., data = marun_table)
vif1 <- vif(LM_1)  
vif1
names(vif1[,1][vif1[,1] == max(vif1[,1])])  # Formation

LM_1_vif1 <- lm(MUDLOSSU ~ . - Formation, data = marun_table)
vif2 <- vif(LM_1_vif1)  
vif2
names(vif2[,1][vif2[,1] == max(vif2[,1])])  # FAN300

LM_1_vif2 <- lm(MUDLOSSU ~ . - Formation - FAN300, data = marun_table)
vif3 <- vif(LM_1_vif2)  
vif3
names(vif3[,1][vif3[,1] == max(vif3[,1])])  # HoleSizeIN

LM_1_vif3 <- lm(MUDLOSSU ~ . - Formation - FAN300 - HoleSizeIN, data = marun_table)
vif4 <- vif(LM_1_vif3)  
vif4
names(vif4[vif4 == max(vif4)])  # FracturePressure

LM_1_vif4 <- lm(MUDLOSSU ~ . - Formation - FAN300 - HoleSizeIN - FracturePressure, data = marun_table)
vif5 <- vif(LM_1_vif4)  
vif5
names(vif5[vif5 == max(vif5)])  # Easting

LM_1_vif5 <- lm(MUDLOSSU ~ . - Formation - FAN300 - HoleSizeIN - FracturePressure - Easting, data = marun_table)
vif6 <- vif(LM_1_vif5)  
vif6
names(vif6[vif6 == max(vif6)])  # MudPressurePSI

LM_1_vif6 <- lm(MUDLOSSU ~ . - Formation - FAN300 - HoleSizeIN - FracturePressure - Easting - MudPressurePSI, data = marun_table)
vif7 <- vif(LM_1_vif6)  
vif7
names(vif7[vif7 == max(vif7)])  # FAN600

LM_1_vif7 <- lm(MUDLOSSU ~ . - Formation - FAN300 - HoleSizeIN - FracturePressure - Easting - MudPressurePSI - FAN600, data = marun_table)
vif8 <- vif(LM_1_vif7)  
vif8
names(vif8[vif8 == max(vif8)])  # PumpFlowRate < 10 stop cutting

step(LM_1_vif7)

# result of step
# Call:
# lm(formula = MUDLOSSU ~ Northing + DepthFT + PorePressure + METERAGE + 
#      PumpFlowRate + PumpPressure + MFVIS + MIN10GEL + RPM, data = marun_table)
LM_1_vif7_step <- lm(MUDLOSSU ~ Northing + DepthFT + PorePressure + 
                      METERAGE + PumpFlowRate + PumpPressure + MFVIS + MIN10GEL + 
                      RPM, data = marun_table)
summary(LM_1_vif7_step)  # Northing & RPM is not significant enough, remove

LM_1_vif7_step1 <- lm(MUDLOSSU ~ DepthFT + PorePressure + METERAGE + 
                        PumpFlowRate + PumpPressure + MFVIS + MIN10GEL, data = marun_table)
summary(LM_1_vif7_step1)

# check the assumptions
par(mfrow = c(2,2))
plot(LM_1_vif7_step1)
par(mfrow = c(1,1))

# row 85 is a potential outlier, remove
marun_table_no85 <- marun_table[-85]

# rebuild the Linear Regression model
LM_1_vif7_step1_no85 <- lm(MUDLOSSU ~ DepthFT + PorePressure + METERAGE + 
                        PumpFlowRate + PumpPressure + MFVIS + MIN10GEL, data = marun_table_no85)
summary(LM_1_vif7_step1_no85)
par(mfrow = c(2,2))
plot(LM_1_vif7_step1_no85)
par(mfrow = c(1,1))
# no significant influence

train_no85 <- sample.split(Y = marun_table_no85$MUDLOSSU, SplitRatio = 0.7)
trainset_no85 <- subset(marun_table_no85, train_no85 == T)
testset_no85 <- subset(marun_table_no85, train_no85 == F)

# train the Linear Regression model using trainset_no85
LM <- lm(formula = MUDLOSSU ~ DepthFT + PorePressure + 
                        METERAGE + PumpFlowRate + PumpPressure + MFVIS + MIN10GEL, data = trainset_no85)
summary(LM)
# RMSE on trainset_no85 based on LM model.
RMSE_LM_train<- sqrt(mean(residuals(LM)^2))  
RMSE_LM_train
# prediction
LM_yhat <- predict(LM, newdata = testset_no85)
testset.error <- testset_no85$MUDLOSSU - LM_yhat
# RMSE on testset_no85 based on RMSE_LM_1_vif7_step1_train model.
RMSE_LM_test <- sqrt(mean(testset.error^2))
RMSE_LM_test

# a full Linear Regression using all variabels is also built to try find any insignt
LM_full <- lm(formula = MUDLOSSU ~ ., data = trainset_no85)
summary(LM_full)

RMSE_LM_train<- sqrt(mean(residuals(LM_full)^2))  
RMSE_LM_train

LM_yhat <- predict(LM_full, newdata = testset_no85)
testset.error <- testset_no85$MUDLOSSU - LM_yhat

RMSE_LM_test <- sqrt(mean(testset.error^2))
RMSE_LM_test

# Regression Tree
# ----------
# build the tree and grow it to the maximum 
cart1 <- rpart(MUDLOSSU ~ . , data = trainset, method = 'anova', control = rpart.control(minsplit = 2, cp = 0))
plotcp(cart1)

# find the best cp to prune the tree. Method adopted from the professor
CVerror.cap <- cart1$cptable[which.min(cart1$cptable[,"xerror"]), "xerror"] + cart1$cptable[which.min(cart1$cptable[,"xerror"]), "xstd"]
i <- 1; j<- 4
while (cart1$cptable[i,j] > CVerror.cap) {
  i <- i + 1
}
cp.opt = ifelse(i > 1, sqrt(cart1$cptable[i,1] * cart1$cptable[i-1,1]), 1)

# prune the tree
cart2 <- prune(cart1, cp = cp.opt)
printcp(cart2, digits = 3)
print(cart2)
rpart.plot(cart2, type = 5)

# calculate RMSE
RMSE_cart_train <- sqrt(mean((residuals(cart2))^2))
RMSE_cart_train

cart_yhat <- predict(cart2, newdata = testset)

RMSE_cart_test <- round(sqrt(mean((testset$MUDLOSSU - cart_yhat)^2)), 3)
RMSE_cart_test

rsquared_cart <- (1 - ( (RMSE_cart_test ^ 2)  / var(testset$MUDLOSSU) ) )
rsquared_cart

# using python script to find the best hyper parameters. refer to WANG JIANAN CBA_para_select_cart.py
cart3 <- rpart(MUDLOSSU ~ . , data = trainset, method = 'anova', control = rpart.control(minsplit = 38, minbucket = 7, maxdepth = 6))
plotcp(cart3)
print(cart3)
rpart.plot(cart3, type = 5)

# calculated the percentage variable importance of pre-purned CART model
cart3$variable.importance
cart3_variableImportanceNoSacle <- cart3$variable.importance
cart3_variableImportanceSacle <- (cart3_variableImportanceNoSacle / sum(cart3_variableImportanceNoSacle))
round(cart3_variableImportanceSacle * 100)

# calculate RMSE
RMSE_cart_train_tune <- sqrt(mean(residuals(cart3)^2))
RMSE_cart_train_tune

cart_yhat_tune <- predict(cart3, newdata = testset)

RMSE_cart_test_tune <- round(sqrt(mean((testset$MUDLOSSU - cart_yhat_tune)^2)), 3)
RMSE_cart_test_tune

tss <- sum((testset$MUDLOSSU - mean(testset$MUDLOSSU))^2)
rss <- sum((testset$MUDLOSSU - cart_yhat_tune)^2)
rsquared <- 1 - (rss / tss)
rsquared

rsquared_cart_tune <- (1 - ( (RMSE_cart_test_tune ^ 2)  / var(testset$MUDLOSSU) ) )
rsquared_cart_tune

# Random Forest
# ----------
RF <- randomForest(MUDLOSSU ~ ., data=trainset, ntree=2000, importance = T)
RF
plot(RF)
RMSE.RF <- sqrt(RF$mse[RF$ntree])
RMSE.RF

RF.yhat <- predict(RF, newdata = testset)
RMSE.test.RF <- round(sqrt(mean((testset$MUDLOSSU - RF.yhat)^2)), 3)
RMSE.test.RF

rsquared <- (1 - ( (RMSE.test.RF ^ 2)  / var(testset$MUDLOSSU) ) )
rsquared

var.impt <- importance(RF)
varImpPlot(RF, type = 1)
RF$importance
