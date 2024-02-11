import { readAll } from "https://deno.land/std/io/read_all.ts";

const numbers = [
    "one", "two", "three",
    "four", "five", "six",
    "seven", "eight", "nine"
];

const numberRegex = new RegExp(`\\d|${numbers.join('|')}`, 'g');

const numberMapping = Array(numbers.length)
    .keys()
    .reduce((obj, i) => {
        const target = String(i + 1);
        obj[numbers[i]] = target;
        obj[target] = target;
        return obj;
    }, {});

function getNumber(line) {
    const digits = line
        .matchAll(numberRegex)
        .toArray()
        .map(String)
        .map((str) => numberMapping[str]);

    switch (digits.length) {
        case 0:
            return 0;
        case 1:
            const first = digits.at(0);
            return Number(first + first);
        default:
            return Number(digits.at(0) + digits.at(-1));
    }
}

function readSum(content) {
    return content
        .split('\n')
        .map(getNumber)
        .reduce((acc, a) => acc + a, 0);
}

const argv = Deno.args;

if (Deno.args.length != 1) {
    console.log("Invalid number of arguments - Expected (1): <inputfile>\n");
    Deno.exit(-1);
}

const fileName = Deno.args[0];

try {
    using file = Deno.openSync(fileName, { read: true });
    const decoder = new TextDecoder();
    const content = decoder.decode(await readAll(file));

    const sum = readSum(content);
    console.log(sum);
    file.close();
} catch (e) {
    console.log(`NotFound - No such file or directory: ${fileName}\n`);
}
