# Pareto on naming

### Do pareto rule (80/20) applies to naming?

tl;dr: Yes, as a rule of thumb.

<sup>Disclaimer: This is not a formal academic research, it's just an attempt to obtain an heuristic of the class names.</sup>

### Objective
Determine if words used for naming classes in codebase follows the pareto rule (80/20)

### Overview
1. Extract words used for class names from open source projects
2. Sort the words by frequency
3. Combine the datasets
4. Analyze

### Procedure
1. Filtered words in the codebase of many open source projects
2. Selected the top 1K of most repeated words for each project.
3. Sorted the words in each file, in descending order by their frequency
4. Combined the results of each file into a single one.
5. Using spreadsheet analyzed the distribution and frequency of the combined dataset

### Results

By combining the results of the following datasets:

* django_top_1k_class_words.txt
* chromium_top_1k_class_words.txt
* dotnet_top_1k_class_words.txt
* python_top_1k_class_words.txt
* rails_top_1k_class_words.txt
* spree_top_1k_class_words.txt

We can obtain the following result:
- **17% of the words appears in 82% of the times in classes names**

### Conclusions

* 20% of the words appears at least 80% of the times in class names.
* Then pareto rules holds for words used in class names (for this analysis)

### Apendix

* [Spreadsheet with the analysis](https://docs.google.com/spreadsheets/d/1OC2qfYwB4PP7pPVt4SRM-pHTIodGlRpDAyt-qQpPl-U/edit?usp=sharing)

Codebase versions used to generate the dataset:
```
* django_top_1k_class_words.txt - Using git commit ref: 107865780aa44914e21d27fdf4ca269bc61c7f01
* chromium_top_1k_class_words.txt - Using archive produced on Wed May  1 01:02:57 2013 from revision 197479
* dotnet_top_1k_class_words.txt - Using .Net Runtime version 7.0.7
* python_top_1k_class_words.txt - Using Python sources version 3.11.4
* rails_top_1k_class_words.txt - Using git commit ref: 06da26afbabb1681d3d680cac13f70f7623cf69a
* spree_top_1k_class_words.txt - Using Spree version 4.6.0
```
