import {parseInput, arrayNumToInt} from "../src/helpers/fileParser"

test("fileparser", () => {
    const content = parseInput("mock1")
    expect(content).toStrictEqual(["123","1234","12345"])
    if (content === undefined) {
        fail("content is undefined")
    }
    expect(arrayNumToInt(content)).toStrictEqual([123,1234,12345])
})
