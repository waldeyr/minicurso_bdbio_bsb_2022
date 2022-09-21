<img src="https://github.com/waldeyr/minicurso_bdbio_bsb_2022/blob/main/img/bsb2022.png" alt="Brazilian Symposium on Bioinformatics" width="600"/>

# :school: Brazilian Symposium on Bioinformatics 

## :point_right: Minicurso de Bancos de Dados Biológicos


[Waldeyr Mendes Cordeiro da Silva](http://lattes.cnpq.br/2391349697609978)

## :notebook_with_decorative_cover: Introdução à Biologia Molecular

### Dogma

<img src="https://github.com/waldeyr/minicurso_bdbio_bsb_2022/blob/main/img/dogma.jpg" width="800" alt="https://en.wikipedia.org/wiki/Central_dogma_of_molecular_biology"/>

---

<img src="https://github.com/waldeyr/minicurso_bdbio_bsb_2022/blob/main/img/dogma_tt.png" width="800"/>

---

<img src="https://github.com/waldeyr/minicurso_bdbio_bsb_2022/blob/main/img/dna01.png" width="800" alt="https://www.my46.org/intro/what-is-dna"/>

---

<img src="https://github.com/waldeyr/minicurso_bdbio_bsb_2022/blob/main/img/dna02.png" width="800" alt="https://www.my46.org/intro/what-is-dna"/>

---

### Sequenciamento de DNA

* Obter string(s) representando as moléculas que compõem o DNA 
* Ainda não é possível sequenciar toda a molécula diretamente
* Sequenciar pedaço da molécula começando em alguma posição na direção 5' → 3'
* Fragmento (read): substring de uma das fitas da molécula alvo de DNA

Não sabemos:

* A que fita pertence
* A posição relativa ao início da fita


## :notebook_with_decorative_cover: Dados de Sequenciamento

### FASTQ
<img src="https://github.com/waldeyr/minicurso_bdbio_bsb_2022/blob/main/img/fastq.png" width="600"/>
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

<img src="https://github.com/waldeyr/minicurso_bdbio_bsb_2022/blob/main/img/phred.png" width="600"/>

---

A qualidade de cada nucleotídeo sequenciado é representada pelo caractere correspondente da tabela ASCII (33 a 126). Os valores sofreram um shift down para 0 a 93 por compatibilidade com a escala PHRED de qualidade que varia de 0 a 60.

É possível gerar relatórios de qualidade das sequências e filtrá-las com softwares como o fastqc, quast, sickle e trimmomatic.

---

<img src="https://github.com/waldeyr/minicurso_bdbio_bsb_2022/blob/main/img/filtragem.png" width="800"/>

### FASTA

<img src="https://github.com/waldeyr/minicurso_bdbio_bsb_2022/blob/main/img/fasta.png" width="800"/>

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

<img src="https://github.com/waldeyr/minicurso_bdbio_bsb_2022/blob/main/img/igv.png" width="800"/>

### BED

<img src="https://github.com/waldeyr/minicurso_bdbio_bsb_2022/blob/main/img/bed.png" width="800"/>

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


## :notebook_with_decorative_cover: Bancos de Dados Biológicos


Vamos explorar os bancos de dados biológicos a partir de um problema dado:

Vitaminas são compostos orgânicos que precisam ser obtidos através da dieta. A vitamina C é produzida no fígado por mamíferos e alguns pássaros e nos rins por peixes, anfíbios, repteis e alguns pássaros. Ela é solúvel em água, tem propriedades antioxidantes e é essencial na síntese de colágeno. Vitaminas que humanos não sintetiza ou não sintetiza em quantidade suficiente: A, B1 (thiamine), B2 (riboflavin), B5 (pantothenic acid), B6 (pyridoxine), B7 (biotin), B9 (folate), B12 (cobalamin), E, K.

* O organismo não produz as enzimas necessárias para sintetizá-la
* Não são produzidas em quantidade suficiente

---

<img src="https://github.com/waldeyr/minicurso_bdbio_bsb_2022/blob/main/img/problema.png" width="600" alt="10.3389/fphys.2015.00397"/>

---
Qual a matéria prima para a vitamina C ?

Como essa materia prima é transformada no organismo ?

Qual a enzima que inicia o processo ?

Como é identificada uma e de onde vem a enzima UTP---glucose-1-phosphate uridylyltransferase?

#### Aqui uma série de links para diversos bancos de dados de onde é possível obter essas respostas.

1. [BRENDA Database: 2.7.7.9](https://www.brenda-enzymes.org/enzyme.php?ecno=2.7.7.9)
2. [KEGG pathway Amino sugar and nucleotide sugar metabolism](https://www.genome.jp/kegg-bin/show_pathway?map00520+2.7.7.9)
3. [KEGG Reaction](https://www.genome.jp/dbget-bin/www_bget?rn:R00289)
4. [KEGG Compounds (Uridine triphosphate)](https://www.genome.jp/dbget-bin/www_bget?cpd:C00075)
5. [PubChem (Uridine triphosphate)](https://pubchem.ncbi.nlm.nih.gov/substance/3375)
6. [KEGG Compounds (D-Glucose 1-phosphate)](https://www.genome.jp/dbget-bin/www_bget?cpd:C00103)
7. [PubChem (D-Glucose 1-phosphate)](https://pubchem.ncbi.nlm.nih.gov/substance/3403)
8. [KEGG Enzyme UTP---glucose-1-phosphate uridylyltransferase: 2.7.7.9](https://www.genome.jp/dbget-bin/www_bget?ec:2.7.7.9)
9. [KEGG Gene UGP2](https://www.genome.jp/dbget-bin/www_bget?hsa:7360)
10. [Uniprot](https://www.uniprot.org/uniprot/Q16851)
11. [PDB](https://www.genome.jp/dbget-bin/www_bget?pdb:4R7P)
12. [Uniprot API](https://www.uniprot.org/help/programmatic_access)


#### Aqui um Python notebook com exemplos de acesso aos dados de alguns desses bancos via scripts

[Python notebook](https://github.com/waldeyr/minicurso_bdbio_bsb_2022/blob/main/Python_notebook_minicurso_bancos_de_dados_biologicos.ipynb)
