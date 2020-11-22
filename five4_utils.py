import pandas as pd
import io
from Color_Console import *

class Datos():
    """[summary]
    Clase que Inicializa las funciones
    """
    def __init__(self, dataset) -> str:
        """[summary]

        Args:
            dataset ([csv]): [path al archivo csv a analizar]
        """
        self.dataset = dataset
        self.info = str()
        self.infoParse = None
        self.infoParseReturn = None
        self.listaParseadaInfo = []
        self.elementosSplit = []
        self.listaNodos = []
        self.resultadoTable = None
        
    def parsearInfo(self):
        self.listaNodos = []
        self.infoAParsear = self.infoParse
        self.infoAParsear = self.infoAParsear.split("\n")[5:]
        for elementoNodo1 in self.infoAParsear:
            if elementoNodo1[:6] != 'dtypes':
                elementoNodo1 = elementoNodo1.replace("Unnamed: ",'')
                self.listaParseadaInfo.append(elementoNodo1)
            else:
                break
        
        for elementoNodo in self.listaParseadaInfo:
            self.elementosSplit = elementoNodo.split()
            self.listaNodos.append(self.elementosSplit)
        
        self.columnas = ['idElemento', 'nombreColumna', 'cantidadRegistros', 'propiedadNulos', 'tipoDato']
        self.dfInfo = pd.DataFrame(self.listaNodos, columns=self.columnas)
        self.dfInfo.set_index('idElemento')
        return self.dfInfo


    def encontrarDatosNulos(self):
        """[summary]
        El dataset instanciado en la clase Datos(dataset)
        es analizado y retorna distintos metodos de análisis en función
        de los parámetros

        Returns:
            [list]: [tabla con los resultados del análisis]
        """
        try:
            self.buf = io.StringIO()
            self.datos = self.dataset
            self.df = pd.read_csv(self.dataset)
            self.contador = 0
            self.contadorx = 0
            self.resultado = str()
            self.info = self.df.info(buf=self.buf)
            self.infoParse = self.buf.getvalue()
            self.infoParseReturn = self.parsearInfo()
            # self.resultTable = self.df.values.tolist()
            self.listaDfs = self.df
            dictColumnas = dict()

            
            for columna in self.listaDfs.columns.tolist():
                if int(self.listaDfs[columna].isnull().sum()) is not 0:
                    dictColumnas[columna]=self.listaDfs[columna].isnull().sum()
            sumaNull = sum(dictColumnas.values())

            self.contador+=1
            self.contadorx+=1

            # ax.bar(dictColumnas.keys(), dictColumnas.values(), label='Nulos')

            self.resultado = 'El df tiene'+ str(len(self.listaDfs.columns.tolist())) + 'columnas de las cuales las siguientes tienen valores nulos:'+ str(dictColumnas)
                # f"{colored.}El df tiene {len(self.listaDfs.columns.tolist())} columnas de las cuales las siguientes tienen valores nulos: {str(dictColumnas)}")
            self.resultadoTable = pd.DataFrame.from_dict(dictColumnas, 'Index')

        except Exception as ex:
            self.resultado = ex.args
            pass
        color(text = "Green" , bg = "black" , delay = 0.67 ,repeat = -1 , dict = {})
        ctext( self.resultado , text = "red" , bg = "black" , delay = 0 , repeat = 1 , dict = {} )
        ctext( self.infoParseReturn , text = "green" , bg = "black" , delay = 0 , repeat = 1 , dict = {} )
        ctext( self.resultadoTable , text = "yellow" , bg = "black" , delay = 0 , repeat = 1 , dict = {} )
        
        # 
        # print(
        #     self.infoParseReturn
        # )
        # color(text = "Red" , bg = "black" , delay = 0.67 ,repeat = -1 , dict = {})
        # print(
        #     self.resultadoTable
        # )
        

        