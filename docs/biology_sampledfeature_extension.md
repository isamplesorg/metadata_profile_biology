---
comment: | 
  WARNING: This file is generated. Any edits will be lost!
format:
  html:
    ascii: true
    toc: true
    toc-depth: 4
    number-sections: true
    anchor-sections: false
    number-depth: 8
execute:
  echo: false
---

[]{#BiologyExtension:Basictaxonclassesforbiologicalentity}

# **Concept scheme:** Biology Extension: Basic taxon classes for biological entity

Vocabulary last modified:  2023-03-23

subtitle: 
  This is a vocabulary to categorize sampled organisms (whole or part) according to taxonomic classes. Classes are based largely on taxonomy found in Wikipedia, particularly Whittaker's five kingdom system (1969) (https://en.wikipedia.org/wiki/Kingdom_(biology), https://doi.org/10.1126%2Fscience.163.3863.150). The intended use is in iSamples cross domain categorization of material samples, recognizing that there are multiple view for taxonaomy and cladistist for the tree of life. This is a high level view intended for cross domain purposes, not expert analysis. Other extension vocablaries should be used for other taxonomic schemes

Namespace: 
[`https://w3id.org/isample/biology/biosampledfeature/1.0/biologicentityvocabulary`](https://w3id.org/isample/biology/biosampledfeature/1.0/biologicentityvocabulary)

**History**

* Based on draft DiSSCo specimen & collection classification, table 2, https://docs.google.com/document/d/19OPyOm9VF2qfI3M6RmJPvRfo8JlZ3tt0II05aGCyBHQ/ , with added classes to attempt a logical hierarchy.

- [Biological entity](#biologicalentity)
    - [Eukaryote](#eukaryote)
        - [Animalia](#animalia)
            - [Vertebrate ](#vertebrate)
                - [Amphibian](#amphibian)
                - [Bird](#bird)
                - [Fish](#fish)
                - [Mammal](#mammal)
                - [Reptile](#reptile)
            - [Arthropod ](#arthropod)
                - [Arachnid](#arachnid)
                - [Crustaceans](#crustacea)
                - [Insect](#hexapoda)
                - [Myriapod](#myriapod)
                - [Other arthropod ](#otherarthropod)
            - [Mollusca](#mollusca)
            - [Other invertebrate ](#otherinvertebrate)
            - [Porifera](#porifera)
        - [Fungi](#fungi)
            - [Macrofungi](#macrofungi)
            - [Microfungi](#microfungi)
        - [Plantae](#plantae)
            - [Bryophyte](#bryophyte)
            - [Other plant](#otherplant)
            - [Pteridophyte](#pteridophyte)
            - [Seed plant](#spermatophyte)
        - [Protista](#protista)
            - [Amoebozoa  ](#amoebozoa)
                - [Myxomycetes](#myxomycete)
            - [Protozoa](#protozoa)
        - [Algae](#algae)
        - [Eukaryotic microorganisms](#eukaryoticmicroorganisms)
    - [Lichen](#lichen)
    - [Plasmid](#plasmid)
    - [Prokaryote](#prokaryote)
        - [Archaea](#archaea)
        - [Bacteria](#bacteria)
    - [Virus](#virus)
        - [Other Virus  ](#othervirus)
        - [Phage](#phage)

**Concepts**

[]{#biologicalentity}

##  Biological entity


- Sampled feature is an organism. Use for samples that represent some
species of organism as the proximate sampled feature for which the
focus is not the environment that the organism inhabits.
- Concept URI token: biologicalentity


[]{#eukaryote}

###  Eukaryote


- Child of:
 [`biologicalentity`](#biologicalentity)

- organism whose cells have a nucleus. Includes all animals, plants,
fungi, and many unicellular organisms
(https://en.wikipedia.org/wiki/Eukaryote)
- Concept URI token: eukaryote


[]{#animalia}

####  Animalia


- Child of:
 [`eukaryote`](#eukaryote)

- Animals are distinguished from other eukaryotes based on several key
characteristics, including: 1)  animals are multicellular organisms 2)
Animals are heterotrophic, they obtain their food by consuming other
organisms or organic matter; 3) Animals lack cell walls; 4) Many
animals have a nervous system; 5\) Most animals reproduce sexually
(Chat GPT)
- Concept URI token: Animalia


[]{#vertebrate}

#####  Vertebrate


- Child of:
 [`Animalia`](#Animalia)

- Animals that have a vertebral column, a cranium, an endoskeleton, a
well-developed muscular system, and an advanced nervous system
(ChatGPT);
- Concept URI token: Vertebrate


[]{#amphibian}

######  Amphibian


- Child of:
 [`Vertebrate`](#Vertebrate)

- Vertebrates that have a dual life cycle, semi-permeable skin,
absence of scales and claws, a three-chambered heart, and dependence
on water for reproduction and survival (ChatGPT)
- Concept URI token: amphibian


[]{#bird}

######  Bird


- Child of:
 [`Vertebrate`](#Vertebrate)

- Vertebrates that have feathers, lightweight, hollow bones, a beak,
an efficient respiratory system, and are warm-blooded. (ChatGPT) {@en}
- Concept URI token: bird


[]{#fish}

######  Fish


- Child of:
 [`Vertebrate`](#Vertebrate)

- Vertebrates that have gills, scales, fins, are cold-blooded, and
commonly have a swim bladder; includes jawless fish, cartilaginous
fish and bony fish. (ChatGPT)
- Concept URI token: fish


[]{#mammal}

######  Mammal


- Child of:
 [`Vertebrate`](#Vertebrate)

- vertebrates that have mammary glands, hair or fur, three middle ear
bones, specialized teeth, and are warm-blooded. (ChatGPT)
- Concept URI token: mammal


[]{#reptile}

######  Reptile


- Child of:
 [`Vertebrate`](#Vertebrate)

- Vertebrates that have scaly skin and claws, amniotic eggs, are cold-
blooded, and are ectothermic (ChatGPT)
- Concept URI token: reptile


[]{#arthropod}

#####  Arthropod


- Child of:
 [`Animalia`](#Animalia)

- invertebrate animals with an exoskeleton, a segmented body, and
paired jointed appendages. Arthropods form the phylum Arthropoda. They
are distinguished by their jointed limbs and cuticle made of chitin,
often mineralised with calcium carbonate. The arthropod body plan
consists of segments, each with a pair of appendages. Arthropods are
bilaterally symmetrical and their body possesses an external skeleton.
(https://en.wikipedia.org/wiki/Arthropod)
- Concept URI token: arthropod


[]{#arachnid}

######  Arachnid


- Child of:
 [`arthropod`](#arthropod)

- a group of arthropods that share several key characteristics,
including two main body segments, four pairs of legs, lack of
antennae, simple eyes, and specialized feeding and defense structures
called chelicerae (ChatGPT)
- Concept URI token: arachnid


[]{#crustacea}

######  Crustaceans


- Child of:
 [`arthropod`](#arthropod)

- arthropod taxon which includes such animals as decapods, seed
shrimp, branchiopods, fish lice, krill, remipedes, isopods, barnacles,
copepods, amphipods and mantis shrimp.  crustaceans have an
exoskeleton, which they moult to grow. They are distinguished from
other groups of arthropods, such as insects, myriapods and
chelicerates, by the possession of biramous (two-parted) limbs, and by
their larval forms, such as the nauplius stage of branchiopods and
copepods. (https://en.wikipedia.org/wiki/Crustacean)
- Concept URI token: crustacea


[]{#hexapoda}

######  Insect


- Child of:
 [`arthropod`](#arthropod)

- Include all hexapoda here; Insects are a group of hexapod arthropods
characterized by having three main body segments (head, thorax, and
abdomen), six legs, and wings in many species. All other hexapod
arthropods, such as springtails and diplurans, are not classified as
insects, but they share the same body plan of three main body segments
and six legs. However, they lack wings and other features that are
unique to insects. Therefore, all insects are hexapods, but not all
hexapods are insects. (ChatGPT)

- **Alternate labels:**
Hexapoda

- Concept URI token: hexapoda


[]{#myriapod}

######  Myriapod


- Child of:
 [`arthropod`](#arthropod)

- Arthropods such as millipedes and centipedes.
(https://en.wikipedia.org/wiki/Myriapoda). A group of arthropods that
have long, segmented body with numerous pairs of legs, simple eyes,
specialized mouthparts, and a primarily terrestrial habitat, which
distinguishes them from other arthropod groups such as insects and
crustaceans. (ChatGPT)
- Concept URI token: myriapod


[]{#otherarthropod}

######  Other arthropod


- Child of:
 [`arthropod`](#arthropod)

- includes Chelicerata (horseshoe crabs, scorpions, and sea spiders),
Trilobitomorpha ( extinct trilobites), and  Pentastomida (parasitic
arthropods that infect the respiratory systems of reptiles and
mammals). (ChatGPT)
- Concept URI token: otherarthropod


[]{#mollusca}

#####  Mollusca


- Child of:
 [`Animalia`](#Animalia)

- animals that have a soft body with a mantle, a radula (ribbon-like
structure covered in tiny teeth that is used to scrape food), a
muscular foot, an open circulatory system, and a visceral mass that
contains the internal organs, including the digestive, excretory, and
reproductive systems. (ChatGPT)

- **Alternate labels:**
bivalves, 
cephalopods, 
gastropods, 

- Concept URI token: mollusca


[]{#otherinvertebrate}

#####  Other invertebrate


- Child of:
 [`Animalia`](#Animalia)

- Includes Cnidaria (jellyfish, coral, anemones), Echinodermata
(starfish, sea urchins, sea cucumbers), Nematoda (roundworms),
Platyhelminthes (flatworms), Annelida (segmented worms), Ctenophora
(comb jellies), Brachiopoda (lamp shells), Bryozoa (moss animals),
Chaetognatha (arrow worms), Hemichordata (acorn worms),
Xenacoelomorpha (simple-bodied worms) (ChatGPT)
- Concept URI token: otherinvertebrate


[]{#porifera}

#####  Porifera


- Child of:
 [`Animalia`](#Animalia)

- multicellular animals that have bodies full of pores and channels
allowing water to circulate through them, consisting of jelly-like
mesohyl sandwiched between two thin layers of cells.
(https://en.wikipedia.org/wiki/Sponge)

- **Alternate labels:**
sponges

- Concept URI token: porifera


[]{#fungi}

####  Fungi


- Child of:
 [`eukaryote`](#eukaryote)

- eukaryotic organisms that contain chitin in their cell walls, are
heterotrophs (they obtain their nutrients by absorbing organic
material from their environment, either as decomposers, parasites, or
symbionts) , lack chloroplasts, reproduce both sexually and asexually,
and can take on a variety of growth forms, including single-celled
yeasts, multicellular molds, and complex, specialized fruiting bodies.
(ChatGPT)
- Concept URI token: Fungi


[]{#macrofungi}

#####  Macrofungi


- Child of:
 [`Fungi`](#Fungi)

- Macrofungi refers to all fungi that produce visible fruiting bodies.
These fungi are evolutionarily and ecologically very divergent.
Evolutionarily, they belong to two main phyla, Ascomycota and
Basidiomycota, and many of them have relatives that cannot form
visible fruiting
bodies.(https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6106070/)
- Concept URI token: macrofungi


[]{#microfungi}

#####  Microfungi


- Child of:
 [`Fungi`](#Fungi)

- Microfungi or micromycetes are fungi—eukaryotic organisms such as
molds, mildews and rusts, which have microscopic spore-producing
structures. They exhibit tube tip-growth and have cell walls composed
of chitin, a polymer of N-acetylglucosamine. Microfungi are a
paraphyletic group, distinguished from macrofungi only by the absence
of a large, multicellular fruiting body. Include moulds, yeasts.
(https://en.wikipedia.org/wiki/Microfungi)

- **Alternate labels:**
micromycetes

- Concept URI token: microfungi


[]{#plantae}

####  Plantae


- Child of:
 [`eukaryote`](#eukaryote)

- Plants are eukaryotes that have cell walls made of cellulose,
specialized organelles called chloroplasts, which contain chlorophyll
and other pigments that allow plants to perform photosynthesis and
produce their own food;  a unique life cycle that involves alternating
between a haploid gametophyte stage and a diploid sporophyte stage;
specialized regions called apical meristems at the tips of their roots
and shoots, which allow for growth and the development of new tissues;
specialized structures for reproduction, including flowers, cones, and
spores, and most plants have specialized tissues called xylem and
phloem, which transport water, nutrients, and other substances
throughout the plant. (ChatGPT)
- Concept URI token: Plantae


[]{#bryophyte}

#####  Bryophyte


- Child of:
 [`Plantae`](#Plantae)

- Non-vascular plants that do not have specialized tissues for
transporting water and nutrients;  includes mosses, Marchantiophyta
(liverworts), and Anthocerotophyta (hornworts). (ChatGPT)
- Concept URI token: bryophyte


[]{#otherplant}

#####  Other plant


- Child of:
 [`Plantae`](#Plantae)

- plants that do not fit in other plant sub class. Includes
Lycopodiophyta (clubmosses) and Equisetophyta (horsetails)
- Concept URI token: otherplant


[]{#pteridophyte}

#####  Pteridophyte


- Child of:
 [`Plantae`](#Plantae)

- a vascular plant (with xylem and phloem) that disperses spores; they
produce neither flowers nor seeds, Includes  Ferns, horsetails (often
treated as ferns), and lycophytes (clubmosses, spikemosses, and
quillworts)
- Concept URI token: pteridophyte


[]{#spermatophyte}

#####  Seed plant


- Child of:
 [`Plantae`](#Plantae)

- Plant that produces seeds, hence the alternative name seed plant.
Spermatophytes are a subset of the embryophytes or land plants. They
include most familiar types of plants, including all flowers and most
trees, but exclude some other types of plants such as ferns, mosses,
algae. (https://en.wikipedia.org/wiki/Spermatophyte). Includes
Gymnosperms (naked-seed plants) and Angiosperms (flowering plants).

- **Alternate labels:**
spermatophyte

- Concept URI token: spermatophyte


[]{#protista}

####  Protista


- Child of:
 [`eukaryote`](#eukaryote)

- any organism whose cells contain a cell nucleus (a eucaryote) that
is not an animal, plant, or fungus.
(https://en.wikipedia.org/wiki/Protist).  Protista is not a specific
taxonomic group, but a term that historically referred to a group of
eukaryotic organisms that did not fit into the other kingdoms of
plants, animals, and fungi. (ChatGPT)
- Concept URI token: Protista


[]{#amoebozoa}

#####  Amoebozoa


- Child of:
 [`Protista`](#Protista)

- a diverse group of organisms that share certain characteristics,
such as the ability to move using pseudopodia, temporary extensions of
the cell membrane and cytoplasm that allow the cell to crawl or engulf
food particles, the lack of rigid cell walls, presence of
mitochondria, which are organelles that generate energy for the cell
through cellular respiration (chatGPT)
- Concept URI token: amoebozoa


[]{#myxomycete}

######  Myxomycetes


- Child of:
 [`amoebozoa`](#amoebozoa)

- Aclass of slime molds. All species pass through several, very
different morphologic phases, such as microscopic individual cells,
slimy amorphous organisms visible with the naked eye and conspicuously
shaped fruit bodies. Although they are monocellular, they can reach
immense widths and weights. Some consider the Myxomycota to be a
separate kingdom, with an unsettled phylogeny because of conflicting
molecular and developmental data. The relations among Myxogastrid
orders are as yet unclear. (https://en.wikipedia.org/wiki/Mycetozoa).
Mycetozoa includes the slime molds, which are a group of organisms
that have both amoeboid and fungal-like characteristics. The Mycetozoa
can be further subdivided into two groups: the plasmodial slime molds
and the cellular slime molds. Myxomycetes are unique among the
Amoebozoa in that they have a complex life cycle involving the
formation of spore-bearing structures called fruiting bodies, which is
a key feature that distinguishes them from other amoebae. (ChatGPT)

- **Alternate labels:**
Mycetozoa

- Concept URI token: myxomycete


[]{#protozoa}

#####  Protozoa


- Child of:
 [`Protista`](#Protista)

- A single-celled eukaryote, either free-living or parasitic, that
feed on organic matter such as other microorganisms or organic tissues
and debris. Historically, protozoans were regarded as 'one-celled
animals', because they often possess animal-like behaviours, such as
motility and predation, and lack a cell wall, as found in plants and
many algae. (https://en.wikipedia.org/wiki/Protozoa)
- Concept URI token: protozoa


[]{#algae}

####  Algae


- Child of:
 [`eukaryote`](#eukaryote)

- informal term for a large and diverse group of photosynthetic
eukaryotic organisms.  Included organisms range from unicellular
microalgae, such as Chlorella, Prototheca and the diatoms, to
multicellular forms, such as the giant kelp, a large brown alga which
may grow up to 50 metres (160 ft) in length. Most are aquatic and
autotrophic (they generate food internally) and lack many of the
distinct cell and tissue types, such as stomata, xylem and phloem that
are found in land plants.  Includes red algae (Rhodophycophyta), brown
algae (Phaeophycophyta), and green algae (Chlorophycophyta).
https://en.wikipedia.org/wiki/Algae
- Concept URI token: algae


[]{#eukaryoticmicroorganisms}

####  Eukaryotic microorganisms


- Child of:
 [`eukaryote`](#eukaryote)

- Eukaryote single-cell organisms that does not fit in one of the
other classes.
- Concept URI token: eukaryoticmicroorganisms


[]{#lichen}

###  Lichen


- Child of:
 [`biologicalentity`](#biologicalentity)

- A composite organism that arises from algae or cyanobacteria living
among filaments of multiple fungi species in a mutualistic
relationship. (https://en.wikipedia.org/wiki/Lichen). Lichens are not
classified under a specific kingdom as they are a symbiotic
association between a fungus and either an alga or a cyanobacterium.
The fungal partner belongs to the kingdom Fungi, while the algal or
cyanobacterial partner belongs to either the kingdom Plantae or the
kingdom Bacteria, respectively. (ChatGPT)
- Concept URI token: lichen


[]{#plasmid}

###  Plasmid


- Child of:
 [`biologicalentity`](#biologicalentity)

- A plasmid is a small, extrachromosomal DNA molecule within a cell
that is physically separated from chromosomal DNA and can replicate
independently. While chromosomes are large and contain all the
essential genetic information for living under normal conditions,
plasmids are usually very small and contain only additional genes that
may be useful in certain situations or conditions.
(https://en.wikipedia.org/wiki/Plasmid)
- Concept URI token: plasmid


[]{#prokaryote}

###  Prokaryote


- Child of:
 [`biologicalentity`](#biologicalentity)

- single-celled organisms that lack a nucleus and other membrane-bound
organelles. Unlike cells of animals and other eukaryotes, bacterial
cells do not contain a nucleus and rarely harbour membrane-bound
organelles. Molecular systematics showed prokaryotic life to consist
of two separate domains, originally called Eubacteria and
Archaebacteria, but now called Bacteria and Archaea that evolved
independently from an ancient common ancestor. Almost all prokaryotes
have a cell wall, a protective structure that allows them to survive
in extreme conditions, which is located outside of their plasma
membrane. Archaea and bacteria cannot reproduce sexually.

- **Alternate labels:**
Monera

- Concept URI token: prokaryote


[]{#archaea}

####  Archaea


- Child of:
 [`prokaryote`](#prokaryote)

- archaeal cell walls are composed of polysaccharides (sugars). they
never have peptidoglycan in their cell walls, their cell membranes
contain lipids of unique composition (glycerol molecules are mirror
images of those found in other cells, and form ether linkages to
isoprenoid side chains), and their 16S ribosomal- RNA nucleotide
sequences are unlike those of bacteria.
(https://quizlet.com/234154298/archaea-and-bacteria-flash-cards/).
The common characteristics of Archaebacteria known to date are these:
(1) the presence of characteristic tRNAs and ribosomal RNAs; (2) the
absence of peptidoglycan cell walls, with in many cases, replacement
by a largely proteinaceous coat; (3) the occurrence of ether linked
lipids built from phytanyl chains and (4) in all cases known so far,
their occurrence only in unusual habitats.
(https://pubmed.ncbi.nlm.nih.gov/691075/)

- **Alternate labels:**
Archaebacteria

- Concept URI token: archaea


[]{#bacteria}

####  Bacteria


- Child of:
 [`prokaryote`](#prokaryote)

- a large domain of prokaryotic microorganisms. Bacterial cells do not
contain a nucleus and rarely harbour membrane-bound organelles.  The
bacterial cell is surrounded by a cell membrane, which is made
primarily of phospholipids. This membrane encloses the contents of the
cell and acts as a barrier to hold nutrients, proteins and other
essential components of the cytoplasm within the cell.  Bacterial cell
walls are composed of peptidoglycan, a complex of protein and sugars,
while archaeal cell walls are composed of polysaccharides (sugars).
(https://en.wikipedia.org/wiki/Bacteria)

- **Alternate labels:**
Eubacteria

- Concept URI token: bacteria


[]{#virus}

###  Virus


- Child of:
 [`biologicalentity`](#biologicalentity)

- A virus is a submicroscopic infectious agent that replicates only
inside the living cells of an organism. Realms are Adnaviria,
Duplodnaviria, Monodnaviria, Riboviria, Ribozyviria, Varidnaviria
(https://en.wikipedia.org/wiki/Virus). Viruses are not cells at all,
so they are neither prokaryotes nor eukaryotes. (https://bio.libretext
s.org/Bookshelves/Introductory_and_General_Biology/Book)
- Concept URI token: virus


[]{#othervirus}

####  Other Virus


- Child of:
 [`virus`](#virus)

- Virus that is not a member of order Caudovirales (e.g.,
bacteriophage T4, lambda phage).
- Concept URI token: othervirus


[]{#phage}

####  Phage


- Child of:
 [`virus`](#virus)

- A bacteriophage, also known informally as a phage, is a
duplodnaviria virus that infects and replicates within bacteria and
archaea. Bacteriophages are composed of proteins that encapsulate a
DNA or RNA genome, and may have structures that are either simple or
elaborate. Their genomes may encode as few as four genes (e.g. MS2)
and as many as hundreds of genes. Phages replicate within the
bacterium following the injection of their genome into its cytoplasm.
(https://en.wikipedia.org/wiki/Bacteriophage).  Includes all virus in
order Caudovirales (e.g., bacteriophage T4, lambda phage).

- **Alternate labels:**
bacteriophage

- Concept URI token: phage



