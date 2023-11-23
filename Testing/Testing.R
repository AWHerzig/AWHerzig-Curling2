library(tidyverse)
setwd('/Users/yungzig/Desktop/CSProjects/Curling2/Testing')

#shots0 <- read.csv('ShotsLeft_0.csv')
shots1 <- read.csv('ShotsLeft_1.csv') %>% 
  group_by(hammer, lead, shot, curscore) %>%
  summarise(hscore = mean(hammerscore), total = n(), .groups = 'keep')
shots1.1 <- read.csv('ShotsLeft_1.csv') 
shots2 <- read.csv('ShotsLeft_2.csv')
shots3 <- read.csv('ShotsLeft_3.csv')
shots4 <- read.csv('ShotsLeft_4.csv')
shots5 <- read.csv('ShotsLeft_5.csv')
shots6 <- read.csv('ShotsLeft_6.csv')
shots7g <- read.csv('ShotsLeft_7.csv') %>% 
  group_by(hammer, lead, shot, curscore) %>%
  summarise(hscore = mean(hammerscore), total = n(), .groups = 'keep')
shots8g <- read.csv('ShotsLeft_8.csv') %>% 
  group_by(hammer, lead, shot, curscore) %>%
  summarise(hscore = mean(hammerscore), total = n(), .groups = 'keep')
#shots9 <- read.csv('ShotsLeft_9.csv')
#shots10 <- read.csv('ShotsLeft_10.csv')
#shots11 <- read.csv('ShotsLeft_11.csv')
#shots12 <- read.csv('ShotsLeft_12.csv')
#shots13 <- read.csv('ShotsLeft_13.csv')
#shots14 <- read.csv('ShotsLeft_14.csv')
#shots15 <- read.csv('ShotsLeft_15.csv')
#shots16 <- read.csv('ShotsLeft_16.csv')
hammer <- read.csv('hammer.csv')
lead <- read.csv('lead.csv')
shot = read.csv('shot.csv')
