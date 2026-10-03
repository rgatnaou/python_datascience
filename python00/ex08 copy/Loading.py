def ft_tqdm(lst: range) -> None:
    num: str = "|"
    lenght = lst.__len__()
    nb: int = 0
    alraedy = -1
    space = "" * 100 + "| "
    for i in lst:
        nb = round(i / lenght * 100)
        if (nb % 2 and nb != alraedy):
            num = num + "██"
            space = " " * (99 - nb) + "| "
        alraedy = nb
        # print(150 - nb)
        print(" " + str(i * 100 // lenght) + "%" + str(num) + space + str(i) + "/" + str(lenght),  end='\r')
        # print(f" {i * 100 // lenght}% {num} {' ' * (100 - round(i /lenght * 100))}| {i}/{lenght}",  end='\r')
        yield num
    num = num + "| "
    print("100%" + str(num) + str(lenght) + "/" + str(lenght) , end='\r')
    yield num
