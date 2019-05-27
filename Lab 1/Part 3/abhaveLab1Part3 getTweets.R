#Group Members: Omkar Thorat (omkarsun) and Abhishek Bhave (abhave)

library(rtweet)

## authenticate via access token

list <-c('flu','fluseason','cough','influenza')
for(i in list)
{
  rt <- search_tweets(i, n = 5000, include_rts = FALSE,geocode = lookup_coords("USA"))
  save_as_csv(rt, file_name = i)
}






