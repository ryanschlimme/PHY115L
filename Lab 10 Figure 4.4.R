library(tidyverse)

single08 = function(x) 0.0159*sin(336*(x-0.00780))^2 / (336*(x-0.00780))^2

single16 = function(x) 0.0321*sin(753*(x-0.0129))^2 / (753*(x-0.0129))^2

single04 = function(x) 0.0114*sin(133*(x-0.0138))^2 / (133*(x-0.0138))^2

single02 = function(x) 0.0159*sin(45.8*(x-0.0244))^2 / (45.8*(x-0.0244))^2

ggplot() +
  xlim(-0.05, 0.1) +
  stat_function(fun = single08, aes(color = "0.08 mm")) +
  stat_function(fun = single16, aes(color = "0.16 mm")) + 
  stat_function(fun = single04, aes(color = "0.04 mm")) +
  stat_function(fun = single02, aes(color = "0.02 mm")) +
  labs(title = "Single-Slit Diffraction as a Function of Slit Width",
       x = "Perpendicular Displacement of PASCO Sensor to Light Source (m)",
       y = "Light Intensity") +
  scale_y_continuous(labels = scales::percent) +
  scale_color_manual(name = "Fitted Models",
                     breaks = c("0.08 mm", "0.16 mm", "0.04 mm", "0.02 mm"),
                     values = c("0.08 mm" = "blue", "0.16 mm" = "red",
                                "0.04 mm" = "green", "0.02 mm" = "black"))