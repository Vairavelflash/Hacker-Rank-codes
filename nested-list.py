if __name__ == '__main__':
    students = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student = [name, score]
        students.append(student)
        scores.append(score)
        
    second_min_score = sorted(set(scores))[1]
   
    for x,y in sorted(students):
        if y == second_min_score:
            print (x)
      
                 
       