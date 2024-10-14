
5. The following table shows the time taken (in minutes) by 100 students to travel to school on a particular day.
Time
0-5
No. of students 5
5-10
10-15
25
40
15-20 17
20-25 13
a. Draw the histogram
b. Draw frequency polygon
xlp<-c(0,5,10,15,20)
xup<-c(5,10,15,20,25)
NumStudents = c(5, 25, 40, 17, 30) midpoints <- c(2.5, 7.5, 12.5, 17.5, 22.5) barplot(NumStudents, width=xup-xlp,space=0, col = "blue",
xlab="Time Interval (minutes)", ylab="Number of Students",
main = "Histogram of Time Taken by Students")
lbls <- sort(union(xlp, xup))
axis(1, labels = lbls, at = lbls, las = 2)
plot(midpoints, NumStudents, type = "b", pch = 19,
col = "red",
xlab="Time Interval (minutes)",
ylab="Number of Students",
main= "Frequency Polygon of Time Taken by Students")


Exp. (Rs. In
Lakhs)
Sales Volume 50
(Rs. In Lakhs)
R Script:
2. Write R script to find the correlation coefficient and type of correlation between advertisement expenses and sales volume using Karl Pearson's coefficient of correlation method (Direct
Method).
Firm
12 3 4 5 6 7
8 9 10
1
Advertisement 11 13 14
18
16 16 15
15
14 13 13
590
55
55
60
60
65
65
65
65
65
65
60
69
60
60
advert_expenses <- c(11, 13, 14, 16, 16, 15, 15, 14, 13, 13) s
ales_volume <- c(50, 50, 55, 60, 65, 65, 65, 60, 60, 50)
correlation coefficient <- cor(advert_expenses, sales_volume, method = "pearson") 
if (correlation coefficient > 0)
{
correlation_type <- "Positive Correlation"
}else if (correlation coefficient < 0) {
correlation_type <- "Negative Correlation"
}else {
}
correlation_type <- "No Correlation"
cat("Pearson Correlation Coefficient:", correlation_coefficient, "\n") cat("Type of Correlation:", correlation_type, "\n")
50
50