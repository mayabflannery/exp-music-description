const fs = require("fs")

const searchLocation = `./resources/music`


fs.readdir(searchLocation, (err, files) => {
  if (err) {
    throw err;
  }
  console.log(files);
});

console.log(`Searching ${searchLocation} directory...`);
