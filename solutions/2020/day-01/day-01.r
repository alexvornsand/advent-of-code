# advent of code
# day 1

# part 1
numbers <- scan('day-01.txt')

findProduct <- function(numbers, partTwo = F){
  if(partTwo == F){
    for(i in 1:length(numbers)){
      for(j in i:length(numbers)){
        if(numbers[i] + numbers[j] == 2020){
          return(numbers[i] * numbers[j])
        }
      }
    }
  } else {
    for(i in 1:length(numbers)){
      for(j in i:length(numbers)){
        for(k in j:length(numbers)){
          if(numbers[i] + numbers[j] + numbers[k] == 2020){
            return(numbers[i] * numbers[j] * numbers[k])
          }
        }
      }
    }
  }
}

findProduct(numbers)

# part 2
findProduct(numbers, partTwo = T)


