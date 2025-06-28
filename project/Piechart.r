library("ggplot")
percentage<-c(20, 18, 15, 12, 10, 8, 7, 5,2,1)
skill<-c("Generative AI", "Big Data Analysis", "Software Development", "UX Design", "Cybersecurity", "Cloud Computing", "Digital Marketing", "Leadership&Management","CriticalThinking","Healthcare")
colors<-c("purple","red","blue","green","yellow","skyblue","brown","grey","pink","skyblue")
pie(percentage,skill,r=1.1,main="In-demand skills for 2025",col=colors,clockwise=TRUE)
legend("topright",skill,cex=0.5,fill=colors)



