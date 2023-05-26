const fs = require('fs');

function writeStringToFile(filePath, content) {
  fs.writeFile(filePath, content, { encoding: 'utf-8' }, (err) => {
    if (err) {
      console.error('Error occurred while writing to file:', err);
    } else {
      console.log('String written to file successfully.');
    }
  });
}

// Check if the script has received the correct number of arguments
if (process.argv.length !== 4) {
  console.log('Usage: node script.js <file_path> <content>');
} else {
  const filePath = process.argv[2];
  const content = process.argv[3];
  writeStringToFile(filePath, content);
}

