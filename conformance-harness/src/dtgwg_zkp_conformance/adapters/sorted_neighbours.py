"""Bounded record-006 sorted-neighbour counterexample; no Merkle verification.

Demonstrates why the canonical issuance invariant (strict ordering of committed
handles) is required for adjacent-neighbour non-membership soundness.
"""
def adjacent_neighbours_claim_absent(handles: list[int], handle: int, index: int) -> bool:
    """Unsafe predicate: assumes two adjacent leaves certify an absent handle."""
    return (0 <= index < len(handles) - 1 and
            handles[index] < handle < handles[index + 1])

def is_strictly_sorted(handles: list[int]) -> bool:
    return all(type(x) is int for x in handles) and all(
        lo < hi for lo, hi in zip(handles, handles[1:])
    )

def guarded_non_membership(handles: list[int], handle: int, index: int) -> bool:
    """Semantic prerequisite check, *not* an authenticated set-root proof."""
    if type(handle) is not int or not is_strictly_sorted(handles):
        return False
    return adjacent_neighbours_claim_absent(handles, handle, index)
