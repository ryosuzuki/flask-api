var fs = require('fs')
var repl = require('repl')
var glob = require('glob')
var esprima = require('esprima')
var espree = require('espree')
var Q = require('q')

var commits;
var stepA = function () {
  var data = fs.readFileSync('hoge.json', 'utf-8');
  commits = JSON.parse(data)
  for (var i=0; i<commits.length; i++) {
    var commit = commits[i];
    try {
      var tokens = esprima.tokenize(commit.patch)
      var words = [];
      tokens.forEach( function (token) {
        for (var key in token) {
          if (key=='value') words.push(token[key]);
        }
      });
      commit.words = words;
      commits[i] = commit;
    }
    catch (err) {
      console.log(err);
    }
  }
}

var stepB = function () {
  var rp = repl.start('> ')
  rp.context.commits = commits;
}

Q.fcall(stepA)
.then(stepB)
.done()


/*
var documents = []
glob('sample/d3/src/', function(err, files) {
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
  var json = JSON.stringify(documents, null, 2);
  fs.writeFileSync('documents.json', json);
})
*/

