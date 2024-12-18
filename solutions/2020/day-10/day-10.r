# advent of code
# day 10

# part 1
input <- readLines('day-10.txt')

findJoltage <- function(input, partTwo = F){
  adapters <- as.integer(input)
  device <- max(adapters) + 3
  sequence <- c(0, adapters[order(adapters)], device)
  differences <- sequence[2:length(sequence)] - sequence[1:length(sequence) - 1]
  if(partTwo == F){
    return(sum(differences == 1) * sum(differences == 3))
  } else {
    gaps <- c()
    i <- 0
    for(diff in differences){
      if(diff == 1){
        i <- i + 1
      } else {
        i <- i - 1
        if(i > 0){
          gaps <- c(gaps, i)
        }
        i <- 0
      }
    }
    combos <- c()
    for(gap in gaps){
      if(gap == 1){
        combos <- c(combos, 2) # 0, 1
      } else if(gap == 2){
        combos <- c(combos, 4) # 0, 1, 2, 12
      } else if(gap == 3){
        combos <- c(combos, 7) # 1, 2, 3, 12, 13, 23, 123
      }
    }
    return(as.character(prod(combos)))
  }
}

findJoltage(input)

# part 2
findJoltage(input, partTwo = T)

