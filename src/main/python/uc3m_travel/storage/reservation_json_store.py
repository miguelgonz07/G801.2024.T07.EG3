from .json_store import JsonStore
from ..hotel_management_config import JSON_FILES_PATH
from ..hotel_management_exception import HotelManagementException


class ReservationJsonStore(JsonStore):
    class __ReservationJsonStore(JsonStore):
        def __init__(self):
            self._file_name = JSON_FILES_PATH + "store_reservation.json"
            self._data_list = []

        def add_item(self, item):
            self.load_store()
            reservation_found = self.find_item("_HotelReservation__localizer", item.localizer)
            if reservation_found:
                raise HotelManagementException("Reservation already exists")
            reservation_found = self.find_item("_HotelReservation__id_card", item.id_card)
            if reservation_found:
                raise HotelManagementException("This ID card has another reservation")
            super().add_item(item)

    __instance = None

    def __new__(cls):
        if not ReservationJsonStore.__instance:
            ReservationJsonStore.__instance = ReservationJsonStore.__ReservationJsonStore()
        return ReservationJsonStore.__instance
