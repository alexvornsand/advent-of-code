# advent of code
# day 21

# part 1
input <- readLines('day-21.txt')

checkForRiskyIngredients <- function(input, partTwo = F){
  ingredientsList <- list()
  allergensList <- list()
  for(i in 1:length(input)){
    ingredientsList[[i]] <- unlist(strsplit(unlist(strsplit(input[i], split  = '(contains ', fixed = T))[1], ' '))
    allergensList[[i]] <- unlist(strsplit(gsub(')', '', unlist(strsplit(input[i], split  = '(contains ', fixed = T))[2], fixed = T), ', '))
  }
  allergens <- unique(unlist(allergensList))
  ingredients <- unique(unlist(ingredientsList))
  possiblePairings <- list()
  for(i in allergens){
    possiblePairings[[i]] <- Reduce(intersect, ingredientsList[which(unlist(lapply(allergensList, function(x){return(i %in% x)})))])
  }
  while(length(unlist(possiblePairings)) > 8){
    for(i in allergens){
      if(length(possiblePairings[[i]]) == 1){
        taken <- possiblePairings[[i]]
        for(j in allergens){
          if(i != j){
            possiblePairings[[j]] <- possiblePairings[[j]][which(possiblePairings[[j]] != taken)]
          }
        }
      }
    }
  }
  if(partTwo == F){
    sum(unlist(lapply(ingredientsList, function(x){return(sum(!(x %in% unlist(possiblePairings))))})))
  } else {
    paste(unlist(setNames(lapply(sort(names(possiblePairings)), FUN = function(n) possiblePairings[[n]]), sort(names(possiblePairings)))), collapse = ',')
  }
}

checkForRiskyIngredients(input)

# part 2
checkForRiskyIngredients(input, partTwo = T)
