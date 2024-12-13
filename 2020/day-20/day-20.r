# advent of code
# day 20

# part 1
input <- readLines('day-20.txt')

readMap <- function(input, partTwo = F){
  updateTileEdges <- function(tile){
    matrix <- tileList[[tile]][['Matrix']]
    tileList[[tile]][['N']] <<- matrix[1,];
    tileDataFrame[which(tileDataFrame$tile == tile), 'N'] <<- paste(tileList[[tile]][['N']], collapse = '');
    tileList[[tile]][['E']] <<- matrix[, ncol(matrix)];
    tileDataFrame[which(tileDataFrame$tile == tile), 'E'] <<- paste(tileList[[tile]][['E']], collapse = '');
    tileList[[tile]][['W']] <<- rev(matrix[, 1]);
    tileDataFrame[which(tileDataFrame$tile == tile), 'W'] <<- paste(tileList[[tile]][['W']], collapse = '');
    tileList[[tile]][['S']] <<- rev(matrix[nrow(matrix),]);
    tileDataFrame[which(tileDataFrame$tile == tile), 'S'] <<- paste(tileList[[tile]][['S']], collapse = '');
    tileList[[tile]][['Nr']] <<- rev(tileList[[tile]][['N']]);
    tileDataFrame[which(tileDataFrame$tile == tile), 'Nr'] <<- paste(tileList[[tile]][['Nr']], collapse = '');
    tileList[[tile]][['Er']] <<- rev(tileList[[tile]][['E']]);
    tileDataFrame[which(tileDataFrame$tile == tile), 'Er'] <<- paste(tileList[[tile]][['Er']], collapse = '');
    tileList[[tile]][['Wr']] <<- rev(tileList[[tile]][['W']]);
    tileDataFrame[which(tileDataFrame$tile == tile), 'Wr'] <<- paste(tileList[[tile]][['Wr']], collapse = '');
    tileList[[tile]][['Sr']] <<- rev(tileList[[tile]][['S']]);
    tileDataFrame[which(tileDataFrame$tile == tile), 'Sr'] <<- paste(tileList[[tile]][['Sr']], collapse = '');
  }
  flipX <- function(mat){
    return(mat[nrow(mat):1,])
  }
  flipY <- function(mat){
    return(mat[, ncol(mat):1])
  }
  rotate90 <- function(mat){
    return(flipY(t(mat)))
  }
  rearrangeTile <- function(childTile, parentSide, childSide, tileList){
    opposite <- c('N' = 'S', 'E' = 'W', 'S' = 'N', 'W' = 'E', 'Nr' = 'Sr', 'Er' = 'Wr', 'Sr' = 'Nr', 'Wr' = 'Er')
    clockwiseOf <- c('N' = 'E', 'E' = 'S', 'S' = 'W', 'W' = 'N', 'Nr' = 'Er', 'Er' = 'Sr', 'Sr' = 'Wr', 'Wr' = 'Nr')
    anticlockwiseOf <- c('N' = 'W', 'E' = 'N', 'S' = 'E', 'W' = 'S', 'Nr' = 'Wr', 'Er' = 'Nr', 'Sr' = 'Er', 'Wr' = 'Sr')
    matrix <- tileList[[childTile]][['Matrix']]
    if(parentSide == childSide){
      if(parentSide %in% c('N', 'S')){
        return(flipX(matrix))
      } else {
        return(flipY(matrix))
      }
    } else if(parentSide == sub('r', '', childSide)){
      return(flipX(flipY(matrix)))
    } else if(parentSide == anticlockwiseOf[childSide]){
      if(parentSide %in% c('N', 'S')){
        return(flipY(rotate90(matrix)))
      } else {
        return(flipX(rotate90(matrix)))
      }
    } else if(parentSide == anticlockwiseOf[sub('r', '', childSide)]){
      return(rotate90(matrix))
    } else if(parentSide == opposite[childSide]){
      if(parentSide %in% c('N', 'S')){
        return(flipY(matrix))
      } else {
        return(flipX(matrix))
      }
    } else if(parentSide == opposite[sub('r', '', childSide)]){
      return(matrix)
    } else if(parentSide == clockwiseOf[childSide]){
      if(parentSide %in% c('N', 'S')){
        return(flipY(rotate90(rotate90(rotate90(matrix)))))
      } else {
        return(flipX(rotate90(rotate90(rotate90(matrix)))))
      }
    } else if(parentSide == clockwiseOf[sub('r', '', childSide)]){
      return(rotate90(rotate90(rotate90(matrix))))
    } 
  }
  tileList <- list()
  sapply(seq(from = 1, to = length(input), by = 12), function(x){
    tileName <- sub(':', '', sub('Tile\\s', '', input[x]), fixed = T);
    matrix <- matrix(unlist(strsplit(input[(x + 1):(x + 10)], split = '')), nrow = 10, byrow = T);
    tileList[[tileName]] <<- list()
    tileList[[tileName]][['Matrix']] <<- matrix;
  })
  tileDataFrame <- data.frame(
    'tile' = names(tileList), 
    'N' = NA, 
    'E' = NA,
    'S' = NA,
    'W' = NA,
    'Nr' = NA,
    'Er' = NA,
    'Sr' = NA,
    'Wr' = NA,
    'nTile' = NA,
    'eTile' = NA,
    'wTile' = NA,
    'sTile' = NA
  )
  sapply(names(tileList), updateTileEdges)
  rownames(tileDataFrame) <- tileDataFrame$tile
  opposite <- c('nTile' = 'sTile', 'eTile' = 'wTile', 'sTile' = 'nTile', 'wTile' = 'eTile')
  for(r in 1:nrow(tileDataFrame)){
    for(d in c('N', 'E', 'S', 'W')){
      lower <- tolower(d)
      var <- paste(lower, 'Tile', sep = '')
      if(is.na(tileDataFrame[r, var])){
        subMatrix <- tileDataFrame[-r,]
        spot <- which(subMatrix == tileDataFrame[r, d], arr.ind = T)
        if(length(spot) > 0){
          childTile <- subMatrix[spot[1], 'tile']
          childSide <- names(tileDataFrame)[spot[2]]
          parentSide <- d
          tileList[[childTile]][['Matrix']] <- rearrangeTile(childTile, parentSide, childSide, tileList = tileList)
          updateTileEdges(childTile)
          tileDataFrame[r, var] <- childTile
          tileDataFrame[childTile, opposite[var]] <- tileDataFrame[r, 'tile']
          tileDataFrame <- rbind(
            tileDataFrame[1:r,], 
            tileDataFrame[which(tileDataFrame$tile == childTile),],
            tileDataFrame[-which(tileDataFrame$tile == childTile),][(1 + r):(nrow(tileDataFrame) - 1),])
        } else {
          tileDataFrame[r, var] <- '0000'
        }
      }
    }    
  }
  pseudoMatrix <- matrix(NA, nrow = 12, ncol = 12)
  nwCorner <- tileDataFrame[which(tileDataFrame$nTile == '0000' & tileDataFrame$wTile == '0000'), 'tile']
  pseudoMatrix[1,1] <- nwCorner
  for(r in 1:12){
    for(c in 1:12){
      row <- tileDataFrame[pseudoMatrix[r, c],]
      if(r == 1 & row$eTile != '0000'){
        pseudoMatrix[r, c + 1] <- row$eTile
      }
      if(row$sTile != '0000'){
        pseudoMatrix[r + 1, c] <- row$sTile
      }
    }
  }
  if(partTwo == F){
    return(as.character(prod(as.integer(c(pseudoMatrix[1,1], pseudoMatrix[1,12], pseudoMatrix[12,1], pseudoMatrix[12,12])))))
  } else {
    trimMatrix <- function(tile){
      matrix <- tileList[[tile]][['Matrix']]
      trimmedMatrix <- matrix[-c(1,nrow(matrix)),-c(1,ncol(matrix))]
      tileList[[tile]][['Matrix']] <<- trimmedMatrix
    }
    sapply(names(tileList), trimMatrix)
    image <- c()
    for(r in 1:12){
      row <- c()
      for(c in 1:12){
        row <- cbind(row, tileList[[pseudoMatrix[r, c]]][['Matrix']])
      }
      image <- rbind(image, row)
    }
    marks <- sum(image == '#')
    countSeaMonsters <- function(image){
      seaMonsters <- 0
      for(r in 2:(nrow(image) - 1)){
        for(c in 1:(ncol(image) - 19)){
          if(image[r, c] == '#'){
            x1 <- image[r + 1, c + 1]
            x2 <- image[r + 1, c + 4]
            x3 <- image[r, c + 5]
            x4 <- image[r, c + 6]
            x5 <- image[r + 1, c + 7]
            x6 <- image[r + 1, c + 10]
            x7 <- image[r, c + 11]
            x8 <- image[r, c + 12]
            x9 <- image[r + 1, c + 13]
            x10 <- image[r + 1, c + 16]
            x11 <- image[r, c + 17]
            x12 <- image[r, c + 18]
            x13 <- image[r, c + 19]
            x14 <- image[r - 1, c + 18]
            spots <- c(x1, x2, x3, x4, x5, x6, x7,
                       x8, x9, x10, x11, x12, x13, x14)
            if(all(spots == '#')){
              seaMonsters <- seaMonsters + 1
            }
          }
        }
      }
      return(seaMonsters)
    }
    numberOfSeaMonstesr <- sum(
      countSeaMonsters(image),
      countSeaMonsters(flipY(image)),
      countSeaMonsters(flipX(image)),
      countSeaMonsters(flipX(flipY(image))),
      countSeaMonsters(rotate90(image)),
      countSeaMonsters(flipY(rotate90(image))),
      countSeaMonsters(flipX(rotate90(image))),
      countSeaMonsters(flipX(flipY(rotate90(image))))
    )
    return(marks - 15 * numberOfSeaMonstesr)
  }
}

readMap(input)

# part 2
readMap(input, partTwo = T)
