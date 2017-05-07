def read_file(changes_file):
    data = [line.strip() for line in open(changes_file, 'r')]
    return data

def get_commits(data):
    sep = 72*'-'
    commits = []
    current_commit = None
    index = 0
    while index < len(data):
        try:
            details = data[index + 1].split('|')
            commit = {'revision': details[0].strip(),
                'author': details[1].strip(),
                'date': details[2].strip(),
                'number_of_lines': details[3].strip().split(' ')[1]
            }
            commits.append(commit)
            index = data.index(sep)
        except IndexError:
            break
    return commits
    

def get_authors(commits):
    authors = {}
    for commit in commits:
        author = commit['author']
        if author not in authors:
            authors[author] = 1
        else:
            authors[author] = authors[author] + 1
    return authors
    
def get_dates(commits):
    dates = {}
    for commit in commits:
        date = commit['date']
        if date not in dates:
            dates[date] = 1
        else:
            dates[date] = dates[date] + 1

if __name__ == '__main__':
    changes_file = 'changes_python.log'
    data = read_file(changes_file)
    commits = get_commits(data)


    
    output = open("DataAnalysis.csv", 'w')
    index = 0
    for commit in commits:
        output.write(commits[index]['author'])
        output.write(';')
        output.write(commits[index]['revision'])
        output.write(';')
        output.write(commits[index]['date'])
        output.write(';')
        output.write(commits[index]['number_of_lines'])
        output.write(';')
        output.write('\n')
        index = index +1
    output.close()
        
           
keys = commits [0].keys()
dict = open('DataAnalysis.csv', 'wb') 
dict_writer = csv.DictWriter(dict,my_dict.keys())
dict_writer.writeheader()
dict_writer.writerows(commits)
dict.close()
    
    #index = 0
        #for commit in commits:
        #print (commits[index]['comment'])
        #index = index +1
        
print(len(data))
print(commits[0])
print(commits[1]['author'])
print(len(commits))
    