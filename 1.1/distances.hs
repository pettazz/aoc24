import Data.List (sort, transpose)

getDiffs :: String -> Int
getDiffs nums = sum diffs
  where sortedLists = map sort . transpose . map (map (read :: String -> Int) . words) . lines $ nums
        diffs = zipWith (\l r -> abs $ l - r) (sortedLists!!0) (sortedLists!!1)

main = do
  nums <- readFile "input.txt"
  print $ getDiffs nums
