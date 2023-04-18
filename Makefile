# run the command "make install" to install requirements and run the command "make run" to run the program
# run the command "make clean" to remove all the files and folders except the Makefile, main.py, requirements.txt and .venv
# run the command "make help" to see the commands

# install requirements
install:
	pip install -r requirements.txt
	sudo apt-get install poppler-utils
	sudo apt-get install tesseract-ocr

# run the program
run:
	python3 main.py

# remove all the files and folders except the Makefile, main.py, requirements.txt and .venv
clean:
	find . -maxdepth 1 -type f -not -name "Makefile" -not -name "main.py" -not -name "requirements.txt" -delete
	find . -maxdepth 1 -type d -not -name "." -not -name ".." -not -name ".venv" -exec rm -rf {} +

# show the commands
help:
	@echo "install - install requirements"
	@echo "run - run the program"
	@echo "clean - remove all the files and folders except the Makefile, main.py, requirements.txt and .venv"
	@echo "help - show the commands"
