import Data.Maybe (isNothing, fromJust)

isReportOk :: [Int] -> Int -> Maybe Int -> Bool
isReportOk [one] _ _ = True
isReportOk (one:two:etc) tolerance prev = (diff > 0 && diff < 4 && isReportOk (two:etc) tolerance (Just one)) || 
                                          tolerance > 0 && ((isReportOk (one:etc) 0 Nothing) ||
                                            if isNothing prev
                                              then isReportOk (two:etc) 0 Nothing
                                              else isReportOk ((fromJust prev):two:etc) 0 Nothing)
  where diff = one - two
isReportOk _ _ _ = False

main = do
  reportstr <- readFile "input.txt"
  let reports = (map (map (read :: String -> Int) . words) . lines $ reportstr)
  print $ length (filter (\r -> isReportOk r 1 Nothing || isReportOk (reverse r) 1 Nothing) reports)
