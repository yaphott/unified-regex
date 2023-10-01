{-# LANGUAGE OverloadedStrings #-}
module Main where

import System.Environment (getArgs)
import System.IO (withFile, IOMode(..), hPutStrLn)
import Text.Regex.PCRE ((=~))
import qualified Data.Text as T
import qualified Data.Text.IO as TIO

iterateCodepoints :: String -> FilePath -> IO ()
iterateCodepoints pattern filePath = do
    withFile filePath WriteMode $ \handle -> do
        mapM_ (checkAndWrite handle) [0x0..0x10FFFF]
    where
        checkAndWrite handle codepoint = do
        --     | i >= 0xD800 && i <= 0xDFFF = return ()
        --     | otherwise = do
            let char = T.singleton $ toEnum codepoint
            if T.unpack char =~ pattern :: Bool
                then hPutStrLn handle (showHex codepoint)
                else return ()

showHex :: Int -> String
showHex n = showHex' n []
    where
        showHex' 0 xs = xs
        showHex' n xs =
            let (q, r) = n `quotRem` 16
                hexChars = "0123456789ABCDEF"
                x = hexChars !! r
            in showHex' q (x : xs)

main :: IO ()
main = do
    args <- getArgs
    case args of
        [pattern, filePath] -> iterateCodepoints pattern filePath
        _ -> putStrLn "Usage: cabal run haskell -- <pattern> <file_path>"
