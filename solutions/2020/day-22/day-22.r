# advent of code
# day 22

# part 1
input <- readLines('day-22.txt')

findCombatWinner <- function(input, partTwo = F){
  hands <- strsplit(unlist(strsplit(sub(',,', '\n', gsub('Player\\s\\d:\\,', '', paste(input, collapse = ',')), fixed = T), split = '\n')), split = ',')
  handA <- as.integer(hands[[1]])
  handB <- as.integer(hands[[2]])
  playCombat <- function(handA, handB, partTwo){
    playStates <- c()
    while(length(handA) > 0 & length(handB > 0)){
      playState <- paste(paste(handA, collapse = '-'), '!', paste(handB, collapse = '-'), sep = '')
      if(partTwo == T & playState %in% playStates){
        return(c(1, sum(rev(handA) * which(rev(handA) == rev(handA)))))
      } else {
        playStates <- c(playStates, playState)
        cardA <- handA[1]
        cardB <- handB[1]
        if(partTwo == T & length(handA) - 1 >= cardA & length(handB) - 1 >= cardB){
          winner <- playCombat(handA[2:(cardA + 1)], handB[2:(cardB + 1)], partTwo = T)[1]
        } else {
          winner <- which.max(c(cardA, cardB))
        }
        if(winner == 1){
          handB <- handB[which(!(handB == cardB))]
          handA <- c(handA[which(!handA == cardA)], cardA, cardB)
        } else {
          handA <- handA[which(!(handA == cardA))]
          handB <- c(handB[which(!handB == cardB)], cardB, cardA)
        }
      }
    }
    winner <- which.max(c(length(handA), length(handB)))
    score <- sum(rev(handA) * which(rev(handA) == rev(handA)))
    return(c(winner, score))
  }
  return(playCombat(handA, handB, partTwo = partTwo)[2])
}

findCombatWinner(input)

# part 2
findCombatWinner(input, partTwo = T)
