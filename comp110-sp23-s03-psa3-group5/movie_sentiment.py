"""
Module: movie_sentiment

Program to analyze movie reviews and predict the sentiment of new reviews.

Authors:
1) Will Dobrzanski - wdobrzanski@sandiego.edu
2) Jared Gutierrez - jaredgutierrez@sandiego.edu
"""

def average_review(word, review_filename):
    """
    This function will loop through all the reviews in the movie review file and calculate/return
    the average score of the reviews that contain the given word.

    Parameters:
    word (type: string): The word to look for in the reviews.
    review_filename (type: file): contains the name of a file containing movie reviews
    Returns:
    (type: float) returns the average review score of a word.
    """

    review_file = open(review_filename, 'r')
    score = 0
    sc = 0
    lw = word.lower()

    for line in review_file:
        # make lower case to avoid case sensitivity
        lower_line = line.lower()
        lower_line = lower_line.split()
        found = False
        for x in lower_line[1:]:
            if lw == x:
                found = True
        if found:
            score += int(lower_line [0])
            sc += 1


    # done reading file, so close it
    review_file.close()
    #calculate the average review score
    if sc > 0:
        score = float(score/sc)
        return score
    else:
        return None

def estimate_review_score(movie_review, review_filename):
    """
    The function should return the estimated review score for that review. This estimated review score
    should be calculated by summing up the average review of each word in the review, and
    dividing that by the number of words in the review

    Parameters:
    moview_review (type: string): Contains a movie review.
    review_filename (type: string): contains the name of a file containing movie reviews
    Returns:
    (type: float) returns the average review score of a movie.
    """
    score = 0
    w = 0
    mr = [*movie_review]
    index = 0
    for ch in mr:
        if "." == ch:
            mr[index] = ""
        if "," == ch:
            mr[index] = ""
        if "!" == ch:
            mr[index] = ""
        if "-" == ch:
            mr[index] = ""
        index += 1

    t = ""
    for i in mr:
        t += i
    print(t)
    mr = t.split()
    for word in mr:
        score += average_review(word, review_filename)
        w += 1

    if w > 0:
        score = float(score/w)
        return score
    else:
        return 2.0



def estimate_user_review():
    """
    Asks user to enter a movie review, then the name of a file with existing
    movie reviews.
    It then calculates the estimated rating of the review they entered, along
    with a description of that rating (e.g. "neutral" or "slightly positive").
    """

    rev = input("Enter movie review")
    rev_filename = input("Enter name of file containing review")
    score = estimate_review_score(rev, rev_filename)
    tscore = round(score)
    txscore = ""
    if tscore == 0:
        txscore = "negative"
    elif tscore == 1:
        txscore = "somewhat negative"
    elif tscore == 2:
        txscore = "neutral"
    elif tscore == 3:
        txscore = "somewhat positive"
    elif tscore == 4:
        txscore = "positive"
    
    print("Estimated score: " + str(score) + " (" + txscore +")")

# Do not modify anything after this point.
if __name__ == "__main__":
    estimate_user_review()
