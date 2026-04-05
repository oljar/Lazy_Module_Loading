import importlib
from  Module_2.bodo import Database_2


class LazyModule:
    def __init__(self, name):
        self._name = name
        self._module = None
    def _load(self):
        if self._module is None:
            self._module = importlib.import_module(self._name)
        return self._module
    def __getattr__(self, item):
        return getattr(self._load(), item)



if __name__ == "__main__":
    ######################################################################
    # pierwszy sposób

    LazyModule('Module_1.modo')
    a = LazyModule('Module_1.modo')

    # Aby użyć 'connection', musisz utworzyć obiekt bazy danych:
    db = a.Database("my_connection_string")
######################################################################

    # drugi sposób - uruchomienie samej metody w klasie modułu - ale import działa odrazu

    b = Database_2()
    b.initialize('con str 2')



