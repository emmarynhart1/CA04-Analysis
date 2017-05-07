import unittest

from Simple import get_authors, get_commits, read_file, get_dates

class TestCommits(unittest.TestCase):

    def setUp(self):
        self.data = read_file('changes_python.log')

    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.data))

    def test_number_of_commits(self):
        commits = get_commits(self.data)
        self.assertEqual(422, len(commits))

    def test_number_of_authors(self):
        commits = get_commits(self.data)
        authors = get_authors(commits)
        print authors
        self.assertEqual(10, len(authors))
        self.assertEqual(191, authors['Thomas'])

    def test_first_commit(self):
        commits = get_commits(self.data)
        self.assertEqual('Thomas', commits[0]['author'])
        self.assertEqual('r1551925', commits[0]['revision'])
        
    def test_first_date(self):
        commits = get_commits(self.data)
        self.assertEqual('x', commits[0]['date'])

if __name__ == '__main__':
    unittest.main()