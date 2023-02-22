"""Functions which helps the locomotive engineer to keep track of the train."""

def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return [*args]

def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    first = [1]
    third, fourth = each_wagons_id[3:], each_wagons_id[:2]
    return first + missing_wagons + third + fourth

def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    route_update = route
    route_update['stops'] = []
    for item, key in kwargs.items():
        route_update['stops'] += [key]
    return route_update

def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    updated_route = route
    for item in more_route_information:
        if item not in route:
            updated_route[item] = more_route_information[item]
    return updated_route

def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    updated_depot = list(map(lambda *x: list(x), *wagons_rows))
    return updated_depot
