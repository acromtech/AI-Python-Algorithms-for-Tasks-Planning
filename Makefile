CURRENT_DIR = $(shell pwd)
PROJET_DIR = $(CURRENT_DIR)/projet

install_dependencies:
	pip3 install python-sat
	pip3 install python-constraint

all : 
	export PYTHONPATH=$(PROJET_DIR):$$PYTHONPATH ; \
	python3 $(PROJET_DIR)/etape2/Etape2.py > log2


diff_log :
	diff log $(PROJET_DIR)/tests/logReference

clear :
	\rm log

doc :	
	pdoc --html -f -o Doc $(PROJET_DIR)


