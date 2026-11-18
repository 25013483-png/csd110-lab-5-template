def solve_hanoi(disks, source, target):
    """Return the move instructions for solving Towers of Hanoi recursively."""
    assert type(disks) is int and disks >= 0
    assert type(source) is int and source in (1, 2, 3)
    assert type(target) is int and target in (1, 2, 3)

    if disks == 0:
        return ""

    spare = 6 - source - target
    move_smaller_disks = solve_hanoi(disks - 1, source, spare)
    move_largest_disk = f"Move disk {disks} from tower {source} to tower {target}.\n"
    move_remaining_disks = solve_hanoi(disks - 1, spare, target)
    return move_smaller_disks + move_largest_disk + move_remaining_disks