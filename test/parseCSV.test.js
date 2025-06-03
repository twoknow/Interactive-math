const assert = require('assert');

/**
 * Parses CSV text into an array of objects based on the new structure.
 * @param {string} csvText - The raw CSV string.
 * @returns {object[]} Array of row objects.
 */
function parseCSV(csvText) {
    const lines = csvText.trim().split('\n');
    lines.shift(); // Remove header line from CSV
    const result = [];

    lines.forEach(line => {
        const values = line.split(',');
        const rowObject = {};

        rowObject.chapter = values[0] ? values[0].trim() : '';
        rowObject.unit = values[1] ? values[1].trim() : '';
        rowObject.section = values[2] ? values[2].trim() : '';
        // values[3] (典型例题) - skipped
        // values[4] (交互类型) - skipped
        rowObject.scenario = values[5] ? values[5].trim() : '';

        let instance1 = values[6] ? values[6].trim() : '';
        let instance2 = values[7] ? values[7].trim() : '';

        let combinedInstances = (instance1 === "暂缺" || instance1 === "略" || !instance1) ? "" : instance1;
        if (instance2 && instance2 !== "暂缺" && instance2 !== "略") {
            if (combinedInstances) {
                combinedInstances += '\n' + instance2;
            } else {
                combinedInstances = instance2;
            }
        }
        rowObject.interactionInstances = combinedInstances;
        // values[8] (补充阅读材料) - skipped
        rowObject.aiActions = ''; // Placeholder for the button column

        result.push(rowObject);
    });
    return result;
}

// Sample CSV for testing
const sampleCSV = [
    '章节,单元,课节,典型例题,交互类型,场景,实例1,实例2,补充材料',
    'C1,U1,S1,,Type1,Scenario1,Link1,Link2,',
    'C2,U2,S2,,Type2,Scenario2,暂缺,Link4,'
].join('\n');

const expected = [
    {
        chapter: 'C1',
        unit: 'U1',
        section: 'S1',
        scenario: 'Scenario1',
        interactionInstances: 'Link1\nLink2',
        aiActions: ''
    },
    {
        chapter: 'C2',
        unit: 'U2',
        section: 'S2',
        scenario: 'Scenario2',
        interactionInstances: 'Link4',
        aiActions: ''
    }
];

// Run the test
const result = parseCSV(sampleCSV);
assert.deepStrictEqual(result, expected);
console.log('parseCSV test passed.');
