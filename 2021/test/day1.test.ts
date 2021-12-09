import getTestData from '../src/index'
const data = getTestData()

data.forEach(dataSet => {
    test(`day-1-test`, () => {
        const exampleAnswer = dataSet[0][0]
        expect(dataSet[0][1]).toBe(exampleAnswer)
    })
    
    test("puzzle-exec", () => {
        const exampleAnswer = dataSet[1][0]
        expect(dataSet[1][1]).toBe(exampleAnswer)
    })

})
