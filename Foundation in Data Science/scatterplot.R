econ <- read.csv("D:/RU/Fall 2021/GradCourses/Foundation in Data Science/Module 15/Final Project/Data.csv")

econs <- as.data.frame(econ)

colnames(econs)<-c("year", "inflation", "unemployment", "real_interest_rate")

regstats <- lm(formula = real_interest_rate ~ inflation + unemployment,
               data = econs)
summary(regstats)



scatterplot <- plot(econs$real_interest_rate, econs$unemployment,
                    main = "Impact of Real Interest Rate on Unemployment Rate",
                    xlab = "Real Interest Rate",
                    ylab = "Unemployment",
                    xlim = c(0,8),
                    ylim = c(0,11),
                    pch=19, col = "orange",
                    cex=2.5)

abline(regstats)

text(econs$real_interest_rate, econs$unemployment, econs$year, pos = 3,
     cex = 1.5)






