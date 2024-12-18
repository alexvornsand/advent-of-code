# advent of code
# day 25

# part 1
input <- readLines('day-25.txt')

unlockDoor <- function(input, partTwo = F){
  cardPublicKey <- as.integer(input[1])
  doorPublicKey <- as.integer(input[2])
  findLoopSize <- function(subjNo, key){
    findKey <- 1
    loopSize <- 0
    while(findKey != key){
      loopSize <- loopSize + 1
      findKey <- (findKey * subjNo) %% 20201227
    }
    return(loopSize)
  }
  if(partTwo == F){
    return(cardLoopSize <- findLoopSize(7, cardPublicKey))
  } else {
    transformSubjNo <- function(subjNo, loopSize){
      val <- 1
      for(i in 1:loopSize){
        val <- (val * subjNo) %% 20201227
      }
      return(val)
    }
    return(encryptionKeyC <- transformSubjNo(doorPublicKey, cardLoopSize))
  }
}

