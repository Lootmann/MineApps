// testdata
// const testdata =
//   "firstname,secondname\nwow0,how0\nwow1,how1\nwow2,how2\nwow3,how3\nwow4,how4\nwow5,how5\nwow6,how6\nwow7,how7\nwow8,how8\nwow9,how9";

const testdata = [
  { firstname: "wow0", secondname: "how0" },
  { firstname: "wow1", secondname: "how1" },
  { firstname: "wow2", secondname: "how2" },
  { firstname: "wow3", secondname: "how3" },
  { firstname: "wow4", secondname: "how4" },
  { firstname: "wow5", secondname: "how5" },
  { firstname: "wow6", secondname: "how6" },
  { firstname: "wow7", secondname: "how7" },
  { firstname: "wow8", secondname: "how8" },
  { firstname: "wow9", secondname: "how9" },
];

const input = document.getElementById("input");
input.value = JSON.stringify(testdata);

const result = document.getElementById("result");

/*
 * [
 *    {key: value, key: value, ...}
 *    {key: value, key: value, ...}
 *    ...
 * ]
 * */
function csv2json(text) {
  const lines = text.split("\n");

  // validtion
  // header has only column name
  const header = lines[0].split(",");

  let json = [];

  for (let i = 1; i < lines.length; i++) {
    // validation
    const rows = lines[i].split(",");
    const obj = {};
    for (let j = 0; j < header.length; ++j) {
      obj[header[j]] = rows[j];
    }
    json.push(obj);
  }

  return JSON.stringify(json);
}

function json2csv(text) {
  const json = JSON.parse(text);

  const header = Object.keys(json[0]);
  let csv = header + "\n";

  for (let i = 1; i < json.length; ++i) {
    const result = [];
    for (let h of header) {
      result.push(json[i][h]);
    }
    csv += result.join(",") + "\n";
  }

  return csv;
}

// buttons
const csv2jsonButton = document.getElementById("csv2json");
csv2jsonButton.addEventListener("click", function () {
  result.value = csv2json(input.value);
});

const json2csvButton = document.getElementById("json2csv");
json2csvButton.addEventListener("click", function () {
  result.value = json2csv(input.value);
});
