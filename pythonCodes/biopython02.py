from Bio.KEGG import REST

human_pathways = REST.kegg_list("pathway", "hsa").read()

# Filtar para humanos, Ascorbate
Ascorbate_pathways = []
for line in human_pathways.rstrip().split("\n"):
    entry, description = line.split("\t")
    if "Ascorbate" in description:
        Ascorbate_pathways.append(entry)

# Pegar genes da via de Ascorbate e adicionar em uma lista
Ascorbate_genes = [] 
for pathway in Ascorbate_pathways:
    pathway_file = REST.kegg_get(pathway).read()  # for each pathway

    # Iterar sobre o pathway
    current_section = None
    for line in pathway_file.rstrip().split("\n"):
        section = line[:12].strip()  # nomes na 12a coluna
        if not section == "":
            current_section = section
        
        if current_section == "GENE":
            gene_identifiers, gene_description = line[12:].split("; ")
            gene_id, gene_symbol = gene_identifiers.split()

            if not gene_symbol in Ascorbate_genes:
                Ascorbate_genes.append(gene_symbol)

print("Existe(m) %d vias de Ascorbate e %d genes relacionados.\\ OS genes são:" % \
      (len(Ascorbate_pathways), len(Ascorbate_genes)))
print(", ".join(Ascorbate_genes))        