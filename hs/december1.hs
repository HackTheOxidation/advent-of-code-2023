import Data.Char
import System.Environment
import System.Exit


getNumberInLine :: String -> Integer
getNumberInLine str = read [head digits, last digits]
                where
                  digits = filter isDigit str

sumLines :: [String] -> Integer
sumLines allLines = foldr (+) 0 $ fmap getNumberInLine allLines

parse [file] = readAndSum file >> exitWith ExitSuccess
parse [] = putStrLn "Missing argument: <file>" >> exitWith (ExitFailure 1)
parse _ = putStrLn "Invalid number of arguments - expected: <file>" >> exitWith (ExitFailure 1)

readAndSum file = do
  filecontent <- readFile file
  let allLines = lines filecontent
  let result = sumLines allLines
  print result

main :: IO()
main = getArgs >>= parse
