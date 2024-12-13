# advent of code
# day 4

# part 1
input <- readLines('day-04.txt')

countValidPassports <- function(input, partTwo = F){
  passports <- gsub('\n', ' ', unlist(strsplit(paste(input, collapse = '\n'), split = '\n\n')))
  evaluatePassport <- function(pp, partTwo){
    kvs <- unlist(strsplit(pp, split = ' '))
    passportKeyValues <- list()
    for(kv in kvs){
      kvPair <- unlist(strsplit(kv, split = ':'))
      passportKeyValues[[kvPair[1]]] <- kvPair[2]
    }
    criticalFields <- c('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    if(partTwo == T){
      if(sum(criticalFields %in% names(passportKeyValues)) == 7){
        byr <- as.integer(passportKeyValues[['byr']]) >= 1920 & 
          as.integer(passportKeyValues[['byr']]) <= 2002
        iyr <- as.integer(passportKeyValues[['iyr']]) >= 2010 & 
          as.integer(passportKeyValues[['iyr']]) <= 2020
        eyr <- as.integer(passportKeyValues[['eyr']]) >= 2020 & 
          as.integer(passportKeyValues[['eyr']]) <= 2030
        if(substr(passportKeyValues[['hgt']], nchar(passportKeyValues[['hgt']]) - 1, nchar(passportKeyValues[['hgt']])) == 'in'){
          hgt <- as.integer(substr(passportKeyValues[['hgt']], 1, nchar(passportKeyValues[['hgt']]) - 2)) >= 59 & 
            as.integer(substr(passportKeyValues[['hgt']], 1, nchar(passportKeyValues[['hgt']]) - 2)) <= 76
        } else if(substr(passportKeyValues[['hgt']], nchar(passportKeyValues[['hgt']]) - 1, nchar(passportKeyValues[['hgt']])) == 'cm'){
          hgt <- as.integer(substr(passportKeyValues[['hgt']], 1, nchar(passportKeyValues[['hgt']]) - 2)) >= 150 & 
            as.integer(substr(passportKeyValues[['hgt']], 1, nchar(passportKeyValues[['hgt']]) - 2)) <= 193
        } else {
          hgt <- F
        }
        hcl <- 1 %in% grep('\\#[a-f0-9]{6}', passportKeyValues[['hcl']])
        ecl <- passportKeyValues[['ecl']] %in% c('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
        pid <- 1 %in% grep('^\\d{9}$', passportKeyValues[['pid']])
        return(byr & iyr & eyr & hgt & hcl & ecl & pid)
      } else {
        return(F)
      }      
    } else {
      if(sum(criticalFields %in% names(passportKeyValues)) == 7){
        return(T)
      } else {
        return(F)
      }
    }
  }
  return(sum(unlist(sapply(passports, evaluatePassport, partTwo = partTwo))))
}

countValidPassports(input)

# part 2
countValidPassports(input, partTwo = T)

