# Quickly categorize a data frame with a column of messy character strings.

categorizeDF <- function(df, searchColName, searchList, catList, newColName="Category") {
  # create empty data frame to hold categories
  catDF <- data.frame(matrix(ncol=ncol(df), nrow=0))
  colnames(catDF) <- paste0(names(df))

  # add sequence so original order can be restored
  df$sequence <- seq(nrow(df))

  # iterate through the strings
  for (i in seq_along(searchList)) {
    rownames(df) <- NULL
    index <- grep(searchList[i], df[,which(colnames(df) == searchColName)], ignore.case=TRUE)
    tempDF <- df[index,]
    tempDF$newCol <- catList[i]
    catDF <- rbind(catDF, tempDF)
    df <- df[-index,]
  }

  # OTHER category for unmatched rows
  if (nrow(df) > 0) {
    df$newCol <- "Undefined"
    catDF <- rbind(catDF, df)
  }

  # return to the original order & remove the sequence data
  catDF <- catDF[order(catDF$sequence),]
  catDF$sequence <- NULL

  # remove row names
  rownames(catDF) <- NULL

  # set Category type to factor
  catDF$newCol <- as.factor(catDF$newCol)

  # rename the new column
  colnames(catDF)[which(colnames(catDF) == "newCol")] <- newColName
  catDF
}