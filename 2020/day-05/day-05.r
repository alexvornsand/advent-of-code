# advent of code
# day 5

# part 1
input <- readLines('day-05.txt')

findSeatID <- function(input, partTwo = F){
  unbinary <- function(x){
    seq <- rev(as.integer(unlist(strsplit(x, split = ''))))
    return(sum(seq * 2 ^ (0:(length(seq) - 1))))
  }
  getSeatID <- function(boardingPass){
    row <- unbinary(substring(gsub('B', '1', gsub('F', '0', boardingPass)), 1, 7))
    column <- unbinary(substring(gsub('R', '1', gsub('L', '0', boardingPass)), 8, 10))
    return(8 * row + column)
  }
  if(partTwo == T){
    seats <- apply(do.call(expand.grid, list('row' = 1:128, 'column' = 0:7)), 1, function(x){return(x[[1]] * 8 + x[[2]])})
    takenSeats <- unlist(sapply(input, getSeatID))
    for(seat in seats){
      if(!(seat %in% takenSeats) & (seat + 1) %in% takenSeats & (seat - 1) %in% takenSeats){
        return(seat)
        break
      }
    }
  } else {
    return(max(unlist(sapply(input, getSeatID))))
  }
}

findSeatID(input)

# part 2
findSeatID(input, partTwo = T)
