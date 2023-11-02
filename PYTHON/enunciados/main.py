import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.ttk as ttk
import pyperclip
from tkinter import font

class Interface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Interfaz de Python")
        self.geometry("200x600")
    

        self.tabControl = ttk.Notebook(self)
        self.fuente = font.Font(size=7)

    

        self.diagnostico_tab = ttk.Frame(self.tabControl)
        self.reparacion_tab = ttk.Frame(self.tabControl)

        self.tabControl.add(self.diagnostico_tab, text="D")
        self.tabControl.add(self.reparacion_tab, text="R")

        self.tabControl.pack(expand=1, fill="both")

        self.create_sections()

    def create_sections(self):
        diagnostico_data = {
            "BUENO": 
            [
               "Tras realizar una evaluación exhaustiva, se ha constatado que el elemento en cuestión se encuentra en óptimas condiciones y cumple plenamente con los estándares y normativas establecidos. No presenta irregularidades"
        ],
            "CAMBIO": 
            [
                "Corrosión: Tras una exhaustiva inspección, se ha determinado que se requiere efectuar el reemplazo de la pieza debido a la presencia de corrosión en su superficie. La corrosión, resultado de la reacción química entre el material de la pieza y agentes externos, ha provocado un deterioro significativo que compromete su integridad estructural y funcionalidad. ",
                "Fuera de tolerancia: Tras un detallado proceso de diagnóstico, se ha constatado de manera inequívoca que la pieza en cuestión se encuentra fuera de los límites de tolerancia establecidos. En consecuencia, es imperativo llevar a cabo la sustitución de la misma, ya que su condición actual compromete su correcto funcionamiento y afecta su capacidad para cumplir con los requisitos y estándares exigidos.",
                "Golpes fuertes: Tras realizar una evaluación técnica exhaustiva, se ha determinado que la pieza en cuestión presenta evidentes signos de impactos fuertes, los cuales han afectado significativamente su integridad y rendimiento. Por consiguiente, se hace necesario proceder con el reemplazo de dicha pieza, ya que los golpes sufridos han comprometido su capacidad para cumplir con las funciones requeridas y los estándares establecidos.",
                "Desprendimiento de cromo: Tras una exhaustiva inspección técnica, se ha evidenciado de manera contundente el desprendimiento de cromo en la superficie de la pieza en cuestión. Este fenómeno representa una clara indicación de un deterioro significativo en el recubrimiento de cromo aplicado previamente. En vista de esto, resulta imprescindible llevar a cabo el reemplazo de la pieza, ya que el desprendimiento de cromo compromete tanto su apariencia estética como su resistencia a la corrosión y su capacidad de cumplir con los estándares de calidad exigidos.",
                "Desgaste: Tras un exhaustivo análisis técnico, se ha determinado que debido al desgaste significativo experimentado por la pieza en cuestión, se recomienda encarecidamente proceder a su sustitución. El deterioro observado en la pieza es evidente tanto a nivel visual como funcional, lo que indica una disminución en su rendimiento y confiabilidad. El desgaste acumulado ha afectado negativamente las propiedades estructurales y mecánicas de la pieza, comprometiendo su capacidad para cumplir con los requisitos operativos y de seguridad establecidos.",
                "Rallas fuertes: De acuerdo con el análisis técnico realizado, se hace imprescindible llevar a cabo la sustitución de la pieza en cuestión debido a la manifestación de rayas de considerable profundidad en su superficie. Estas marcas abrasivas y notorias representan un factor determinante que compromete significativamente tanto el funcionamiento fluido del componente como su capacidad para cumplir con los estándares de desempeño requeridos. ",
                "Flexión: Se ha determinado que es necesario realizar el reemplazo de la pieza debido a la presencia de deformación por flexión. Después de un análisis exhaustivo y pruebas de resistencia, se ha confirmado que la pieza ha experimentado una deformación significativa debido a fuerzas de flexión aplicadas en su entorno operativo."
            ],
            "RECTIFICAR": 
            [
                "Cromar: Tras un análisis exhaustivo, se ha determinado la necesidad imperante de someter la pieza a un proceso de cromado debido a la presencia significativa de corrosión en su superficie. La corrosión ha ocasionado un deterioro progresivo y visible en la estructura metálica de la pieza, comprometiendo tanto su resistencia como su funcionalidad.",
                "Brillar: Una vez finalizado el minucioso proceso de diagnóstico de la pieza, se ha determinado que es necesario llevar a cabo un procedimiento de pulido con el fin de restaurar su acabado original, eliminar cualquier imperfección superficial y mejorar significativamente su apariencia estética. Mediante este proceso de pulido, se aplicarán técnicas especializadas para eliminar cualquier rastro de desgaste, marcas o defectos que puedan haberse manifestado debido a condiciones de uso, daños externos o desgaste natural",
                "Bruñir: Luego de un minucioso diagnóstico, se determina que es indispensable llevar a cabo el proceso de bruñido en la pieza en cuestión. Esta acción se hace necesaria para eliminar las irregularidades y asperezas presentes en su superficie, las cuales afectan de manera directa tanto la funcionalidad como la durabilidad del componente. El bruñido, mediante la utilización de abrasivos finos y técnicas de pulido específicas, permitirá obtener una superficie lisa, uniforme y libre de imperfecciones, restableciendo así las condiciones óptimas de deslizamiento",
                "Deformación: Se ha determinado la necesidad de realizar la rectificación de la pieza debido a la presencia de deformación. Esta deformación, detectada mediante análisis dimensional y pruebas exhaustivas, ha comprometido la geometría y la precisión requeridas para el correcto funcionamiento de la pieza.",
                "Rosca: Tras realizar una evaluación detallada, se ha identificado que la rosca de la pieza presenta irregularidades y dimensiones fuera de tolerancia. Estas condiciones inadecuadas afectan negativamente la funcionalidad y seguridad del ensamblaje al que pertenece."
            ],
            "EMPAQUES":
            ["En el desarrollo del diagnóstico, se evidencia que los sellos hidráulicos se encuentran desgastados y cristalizados, por tal motivo no se pueden usar nuevamente ya que perdieron sus propiedades elásticas, lo cual es una característica fundamental al momento de realizar del sellado hidráulico, no se cumple con los parámetros establecidos en las especificaciones de la EPS 5350 Parker Hannifin."]
       
        }

        reparacion_data = {
            "Cambio": 
            [
                "Se procedió al reemplazo de la pieza defectuosa por una de características idénticas que garantiza el correcto funcionamiento del sistema. La nueva pieza cumple con los requisitos y especificaciones técnicas necesarias, asegurando un rendimiento óptimo y la continuidad operativa de acuerdo con las normativas y estándares vigentes"
                ],
            "Rectificar": 
            [
                "Bruñido: Se ha completado el proceso de bruñido de la pieza como parte del procedimiento de reparación, garantizando la eliminación de imperfecciones superficiales y logrando una superficie suave y uniforme para su óptimo funcionamiento.",
                "Cromado: Se ha llevado a cabo exitosamente el proceso de cromado de la pieza como parte del procedimiento de reparación, mediante el cual se depositó una capa de cromo sobre su superficie para proporcionar mayor resistencia a la corrosión, mejorar la estética y restaurar sus propiedades mecánicas, asegurando así su durabilidad y rendimiento óptimo.",
                "Brillado: Se ha completado con éxito el proceso de brillado de la pieza como parte del procedimiento de reparación, mediante el cual se ha aplicado un tratamiento especial para obtener una superficie lisa, pulida y de alto brillo. Este proceso ha mejorado tanto la estética como la funcionalidad de la pieza, realzando su apariencia visual y optimizando su rendimiento en términos de resistencia al desgaste y reducción de fricción.",
                "Deformación: Mediante técnicas de rectificación especializadas, se ha corregido la deformación y se han restablecido las dimensiones y tolerancias precisas requeridas. Este procedimiento ha garantizado la recuperación de la geometría original de la pieza, asegurando su alineación correcta y su adecuado funcionamiento en la aplicación final, sin comprometer su resistencia mecánica ni su integridad estructural.",
                "Rosca: Se ha completado con éxito la reparación de la rosca, abordando la desviación dimensional previamente identificada. Mediante el proceso de rectificación, se han restablecido las especificaciones geométricas de la rosca, asegurando así un acoplamiento adecuado y una funcionalidad óptima de las piezas involucradas. "
                ],
            "Empaques":[
                "Este proceso de reemplazo ha permitido restaurar la estanqueidad y eficiencia del sistema hidráulico, asegurando un funcionamiento óptimo y evitando posibles fugas o pérdida de presión hidráulica. Con los sellos hidráulicos renovados, se ha mejorado la confiabilidad y la vida útil del sistema hidráulico en su conjunto."
            ],
            "Claves":[
                "HYT2023",
                "HYDRA23"
            ]
                  }

        for section, data in diagnostico_data.items():
            frame = ttk.LabelFrame(self.diagnostico_tab, text=section)
            frame.pack(fill="both", padx=10, pady=10)

            for enunciado in data:
                frame_inner = ttk.Frame(frame)
                frame_inner.pack(fill="both", pady=5)
                button = ttk.Button(frame_inner, text="", command=lambda enunciado=enunciado: self.copy_to_clipboard(enunciado),width=2, )
                button.pack(side="left", padx=2)

                label = ttk.Label(frame_inner, text=enunciado, font=self.fuente)
                label.pack(side="left")

                

        for section, data in reparacion_data.items():
            frame = ttk.LabelFrame(self.reparacion_tab, text=section)
            frame.pack(fill="both", padx=10, pady=10)

            for enunciado in data:
                frame_inner = ttk.Frame(frame)
                frame_inner.pack(fill="both", pady=5)
                button = ttk.Button(frame_inner, command=lambda enunciado=enunciado: self.copy_to_clipboard(enunciado), width=2)
                button.pack(side="left", padx=10)

                label = ttk.Label(frame_inner, text=enunciado)
                label.pack(side="left")
        informes = ttk.Button(self.reparacion_tab)
        informes.pack(side="bottom")

                

    def copy_to_clipboard(self, text):
        pyperclip.copy(text)

if __name__ == "__main__":
    interface = Interface()
    interface.mainloop()
