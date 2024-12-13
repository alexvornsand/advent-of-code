# advent of code
# day 16

# part 1
input <- readLines('day-16.txt')

readTickets <- function(input, partTwo = F){
  fields <- input[1:20]
  fieldData <- list()
  getRanges <- function(field){
    fieldName <- unlist(strsplit(field, split = ': '))[1]
    fieldRanges <- unlist(strsplit(field, split = ': '))[2]
    firstRange <- unlist(strsplit(fieldRanges, split = ' or '))[1]
    firstRangeStart <- unlist(strsplit(firstRange, split = '-'))[1]
    firstRangeEnd <- unlist(strsplit(firstRange, split = '-'))[2]
    secondRange <- unlist(strsplit(fieldRanges, split = ' or '))[2]
    secondRangeStart <- unlist(strsplit(secondRange, split = '-'))[1]
    secondRangeEnd <- unlist(strsplit(secondRange, split = '-'))[2]
    range <- c(firstRangeStart:firstRangeEnd, secondRangeStart:secondRangeEnd)
    fieldData[[fieldName]] <<- range
    return(range)
  }
  fullRanges <- sort(unique(unlist(sapply(fields, getRanges))))
  otherTicketValues <- t(sapply(input[26:262], function(x){as.integer(unlist(strsplit(x, split = ',')))}))
  rownames(otherTicketValues) <- NULL
  if(partTwo == F){
    return(sum(unlist(otherTicketValues)[which(!(unlist(otherTicketValues) %in% fullRanges))]))
  } else {
    validTickets <- c()
    for(i in 1:nrow(otherTicketValues)){
      if(all(otherTicketValues[i,] %in% fullRanges)){
        validTickets <- rbind(validTickets, otherTicketValues[i,])
      }
    }
    evaluateColAndField <- function(row){
      column <- row[1]
      field <- row[2]
      return(1 * (all(validTickets[,column] %in% fieldData[[field]])))
    }
    possibilitiesMatrix <- matrix(apply(do.call(expand.grid, list(1:20, 1:20)), 1, evaluateColAndField), nrow = 20, byrow = T)
    colnames(possibilitiesMatrix) <- as.character(1:20)
    rownames(possibilitiesMatrix) <- names(fieldData)
    solutionList <- list()
    while(exists('possibilitiesMatrix')){
      if(!is.matrix(possibilitiesMatrix)){
        lastField <- names(fieldData)[which(!(names(fieldData)) %in% names(solutionList))]
        lastColumn <- as.character(1:20)[which(!(as.character(1:20) %in% unlist(sapply(names(solutionList), function(x){solutionList[[x]]}))))]
        solutionList[[lastField]] <- lastColumn
        break
      } else {
        for(row in 1:nrow(possibilitiesMatrix)){
          if(sum(possibilitiesMatrix[row,]) == 1){
            solutionList[[rownames(possibilitiesMatrix)[row]]] <- colnames(possibilitiesMatrix)[which(possibilitiesMatrix[row,] == 1)]
            possibilitiesMatrix <- possibilitiesMatrix[-row, -which(possibilitiesMatrix[row,] == 1)]
            break
          }
        }
      }
      if(!is.matrix(possibilitiesMatrix)){
        lastField <- names(fieldData)[which(!(names(fieldData)) %in% names(solutionList))]
        lastColumn <- as.character(1:20)[which(!(as.character(1:20) %in% unlist(sapply(names(solutionList), function(x){solutionList[[x]]}))))]
        solutionList[[lastField]] <- lastColumn
        break
      } else {
        if(exists('possibilitiesMatrix')){
          for(col in 1:ncol(possibilitiesMatrix)){
            if(sum(possibilitiesMatrix[, col]) == 1){
              solutionList[[rownames(possibilitiesMatrix)[which(possibilitiesMatrix[, col] == 1)]]] <-   colnames(possibilitiesMatrix)[col]
              possibilitiesMatrix <- possibilitiesMatrix[-which(possibilitiesMatrix[, col] == 1), -col]
              break
            }
          }
        }
      }
    }
    myTicket <- as.integer(unlist(strsplit(input[23], split = ',')))
    return(as.character(prod(myTicket[c(
      as.integer(solutionList[['departure platform']]),
      as.integer(solutionList[['departure station']]),
      as.integer(solutionList[['departure date']]),
      as.integer(solutionList[['departure time']]),
      as.integer(solutionList[['departure track']]),
      as.integer(solutionList[['departure location']])
    )])))
  }
}

readTickets(input)

# part 2
readTickets(input, partTwo = T)

                       