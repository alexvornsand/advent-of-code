# advent of code
# day 17

# part 1

input <- readLines('day-17.txt')

runCycles <- function(input, partTwo = F){
  values <- as.integer(unlist(strsplit(gsub('.', '0', gsub('#', '1', input), fixed = T), split = '')))
  evaluateNeighbors <- function(row, grid, partTwo){
    if(partTwo == F){
      x <- grid$x[row]
      y <- grid$y[row]
      z <- grid$z[row]
    } else {
      w <- grid$w[row]
      x <- grid$x[row]
      y <- grid$y[row]
      z <- grid$z[row]
    }
    if(partTwo == F){
      neighbors <- do.call(expand.grid, list(x = (x-1):(x+1), y = (y-1):(y+1), z = (z-1):(z+1)))
    } else {
      neighbors <- do.call(expand.grid, list(w = (w-1):(w+1), x = (x-1):(x+1), y = (y-1):(y+1), z = (z-1):(z+1)))
    }
    testNeighbor <- function(i, neighbors, partTwo){
      if(partTwo == F){
        if(length(which(grid$x == neighbors$x[i] & grid$y == neighbors$y[i] & grid$z == neighbors$z[i])) != 0){
          return(grid[which(grid$x == neighbors$x[i] & grid$y == neighbors$y[i] & grid$z == neighbors$z[i]), 'value'])
        } else {
          return(0)
        }
      } else {
        if(length(which(grid$w == neighbors$w[i] & grid$x == neighbors$x[i] & grid$y == neighbors$y[i] & grid$z == neighbors$z[i])) != 0){
          return(grid[which(grid$w == neighbors$w[i] & grid$x == neighbors$x[i] & grid$y == neighbors$y[i] & grid$z == neighbors$z[i]), 'value'])
        } else {
          return(0)
        }
      }
    }
    if(partTwo == F){
      numNeighbors <- sum(unlist(sapply(1:nrow(neighbors), testNeighbor, neighbors = neighbors, partTwo = F))) - grid$value[which(grid$x == x & grid$y == y & grid$z == z)]
    } else {
      numNeighbors <- sum(unlist(sapply(1:nrow(neighbors), testNeighbor, neighbors = neighbors, partTwo = T))) - grid$value[which(grid$w == w & grid$x == x & grid$y == y & grid$z == z)]
    }
    if(grid$value[row] == 1){
      if(numNeighbors == 2 | numNeighbors == 3){
        return(1)
      } else {
        return(0)
      }
    } else {
      if(numNeighbors == 3){
        return(1)
      } else {
        return(0)
      }
    }
  }
  if(partTwo == F){
    xmin <- 0
    xmax <- 7
    ymin <- 0
    ymax <- 7
    zmin <- 0
    zmax <- 0
    newGrid <- do.call(expand.grid, list(x = xmin:xmax, y = ymin:ymax, z = zmin:zmax))
    newGrid <- cbind(newGrid, values)
    colnames(newGrid) <- c('x', 'y', 'z', 'value')
  } else {
    wmin <- 0
    wmax <- 0
    xmin <- 0
    xmax <- 7
    ymin <- 0
    ymax <- 7
    zmin <- 0
    zmax <- 0
    newGrid <- do.call(expand.grid, list(w = wmin:wmax, x = xmin:xmax, y = ymin:ymax, z = zmin:zmax))
    newGrid <- cbind(newGrid, values)
    colnames(newGrid) <- c('w', 'x', 'y', 'z', 'value')
  }
  for(i in 1:6){
    oldGrid <- newGrid
    xmin <- xmin - 1
    xmax <- xmax + 1
    ymin <- ymin - 1
    ymax <- ymax + 1
    zmin <- zmin - 1
    zmax <- zmax + 1
    if(partTwo == T){
      wmin <- wmin - 1
      wmax <- wmax + 1
    }
    if(partTwo == F){
      expandedGrid <- do.call(expand.grid, list(x = xmin:xmax, y = ymin:ymax, z = zmin:zmax))
      expandedGrid <- merge(expandedGrid, oldGrid, by = c('x', 'y', 'z'), all.x = T)
      expandedGrid$value[which(is.na(expandedGrid$value))] <- 0
      colnames(expandedGrid) <- c('x', 'y', 'z', 'value')
    } else {
      expandedGrid <- do.call(expand.grid, list(w = wmin:wmax, x = xmin:xmax, y = ymin:ymax, z = zmin:zmax))
      expandedGrid <- merge(expandedGrid, oldGrid, by = c('w', 'x', 'y', 'z'), all.x = T)
      expandedGrid$value[which(is.na(expandedGrid$value))] <- 0
      colnames(expandedGrid) <- c('w', 'x', 'y', 'z', 'value')
    }
    newVals <- unlist(sapply(1:nrow(expandedGrid), evaluateNeighbors, grid = expandedGrid, partTwo = partTwo))
    newGrid <- expandedGrid
    newGrid$value <- newVals
  }
  return(sum(newGrid$value))
}  

