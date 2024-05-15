open System


let lines = IO.File.ReadLines("input")

let calculateSum =
  let toDigits = String.filter Char.IsDigit >> (_.ToCharArray()) >> List.ofArray
  let getNumber = function
    | [] -> 0
    | xs -> int $"{List.head xs}{List.tail xs}"

  lines
  |> Seq.map (toDigits >> getNumber)
  |> Seq.fold (+) 0


printf "%d\n" calculateSum
