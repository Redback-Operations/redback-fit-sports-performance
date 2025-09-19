data <- read.csv("ImprovedData.csv")
head(data)
str(data)

library(dplyr)

# Check for duplicate names and name counts
name_counts <- data %>%
  count(Name, sort = TRUE) %>%
  rename(Count = n)
head(name_counts, 15)  # Shows top 15 most frequent names

loc_counts <- data %>%
  count(Location, sort = TRUE) %>%
  rename(Count = n)
head(loc_counts)

library(ggplot2)
# Visualisation for location counts
top_locations <- loc_counts %>% 
  top_n(8, Count)

ggplot(top_locations, aes(x = reorder(Location, Count), y = Count, fill = Count)) +
  geom_bar(stat = "identity") +
  geom_text(aes(label = Count), hjust = -0.3, size = 3) +
  labs(title = "Location Frequency",
       x = "Location",
       y = "Count") +
  coord_flip() +
  scale_fill_viridis_c(option = "plasma", direction = -1) +
  theme_minimal() +
  theme(plot.title = element_text(hjust = 0.5, face = "bold"),
        legend.position = "right")  # Position legend on the right

# Calculate the new composite variables
ImprovedData <- data %>%
  mutate(
    # Total minutes across all activity levels
    Total_minutes = Very_Active_Minutes + Fairly_Active_Minutes + 
      Lightly_Active_Minutes + Sedentary_Minutes,
    
    # Percentage of active minutes (non-sedentary)
    Active_minutes_pct = (Total_minutes - Sedentary_Minutes) / Total_minutes * 100,
    
    # Percentage of active distance (non-sedentary)
    Active_distance_pct = (Total_Distance - Sedentary_Active_Distance) / Total_Distance * 100,
    
    # Additional suggested metrics:
    # Intensity ratio (vigorous to moderate activity)
    Intensity_ratio = Very_Active_Minutes / (Fairly_Active_Minutes + 0.01), # +0.01 to avoid division by zero
    
    # Steps per minute ratio
    Steps_per_minute = Steps / (Total_minutes - Sedentary_Minutes + 0.01),
    
    # Calories per active minute
    Calories_per_active_min = Calories_Burned / (Total_minutes - Sedentary_Minutes + 0.01)
  )

# Handle potential infinite/NA values from divisions
ImprovedData <- ImprovedData %>%
  mutate(across(where(is.numeric), ~ ifelse(is.infinite(.) | is.nan(.), NA, .)))

# Summary statistics of key activity metrics
activity_summary <- ImprovedData %>%
  select(Total_Distance, Total_minutes, Active_minutes_pct, 
         Active_distance_pct, Steps, Calories_Burned) %>%
  summary()

# View the summary
activity_summary

library(ggplot2)
library(tidyr)

# Reshape data for visualization
activity_long <- ImprovedData %>%
  select(Very_Active_Minutes, Fairly_Active_Minutes, 
         Lightly_Active_Minutes, Sedentary_Minutes) %>%
  pivot_longer(everything(), names_to = "Activity_Level", values_to = "Minutes")

# Plot activity time distribution
ggplot(activity_long, aes(x = reorder(Activity_Level, -Minutes), y = Minutes, fill = Activity_Level)) +
  geom_boxplot() +
  scale_fill_brewer(palette = "Set2") +
  labs(title = "Distribution of Activity Time by Intensity Level",
       x = "Activity Intensity",
       y = "Total Minutes") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

library(corrplot)

# Select numeric activity columns
activity_corr <- ImprovedData %>%
  select(Total_Distance, Very_Active_Distance, Moderately_Active_Distance,
         Light_Active_Distance, Very_Active_Minutes, Fairly_Active_Minutes,
         Lightly_Active_Minutes, Steps, Calories_Burned) %>%
  cor(use = "complete.obs")

# Visualize correlation matrix
corrplot(activity_corr, method = "color", type = "upper",
         tl.col = "black", tl.srt = 45,
         addCoef.col = "black", number.cex = 0.7)

# Create activity profiles based on behavior patterns
ImprovedData <- ImprovedData %>%
  mutate(
    Activity_Profile = case_when(
      Very_Active_Minutes > 60 ~ "Highly Active",
      Fairly_Active_Minutes > 30 ~ "Moderately Active",
      Lightly_Active_Minutes > 120 ~ "Lightly Active",
      Sedentary_Minutes > 600 ~ "Sedentary",
      TRUE ~ "Balanced"
    ),
    Activity_Profile = factor(Activity_Profile,
                              levels = c("Highly Active", "Moderately Active",
                                         "Balanced", "Lightly Active", "Sedentary"))
  )

# Visualize the activity profiles
ggplot(ImprovedData, aes(x = Activity_Profile, fill = Activity_Profile)) +
  geom_bar() +
  geom_text(stat = 'count', aes(label = ..count..), vjust = -0.5) +
  scale_fill_brewer(palette = "Set1") +
  labs(title = "Distribution of Activity Profiles",
       x = "Activity Profile",
       y = "Count") +
  theme_minimal()

########################################################
####Data Preparation & Enhanced Feature Engineering#####
########################################################
# Create more sophisticated activity metrics
ImprovedData <- ImprovedData %>% 
  mutate(
    # Activity Time Metrics
    Total_active_minutes = Very_Active_Minutes + Fairly_Active_Minutes + Lightly_Active_Minutes,
    Vigorous_vs_Total = Very_Active_Minutes / (Total_active_minutes + 0.01),
    
    # Movement Efficiency Metrics
    Distance_per_step = Total_Distance / (Steps + 1),
    Caloric_efficiency = Calories_Burned / (Total_active_minutes + 1),
    
    # Activity Balance Scores
    Activity_balance = (Very_Active_Minutes*2 + Fairly_Active_Minutes*1.5 + 
                          Lightly_Active_Minutes) / (Sedentary_Minutes + 0.01),
    
    # Time Allocation Ratios
    Sedentary_ratio = Sedentary_Minutes / Total_minutes,
    MVPA_ratio = (Very_Active_Minutes + Fairly_Active_Minutes) / Total_minutes
  ) %>%
  # Handle potential infinite/NA values
  mutate(across(where(is.numeric), ~ ifelse(is.infinite(.) | is.nan(.), NA, .)))

## Data quality check
# Comprehensive summary of all activity metrics
activity_summary <- ImprovedData %>%
  select(contains("Active"), Steps, Calories_Burned, contains("pct"), contains("ratio")) %>%
  psych::describe(quant = c(.25, .75)) %>%
  as.data.frame() %>%
  tibble::rownames_to_column("Metric")

View(activity_summary)

# Check missing values pattern
visdat::vis_miss(ImprovedData)


# Handle any remaining missing values
ImprovedData <- na.omit(ImprovedData)

# Verify Activity_Profile factor levels
ImprovedData$Activity_Profile <- factor(ImprovedData$Activity_Profile,
                                        levels = c("Highly Active", "Moderately Active",
                                                   "Balanced", "Lightly Active", "Sedentary"))

# Create a simplified cluster variable if needed
ImprovedData <- ImprovedData %>%
  mutate(Activity_Simple = case_when(
    Very_Active_Minutes > 30 ~ "Active",
    Fairly_Active_Minutes > 20 ~ "Moderate",
    Lightly_Active_Minutes > 180 ~ "Light",
    TRUE ~ "Sedentary"
  ))

# Activity Profile Distribution
ggplot(ImprovedData, aes(x = Activity_Profile, fill = Activity_Profile)) +
  geom_bar() +
  geom_text(stat = 'count', aes(label = ..count..), vjust = -0.5) +
  scale_fill_brewer(palette = "Set1") +
  labs(title = "Distribution of Activity Profiles",
       x = "Activity Profile",
       y = "Count") +
  theme_minimal()

# Activity Minutes Composition
library(reshape2)
activity_melt <- melt(ImprovedData, 
                      id.vars = "UserID",
                      measure.vars = c("Very_Active_Minutes", 
                                       "Fairly_Active_Minutes",
                                       "Lightly_Active_Minutes"))

ggplot(activity_melt, aes(x = variable, y = value, fill = variable)) +
  geom_boxplot() +
  scale_fill_brewer(palette = "Set2") +
  labs(title = "Distribution of Activity Minutes by Intensity",
       x = "Activity Level",
       y = "Minutes") +
  theme_minimal() +
  coord_flip()

# Steps vs. Calories by Activity Profile
ggplot(ImprovedData, aes(x = Steps, y = Calories_Burned, color = Activity_Profile)) +
  geom_point(alpha = 0.6) +
  geom_smooth(method = "lm", se = FALSE) +
  scale_color_brewer(palette = "Set1") +
  labs(title = "Steps vs Calories Burned by Activity Profile",
       x = "Daily Steps",
       y = "Calories Burned") +
  theme_minimal()

#############################################
########### Advanced Analysis ###############
#############################################

# Correlation Heatmap
library(corrplot)

activity_cor <- ImprovedData %>%
  select(Total_Distance, Very_Active_Minutes, Fairly_Active_Minutes,
         Lightly_Active_Minutes, Steps, Calories_Burned) %>%
  cor()

corrplot(activity_cor, method = "color", type = "upper",
         tl.col = "black", tl.srt = 45,
         addCoef.col = "black", number.cex = 0.7,
         title = "Activity Metrics Correlation")

# Sedentary Behavior Analysis
ggplot(ImprovedData, aes(x = Sedentary_ratio)) +
  geom_histogram(binwidth = 0.05, fill = "steelblue", color = "white") +
  geom_vline(xintercept = mean(ImprovedData$Sedentary_ratio), 
             color = "red", linetype = "dashed") +
  labs(title = "Distribution of Sedentary Time Ratio",
       x = "Proportion of Sedentary Time",
       y = "Count") +
  theme_minimal()


################################
### Statistical Comparisons ####
################################

# ANOVA Across Activity Profiles
# Compare means across groups
aov_steps <- aov(Steps ~ Activity_Profile, data = ImprovedData)
summary(aov_steps)

# Post-hoc tests
TukeyHSD(aov_steps) 

# Activity Profile Characteristics
ImprovedData %>%
  group_by(Activity_Profile) %>%
  summarise(
    Avg_Steps = mean(Steps),
    Avg_Calories = mean(Calories_Burned),
    Avg_Sedentary = mean(Sedentary_ratio),
    Avg_MVPA = mean(MVPA_ratio),
    n = n()
  ) %>%
  knitr::kable(digits = 2)

# Maintenance & Optimization
recommendations_high <- list(
  strategy = "Maintain excellence with intensity variation",
  actions = c(
    "Incorporate cross-training to prevent overuse injuries",
    "Focus on recovery and sleep quality",
    "Consider adding strength training if primarily cardio-based"
  ),
  metrics = c("Maintain MVPA ratio > 0.08", "Target 14,000+ steps daily")
)

# Progression to Highly Active
recommendations_moderate <- list(
  strategy = "Bridge to highly active category",
  actions = c(
    "Increase vigorous activity by 15 minutes daily",
    "Add one high-intensity session weekly",
    "Focus on step count consistency"
  ),
  metrics = c("Target 12,000 steps", "Increase MVPA ratio to 0.09")
)

# Biggest opportunity for impact
recommendations_light <- list(
  strategy = "From light to moderate activity",
  actions = c(
    "Implement walking meetings/movement breaks",
    "Set gradual step increase goals (+500 steps weekly)",
    "Reduce sedentary time by standing hourly"
  ),
  metrics = c("Reach 8,500 steps", "Reduce sedentary ratio to 0.72")
)

# Critical intervention needed
recommendations_sedentary <- list(
  strategy = "Break sedentary patterns",
  actions = c(
    "Start with 5-minute movement breaks every hour",
    "Focus on standing time before increasing steps",
    "Set micro-goals (e.g., 100 extra steps daily)"
  ),
  metrics = c("Reduce sedentary ratio to 0.85", "Achieve 4,000 steps daily")
)


# Investigate and re-evaluate
recommendations_balanced <- list(
  strategy = "Data quality investigation",
  actions = c(
    "Verify device usage and data collection",
    "Consider alternative activity metrics",
    "Personalized assessment needed"
  ),
  metrics = c("Validate data quality", "Individual assessment")
)

priority_matrix <- data.frame(
  Profile = c("Sedentary", "Lightly Active", "Moderately Active", "Highly Active", "Balanced"),
  Population_Size = c(114, 513, 108, 112, 15),
  Health_Risk = c("High", "Medium", "Low", "Very Low", "Unknown"),
  Intervention_Priority = c(1, 2, 3, 4, 5),
  Expected_Impact = c("High", "High", "Medium", "Low", "Unknown")
)
print(priority_matrix)

quick_wins <- list(
  Sedentary = "10-minute daily walking routine",
  Lightly_Active = "30-minute lunch walk",
  Moderately_Active = "2 weekly intensity sessions",
  Highly_Active = "Recovery optimization",
  Balanced = "Data validation check"
)

## Geography demographic analysis
# First, verify the states present in your data
location_summary <- ImprovedData %>%
  count(Location, sort = TRUE) %>%
  mutate(Percentage = n / nrow(ImprovedData) * 100)

print(location_summary)

# Check if we have all 7 states + any unexpected values
unique(ImprovedData$Location)

# Summary statistics by location
location_activity <- ImprovedData %>%
  group_by(Location) %>%
  summarise(
    n_users = n(),
    Avg_Steps = mean(Steps, na.rm = TRUE),
    Avg_Calories = mean(Calories_Burned, na.rm = TRUE),
    Avg_Total_Minutes = mean(Total_active_minutes, na.rm = TRUE),
    Avg_Sedentary_Ratio = mean(Sedentary_ratio, na.rm = TRUE),
    Avg_MVPA_Ratio = mean(MVPA_ratio, na.rm = TRUE),
    .groups = 'drop'
  ) %>%
  arrange(desc(Avg_Steps))

print(location_activity)

# Visualisation
ggplot(ImprovedData, aes(x = reorder(Location, Steps, FUN = median), y = Steps)) +
  geom_boxplot(aes(fill = Location), alpha = 0.7) +
  stat_summary(fun = mean, geom = "point", shape = 18, size = 3, color = "red") +
  labs(title = "Step Count Distribution by Australian State",
       x = "State/Territory",
       y = "Daily Steps") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1)) +
  scale_fill_brewer(palette = "Set3")

# Activity profile proportions by state
activity_by_location <- ImprovedData %>%
  count(Location, Activity_Profile) %>%
  group_by(Location) %>%
  mutate(Percentage = n / sum(n) * 100)

ggplot(activity_by_location, aes(x = Location, y = Percentage, fill = Activity_Profile)) +
  geom_bar(stat = "identity", position = "fill") +
  scale_fill_brewer(palette = "Set1") +
  labs(title = "Activity Profile Distribution by State",
       x = "State/Territory",
       y = "Proportion",
       fill = "Activity Profile") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

# Test if step differences by location are statistically significant
aov_location_steps <- aov(Steps ~ Location, data = ImprovedData)
summary(aov_location_steps)

# Post-hoc test to see which states differ
if(summary(aov_location_steps)[[1]]$'Pr(>F)'[1] < 0.05) {
  tukey_location <- TukeyHSD(aov_location_steps)
  print(tukey_location)
}

## Sedentary behaviour across states
ggplot(ImprovedData, aes(x = Location, y = Sedentary_ratio, fill = Location)) +
  geom_violin(alpha = 0.7) +
  geom_boxplot(width = 0.1, fill = "white") +
  labs(title = "Sedentary Time Ratio by State",
       x = "State/Territory",
       y = "Proportion of Sedentary Time") +
  theme_minimal() +
  scale_fill_brewer(palette = "Pastel1")

library(corrplot)

# Create correlation matrix by location
location_correlations <- ImprovedData %>%
  group_by(Location) %>%
  summarise(
    Steps_Calories_Cor = cor(Steps, Calories_Burned, use = "complete.obs"),
    Active_Sedentary_Cor = cor(Total_active_minutes, Sedentary_Minutes, use = "complete.obs"),
    MVPA_Steps_Cor = cor(MVPA_ratio, Steps, use = "complete.obs")
  )

print(location_correlations)

# Compare vigorous activity patterns
intensity_by_location <- ImprovedData %>%
  group_by(Location) %>%
  summarise(
    Vigorous_Minutes = mean(Very_Active_Minutes),
    Moderate_Minutes = mean(Fairly_Active_Minutes),
    Light_Minutes = mean(Lightly_Active_Minutes)
  ) %>%
  pivot_longer(cols = -Location, names_to = "Intensity", values_to = "Minutes")

ggplot(intensity_by_location, aes(x = Location, y = Minutes, fill = Intensity)) +
  geom_bar(stat = "identity", position = "dodge") +
  labs(title = "Average Activity Intensity Minutes by State",
       x = "State/Territory",
       y = "Minutes",
       fill = "Intensity Level") +
  theme_minimal() +
  scale_fill_brewer(palette = "Set2") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

# Add population density context (approximate values)
population_density <- data.frame(
  Location = c("ACT", "NSW", "NT", "QLD", "SA", "TAS", "VIC", "WA"),
  Pop_Density = c(171, 9.6, 0.2, 2.8, 1.7, 7.6, 27, 1.0) # persons per km²
)

# Merge with activity data
location_analysis <- location_activity %>%
  left_join(population_density, by = "Location")

# Check correlation with population density
ggplot(location_analysis, aes(x = Pop_Density, y = Avg_Steps)) +
  geom_point(aes(size = n_users, color = Location), alpha = 0.7) +
  geom_smooth(method = "lm", se = FALSE) +
  geom_text(aes(label = Location), vjust = -0.5, hjust = 0.5) +
  labs(title = "Activity vs Population Density by Australian State",
       x = "Population Density (persons/km²)",
       y = "Average Daily Steps") +
  theme_minimal()

#############################################
#########Predictive modelling################
#############################################
# Ensure factors are properly coded
ImprovedData <- ImprovedData %>%
  mutate(
    Location = as.factor(Location),
    Activity_Profile = as.factor(Activity_Profile)
  )

# Check for multicollinearity
library(car)
vif_data <- ImprovedData %>%
  select(Total_active_minutes, Steps, Calories_Burned, 
         Sedentary_ratio, MVPA_ratio, Very_Active_Minutes)

# Calculate VIF
vif_model <- lm(Steps ~ Total_active_minutes + Calories_Burned + 
                  Sedentary_ratio + MVPA_ratio, data = ImprovedData)
vif(vif_model)

# Model 1: Basic activity metrics predicting steps
model_steps <- lm(Steps ~ Total_active_minutes + Calories_Burned + 
                    Sedentary_ratio + MVPA_ratio, 
                  data = ImprovedData)

summary(model_steps)

# Check assumptions
par(mfrow = c(2, 2))
plot(model_steps)
par(mfrow = c(1, 1))

# Model 2: Adding location effects
model_steps_geo <- lm(Steps ~ Total_active_minutes + Calories_Burned + 
                        Sedentary_ratio + MVPA_ratio + Location,
                      data = ImprovedData)

summary(model_steps_geo)

# Compare models
anova(model_steps, model_steps_geo)

# Model 3: What drives calorie expenditure?
model_calories <- lm(Calories_Burned ~ Steps + Total_active_minutes + 
                       Very_Active_Minutes + Fairly_Active_Minutes +
                       Lightly_Active_Minutes + Location,
                     data = ImprovedData)

summary(model_calories)

# Simplified version using stepwise selection
library(MASS)
model_calories_step <- stepAIC(model_calories, direction = "both")
summary(model_calories_step)

# Multinomial logistic regression for activity profiles
library(nnet)

# Use "Sedentary" as reference category
ImprovedData$Activity_Profile <- relevel(ImprovedData$Activity_Profile, ref = "Sedentary")

model_profile <- multinom(Activity_Profile ~ Steps + Calories_Burned + 
                            Sedentary_ratio + MVPA_ratio + Location,
                          data = ImprovedData)

summary(model_profile)

# Get odds ratios and confidence intervals
exp(coef(model_profile))
exp(confint(model_profile))

# Cross-validation function
library(caret)
set.seed(123)
train_control <- trainControl(method = "cv", number = 10)

# Compare multiple models
models <- list(
  "Basic" = train(Steps ~ Total_active_minutes + Calories_Burned, 
                  data = ImprovedData, method = "lm", trControl = train_control),
  "With Geography" = train(Steps ~ Total_active_minutes + Calories_Burned + Location,
                           data = ImprovedData, method = "lm", trControl = train_control),
  "With Ratios" = train(Steps ~ Total_active_minutes + Calories_Burned + 
                          Sedentary_ratio + MVPA_ratio + Location,
                        data = ImprovedData, method = "lm", trControl = train_control)
)

# Compare performance
results <- resamples(models)
summary(results)
bwplot(results)

# Create a clean, interpretable final model
final_model <- lm(Steps ~ Total_active_minutes + Calories_Burned + 
                    MVPA_ratio + Location,
                  data = ImprovedData)

# Model summary with confidence intervals
summary(final_model)
confint(final_model)

# Calculate standardized coefficients
library(lm.beta)
std_coef <- lm.beta(final_model)
print(std_coef)

# Predictions for typical cases
new_data <- data.frame(
  Total_active_minutes = c(150, 250, 350),
  Calories_Burned = mean(ImprovedData$Calories_Burned),
  MVPA_ratio = mean(ImprovedData$MVPA_ratio),
  Location = "NSW"  # most common location
)

predict(final_model, newdata = new_data, interval = "confidence")
