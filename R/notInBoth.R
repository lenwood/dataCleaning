DF1 <- data.frame(AA = 3:7, BB=LETTERS[3:7])
DF1 <- rbind(DF1, data.frame(AA=11:12, BB=LETTERS[11:12]))
n1 <- data.frame(AA=14, BB=NA)
DF1 <- rbind(DF1, n1)
DF2 <- data.frame(AA = 4:5, BB=LETTERS[4:5])
DF2 <- rbind(DF2, data.frame(AA=8:12, BB=LETTERS[8:12]))
n2 <- data.frame(AA=16, BB=NA)
DF2 <- rbind(DF2, n2)
rm(n1, n2)

DF1$inDF1 <- TRUE
DF2$inDF2 <- TRUE
together <- merge(DF1, DF2, all=TRUE)
DF1$inDF1 <- NULL; DF2$inDF2 <- NULL

not_in_both <- together[!complete.cases(together),]; rm(together)

F1 <- not_in_both
F1$inDF1 <- NULL
not_in_DF2 <- F1[!complete.cases(F1$inDF2),]; rm(F1)
not_in_DF2$inDF2 <- NULL

F2 <- not_in_both
F2$inDF2 <- NULL; rm(not_in_both)
not_in_DF1 <- F2[!complete.cases(F2$inDF1),]; rm(F2)
not_in_DF1$inDF1 <- NULL
