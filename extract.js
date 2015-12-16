var fs = require('fs')
var repl = require('repl')
var glob = require('glob')
var esprima = require('esprima')
var espree = require('espree')

var documents = []
glob('sample/d3/src/**/*.js', function(err, files) {
  for (var i=0; i<files.length; i++) {
    console.log(i + '/' + files.length);
    var file = files[i];
    try {
      var words = [];
      var code = fs.readFileSync(file, 'utf-8')
      // var ast = esprima.parse(code);
      var ast = espree.parse(code);
      var tokens = esprima.tokenize(code)
      tokens.forEach( function (token) {
        for (var key in token) {
          if (key=='value') words.push(token[key]);
        }
      })
      documents.push(words);
    }
    catch(err) {
      console.log(err);
    }
  }
})

var json = JSON.stringify(documents, null, 2);
fs.writeFileSync('documents.json', json);

// var rp = repl.start('> ')
// rp.context.documents = documents;