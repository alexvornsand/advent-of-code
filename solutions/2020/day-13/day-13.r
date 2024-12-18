# advent of code
# day 13

# part 1
input <- readLines('day-13.txt')

trackBuses <- function(input, partTwo = F){
  departureTime <- as.integer(input[1])
  busRoutes <- suppressWarnings(as.integer(unlist(strsplit(input[2], split = ','))))
  if(partTwo == F){
    waitTimes <- busRoutes - (departureTime %% busRoutes)
    nextBus <- busRoutes[which(waitTimes == min(waitTimes, na.rm = T))]
    return(nextBus * min(waitTimes, na.rm = T))
  } else {
    correctOffSet <- function(t, rte, busRoutes){
      if(is.na(rte)){
        return(NA)
      } else {
        return((t + which(busRoutes == rte) - 1) %% rte == 0)
      }
    }
    t <- 0
    while(T){
      inSequence <- unlist(sapply(busRoutes, correctOffSet, t = t, busRoutes = busRoutes))
      if(all(inSequence, na.rm = T)){
        return(as.character(t))
      } else {
        t <- t + prod(busRoutes[which(inSequence == T)])
      }
    }
  }
}

trackBuses(input), unit = c('us')

# part 2
trackBuses(input, partTwo = T)
