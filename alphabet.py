# I think this is a problem from ICPC 2012 Gulf Coast Region?????

# Solution dictionary to cache optimal results for strings.
# Without this, the program works but wastes a lot of time finding scores for
# strings it has already checked.
sltn_dict = {}

def score_string(word):
    # Base case; if string is only 1 character wide, 1 character is in order.
    if len(word) == 1:
        return 1
    
    else:
        highest_subscore = 0

        # Look at every character coming after the first, and see how good
        # the score is when considering that character.
        for i in range(1, len(word)):
            subscore = 0
            
            # Check if the char at current index is higher than at the starting
            # one; if not, don't bother with it.
            # If it is, find the highest score for the string starting with
            # that letter.
            if word[i] > word[0]:
                # The if statement in here is just checking if the result is
                # already cached. If not, the result is calculated then cached.
                if word[i:] in sltn_dict:
                    subscore = sltn_dict[word[i:]]
                else:
                    subscore = score_string(word[i:])
                    sltn_dict[word[i:]] = subscore
                    
            # Update highest_subscore so when this for loop is over,
            # it is storing the highest score found.
            if subscore > highest_subscore:
                highest_subscore = subscore

        return 1 + highest_subscore

# This function finds the highest score out of all the different starting
# points in the string.
def find_number(word):
    best_score = 0
    for i in range(len(word)):
        score = score_string(word[i:])
        if score > best_score:
            best_score = score

    return best_score

# The problem spec asks for how many letters need to be added, not how
# many letters are already in order. So subtract the score from 26
# before output.
print(26 - find_number("xyzabcdefghijklmnopqrstuvw"))
print(26 - find_number("aiemckgobjfndlhp"))
