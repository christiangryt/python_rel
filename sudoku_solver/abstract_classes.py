from __future__ import annotations
from abc import ABC, abstractmethod

class abstract_board(ABC):

    """

    Board object declares methods for managing subscribers to board

    """

    @abstractmethod
    def attach(self, observer: abstract_drawer) -> None:
        """
        Attach observer to subject
        """
        pass

    @abstractmethod
    def detach(self, observer: abstract_drawer) -> None:
        """
        Detach observer from the subject 
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify observers about an event
        """
        pass

class abstract_drawer(ABC):

    """

    Abstract observer interface, declares update method, used by subject

    """

    @abstractmethod
    def update(self, subject: abstract_board) -> None:
        """
        Receive update from abstract_board
        """
    