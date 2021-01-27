PYTHON=python

all:
	$(PYTHON) dataAnalysis.py negData
	$(PYTHON) dataAnalysis.py posData
	mkdir -p traintest/negData traintest/posData
	$(PYTHON) split.py 0.15
	$(PYTHON) format2CSV.py traintest
	$(PYTHON) format2CSV.py original
	$(PYTHON) preProcess.py traintest
	$(PYTHON) preProcess.py original
	rm original.csv
	rm traintest.csv
    
clean:
	rm traintest/posData/*
	rm traintest/negData/*
	rmdir traintest/negData traintest/posData
	rmdir traintest
	rm traintestPreProcessed.csv
	rm originalPreProcessed.csv
	rm negDataAnalysis.csv
	rm posDataAnalysis.csv

