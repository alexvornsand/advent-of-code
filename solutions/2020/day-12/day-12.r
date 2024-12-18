# advent of code
# day 12

# part 1
input <- readLines('day-12.txt')

getManhattanDistance <- function(input, partTwo = F){
  xtar <- 10
  ytar <- 1
  xpos <- 0
  ypos <- 0
  r <- 0
  for(direction in input){
    action <- unlist(strsplit(direction, split = ''))[1]
    magnitude <- as.integer(paste(unlist(strsplit(direction, split = ''))[2:nchar(direction)], collapse = ''))
    if(partTwo == F){
      if(action == 'N'){
        ypos <- ypos + magnitude
      } else if(action == 'S'){
        ypos <- ypos - magnitude
      } else if(action == 'E'){
        xpos <- xpos + magnitude
      } else if(action == 'W'){
        xpos <- xpos - magnitude
      } else if(action == 'L'){
        r <- (r + magnitude) %% 360
      } else if(action == 'R'){
        r <- (r - magnitude) %% 360
      } else {
        xpos <- xpos + cos(2 * pi * r / 360) * magnitude
        ypos <- ypos + sin(2 * pi * r / 360) * magnitude
      }
    } else {
      if(action == 'N'){
        ytar <- ytar + magnitude
      } else if(action == 'S'){
        ytar <- ytar - magnitude
      } else if(action == 'E'){
        xtar <- xtar + magnitude
      } else if(action == 'W'){
        xtar <- xtar - magnitude
      } else if(action == 'L'){
        if(magnitude == 180){
          xtar <- -xtar
          ytar <- -ytar
        } else if(magnitude == 90){
          oldX <- xtar
          oldY <- ytar
          xtar <- -oldY
          ytar <- oldX
        } else {
          oldX <- xtar
          oldY <- ytar
          xtar <- oldY
          ytar <- -oldX
        }
      } else if(action == 'R'){
        if(magnitude == 180){
          xtar <- -xtar
          ytar <- -ytar
        } else if(magnitude == 90){
          oldX <- xtar
          oldY <- ytar
          xtar <- oldY
          ytar <- -oldX
        } else {
          oldX <- xtar
          oldY <- ytar
          xtar <- -oldY
          ytar <- oldX
        }
      } else {
        xpos <- xpos + xtar * magnitude
        ypos <- ypos + ytar * magnitude
      }
    }
  }
  return(abs(xpos) + abs(ypos))
}

getManhattanDistance(input)

# part 2
getManhattanDistance(input, partTwo = T)

