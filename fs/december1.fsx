open System


let lines = IO.File.ReadLines("input")

let calculateSum =
  let getNumber line =
    let digits = line |> String.filter Char.IsDigit
    match List.ofArray (digits.ToCharArray()) with
      | [] -> 0
      | [d] -> int $"{d}{d}"
      | first::tail ->
        let (last::_) = List.rev tail
        int $"{first}{last}"

  lines
  |> Seq.map getNumber
  |> Seq.fold (+) 0


printf "%d\n" calculateSum
