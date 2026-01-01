import random
from typing import List, Tuple


class TicketStore:
    def __init__(
        self,
        main_max: int = 37,
        main_count: int = 6,
        strong_max: int = 7,
    ) -> None:
        """
        Args:
            main_max: highest allowed main number (inclusive)
            main_count: how many main numbers per ticket
            strong_max: highest allowed strong number (inclusive)
        """
        self._main_max: int = main_max
        self._main_count: int = main_count
        self._strong_max: int = strong_max

        self._masks: List[int] = []     # PRIVATE: bitmasks
        self._strongs: List[int] = []   # PRIVATE: strong numbers

    # --------------------
    # Ticket creation
    # --------------------

    def add_random_ticket(self) -> int:
        """
        Add a random ticket.
        Returns the index of the new ticket.
        """
        nums: List[int] = random.sample(
            range(1, self._main_max + 1),
            self._main_count,
        )

        strong: int = random.randint(1, self._strong_max)

        mask: int = 0
        for n in nums:
            mask |= 1 << (n - 1)

        self._masks.append(mask)
        self._strongs.append(strong)

        return len(self._masks) - 1

    # --------------------
    # Public accessors
    # --------------------

    def count(self) -> int:
        return len(self._masks)

    def get_ticket_numbers(self, index: int) -> Tuple[int, ...]:
        """
        Return the main numbers for a ticket as a tuple.
        """
        mask: int = self._masks[index]
        return self._mask_to_numbers(mask)

    def get_ticket_strong(self, index: int) -> int:
        """
        Return the strong number for a ticket.
        """
        return self._strongs[index]

    def get_ticket(self, index: int) -> Tuple[Tuple[int, ...], int]:
        """
        Return full ticket: (main_numbers, strong_number)
        """
        return (
            self.get_ticket_numbers(index),
            self.get_ticket_strong(index),
        )

    # --------------------
    # Internal helpers
    # --------------------

    def _mask_to_numbers(self, mask: int) -> Tuple[int, ...]:
        """
        Decode a bitmask into a tuple of numbers.
        """
        return tuple(
            n
            for n in range(1, self._main_max + 1)
            if mask & (1 << (n - 1))
        )
