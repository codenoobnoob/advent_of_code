import {getDay1, getDay1_2} from './days/day1'
import { getDay2_1, getDay2_2} from './days/day2'
import {getDay3_1, getDay3_2} from './days/day3'


const getSolution: (day?:number) => Array<any>[] = (day = 0) => {
    const data: Array<any>[] = []
    const functions = [
        getDay1, 
        getDay1_2, 
        getDay2_1, 
        getDay2_2, 
        getDay3_1,
        getDay3_2,
    ]
    if (day !== 0) {
        data.push([functions[day-1]("test"), functions[day-1]("exec")])
        return data
    }
    functions.forEach(func => {
        data.push([func("test"), func("exec")])
    })

    return data
}

export default getSolution