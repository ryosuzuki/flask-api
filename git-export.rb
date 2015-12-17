require 'git_diff_parser'
require 'rugged'
require 'json'

repo = Rugged::Repository.new('sample/d3')
walker = Rugged::Walker.new(repo)
walker.sorting(Rugged::SORT_DATE)
walker.push(repo.head.target)
commits = {}
i = 0
walker.to_a[3490..3503].each do |commit|
  begin
    print "\s#{i}"
    id = commit.oid
    hash = {
      id: id,
      message: commit.message.force_encoding('UTF-8'),
      patch: commit.diff.patch.force_encoding('UTF-8'),
    }
    hash[:words] = hash[:patch].split(/(\s|,|;|\.|\(|\))/)
    i = i+1
    commits[id] = hash
  rescue
    puts "error #{i}"
    next
  end
end

File.open('documents.json', 'w') do |f|
  f.write(JSON.pretty_generate(commits))
end




