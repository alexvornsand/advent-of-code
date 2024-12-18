# advent of code
# day 3

# part 1
input <- readLines('day-03.txt')

traverseMap <- function(input, xDelta, yDelta){
  binaryMap <- function(str){
    return(1 * (unlist(strsplit(str, split = '')) == '#'))
  }
  bMap <- matrix(sapply(input, binaryMap), ncol = 31, byrow = T)
  x <- 1
  y <- 1
  trees <- 0
  while(y < 323){
    y <- y + yDelta
    if((x + xDelta) != 31){
      x <- (x + xDelta) %% 31
    } else {
      x <- 31
    }
    trees <- trees + bMap[y, x]
  }
  return(trees)
}

traverseMap(input, 3, 1)

# part 2
traverseMap(input, 1, 1) * traverseMap(input, 3, 1) * traverseMap(input, 5, 1) * traverseMap(input, 7, 1) * traverseMap(input, 1, 2)
