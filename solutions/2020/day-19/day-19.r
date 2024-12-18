# advent of code
# day 19

# part 1
input <- readLines('day-19.txt')

assessPatterns <- function(input, partTwo = F){
  rules <- input[1:134]
  messages <- input[136:514]
  ruleList <- list()
  for(rule in rules){
    ruleId <- unlist(strsplit(rule, split = ': '))[1]
    ruleVal <- gsub('\"', '', unlist(strsplit(rule, split = ': '))[2])
    ruleList[[ruleId]] <- ruleVal
  }
  if(partTwo == T){
    ruleList[['8']] <- '42+'
    ruleList[['11']] <- '42 31 | 42 42 31 31 | 42 42 42 31 31 31 | 42 42 42 42 31 31 31 31' # this is really poor form. Sorry
  }
  stringPattern <- '^0$'
  while(length(grep('\\d+', unlist(strsplit(stringPattern, split = '')))) > 0){
    numberStart <- regexpr('\\d+', stringPattern)[1]
    numberEnd <- numberStart - 1 + attr(regexpr(pattern = '\\d+', stringPattern), "match.length")
    numberString <- paste(unlist(strsplit(stringPattern, split = ''))[numberStart:numberEnd], collapse = '')
    replacement <- ruleList[[numberString]]
    if('|' %in% unlist(strsplit(replacement, split = ''))){
      replacement <- paste('(', replacement, ')', sep = '')
    }
    stringPattern <- sub(numberString, replacement, stringPattern, fixed = T)
  }
  stringPattern <- gsub('\\s', '', stringPattern)
  return(length(grep(stringPattern, messages)))
}

assessPatterns(input)

# part 2
asssessPatterns(input, partTwo = T)
