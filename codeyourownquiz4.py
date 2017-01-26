# This list is for the full answers for the various quizzes.
quizfullanswer = ["An operator is a special symbol in Python that carries out arithmetic or logical expressions. Some operations include <= which means less than or equal to, + which means addition, and == which means equal.",
"A loop statement allows us to execute a statement or group of statements multiple times. A for loop is a type of loop when you want a piece of code to repeat a specific number of times. A while loop is a type of loop when you run a piece of code until a condition is met. A nested loop is when you have a loop inside another loop.",
"Python was invented by Guido van Rossum as a successor to ABC language. It writes fewer lines of code compared to other programming languages like C++ or Java."]


# These are my lists for my three tuples with each one corresponding to a difficulty level (easy is quiz1, medium is quiz2, and hard is quiz3). I looked it up and adapted it for this project. Each one does double duty asking the quiz question and the prompt to answer the quiz question. It also fills in the blanks as the quiz progresses. Used the """ to get line breaks to make the quiz look neater. 
quiz1 = [
		("""An ___1___ is a special symbol in Python that carries out arithmetic or logical expressions. Some operations include ___2___ which means less than or equal to, ___3___ which means addition, and ___4___ which means equal.
		
"What is the answer to ___1___? """, "operator"),
		("""An operator is a special symbol in Python that carries out arithmetic or logical expressions. Some operations include ___2___ which means less than or equal to, ___3___ which means addition, and ___4___ which means equal. 

What is the answer to ___2___?""", "<="),
		("""An operator is a special symbol in Python that carries out arithmetic or logical expressions. Some operations include <= which means less than or equal to, ___3___ which means addition, and ___4___ which means equal.
		
What is the answer to ___3___? """, "+"),
		("""An operator is a special symbol in Python that carries out arithmetic or logical expressions. Some operations include <= which means less than or equal to, + which means addition, and ___4___ which means equal.
		
What is the answer to ___4___? """, "==")]

quiz2 = [
		("""A ___1___ statement allows us to execute a statement or group of statements multiple times. A ___2___ loop is a type of loop when you want a piece of code to repeat a specific number of times. A ___3___ loop is a type of loop when you run a piece of code until a condition is met. A ___4___ loop is when you have a loop inside another loop.
		
What is the answer for ___1___? """, "loop"),
		("""A loop statement allows us to execute a statement or group of statements multiple times. A ___2___ loop is a type of loop when you want a piece of code to repeat a specific number of times. A ___3___ loop is a type of loop when you run a piece of code until a condition is met. A ___4___ loop is when you have a loop inside another loop.
	
What is the answer for ___2___? """, "for"),
		("""A loop statement allows us to execute a statement or group of statements multiple times. A for loop is a type of loop when you want a piece of code to repeat a specific number of times. A ___3___ loop is a type of loop when you run a piece of code until a condition is met. A ___4___ loop is when you have a loop inside another loop.
		
What is the answer for ___3___? """, "while"),
		("""A loop statement allows us to execute a statement or group of statements multiple times. A for loop is a type of loop when you want a piece of code to repeat a specific number of times. A while loop is a type of loop when you run a piece of code until a condition is met. A ___4___ loop is when you have a loop inside another loop.
		
What is the answer for ___4___? """, "nested")]

quiz3 = [
		("""Python was invented by ___1___ as a successor to ___2___. It writes fewer lines of code compared to other programming languages like ___3___ or ___4___.		

What is the answer for ___1___? """, "guido van rossum"),
		("""Python was invented by Guido van Rossum as a successor to ___2___. It writes fewer lines of code compared to other programming languages like ___3___ or ___4___.
	
What is the answer for ___2___? """, "abc language"),
		("""Python was invented by Guido van Rossum as a successor to ABC language. It writes fewer lines of code compared to other programming languages like ___3___ or ___4___.
		
What is the answer for ___3___? """, "c++"),
		("""Python was invented by Guido van Rossum as a successor to ABC language. It writes fewer lines of code compared to other programming languages like C++ or ___4___.
		
What is the answer for ___4___? """, "java")]

quiz = [quiz1, quiz2,quiz3]

# This function now combines my previous easy, medium, and hard functions into just one function. Using the 'quiz' parameter helps in consolidating those three previously similar functions into one function. 
def play_game(quiz):
	
	#Used a for loop to go through the varous tuples listed.
	for question, answer in quiz:
		quizQuestion = raw_input(question + "")
		attempts = 0
		# The 'tries' is to fix the magic number issue.
		tries = 3
		
		#This is to limit the attempts to three tries.
		while attempts < tries:
			attempts += 1
			#The if statements check if the answer is right or not.
			if quizQuestion.lower() == answer:
				print "Correct", "\n"
				break	
		
			else: 
				print "Try Again", "\n"
				quizQuestion = raw_input(question + "")
				#This one stops the attempts at three tries when I equaled attempts and tries. After the third try, the quiz gives the quiz taker the right answer.
				if attempts ==  tries and quizQuestion.lower() == answer:
					print "Correct", "\n"
					break
				elif attempts == tries and quizQuestion.lower() != answer: 
					print "Sorry too many tries. The answer was " + answer + ".", "\n"
		
	return 


# This puts the if statements for the difficulty options in my previous attempts into one neat function. 	
def start_game():
	# This asks the difficulty option question and starts the quiz.
	difficulty = raw_input("Hello, please pick a difficulty level: Easy, Medium, Hard: ")
	print ""

	# The quiz branches off here to three options depending on what difficulty option the quiz taker takes.
	if difficulty.lower() == "easy":
		play_game(quiz[0])
		print "This is the correct answer:", quizfullanswer[0]
	elif difficulty.lower() == "medium":
		play_game(quiz[1])
		print "This is the correct answer:", quizfullanswer[1]
	elif difficulty.lower() == "hard": 
		play_game(quiz[2])
		print "This is the correct answer:", quizfullanswer[2]
	else: 
		print "You did not follow directions."

	# This ends the quiz. 
	print "\n", "Thank you for taking my quiz!"	

# Quiz starts here and uses the function start_game().
start_game()





