setwd("/Users/jiananwang/ob_library/StoriesofYourLifeandOthers/Others/MediaNote/DocumentNote/AC6006 Course Materials/Gender Discrimination Lawsuit Activity")
set.seed(6006)

library(data.table)
library(rpart)
library(rpart.plot)
library(car)
library(nnet)

LsDataTable <- fread("Lawsuit.csv")

# a new column is created to see if the change of the salary is also free of gender bias
LsDataTable[, `:=`(increase9495 = Sal95 - Sal94)]

# data is quite clean
sum(is.na(LsDataTable))
summary(LsDataTable)

LsDataTable$Dept <- factor(LsDataTable$Dept, levels = c(1, 2, 3, 4, 5, 6))
LsDataTable$Gender <- factor(LsDataTable$Gender, levels = c(0, 1))
LsDataTable$Clin <- factor(LsDataTable$Clin, levels = c(0, 1))
LsDataTable$Cert <- factor(LsDataTable$Cert, levels = c(0, 1))
LsDataTable$Rank <- factor(LsDataTable$Rank, levels = c(1, 2, 3))

# LGR modeling ------------------------------------------------------------------
LGR_rank_full <- multinom(Rank ~ Dept + Gender + Clin + Cert + Prate + Exper, data = LsDataTable)
summary(LGR_rank_full)

OR_LGR_rank_full <- exp(coef(LGR_rank_full))
OR_LGR_rank_full
OR_CI_LGR_rank_full <- exp(confint(LGR_rank_full))
OR_CI_LGR_rank_full

LGR_rank_full_cut <- multinom(Rank ~ Gender + Exper + Cert, data = LsDataTable)
summary(LGR_rank_full_cut)

OR_LGR_rank_full_cut <- exp(coef(LGR_rank_full_cut))
OR_LGR_rank_full_cut
OR_CI_LGR_rank_full_cut <- exp(confint(LGR_rank_full_cut))
OR_CI_LGR_rank_full_cut

# classification tree ------------------------------------------------------------------
CART_rank_full <- rpart(Rank ~ Dept + Gender + Clin + Cert + Prate + Exper, data = LsDataTable, 
                        method = 'class',
                        control = rpart.control(minsplit = 2, cp = 0))
printcp(CART_rank_full)
plotcp(CART_rank_full)
variableImportanceNoSacle <- CART_rank_full$variable.importance
variableImportanceSacle <- (variableImportanceNoSacle / sum(variableImportanceNoSacle))
round(variableImportanceSacle*100, 0)

CVerror.cap <- CART_rank_full$cptable[which.min(CART_rank_full$cptable[,"xerror"]), "xerror"] + CART_rank_full$cptable[which.min(CART_rank_full$cptable[,"xerror"]), "xstd"]
i <- 1; j<- 4
while (CART_rank_full$cptable[i,j] > CVerror.cap) {i <- i + 1}
cp.opt_rank = ifelse(i > 1, sqrt(CART_rank_full$cptable[i,1] * CART_rank_full$cptable[i-1,1]), 1)

CART_rank_full_prune <- prune(CART_rank_full, cp = cp.opt_rank)
printcp(CART_rank_full_prune)
rpart.plot(CART_rank_full_prune)
variableImportanceNoSacle <- CART_rank_full_prune$variable.importance
variableImportanceSacle <- (variableImportanceNoSacle / sum(variableImportanceNoSacle))
round(variableImportanceSacle*100, 0)

summary(CART_rank_full_prune)

# gender and expir are closing related as more male has longer experience
# so that gender could be a good substituent for experience in classification

