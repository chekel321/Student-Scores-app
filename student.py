class Student(object):
    """Represents a student."""

    def __init__(self, name = "", numberOfScores = 3):
        """All scores are initially 0."""
        self.name = name
        self.scores = []

    def display(self):
        """Display name, scores, highest and average score of the student."""

        print(f"Name: {self.name} \nscores: {str(self.scores[0])} {str(self.scores[1])} {str(self.scores[2])}\nHigh Score: {self.getHighScore()} \nAverage: {self.getAverage()}\n" )

    def getNumberOfScores(self):
        """Returns the number of scores."""
        return self.scores

    def getName(self):
        """Returns the student's name."""
        return self.name
    def setScore(self, i, score):
        """Resets the ith score, counting from 0."""
        self.scores.insert(i, score)

    def getScore(self, i):
        """Returns the ith score, counting from 0."""

        return self.scores[i]
    def getAverage(self):
        """Returns the average score."""
        ave = float(sum(self.scores) / len(self.scores))
        ave = str(round(ave, 2))
        return ave

    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)

from random import randint

def main(numScores = 3):
    """Tests sorting."""
    # Create the list and put 5 students into it
    students = list()
    names = ("Juan", "Bill", "Stacy", "Maria", "Charley")
    for name in names:
        s = Student(name, numScores)
        for index in range(numScores):
            s.setScore(index, randint(70, 100))
        students.append(s)
    # Print the contents
    print("The list of students:\n")
    for s in students:
        s.display()

if __name__ == "__main__":
    main()
