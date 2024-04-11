'''
Solved by: Linda Mansour
Date: 04/07/2024
Language: Python
ID: PROT
Problem: Translating RNA into Protein
The 20 commonly occurring amino acids are abbreviated by
using 20 letters from the English alphabet (all letters 
except for B, J, O, U, X, and Z). Protein strings are constructed
from these 20 symbols. Henceforth, the term genetic string will
incorporate protein strings along with DNA strings and RNA strings.

The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.
'''

with open ("rosalind_prot.txt") as file:
    s = file.readline().strip()
# holds RNA sequence

codons_dictionary = {
    "UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
    "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
    "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
    "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
    "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
    "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
    "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
    "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
    "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
    "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
    "UAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
    "UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E",
    "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
    "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
    "UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
    "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
}

# creates a list from string s, specifically taking from
# the current i position to i + 3 ( codon length) and 
# repeating this for every 3 bases in s.
codons = [s[i:i+3] for i in range(0, len(s), 3)]


protein_sequence = "" # will hold our final protein sequence
for codon in codons: # for each codon in the list of codons
    amino_acid = codons_dictionary[codon] # converted letter
    if amino_acid == "Stop":
        break
    protein_sequence+= amino_acid
    
print(protein_sequence)

# Correct output:
# MTPRPVLTLTSGCGLKAVWPKLRLETPANSTSRTGFSAILRHYPASYFLLSDSRTFHPDHPLHYHYILPKPKFFIWHVPYLRPRGPSWLSMLSRGAQNIARMLRPVIRDISGKAALRTVAFPCQLSVYPFRGLGGVAREGSRTATLDQTLSSHHRCASCGSSSTRFCLSDFPAHVRYHVTRKIMSGFILILSLRGISTRLGVGVSVNMLAVLESALAHHGFVSCSTSSLIEKLHPHPALRNSSDTDLRTSMLLPAGCSYRENKEGLSWPRHWHFIIRTREAHNAPLFLVITLSPPSIPKLAVPTPAPTKIVTIKSLDCLGGDPVADATVASTSMYVLGPGRSTSPCSIEGRPRDVMRTNIIDRNLLASMICQKDHVSRARYGDFIESTAVEPAPSCLRAPATPPFDSLIVPFSVSVNPIPFITRLTVPSGPGTNTKWSWAGSCAKFWLDGGRARHVPSWWKAGSGTPRSATPQNTLRSITTYSVTLDPFAPISYPKTNYDRISAQMSMRSIHIVRDGCLFPAFPRIREHFRWANSNQPAGKLRICIRRSHKRAMLVTCHNILRGDGAHLDFRTSPFVPSTPAGGRQCGPLQAPVRLALITHQFLYWHEILLTPQVEPYRSLCRLSDIIYLLGTFCGTLGNIHPNPIERTISWNQMAMRRFFPDAESDHLSVHGANNIVSQSRWGLGVSVKLLALVPRWRGIQLRYRGLRRRSHWACICMIRHKLILRSIAKGQNFQQIVMLASARRSAAYGPWRQFRIGSCYCTVLYYDLRLNTSCHGTADAFKIVGLIVPADEVIAKSHELSRKDRILRGATVSRLRRPFRLIGCEREPDLVGLFKGIQRLVYMALRLNHSRQVLAAGHPKKCNYRKCFNAYRYRTRKLYLFTHSICPIRYCWLTLPTAGEVGHLTLSRSSLGLWSRSQTRDSLQIQWRSTRRATNRVFLDRPACTVSTFELIVSEPQRLDHQILILASIQNGEIMTTRTYVCRTSTHGKEPPAPLHVKVFVGIAKWQDILLEATIVSIPLLHLRNLRSASIDTHLQSPPTGHQLERFWFRRLKCWRGATSVVLLSNTKMRDCKDQRLVLQCEQRGNESRPYTQATCSKSEHGAFVMGVARTPKSGSRRASSFFYVSREGDLARRTASVGVCGRYCTTGNIRQSAGDTRGFTPTSLSYWRGSPADRLGHWIAWSFAEAYKVSWRLRCERVAALGTVGPVPSGRAVAVYTTTIVFASPRLASNRFSELRSQPLWWGAVTALLVISLTAYGTVSVLGSVSHHARLSGVAQLTSIPQHFKLTPANYLAYLKRTRLEIPHCFESEQPRKKRRPLEFHTVSRKHACAARNGVSGCKLISSFGMTRIGDALRMYPMFVVHITRIGIPRFENSSGSVMSIVQRRGISFSNYQRSKDSFWGHAHPNPCWGRVPRRTEDSEDYPPGVYCHKIKGQYPTYVLGVRDAIIRTRLVYCYKWGYKAMRGCRHKQQAADRTGATNVSGGTRCLWNYLRSTVLGPIAGRRPVPEGPKFWGPDAFVDMYLFPDQRKLKSLARRLRQDNCHSKYGLSDRSHCQQNLCHSVSLGSAYFNNLYPSKKLLKTRDLSVRGMSDLRSTPLVTGNQLRCTVGKVTRFSSVLARRVHSRNLHGAASLAVLIQTLPKDARKERRGLGRFTYLLLNIRGAIAELPGAAYSVSLLTCVATKLFLYKRYGALPLDRISEYKNLFFVIPRTDCSGHTGFGSLLSRYVRFGCPILCLRSVLAARALETTSSLPNTALGLRPRQHGLHLEELYSWEHISLSVTCYKARRADENASPCGWNTAPPCDDRALKKRGEYFTGRTEYPRLPSILLHENTVTSDLGLITGFRGARKHSKVNHSGMSQGSPRRGTTLPARLPEDSDLSGSLPRVKQLIPLRIFLNKLPSPRIKFESLEEPPTPQCDKRTPTDFPGNSGQAICASQLGKKYPRSLRTGSVTLGGMDSPHCNHLRLIETVAYVFTDLTQWCTSSVFIEHDVWLGSDIPRSLSSAKGVRISNRHIRETLFVFCQESSVCGGPRESLPLPCPLQYTHKTREIRRWSRSWTNWGNAFSGRPLQEVGLATNAQTVMRLGLKKVRSGQLERYCSPNRREVIILSIGPVSFLLSRVPSLEDERKCDYISLLAEQPIADSCATTNSTSPLTSEGASDRYLAYLLSRLRSFTAHNALIRKLTYGNAKVSLCNSWTTAEGWTCDVGTAAISPHGICRPYCEVIFLWHHSNKRTNPSPALYITWYRLIPEYTQAYDFHSENRRNQLALTGGLDPSAALALITSFFRLALFSVRVCPVPCAHSEAASEPAEEDKRGRFFRNSYACGTTVNEGTHMVYYLIYVPFPFNQLEMHSSIPLFDKRGPRELDKRPKRTCINDRSRSLTRRRRINSNYRMPMAKYHLRTVLWSSHQPLSVPYRSQTKKNASQISVRKHLISCDLRKYKRAIELLLFLPNKTFRQLANRRCLLNTVSIRQSMLPSCIKARVGEITLIFLRAIIDVGPPNARSRRVSSIICLPRICEERSPRCLPPPSKKLPNIQPKRHCACNTGVAPFPPSPSIESPNLGTLRLELLKTRNQSRTGQRYTSIVGEVARQAINCRAPVSSRLHAHNHATRRGAPFHILRLPNVSTRYSSDCLGIVRRWYIKGSIKLSNMPPYAHSISAPCTSSIARRSYAQASVSKHAQANGRDCVTLGSLQRKSCRPPSDEVCRKLAVIVGRAVLAMELPILWPKLPQTEVSLCKPLIPYQHQFETISAGKGRSSLTGQVRMQQCLGGSSSSPVARFIVQYRIVRCKNDRGLLMLLIRQPVNPSLSINVSHAWTLVSHRSPSSLLKSWAKDPHFSVSAPQLVKSARVLRLMMHQDKRTDVYLDLRSCSKLVRLFSRPPTVTAKAISNPPLFIVRGRPHPQTLQYSLTLHWAQHTYAPNNRTMGQRTLKSPCDTQYPPFVVLADIVTSRKARVSCQYYDALSSGDVVRATRVHGVTKRASHLRTEEAMPTISVTPPLARRRLACDYYNLPVRRSYVRLALAATPVYCKIFQLPIYGDLQYGNRPSTYGTRAITDGYEKRTSLHAIVSQKYSLPHRSRWTAGMRVILPSFPISSFIDCSFELRPAKMSGSPIACQTTVPPSGNTGEVSSFSPLIIRAHHVSIASAFATVFLRVYVSVNRSICCLPTARIARRHLSRGIAGSIIRRTLVLQQHLGRHVRYWAW