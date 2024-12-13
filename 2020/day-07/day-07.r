# advent of code
# day 7

# part 1
input <- readLines('day-07.txt')

countBags <- function(input, partTwo = F){
  ruleList <- list()
  for(rule in input){
    keyValue <- trimws(unlist(strsplit(gsub('bag', '', gsub('bags', 'bag', rule)), split = ' contain ')))
    bags <- trimws(gsub('.', '', unlist(strsplit(keyValue[2], split = ',')), fixed = T))
    if(bags[1] == 'no other'){
      ruleList[[keyValue[1]]] <- 'no other'
    } else {
      ruleList[[keyValue[1]]] <- list()
      for(bag in bags){
        bagCount <- as.integer(substring(bag, 1, 1))
        bagId <- trimws(substring(bag, 3, nchar(bag)))
        ruleList[[keyValue[1]]][[bagId]] <- bagCount
      }
    }
  }
  if(partTwo == T){
    countBagContents <- function(bag){
      if(ruleList[bag] == 'no other'){
        return(0)
      } else {
        return(sum(unlist(sapply(names(ruleList[[bag]]), function(x){return(ruleList[[bag]][[x]] * (1 + countBagContents(x)))}))))
      }
    }
    return(countBagContents('shiny gold'))
  } else {
    checkForShinyGold <- function(bag){
      if(any(names(ruleList[[bag]]) == 'shiny gold')){
        return(T)
      } else if(ruleList[[bag]][1] == 'no other'){
        return(F)
      } else {
        return(any(unlist(sapply(names(ruleList[[bag]]), checkForShinyGold))))
      }
    }
    return(sum(unlist(sapply(names(ruleList), checkForShinyGold))))
  }
}

countBags(input)

# part 2
countBags(input, partTwo = T)
