from Modelos.Resultado import Resultado
from Modelos.Mesa import Mesa
from Modelos.Candidato import Candidato
from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioCandidato import RepositorioCandidato
class ControladorResultado():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        self.repositorioMesas = RepositorioMesa()
        self.repositorioCandidatos = RepositorioCandidato()
    def index(self):
        return self.repositorioResultado.findAll()
    """
    Asignacion mesa y candidato a resultado
    """
    def create(self,infoResultado,id_mesa,id_candidato):
        nuevoResultado=Resultado(infoResultado)
        laMesa=Mesa(self.repositorioMesas.findById(id_mesa))
        elCandidato=Candidato(self.repositorioCandidatos.findById(id_candidato))
        nuevoResultado.mesa=laMesa
        nuevoResultado.candidato=elCandidato
        return self.repositorioResultado.save(nuevoResultado)
    def show(self,id):
        elResultado=Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__
    """
    Modificación de resultado (mesa y candidato)
    """
    def update(self,id,infoResultado,id_mesa,id_candidato):
        elResultado=Resultado(self.repositorioResultado.findById(id))
        elResultado.numero_mesa=infoResultado["numero_mesa"]
        elResultado.id_partido = infoResultado["id_partido"]
        # elResultado.notaFinal=infoResultado["nota_final"]
        laMesa = Mesa(self.repositorioMesas.findById(id_mesa))
        elCandidato = Candidato(self.repositorioCandidatos.findById(id_candidato))
        elResultado.mesa = laMesa
        elResultado.candidato = elCandidato
        return self.repositorioResultado.save(elResultado)
    def delete(self, id):
        return self.repositorioResultado.delete(id)

    "Obtener todos los resultados en una candidato"
    def listarResultadosPorCandidato(self,id_candidato):
        return self.repositorioResultado.getListadoResultadosPorCandidato(id_candidato)

    "Obtener notas mas altas por curso"
    def notasMasAltasPorCurso(self):
        return self.repositorioResultado.getMayorNotaPorCurso()

    "Obtener promedio de notas en candidato"
    def promedioNotasPorCandidato(self,id_candidato):
        return self.repositorioResultado.promedioNotasPorCandidato(id_candidato)












