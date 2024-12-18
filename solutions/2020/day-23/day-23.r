# advent of code
# day 23

# part 1
input <- '135468729'

predictCups <- function(input, partTwo = F){
  if(partTwo == T){
    k = 10000000
    l = 1000000
  } else {
    k = 100
    l = 9
  }
  sequence <- 1:l
  header <- as.integer(unlist(strsplit(input, '')))
  sequence[1:length(header)] <- header
  max <- max(sequence)
  nextSequence <- rep(NA, k)
  nextSequence[sequence[1:(max - 1)]] <- sequence[-1]
  nextSequence[sequence[max]] <- sequence[1]
  current <- sequence[1]
  for(i in 1:k){
    removed1 <- nextSequence[current]
    removed2 <- nextSequence[removed1]
    removed3 <- nextSequence[removed2]
    if(current == 1){
      target <- max
    } else {
      target <- current - 1
    }
    while(target %in% c(removed1, removed2, removed3)){
      if(target == 1){
        target <- max
      } else {
        target <- target - 1
      }
    }
    nextSequence[current] <- nextSequence[removed3]
    current <- nextSequence[removed3]
    nextSequence[removed3] <- nextSequence[target]
    nextSequence[target] <- removed1
  }
  if(partTwo == T){
    return(prod(nextSequence[1], nextSequence[nextSequence[1]]))
  } else {
    result <- nextSequence[1]
    for(i in 2:8){
      result <- c(result, nextSequence[tail(result, 1)])
    }
    return(paste(result, collapse = ''))
  }
}

predictCups(input)

# part 2

predictCups(input, partTwo = T)
