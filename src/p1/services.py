"""
Systemy i ich depnencje

- users (clients)
- users (employees)
- access_rights
- logging
- metrics
- secret_storage

Zadnie do zrobienia:

 Poprawnie zainicjalizować system

 Poprawnie wyłączyć system







      ClientStore                          EmployeeStore

               │  ┌────────────────────────────    │
               │ ┌┤                              │ │
               │ ││                              │ │
               │ ││                              │ │
               │ ││                              │ └─────────────────────────────►
               │ ││                              │                              MetricsExporter
               │ ││                              │
               │ ││                              │
               │ ││                              │
               │ ││                              │
               │ ││                              │
               │ ││                              │
               │ ││                              │
               │ └▼───────────────────────────►  ▼
               ▼

          Logger                               AccessRightsChecker





"""
from dataclasses import dataclass
from typing import Dict

from p1.model import Client, Request


class AccessRightsChecker:
    rights = {}

    def can_get_client_details(self, request: Request):
        # jakiś check...
        return True


class Logger:
    pass


class LoggedProtectedStore:
    l: Logger
    access_checker: AccessRightsChecker

    def __init__(self, access_checker: AccessRightsChecker, logger: Logger):
        print('executing constructor of LoggedProtectedStore')
        self.l = logger
        self.access_checker = access_checker


class ClientStore(LoggedProtectedStore):
    clients: Dict[int, Client] = {1: Client(1, 'Kadabra'), 2: Client(2, 'Xiaoli'), 3: Client(3, 'Evgeny')}

    def get_client_by_id(self, request: Request, clientid: int) -> Client:
        if not self.access_checker.can_get_client_details(request):
            raise RuntimeError('Unauthorized')
        return self.clients.get(clientid)


class MetricsExporter:
    pass


class EmployeeHrStore(LoggedProtectedStore):

    def __init__(self, access_checker: AccessRightsChecker, logger: Logger, metrics_exporter: MetricsExporter):
        print('executing constructor of EmployeeHrStore')
        super(EmployeeHrStore, self).__init__(access_checker, logger)
        print('done executing constructor of EmployeeHrStore')



class Context:
    __logger: Logger
    __client_store: ClientStore
    __employee_store: EmployeeHrStore
    __access_checker: AccessRightsChecker
    __metrics: MetricsExporter

    @property
    def client_store(self):
        return self.client_store

    def setup(self):
        # tworzenie pełnego grafu serwisów
        print('setting up context')
        self.__logger = Logger()
        self.__access_checker = AccessRightsChecker()
        self.__metrics = MetricsExporter()
        self.__client_store = ClientStore(access_checker=self.__access_checker, logger=self.__logger)
        self.__employee_store = EmployeeHrStore(access_checker=self.__access_checker, logger=self.__logger,
                                                metrics_exporter=self.__metrics)
        print('context initialized')

    def teardown(self):
        # wyłączanie wszystkich serwisów
        print('tearing down context')
        # .....
        print('context destroyed successfully')


if __name__ == '__main__':
    # cs = ClientStore(access_checker=None, logger=None)
    # print(cs.get_client_by_id(3))
    context = Context()
    context.setup()
    print('context created')
    print('now tearing down context')
    context.teardown()
