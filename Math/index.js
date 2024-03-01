let myList = [3, 7, 2, 8, 10, 5];
let maxSoFar = -Infinity;
let minSoFar = Infinity;

for (let i = 0; i < myList.length; i++) {
    maxSoFar = Math.max(maxSoFar, myList[i]);
    minSoFar = Math.min(minSoFar, myList[i]);
    console.log("Maximum value from index 0 to", i, ":", maxSoFar);
    console.log("Minimum value from index 0 to", i, ":", minSoFar);
}
