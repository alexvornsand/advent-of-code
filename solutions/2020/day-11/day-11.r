# advent of code
# day 11

# part 1
library(microbenchmark)
library(pbapply)

input <- readLines('day-11.txt')

fillSeats <- function(input, partTwo = F){
  seatGrid <- do.call(expand.grid, list('column' = 1:nchar(input[1]), 'row' = 1:length(input)))
  seatGrid$status <- as.integer(gsub('L', 0, gsub('\\.', NA, unlist(strsplit(input, split = '')))))
  findNewSeats <- function(seat, partTwo){
    column <- seat[[1]]
    row <- seat[[2]]
    status <- seat[[3]]
    if(partTwo == T){
      NE <- c()
      i <- 1
      while(is.null(NE)){
        if(length(which(seatGrid$column == column + i & seatGrid$row == row + i)) == 1){
          if(is.na(seatGrid[which(seatGrid$column == column + i & seatGrid$row == row + i), 'status'])){
            i <- i + 1
          } else {
            NE <- seatGrid[which(seatGrid$column == column + i & seatGrid$row == row + i), 'status']
          }
        } else {
          NE <- NA
        }
      }
      E <- c()
      i <- 1
      while(is.null(E)){
        if(length(which(seatGrid$column == column + i & seatGrid$row == row)) == 1){
          if(is.na(seatGrid[which(seatGrid$column == column + i & seatGrid$row == row), 'status'])){
            i <- i + 1
          } else {
            E <- seatGrid[which(seatGrid$column == column + i & seatGrid$row == row), 'status']
          }
        } else {
          E <- NA
        }
      }
      SE <- c()
      i <- 1
      while(is.null(SE)){
        if(length(which(seatGrid$column == column + i & seatGrid$row == row - i)) == 1){
          if(is.na(seatGrid[which(seatGrid$column == column + i & seatGrid$row == row - i), 'status'])){
            i <- i + 1
          } else {
            SE <- seatGrid[which(seatGrid$column == column + i & seatGrid$row == row - i), 'status']
          }
        } else {
          SE <- NA
        }
      }
      S <- c()
      i <- 1
      while(is.null(S)){
        if(length(which(seatGrid$column == column & seatGrid$row == row - i)) == 1){
          if(is.na(seatGrid[which(seatGrid$column == column & seatGrid$row == row - i), 'status'])){
            i <- i + 1
          } else {
            S <- seatGrid[which(seatGrid$column == column & seatGrid$row == row - i), 'status']
          }
        } else {
          S <- NA
        }
      }
      SW <- c()
      i <- 1
      while(is.null(SW)){
        if(length(which(seatGrid$column == column - i & seatGrid$row == row - i)) == 1){
          if(is.na(seatGrid[which(seatGrid$column == column - i & seatGrid$row == row - i), 'status'])){
            i <- i + 1
          } else {
            SW <- seatGrid[which(seatGrid$column == column - i & seatGrid$row == row - i), 'status']
          }
        } else {
          SW <- NA
        }
      }
      W <- c()
      i <- 1
      while(is.null(W)){
        if(length(which(seatGrid$column == column - i & seatGrid$row == row)) == 1){
          if(is.na(seatGrid[which(seatGrid$column == column - i & seatGrid$row == row), 'status'])){
            i <- i + 1
          } else {
            W <- seatGrid[which(seatGrid$column == column - i & seatGrid$row == row), 'status']
          }
        } else {
          W <- NA
        }
      }
      NW <- c()
      i <- 1
      while(is.null(NW)){
        if(length(which(seatGrid$column == column - i & seatGrid$row == row + i)) == 1){
          if(is.na(seatGrid[which(seatGrid$column == column - i & seatGrid$row == row + i), 'status'])){
            i <- i + 1
          } else {
            NW <- seatGrid[which(seatGrid$column == column - i & seatGrid$row == row + i), 'status']
          }
        } else {
          NW <- NA
        }
      }
      N <- c()
      i <- 1
      while(is.null(N)){
        if(length(which(seatGrid$column == column & seatGrid$row == row + i)) == 1){
          if(is.na(seatGrid[which(seatGrid$column == column & seatGrid$row == row + i), 'status'])){
            i <- i + 1
          } else {
            N <- seatGrid[which(seatGrid$column == column & seatGrid$row == row + i), 'status']
          }
        } else {
          N <- NA
        }
      }
    } else {
      NE <- ifelse(
        length(which(seatGrid$column == column + 1 & seatGrid$row == row + 1)) == 1, 
        seatGrid[which(seatGrid$column == column + 1 & seatGrid$row == row + 1), 'status'],
        NA
      )
      E <- ifelse(
        length(which(seatGrid$column == column + 1 & seatGrid$row == row)) == 1, 
        seatGrid[which(seatGrid$column == column + 1 & seatGrid$row == row), 'status'],
        NA
      )
      SE <- ifelse(
        length(which(seatGrid$column == column + 1 & seatGrid$row == row - 1)) == 1, 
        seatGrid[which(seatGrid$column == column + 1 & seatGrid$row == row - 1), 'status'],
        NA
      )
      S <- ifelse(
        length(which(seatGrid$column == column & seatGrid$row == row - 1)) == 1, 
        seatGrid[which(seatGrid$column == column & seatGrid$row == row - 1), 'status'],
        NA
      )
      SW <- ifelse(
        length(which(seatGrid$column == column - 1 & seatGrid$row == row - 1)) == 1, 
        seatGrid[which(seatGrid$column == column - 1 & seatGrid$row == row - 1), 'status'],
        NA
      )
      W <- ifelse(
        length(which(seatGrid$column == column - 1 & seatGrid$row == row)) == 1, 
        seatGrid[which(seatGrid$column == column - 1 & seatGrid$row == row), 'status'],
        NA
      )
      NW <- ifelse(
        length(which(seatGrid$column == column - 1 & seatGrid$row == row + 1)) == 1, 
        seatGrid[which(seatGrid$column == column - 1 & seatGrid$row == row + 1), 'status'],
        NA
      )
      N <- ifelse(
        length(which(seatGrid$column == column & seatGrid$row == row + 1)) == 1, 
        seatGrid[which(seatGrid$column == column & seatGrid$row == row + 1), 'status'],
        NA
      )
    }
    neighbors <- c(NE, E, SE, S, SW, W, NW, N)
    newSeatStatus <- ifelse(
      partTwo == T,
      ifelse(
        is.na(status),
        NA,
        ifelse(
          status == 0,
          ifelse(
            sum(neighbors, na.rm = T) == 0,
            1,
            0
          ),
          ifelse(
            sum(neighbors, na.rm = T) >= 5,
            0,
            1
          )
        )
      ),
      ifelse(
        is.na(status),
        NA,
        ifelse(
          status == 0,
          ifelse(
            sum(neighbors, na.rm = T) == 0,
            1,
            0
          ),
          ifelse(
            sum(neighbors, na.rm = T) >= 4,
            0,
            1
          )
        )
      )
    )
    return(newSeatStatus)
  }
  newSeats <- apply(seatGrid, 1, findNewSeats, partTwo = partTwo)
  while(!identical(seatGrid$status, newSeats)){
    seatGrid$status <- newSeats
    newSeats <- apply(seatGrid, 1, findNewSeats, partTwo = partTwo)
  }
  return(sum(seatGrid$status, na.rm = T))
}

microbenchmark(fillSeats(input), times = 10)

# part 2
microbenchmark(fillSeats(input, partTwo = T), times = 10)
