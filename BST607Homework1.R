#Problem 1
SumSqNo3 <- function(n) {
  if (n>0) {
    numbers <- 1:n
    numbers_not3 <- numbers[numbers %% 3 != 0]
    sumofsquares <- sum(numbers_not3^2)
    return(sumofsquares)
    }
}
SumSqNo3(3) # =5
SumSqNo3(8) # =159
SumSqNo3(52) # =32165
SumSqNo3(1024) # =238959161


#Problem 2
#Part a
k <- c(1:120)
x <- cos(k)
x

#Part b
y <- if (x < -0.25) {
  "L"
} else if (x>=-0.25 || x<=0.25) {
  "M"
} else {
  "H"
}
print(y)

#Part C
length(y=="M")
#120 elements are equal to M


#Problem 3

DaysFromYearStart <- function(dates, format="MonthsFirst") {
  days_in_month <- c(31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
  
  calculate_days <- function(month, day) {
    return(sum(days_in_month[0:(month-1)]) + day)
  }
  result <- numeric(length(dates))
  
  for (i in 1:length(dates)) {
    xx <- as.numeric(substr(dates[i], 1, 2))
    yy <- as.numeric(substr(dates[i], 4, 5))
    
    if (format == "MonthsFirst") {
      month <- xx
      day <- yy
    } else if (format == "DatesFirst") {
      month <- yy
      day <- xx
    } 
    result[i] <- calculate_days(month, day)
  }
  
  return(result)
}


DaysFromYearStart(dates=c("01-23", "03-30", "10-12", "12-31") )
DaysFromYearStart(dates=c("13-01", "30-04", "12-08", "31-12"),
                  format="DatesFirst")                  

DaysFromYearStart(dates=c("06-06"))
# = 157
DaysFromYearStart(dates=c("05-18", "07-01", "04-11"))
# = 138, 182, 101

DaysFromYearStart(dates=c("18-05", "01-07", "11-04"), format="DatesFirst")
# = 138, 182, 101

DaysFromYearStart(dates=c("04-11", "02-19", "11-09", "12-02", "12-24"),
                  format="MonthsFirst")
# = 101, 50, 313, 336, 358

DaysFromYearStart(dates=c("28-03", "30-11", "07-06", "21-10", "10-03"),
                  format="DatesFirst")                  
# = 87, 334, 158, 294, 69