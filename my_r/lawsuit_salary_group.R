setwd("/Users/jiananwang/ob_library/StoriesofYourLifeandOthers/Others/MediaNote/DocumentNote/AC6006 Course Materials/Gender Discrimination Lawsuit Activity")
set.seed(6006)

library(data.table)
library(rpart)
library(car)

LsDataTable <- fread("Lawsuit.csv")

# a new column is created to see if the change of the salary is also free of gender bias
LsDataTable[, `:=`(increase9495 = Sal95 - Sal94)]

# data is quite clean
sum(is.na(LsDataTable))

LsDataTable$Dept <- factor(LsDataTable$Dept, levels = c(1, 2, 3, 4, 5, 6))
LsDataTable$Gender <- factor(LsDataTable$Gender, levels = c(0, 1))
LsDataTable$Clin <- factor(LsDataTable$Clin, levels = c(0, 1))
LsDataTable$Cert <- factor(LsDataTable$Cert, levels = c(0, 1))
LsDataTable$Rank <- factor(LsDataTable$Rank, levels = c(1, 2, 3))

# Linear Regression for Salary94 ------------------------------------------------------------------------
LR_Sal94_full <- lm(Sal94 ~ Dept + Gender + Clin + Cert + Prate + Exper + Rank, data = LsDataTable)
summary(LR_Sal94_full)
par(mfrow = c(2,2))
plot(LR_Sal94_full)
par(mfrow = c(1,1))

# try step function
LR_Sal94_full_step <- step(LR_Sal94_full)
summary(LR_Sal94_full_step)
# Gender Variable is the very first variable got eliminated
# step stops when removing the next variabel will no longer reduce the AIC
# which means the reword of adding it to the model is not worth for the increase of likelyhood

# exam the multicollinearity so that the coefficient are more meaningful
vif(LR_Sal94_full)
# Prate get about 16.62605 GVIF, which means the R^2 is around 0.93985, very high, remove

LR_Sal94_full_vif1 <- lm(Sal94 ~ Dept + Gender + Clin + Cert + Exper + Rank, data = LsDataTable)
vif(LR_Sal94_full_vif1)
# after remove Prate, the GVIF of all the remaining are acceptable
summary(LR_Sal94_full_vif1)

# Linear Regression for Salary95 ------------------------------------------------------------------------
LR_Sal95_full <- lm(Sal95 ~ Dept + Gender + Clin + Cert + Prate + Exper + Rank, data = LsDataTable)
summary(LR_Sal95_full)
par(mfrow = c(2,2))
plot(LR_Sal95_full)
par(mfrow = c(1,1))

LR_Sal95_full_step <- step(LR_Sal95_full)
summary(LR_Sal95_full_step)

vif(LR_Sal95_full)

LR_Sal95_full_vif1 <- lm(Sal95 ~ Dept + Gender + Clin + Cert + Exper + Rank, data = LsDataTable)
vif(LR_Sal95_full_vif1)

summary(LR_Sal95_full_vif1)

# Linear Regression for salary increase ------------------------------------------------------------------------
LR_increase9495_full <- lm(increase9495 ~ Dept + Gender + Clin + Cert + Prate + Exper + Rank, data = LsDataTable)
summary(LR_increase9495_full)
par(mfrow = c(2,2))
plot(LR_increase9495_full)
par(mfrow = c(1,1))


LR_increase9495_full_step <- step(LR_increase9495_full)
summary(LR_increase9495_full_step)

vif(LR_increase9495_full)


LR_increase9495_full_vif1 <- lm(increase9495 ~ Dept + Gender + Clin + Cert + Exper + Rank, data = LsDataTable)
vif(LR_increase9495_full_vif1)
summary(LR_increase9495_full_vif1)

# Tree for Salary94------------------------------------------------------------------------
CART_Sal94_full <- rpart(Sal94 ~ Dept + Gender + Clin + Cert + Prate + Exper + Rank, data = LsDataTable, method = 'anova', control = rpart.control(minsplit = 2, cp = 0))

variableImportanceNoSacle <- CART_Sal94_full$variable.importance
variableImportanceSacle <- (variableImportanceNoSacle / sum(variableImportanceNoSacle))
round(variableImportanceSacle*100, 0)

printcp(CART_Sal94_full)
plotcp(CART_Sal94_full)
# eyesight not good enough

# prune the tree
# get the optimal cp
CVerror.cap <- CART_Sal94_full$cptable[which.min(CART_Sal94_full$cptable[,"xerror"]), "xerror"] + CART_Sal94_full$cptable[which.min(CART_Sal94_full$cptable[,"xerror"]), "xstd"]
# Find the optimal CP region whose CV error is just below CVerror.cap in maximal tree CART_Sal94_full.
i <- 1; j<- 4
while (CART_Sal94_full$cptable[i,j] > CVerror.cap) {i <- i + 1}
# Get geometric mean of the two identified CP values in the optimal region if optimal tree has at least one split.
cp.opt_94 = ifelse(i > 1, sqrt(CART_Sal94_full$cptable[i,1] * CART_Sal94_full$cptable[i-1,1]), 1)
# actual prune
CART_Sal94_full_prune <- prune(CART_Sal94_full, cp = cp.opt_94)
printcp(CART_Sal94_full_prune)
# gender variable is not even used in building the tree
print(CART_Sal94_full_prune)
rpart.plot(CART_Sal94_full_prune, nn = T, main = "Optimal Tree in Sal94")

variableImportanceNoSacle <- CART_Sal94_full_prune$variable.importance
variableImportanceSacle <- (variableImportanceNoSacle / sum(variableImportanceNoSacle))
round(variableImportanceSacle*100, 0)

summary(CART_Sal94_full_prune)
# Questions: why the tree itself is constructed only using Dept, Prate, and Exper, why it would have feature importance for Gender, Rank, Clin...?
# one possible reason is that the feature importance also consider the Surrogate, which is calcualted even though not used.

# Tree for Salary95------------------------------------------------------------------------
CART_Sal95_full <- rpart(Sal95 ~ Dept + Gender + Clin + Cert + Prate + Exper + Rank, data = LsDataTable, method = 'anova', control = rpart.control(minsplit = 2, cp = 0))

variableImportanceNoSacle <- CART_Sal95_full$variable.importance
variableImportanceSacle <- (variableImportanceNoSacle / sum(variableImportanceNoSacle))
round(variableImportanceSacle*100, 0)

printcp(CART_Sal95_full)
plotcp(CART_Sal95_full)

CVerror.cap <- CART_Sal95_full$cptable[which.min(CART_Sal95_full$cptable[,"xerror"]), "xerror"] + CART_Sal95_full$cptable[which.min(CART_Sal95_full$cptable[,"xerror"]), "xstd"]
i <- 1; j<- 4
while (CART_Sal95_full$cptable[i,j] > CVerror.cap) {i <- i + 1}
cp.opt_95 = ifelse(i > 1, sqrt(CART_Sal95_full$cptable[i,1] * CART_Sal95_full$cptable[i-1,1]), 1)

CART_Sal95_full_prune <- prune(CART_Sal95_full, cp = cp.opt_95)
printcp(CART_Sal95_full_prune)

print(CART_Sal95_full_prune)
rpart.plot(CART_Sal95_full_prune, nn = T, main = "Optimal Tree in Sal95")

variableImportanceNoSacle <- CART_Sal95_full_prune$variable.importance
variableImportanceSacle <- (variableImportanceNoSacle / sum(variableImportanceNoSacle))
round(variableImportanceSacle*100, 0)

summary(CART_Sal95_full_prune)

# Tree for increase9495------------------------------------------------------------------------
CART_increase9495_full <- rpart(increase9495 ~ Dept + Gender + Clin + Cert + Prate + Exper + Rank, data = LsDataTable, method = 'anova', control = rpart.control(minsplit = 2, cp = 0))

variableImportanceNoSacle <- CART_increase9495_full$variable.importance
variableImportanceSacle <- (variableImportanceNoSacle / sum(variableImportanceNoSacle))
round(variableImportanceSacle*100, 0)

printcp(CART_increase9495_full)
plotcp(CART_increase9495_full)

CVerror.cap <- CART_increase9495_full$cptable[which.min(CART_increase9495_full$cptable[,"xerror"]), "xerror"] + CART_increase9495_full$cptable[which.min(CART_increase9495_full$cptable[,"xerror"]), "xstd"]
i <- 1; j<- 4
while (CART_increase9495_full$cptable[i,j] > CVerror.cap) {i <- i + 1}
cp.opt_95 = ifelse(i > 1, sqrt(CART_increase9495_full$cptable[i,1] * CART_increase9495_full$cptable[i-1,1]), 1)

CART_increase9495_full_prune <- prune(CART_increase9495_full, cp = cp.opt_95)
printcp(CART_increase9495_full_prune)

print(CART_increase9495_full_prune)
rpart.plot(CART_increase9495_full_prune, nn = T, main = "Optimal Tree in increase9495")

variableImportanceNoSacle <- CART_increase9495_full_prune$variable.importance
variableImportanceSacle <- (variableImportanceNoSacle / sum(variableImportanceNoSacle))
round(variableImportanceSacle*100, 0)

summary(CART_increase9495_full_prune)
