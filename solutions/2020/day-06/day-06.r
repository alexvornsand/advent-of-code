# advent of code
# day 6

# part 1
input <- readLines('day-06.txt')

countDeclarations <- function(input, partTwo = F){
  declarations <- strsplit(gsub('\n', ' ', unlist(strsplit(paste(input, collapse = '\n'), split = '\n\n'))), split = ' ')
  countDeclarations <- function(dec, partTwo){
    if(partTwo == T){
      return(length(names(which(table(unlist(strsplit(paste(dec, collapse = ''), split = ''))) == length(dec)))))
    } else {
      return(length(unique(unlist(strsplit(paste(dec, collapse = ''), split = '')))))
    }
  }
  return(sum(unlist(sapply(declarations, countDeclarations, partTwo = partTwo))))
}

countDeclarations(input)

# part 2
countDeclarations(input, partTwo = T)

