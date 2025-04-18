
library(MASS)

#Correlation Matrix
cor_matrix <- matrix(c(
  1,  0.5, -0.3, -0.4,  # Heart Rate
  0.5,  1, -0.4, -0.5,  # Reaction Time
  -0.3, -0.4,  1,  0.3,  # Swing Speed
  -0.4, -0.5,  0.3,  1   # Grip Pressure
), nrow = 4, ncol = 4)

# Means and standard deviations for the features
means <- c(120, 480, 30, 30) 
sds <- c(20, 50, 5, 10)    

# Making 500 observations
data <- mvrnorm(n = 500, mu = means, Sigma = diag(sds) %*% cor_matrix %*% diag(sds))

# data frame
batting_data <- data.frame(
  Heart_Rate = data[, 1],        
  Reaction_Time = data[, 2],      
  Swing_Speed = data[, 3],      
  Grip_Pressure = data[, 4]     
)

# Keeping feature within realistic ranges
batting_data$Heart_Rate <- pmax(pmin(batting_data$Heart_Rate, 180), 70)
batting_data$Reaction_Time <- pmax(pmin(batting_data$Reaction_Time, 700), 400)
batting_data$Swing_Speed <- pmax(pmin(batting_data$Swing_Speed, 40), 20)
batting_data$Grip_Pressure <- pmax(pmin(batting_data$Grip_Pressure, 50), 10)

write.csv(batting_data, "batting_data.csv", row.names = FALSE)
head(batting_data)

