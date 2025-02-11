import Data.List (transpose)

getScores :: String -> Int
getScores nums = sum scores
  where lists = transpose . map (map (read :: String -> Int) . words) . lines $ nums
        scores = map (\l -> l * length (filter (==l) (lists!!1))) (lists!!0)

main = do
  nums <- readFile "input.txt"
  print $ getScores nums
