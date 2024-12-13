# advent of code
# day 8

# part 1
input <- readLines('day-08.txt')

findAccumulator <- function(input, partTwo = F){
  testInput <- function(input){
    index <- 1
    inputRun <- c()
    accumulator <- 0
    while(index <= length(input)){
      if(index %in% inputRun){
        return(list('result' = F, 'acc' = accumulator))
      } else {
        if(substr(input[index], 1, 3) == 'nop') {
          inputRun <- c(inputRun, index)
          index <- index + 1
        } else if (substr(input[index], 1, 3) == 'acc') {
          if(substr(input[index], 5, 5) == '+'){
            accumulator <- accumulator + as.integer(substr(input[index], 6, nchar(input[index])))
          } else {
            accumulator <- accumulator - as.integer(substr(input[index], 6, nchar(input[index])))
          }
          inputRun <- c(inputRun, index)
          index <- index + 1
        } else {
          inputRun <- c(inputRun, index)
          if(substr(input[index], 5, 5) == '+'){
            index <- index + as.integer(substr(input[index], 6, nchar(input[index])))
          } else {
            index <- index - as.integer(substr(input[index], 6, nchar(input[index])))
          }
        }
      }
    }
    return(list('result' = T, 'acc' = accumulator))
  }
  if(partTwo == F){
    return(testInput(input)[['acc']])
  } else {
    for(i in 1:length(input)){
      trialInput <- input
      if(substr(trialInput[i], 1, 3) == 'jmp'){
        substr(trialInput[i], 1, 3) <- 'nop'
        trialResults <- testInput(trialInput)
        if(trialResults[['result']] == T){
          return(trialResults[['acc']])
        }
      } else if(substr(trialInput[i], 1, 3) == 'nop'){
        substr(trialInput[i], 1, 3) <- 'jmp'
        trialResults <- testInput(trialInput)
        if(trialResults[['result']] == T){
          return(trialResults[['acc']])
        }
      }
    }
  }
}

findAccumulator(input)

# part 2
findAccumulator(input, partTwo = T)