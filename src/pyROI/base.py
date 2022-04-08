from abc import ABC
from abc import abstractmethod
from abc import abstractproperty

from numpy import ndarray

from .point import Point


class Roi(ABC):
    @abstractmethod
    def select(
        self,
        src: ndarray,
        *,
        winname: str = "",
        winpos_x: int = 400,
        winpos_y: int = 100,
    ) -> "Roi":
        ...

    @abstractproperty
    def centroid(self) -> Point:
        ...
