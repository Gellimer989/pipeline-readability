require 'rust'
require 'code-assertions'
require 'set'

Dir.chdir(File.join(File.expand_path(File.dirname(__FILE__)), "..", ".."))

parents = Rust::CSV.read('data/dataset/parentFiltered.csv', headers: true)
metrics = Rust::CSV.read('data/dataset/metrics.csv', headers: true)

after_version  = {}
before_version = {}
reponames = {}

index = 0
after_commit = nil
last_repo = nil
parents.each do |row|
    if index.odd?
        after_version[row['CommitId']] = after_commit
        before_version[after_commit]   = row['CommitId']
        
        assert { row['Redable']  == 0 }
        assert { row['RepoName'] == last_repo }
    else
        after_commit = row['CommitId']
        assert { row['Redable'] == 1 }
    end
    
    #p reponames[row['CommitId']]
    #p row['RepoName']
    #assert { reponames[row['CommitId']] == nil || reponames[row['CommitId']] == row['RepoName'] }
    
    reponames[row['CommitId']] = row['RepoName']
    
    last_repo = row['RepoName']
    index += 1
end

METRICS = metrics.colnames - ['FileName']
deltas = Rust::DataFrame.new(['repo', 'before', 'after'] + METRICS)

hashed_metrics = {}
metrics.each do |row|
    commit = row['FileName'].split(".").first
    hashed_metrics[commit] = row
end

done = Set[]
hashed_metrics.each do |commit, row|    
    before = before_version[commit]
    if before && !done.include?(before)
        before_row = hashed_metrics[before]
        unless before_row
            warn "No rows found for #{before}, which comes before #{commit}"
            next
        end
        
        resulting_row = {}
        METRICS.each do |m|s
            resulting_row[m] = row[m] - before_row[m]
        end
        resulting_row['repo'] = reponames[before]
        resulting_row['before'] = before
        resulting_row['after'] = commit
        
        deltas << resulting_row
        done << before
    end
end

Rust::CSV.write("data/dataset/deltas.csv", deltas)

#p deltas
