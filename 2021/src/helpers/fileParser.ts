import * as fs from 'fs';
import {GetFunction, ComputeFunction} from "../types"

export const parseInput: (fileName: string) => string[] = (fileName) => {
    try {
        const content = fs.readFileSync(`src/input/${fileName}.txt`, "utf-8")
        return content.split("\r\n");
    } catch (err) {
        return []
    }
}

export const arrayNumToInt: (input: string[]) => number[] = (input) => {
    let result: number[] = []
    input.forEach((item) => {
        result.push(parseInt(item, 10))
    })
    return result
}

export const getFileName: (mode: string, day: string) => string = (mode, day) => {
    if(mode === "test") {
        return "example" + day
    }
    if(mode === "exec") {
        return "day" + day
    } else {
        return ""
    }
}

export const getInputData: (mode: string, day: string) => number[] = (mode, day) => {
    const filename = getFileName(mode, day)
    if (filename === "") return []

    const content = parseInput(filename)
    if (content === undefined) {
        return []
    }
    return arrayNumToInt(content)

}

export const getDay: (mode: string, day: string, testAnswer: number, solution: number, computeFunction: ComputeFunction) => (GetFunction|number)[] = (mode, day, testAnswer, solution, computeFunction) => {
    if(mode === "test")
        return [testAnswer, computeFunction(mode, day)]
    else 
        return [solution, computeFunction(mode, day)]
}