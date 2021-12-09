import {parseInput, getFileName} from "../helpers/fileParser"
import {GetFunction} from "../types"

export const getDay2_1: (mode: string) => (GetFunction|number)[] = (mode) => {
    const day = "2-1"
    const answer = 150
    const solution = 1654760
    if(mode === "test")
        return [answer, getAnswer1(mode, day)]
    else 
        return [solution, getAnswer1(mode, day)]
}

const getInt: (instruction: string) => number = (instruction) => {
    const parsed = instruction.split(" ");
    if (parsed[0] === "down") {
        return parseInt(parsed[1])
    }
    if (parsed[0] === "up") {
        return -parseInt(parsed[1])
    } else {
        throw Error(parsed[1])
    }
}

const getAnswer1: (mode: string, day: string) => number = (mode, day) => {
    const filename = getFileName(mode, day)
    const data = parseInput(filename)
    let horizontal = 0
    let depth = 0
    data.forEach((instr) => {
        try{
            depth += getInt(instr)
        } catch (e:any) {
            horizontal += parseInt(e.message)
        }
    })
    return horizontal * depth
}

export const getDay2_2: (mode: string) => (GetFunction|number)[] = (mode) => {
    const day = "2-1"
    const answer = 900
    const solution = 1956047400
    if(mode === "test")
        return [answer, getAnswer2(mode, day)]
    else 
        return [solution, getAnswer2(mode, day)]
}

const getAnswer2: (mode: string, day: string) => number = (mode, day) => {
    const filename = getFileName(mode, day)
    const data = parseInput(filename)
    let horizontal = 0
    let depth = 0
    let aim = 0
    data.forEach((instr) => {
        try{
            depth += getInt(instr)
        } catch (e:any) {
            const forward = parseInt(e.message)
            horizontal += forward
            aim += forward * depth
        }
    })
    return horizontal * aim
}
