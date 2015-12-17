require 'git_diff_parser'
require 'rugged'
require 'json'

repo = Rugged::Repository.new('sample/sift')
walker = Rugged::Walker.new(repo)
# walker.sorting(Rugged::SORT_DATE)
walker.push(repo.head.target)
commits = {}
i = 0
walker.each do |commit|
  id = commit.oid
  hash = {
    id: id,
    message: commit.message,
    patch: commit.diff.patch,
  }
  hash[:words] = hash[:patch].split(/(\s|,|;|\.|\(|\))/)
  commits[id] = hash
  print "\s#{i}"
  i = i+1
  break if (i > 0)
end

File.open('documents.json', 'w') do |f|
  f.write(JSON.pretty_generate(commits))
end




