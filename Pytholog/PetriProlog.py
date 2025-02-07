import pytholog as pl


class PetriProlog:
    def __init__(self, pl, kbase):
        self.kb = pl.KnowledgeBase(kbase)

    def query(self,predicate):
        return self.kb.query(pl.Expr(predicate))

    def setKnowledgebase(self,knowledgebase):
        self.kb(knowledgebase)

