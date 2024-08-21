class Door:
    """
    Diese Klasse beschreibt eine Türe mit der Eigenschaft color (Farbe) und den Zuständen
    door_is_open (für geöffnete Türe) sowie door_is_locked (für verriegelte Türe).
    Die Türe überwacht die beiden Zustände und verhindert so Aktionen, die nicht möglich sind.
    Das Verriegeln selber delegiert die Türe an ein Objekt vom Typ Door_lock (Türschloss).
    """

    def __init__(self, ref2door_lock, base_color):
        """
        Erzeugt ein Tür-Objekt.
        :param ref2door_lock: Ein Referenzobjekt vom Typ Door_lock, das für das Verriegeln/Entriegeln zuständig ist.
        :param base_color: Die Farbe der Türe.
        """
        self._the_door_lock = ref2door_lock
        self.color = base_color
        self._door_is_open = False
        self._door_is_locked = False

    def open_the_door(self):
        """
        Methode zum Öffnen der Türe.
        Dies ist nur möglich, wenn die Türe nicht verriegelt ist.
        """
        if not self._door_is_locked:
            self._door_is_open = True

    def close_the_door(self):
        """
        Methode zum Schließen der Türe.
        Dies ist immer möglich, auch wenn die Türe bereits geschlossen oder verriegelt ist.
        """
        self._door_is_open = False

    def lock_the_door(self):
        """
        Methode zum Verriegeln der Türe.
        Dies ist nur möglich, wenn die Türe nicht offen ist.
        Das Verriegeln wird an das Türschloss-Objekt delegiert.
        """
        if not self._door_is_open:
            self._door_is_locked = self._the_door_lock.lock()

    def unlock_the_door(self):
        """
        Methode zum Entriegeln der Türe.
        Dies ist nur möglich, wenn die Türe verriegelt ist.
        Das Entriegeln wird an das Türschloss-Objekt delegiert.
        """
        if self._door_is_locked:
            self._door_is_locked = not self._the_door_lock.unlock()

    def test(self):
        """
        Gibt alle Attribute der Tür in der Konsole aus.
        """
        print(f'Türfarbe: {self.color}')
        print(f'Türe offen: {self._door_is_open}')
        print(f'Türe verriegelt: {self._door_is_locked}')

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value
