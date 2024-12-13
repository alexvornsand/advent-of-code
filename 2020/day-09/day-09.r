# advent of code
# day 9

# part 1
input <- readLines('day-09.txt')

findEncription <- function(input, partTwo = F){
  numbers <- as.numeric(input)
  findPair <- function(i, nums){
    nums <- nums[(i-25):i]
    for(j in 1:24){
      for(k in (j+1):25){
        if(nums[j] + nums[k] == nums[26]){
          return(T)
        }
      }
    }
    return(F)
  }
  targetNumber <- numbers[25 + min(which(unlist(sapply(26:length(numbers), findPair, nums = numbers)) == F))]
  if(partTwo == F){
    return(targetNumber)
  } else {
    findContiguousSum <- function(i, target){
      sum <- numbers[i]
      n <- i
      while(sum < target){
        n <- n + 1
        sum <- sum + numbers[n]
      }
      if(sum == target){
        key <- min(numbers[i:n]) + max(numbers[i:n])
        return(key)
      } else {
        return(NA)
      }
    }
    contiguousSums <- sapply(1:length(numbers), findContiguousSum, target = targetNumber)
    contiguousSums <- contiguousSums[!is.na(contiguousSums)]
    return(contiguousSums[1])
  }
}

findEncription(input)

# part 2
findEncription(input, partTwo = T)
