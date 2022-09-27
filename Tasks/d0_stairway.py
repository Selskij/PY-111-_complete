from typing import Union, Sequence
# нужно записать случай с кэшем

def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    print(stairway)

    def lazy_stairway_path(stair_number: int) -> Union[float, int]:
        """

        :param stair_number: принимает нгомер ступени
        :return: стоимость до неё
        """
        if stair_number == 0:
            return stairway[stair_number] # stairway [0]
        if stair_number == 1:
            return stairway[stair_number] # stairway [1]

        current_cost = stairway[stair_number]
        return current_cost + min(lazy_stairway_path(stair_number-1),
                                  lazy_stairway_path(stair_number-2))

    return lazy_stairway_path(len(stairway)-1) # lazy\ рекурсивный случай
# случай прямой   #return direct_stairway_path(stairway)
# случай обратный    #return reverse_stairway_path(stairway)

def direct_stairway_path(stairway: Sequence[Union[float,int]]) -> Union[float,int]:
    #stairway - цена ступени
    count_stairs = len(stairway) # колличество ступеней
    total_cost: list[int] = [0] * count_stairs  # стоимость дойти до ступеней

    # изначальные условия 1 и 2 ступени
    total_cost[0] = stairway[0] # для первой ступени
    total_cost[1] = stairway[1] # дя второй ступени

    # прямой метод обхода = (i-ая цена) + min(стоимость(i-1), стоимость (i-2))

    for i in range (2,count_stairs):
        total_cost[i] = stairway[i] + min(total_cost[i-1], total_cost[i-2])

    return total_cost[-1]  # цена последнего элемента

def reverse_stairway_path(stairway: Sequence[Union[float,int]]) -> Union[float,int]:
    count_stairs = len(stairway)  # колличество ступеней
    total_cost: list[int] = [float("inf")] * count_stairs  # стоимость дойти до ступеней

    # изначальные условия 1 и 2 ступени
    total_cost[0] = stairway[0]  # для первой ступени
    total_cost[1] = stairway[1]  # дя второй ступени

    # обратный метод перерасчёта
    for i in range(0,count_stairs):
        if i+1 < count_stairs:
            total_cost[i+1] = min(total_cost[i] + stairway[i+1], total_cost[i+1])

        if i + 2 < count_stairs:
            total_cost[i + 2] = min(total_cost[i] + stairway[i + 2], total_cost[i + 2])
    return total_cost[-1]



