from Bio.Seq import Seq


class RNA:
    def __init__(self, rna_seq):
        self.rna_seq = Seq(rna_seq)

    def translation(self):
        """
        Translates the RNA sequence
        @return: Bio.Seq.Seq object, protein sequence
        """
        return self.rna_seq.translate()

    def back_transcription(self):
        """
        Back transcribes the RNA sequence
        @return: Bio.Seq.Seq object, dna sequence
        """
        return self.rna_seq.back_transcribe()


rna_seq = RNA("AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG")
protein_seq = rna_seq.translation()
dna_seq = rna_seq.back_transcription()
print(protein_seq)
print(dna_seq)
