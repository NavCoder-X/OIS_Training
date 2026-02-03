# Compilatore e flag
CXX = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -O2

# Trova tutti i file .cpp nella directory
SOURCES = $(wildcard *.cpp)
PROGRAMS = $(SOURCES:.cpp=.exe)

# Target di default
.PHONY: all build run clean list help test-all input output

all: build

# ========== COMPILAZIONE ==========

# Compila tutti i programmi
build: $(PROGRAMS)

# Regola generale per compilare ogni .cpp
%.exe: %.cpp
	$(CXX) $(CXXFLAGS) -o $@ $<
	@echo "✓ Compilato: $@"

# ========== ESECUZIONE ==========

# Esegui il primo programma con input.txt
run: build
	@if [ -f "$(firstword $(PROGRAMS))" ]; then \
		./$(firstword $(PROGRAMS)) < input.txt > output.txt; \
		echo "Output salvato in output.txt"; \
	else \
		echo "Nessun programma trovato"; \
	fi

# Esegui un programma specifico: make run-filename
run-%: %.exe
	@if [ -f "$<" ]; then \
		./$< < input.txt > output.txt; \
		echo "Output di $< salvato in output.txt"; \
	else \
		echo "File $< non trovato"; \
	fi

# Esegui interattivamente il primo programma
interactive: build
	@./$(firstword $(PROGRAMS))

# Esegui un programma specifico in modo interattivo: make interactive-filename
interactive-%: %.exe
	@./$<

# ========== VISUALIZZAZIONE ==========

# Mostra l'input
input:
	@cat input.txt

# Mostra l'output
output:
	@cat output.txt

# Lista tutti i programmi compilabili
list:
	@echo "Programmi disponibili:"
	@for prog in $(SOURCES); do \
		echo "  - $$prog -> $${prog%.cpp}.exe"; \
	done

# ========== PULIZIA ==========

# Pulisci tutti i file compilati
clean:
	@rm -f $(PROGRAMS) *.o
	@echo "✓ File puliti"

# Pulisci un programma specifico: make clean-filename
clean-%:
	@rm -f $*.exe $*.o
	@echo "✓ Pulito: $*.exe"

# ========== TEST ==========

# Compila ed esegui tutti i programmi
test-all: build
	@echo "Test di tutti i programmi:"
	@for prog in $(PROGRAMS); do \
		echo "\n--- Eseguo $$prog ---"; \
		./$$prog < input.txt; \
	done

# ========== HELP ==========

help:
	@echo "╔════════════════════════════════════════════════════════════════╗"
	@echo "║         CodeForces Solutions - Makefile Help                   ║"
	@echo "╚════════════════════════════════════════════════════════════════╝"
	@echo ""
	@echo "COMPILAZIONE:"
	@echo "  make build                  - Compila tutti i programmi"
	@echo "  make list                   - Lista i programmi disponibili"
	@echo ""
	@echo "ESECUZIONE (usa input.txt):"
	@echo "  make run                    - Esegui il primo programma"
	@echo "  make run-filename           - Esegui programma specifico"
	@echo "  make test-all               - Testa tutti i programmi"
	@echo ""
	@echo "ESECUZIONE INTERATTIVA:"
	@echo "  make interactive            - Esegui interattivo (primo)"
	@echo "  make interactive-filename   - Esegui interattivo (specifico)"
	@echo ""
	@echo "VISUALIZZAZIONE:"
	@echo "  make input                  - Mostra input.txt"
	@echo "  make output                 - Mostra output.txt"
	@echo ""
	@echo "PULIZIA:"
	@echo "  make clean                  - Rimuovi tutti i file compilati"
	@echo "  make clean-filename         - Rimuovi programma specifico"
	@echo ""
	@echo "AIUTO:"
	@echo "  make help                   - Mostra questo messaggio"
	@echo ""
	@echo "ESEMPI:"
	@echo "  make build && make run-problem1"
	@echo "  make interactive-problem2"
	@echo "  make test-all"
