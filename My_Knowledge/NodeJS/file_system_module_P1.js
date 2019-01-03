const fs = require('fs');
// Create a file
// fs.writeFile('example.txt', "This is an Example", (err) => {
//   if(err)
//     console.log(err);
//   else {
//     console.log('File Successfully created');
//     fs.readFile('example.txt', 'utf8', (err, file) => {
//       if (err)
//         console.log(err);
//       else
//         console.log(file);
//     });
//   }
// })

// Rename a file
// fs.rename('example.txt', 'example2.txt', (err) => {
//   if (err)
//     console.log(err);
//   else
//     console.log('File Successfully Renamed');
// })

// Append Data to the file
// fs.appendFile('example2.txt', 'Some data being append', (err) => {
//   if (err)
//     console.log(err);
//   else
//     console.log(' File Successfully Append Data');
// })

fs.unlink('example2.txt', (err) => {
  if (err)
    console.log(err);
  else
    console.log('File Successfully Deleted');
})
