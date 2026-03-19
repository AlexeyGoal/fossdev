.DEFAULT_GOAL := help 


create-practice:
ifdef PRACTICE
    ${error must pass val via PRACTICE}
endif
    @echo "creating practice"
    mkdir -p ${PRACTICE}

remove-practice:
ifdef PRACTICE
	${error}
endif 
    rm -rf ${PRACTICE}

help:
    @echo "This makefile for repo-level activity"


