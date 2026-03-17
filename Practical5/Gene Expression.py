import matplotlib.pyplot as plt

#establish the dictionary for the gene expression data
gene_expression = {"TP53": 12.4, "EGFR": 15.1, "BRCA1": 8.2, "PTEN": 5.3, "ESR1": 10.7}

#Print innitial gene expression data
print("Initial Gene Expression Data:")
for gene, expression in gene_expression.items():
    print(f"{gene}: {expression}")

#Add a new gene to the dictionary
gene_expression["MYC"] = 11.6
print(f"\nAfter adding MYC:") 
for gene, expression in gene_expression.items():
    print(f"{gene}: {expression}")

#Draw a bar chart to visualize the gene expression levels
plt.figure(figsize=(10, 5))
plt.bar(gene_expression.keys(), gene_expression.values(), color='skyblue')
plt.xlabel('Genes')
plt.ylabel('Expression Level') 
plt.title('Gene Expression Levels in Sample')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

#Search for the target gene in the dictionary
target_gene = "EGFR"
print(f"\nSearching for {target_gene} in the gene expression data...")
if target_gene in gene_expression:
    print(f"\n{target_gene} is present in the dictionary with expression level: {gene_expression[target_gene]}")
else:
    print(f"\n{target_gene} is not present in the dictionary.")

#Calculate the average expression level of all genes
average_expression = sum(gene_expression.values()) / len(gene_expression)
print(f"\nAverage gene expression level: {average_expression:.2f}")  