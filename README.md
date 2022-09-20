<img src="https://github.com/waldeyr/bsb2019/blob/master/img/bsb2022.png" alt="Brazilian Symposium on Bioinformatics" width="600"/>

# Brazilian Symposium on Bioinformatics Minicurso: Bancos de Dados Biológicos

[Waldeyr Mendes Cordeiro da Silva](http://lattes.cnpq.br/2391349697609978)

## Introdução à Biologia Molecular

### Dogma

<img src="https://github.com/waldeyr/bsb2019/blob/master/img/dogma.jpg" width="800" alt="https://en.wikipedia.org/wiki/Central_dogma_of_molecular_biology"/>

---

<img src="https://github.com/waldeyr/bsb2019/blob/master/img/dogma_tt.png" width="800"/>

---

<img src="https://github.com/waldeyr/bsb2019/blob/master/img/dna01.png" width="800" alt="https://www.my46.org/intro/what-is-dna"/>

---

<img src="https://github.com/waldeyr/bsb2019/blob/master/img/dna02.png" width="800" alt="https://www.my46.org/intro/what-is-dna"/>

---

### Sequenciamento de DNA

* Obter string(s) representando as moléculas que compõem o DNA 
* Ainda não é possível sequenciar toda a molécula diretamente
* Sequenciar pedaço da molécula começando em alguma posição na direção 5' → 3'
* Fragmento (read): substring de uma das fitas da molécula alvo de DNA

Não sabemos:

* A que fita pertence
* A posição relativa ao início da fita


## Dados de Sequenciamento

### FASTQ
<img src="https://github.com/waldeyr/bsb2019/blob/master/img/fastq.png" width="600"/>
Exemplo de identificador Illumina:

* @HWUSI-EAS100R:6:73:941:1973#0/1

* HSWUSI-EAS100R → Unique instrument name

* 6 → Flowcell lane

* 73 → Tile number within the flow cell lane

* 941 → x-coordinate of the cluster within the tile

* 1973 → y-coordinate of cluster within the tile

* #0 → Index number for multiplexed sample

* /1 → Member of a pair

---

<img src="https://github.com/waldeyr/bsb2019/blob/master/img/phred.png" width="600"/>

---

A qualidade de cada nucleotídeo sequenciado é representada pelo caractere correspondente da tabela ASCII (33 a 126). Os valores sofreram um shift down para 0 a 93 por compatibilidade com a escala PHRED de qualidade que varia de 0 a 60.

É possível gerar relatórios de qualidade das sequências e filtrá-las com softwares como o fastqc, quast, sickle e trimmomatic.

---

<img src="https://github.com/waldeyr/bsb2019/blob/master/img/filtragem.png" width="800"/>

### FASTA

<img src="https://github.com/waldeyr/bsb2019/blob/master/img/fasta.png" width="800"/>

---

Pode ser usado para nucleotídeos ou aminoácidos e consiste basicamente de 2 partes:

* Um cabeçalho iniciado por `>` seguido de um identificador da sequência e outras informações. Alguns bancos de dados tem padrões para este cabeçalho. 
* Na linha seguinte ao cabeçalho aparece a sequência em si. 

Pode haver várias sequências em um meesmo arquivo (multifasta).

### SAM/BAM

Alinhamentos pós-processados de reads.

SAM (Sequence Alignment/MAP) guarda o alinhamento das reads e pode ser lido por diversos softwares como o IGV (Integrated Genome Viewer).

BAM (Binary Alignment/MAP) é uma versão comprimida de um alinhamento das reads. Pode ser obtido diretamente do alinhamento ou convertido a partir de um arquivo SAM.

---

<img src="https://github.com/waldeyr/bsb2019/blob/master/img/igv.png" width="800"/>

### BED

<img src="https://github.com/waldeyr/bsb2019/blob/master/img/bed.png" width="800"/>

---

BED é um arquivo organizado em colunas separadas por tabulação (tab) com anotações da sequência e também pode ser aberto em um genome browser como o IGV.

Arquivos BED têm 12 colunas, 1-3 obrigatórias, 4-12 opcionais

1. *chrom* → nome do cromossomo no qual a feature existe
2. *start* → posição inicial na sequência
3. *end* → posição final na sequência
4. name → nome da feature
5. score → 0 and 1000 determina o nível de cinza mostrado, sendo 1000 mais escuro. Pode ser usado para 
outras medidas, como p-values, up/down, enriquecimento
6. strand → direção da fita “+” ou “-”
7. thickStart → posição inicial onde a feature é desenhada
8. thickEnd → posição final onde a feature é desenhada
9. itemRgb → determina a cor dos dados
10. blockCount → número de bloco (exons)
11. blockSizes → lista de blocos separados por vírgula
12. blockStarts → lista de posições iniciais dos blocos

### GFF

Arquivos GFF são similares aos BED e têm 9 colunas, todas obrigatórias:

1. *seqname* → nome da sequência
2. *source* → origem da feature
3. *feature* → tipo de feature, equivalente ao campo name do BED
4. *start* → posição inicial
5. *end* → posição final
6. *score* → assim como o arquivo BED permite níveis de valores representando a expressividade da anotação
7. *strand* → direção da fita “+” ou “-”
8. *frame* → frame da sequência codificadora: “0”,“1”,“2” ou “.”,
9. *attribute* → muda conforme a versão do GFF (GFF1, GFF2, GFF3) e denota texto descritivo do significado biológico


## Bancos de Dados Biológicos

Vamos explorar os bancos de dados biológicos a partir de um problema dado:

Vitaminas são compostos orgânicos que precisam ser obtidos através da dieta:

* O organismo não produz as enzimas necessárias para sintetizá-la
* Não são produzidas em quantidade suficiente

Vitaminas que humanos não conseguem sintetizar: A, B1 (thiamine), B2 (riboflavin), B5 (pantothenic acid), B6 (pyridoxine), B7 (biotin), B9 (folate), B12 (cobalamin), E, K.

A vitamina C é produzida no fígado por mamíferos e alguns pássaros e nos rins por peixes, anfíbios, repteis e alguns pássaros. Ela é solúvel em água, tem propriedades antioxidantes e é essencial na síntese de colágeno.

---

<img src="https://github.com/waldeyr/bsb2019/blob/master/img/problema.png" width="600" alt="10.3389/fphys.2015.00397"/>

---
Qual a matéria prima para a vitamina C ?

Como essa materia prima é transformada no organismo?

Qual a enzima que inicia o processo ?

Como é identificada uma e de onde vem a enzima UTP---glucose-1-phosphate uridylyltransferase?

1. [BRENDA Database: 2.7.7.9](https://www.brenda-enzymes.org/enzyme.php?ecno=2.7.7.9)
2. [KEGG pathway Amino sugar and nucleotide sugar metabolism](https://www.genome.jp/kegg-bin/show_pathway?map00520+2.7.7.9)
3. [KEGG Reaction](https://www.genome.jp/dbget-bin/www_bget?rn:R00289)
4. [KEGG Compounds (Uridine triphosphate)](https://www.genome.jp/dbget-bin/www_bget?cpd:C00075)
* [PubChem (Uridine triphosphate)](https://pubchem.ncbi.nlm.nih.gov/substance/3375)
5. [KEGG Compounds (D-Glucose 1-phosphate)](https://www.genome.jp/dbget-bin/www_bget?cpd:C00103)
* [PubChem (D-Glucose 1-phosphate)](https://pubchem.ncbi.nlm.nih.gov/substance/3403)
6. [KEGG Enzyme UTP---glucose-1-phosphate uridylyltransferase: 2.7.7.9](https://www.genome.jp/dbget-bin/www_bget?ec:2.7.7.9)
7. [KEGG Gene UGP2](https://www.genome.jp/dbget-bin/www_bget?hsa:7360)
* [Uniprot](https://www.uniprot.org/uniprot/Q16851)
* [PDB](https://www.genome.jp/dbget-bin/www_bget?pdb:4R7P)

## Acesso aos dados via API com Biopython

### Obter dados de uma enzima

```python
from Bio.KEGG import REST
from Bio.KEGG import Enzyme
request = REST.kegg_get("ec:2.7.7.9")
open("ec_2.7.7.9.txt", "w").write(request.read())
records = Enzyme.parse(open("ec_2.7.7.9.txt"))
record = list(records)[0]
record.classname
record.entry
```

### Obter todos os genes relacionados com a via metabólica de'vitamina C

```python
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
```

### Obter detalhes da enzima UTP---glucose-1-phosphate uridylyltransferase   

```python
from Bio import ExPASy
from Bio import SeqIO
with ExPASy.get_sprot_raw("Q16851") as handle:
    seq_record = SeqIO.read(handle, "swiss")
print(seq_record.id)
print(seq_record.name)
print(seq_record.description)
print(repr(seq_record.seq))
print("Length %i" % len(seq_record))
print(seq_record.annotations["keywords"])
```    

### Uniprot API

[Uniprot API](https://www.uniprot.org/help/programmatic_access)
