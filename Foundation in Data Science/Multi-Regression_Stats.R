econ <- read.csv("D:/RU/Fall 2021/GradCourses/Foundation in Data Science/Module 15/Final Project/Data.csv")

econs <- as.data.frame(econ)

colnames(econs)<-c("year", "inflation", "unemployment", "real_interest_rate")
names(econs)

regstats <- lm(formula = real_interest_rate ~ unemployment + inflation,
               data = econs)
summary(regstats)
