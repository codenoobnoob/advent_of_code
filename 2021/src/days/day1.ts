import {parseInput, arrayNumToInt, getInputData} from "../helpers/fileParser"
import {GetFunction} from "../types"


export const getDay1: (mode: string) => (GetFunction|number)[] = (mode) => {
    const answer = 7
    const solution = 1583
    const getAnswer: () => number = () => { 
        const measurements = getInputData(mode,"1-1")
        var solution = 0
        for(var i=1; i <= measurements.length; i++) {
            if (measurements[i] > measurements[i-1]) {
                solution += 1
            };
        }
        return solution;  
    }
    if(mode === "test")
        return [answer, getAnswer()]
    else 
        return [solution, getAnswer()]
}

const getSum: (data: number[], index: number) => number = (data, index) => {
    return data[index] + data[index+1] +data[index+2]
}

const getDiff: (data: number[], index: number) => boolean = (data, index) => {
    if(getSum(data, index) < getSum(data, index+1)){
        return true
    }
    return false
}

export const getDay1_2: (mode: string) => (GetFunction|number)[] = (mode) => {
    const answer = 5
    const solution = 1627
    const getAnswer: () => number = () => { 
        const measurements = getInputData(mode,"1-1")
        var solution = 0
        for(var i=0; i <= measurements.length-3; i++) {
            if (getDiff(measurements, i)) {
                solution += 1
            };
        }
        return solution;  
    }
    if(mode === "test")
        return [answer, getAnswer()]
    else 
        return [solution, getAnswer()]
}