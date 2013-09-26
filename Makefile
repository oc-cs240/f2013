# Make target converts iPyhon Notebook files to Markdown
# Get listing of .ipynb files and corresponding .md files
IPYNB_FILES = $(shell find . -type f \( -name '*.ipynb' ! -wholename './.ipynb_checkpoints/*.ipynb' \))
MD_FILES = $(patsubst %.ipynb, %.md, $(IPYNB_FILES))

.PHONY: all
all: $(MD_FILES)

%.md: %.ipynb
	ipython nbconvert --to markdown $<

