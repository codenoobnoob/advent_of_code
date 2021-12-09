import {getFileName, parseInput} from "../helpers/fileParser"
import { ComputeFunction, GetFunction } from "../types"

const getArraySize: (content: string[]) => Array<string>[] = (content) => {
    const result = []
    for(let i = 0; i < content[0].length; i++) {
        result.push([])
    }
    return result
} 

const isMostCommonOne: (bytes: string[]) => Boolean = (bytes) => {
    let one = 0
    let zero = 0
    bytes.forEach(byte => {
        if (byte === "1") {
            one += 1
        } else if (byte === "0") {
            zero += 1
        }
    })
    return one > zero
}

const getBinaries: (content: string[]) => Array<string>[] = (content) => {
    const binaries = getArraySize(content)
    content.forEach(byte => {
        for(let i = 0; i < byte.length; i++) {
            binaries[i].push(byte.charAt(i))
        }
    });
    return binaries
} 

const getMostAndLeastCommon: (binaries: Array<string>[]) => Array<string> = (binaries) => {
    let val1 = ""
    let val2 = ""
    
    binaries.forEach(bytes => {
        if (isMostCommonOne(bytes)){
            val1 += "1"
            val2 += "0"
        } else {
            val1 += "0"
            val2 += "1"
        }
    })
    return [val1, val2]
}

const computeDay3_1: ComputeFunction = (mode, day) => {
    const filename = getFileName(mode, day)
    const content = parseInput(filename)

    const binaries = getBinaries(content)

    const mostSomething = getMostAndLeastCommon(binaries)

    return parseInt(mostSomething[0], 2) * parseInt(mostSomething[1], 2)
}

export const getDay3_1: (mode: string) => (GetFunction|number)[] = (mode) => {
    const day = "3-1"
    const answer = 198
    const solution = 3885894
    if(mode === "test")
        return [answer, computeDay3_1(mode, day)]
    else 
        return [solution, computeDay3_1(mode, day)]
}

export const getDay3_2: (mode: string) => (GetFunction|number)[] = (mode) => {
    const day = "3-1"
    const answer = 230
    const solution = 0
    if(mode === "test")
        return [answer, computeDay3_2(mode, day)]
    else 
        return [solution, computeDay3_2(mode, day)]
}

const getValues: (key: string, content: string[]) => string | undefined = (key, content) => {
    let arr: string[] = []
    for(let i =0; i< key.length; i++) {
        if (content.length === 1) {
            return content.pop()
        }
        if (content.length === 0) {
            return arr.pop()
        }
        if (isMostCommonOne(content.map(item => item.charAt(i)))) {
            content.filter(item => item.charAt(i) === "1")
        } else {
            content.filter(item => item.charAt(i) === "0")
        }
        
        
        if (content.length > 0) {
            arr = []
            arr = [...content]
        }
    }
    if (content.length > 1) {
        getValues(key, arr)
    } else {
        return content.pop()
    }
}

const computeDay3_2: ComputeFunction = (mode, day) => {
    const filename = getFileName(mode, day)
    const content = parseInput(filename)
    const binaries = getBinaries(content)
    const [mostCommon, leastCommon] = getMostAndLeastCommon(binaries)
    
    const val1 = getValues(mostCommon, content)
    const val2 = getValues(leastCommon, content)
    const result = val1 && val2 && parseInt(val1, 2) * parseInt(val2, 2)

    return result ? result : 0
}