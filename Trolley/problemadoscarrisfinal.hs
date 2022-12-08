module Trolley where

data Entidades = Baby          --(1)
                | Criança      --(2)
                | AdultoHomem  --(3) 
                | AdultoMulher --(4)
                | Dog          --(5)
                | Cat          --(6)
                | Nada
            deriving (Show,Eq)

type Baby = Int 
type AdultoMulher = Int 
type AdultoHomem = Int
type Criança = Int
type Dog = Int
type Cat = Int

converteEntidades :: Int -> Entidades
converteEntidades a | a == 1 = Baby
                | a == 2 = Criança
                | a == 3 = AdultoHomem
                | a == 4 = AdultoMulher
                | a == 5 = Dog
                | a == 6 = Cat
                | otherwise = Nada 

converteEntidadesList :: [Int] -> [Entidades] 
converteEntidadesList [] = []
converteEntidadesList (x:xs) = converteEntidades x : converteEntidadesList (xs)

saveNumero :: [Int] -> [Int] -> [Entidades]
saveNumero a b | length (saveHumans a) > length (saveHumans b) = converteEntidadesList a 
               | length (saveHumans b) > length (saveHumans a) = converteEntidadesList b
               | otherwise = converteEntidadesList (criancaBebe (saveHumans a) (saveHumans b)) 

saveHumans :: [Int] -> [Int]
saveHumans [] = []
saveHumans (x:xs) = if person x == True then x: saveHumans (xs) else saveHumans (xs) 

person :: Int -> Bool 
person a = if a >= 1 && a <= 4 then True else False 

criancaBebe :: [Int] -> [Int] ->[Int]
criancaBebe a b | length (filter (==1) a) > length (filter (==1) b) = a
                | length (filter (==1) a) < length (filter (==1) b) = b
                | length (filter (==2) a) > length (filter (==2) b) = a
                | length (filter (==2) a) < length (filter (==2) b) = b
                | length (filter (==4) a) > length (filter (==4) b) = a
                | length (filter (==4) a) < length (filter (==4) b) = b
                | otherwise = []  

