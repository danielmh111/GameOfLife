def plot_grid(turns):
    filepath = Path(r"C:\Users\Daniel\projects\GameOfLife\testplot.png")
    figure, ax = plt.subplots()
    plots = []
    print("AAAAAA")
    counter = 1
    print(f"BBBB: counter = {counter}")
    for turn in turns:
        generation, grid = turn
        print(f"CCCCCC: counter = {counter}")
        plot = ax.pcolor(grid)
        ax.set_title(f"Generation {generation}")
        print("DDDDDD")
        plots.append(plot)
        counter += 1
        print("EEEEEE")

    print("XXXXXX")
    animation = ani.ArtistAnimation(fig=figure, artists=plots, interval=1000)
    print("YYYYY")
    writer = ani.PillowWriter(
        fps=1
    )
    animation.save(
        filename=filepath
        ,writer=writer
        )




def plot_grid(turns):
    
    for turn in turns:
        generation, grid = turn
        filepath = Path(f"C:/Users/Daniel/projects/GameOfLife/testplot_{generation}.png")
        figure = plt.figure(figsize=(12,12))
        plot = plt.pcolor(grid)
        plt.title(f"Generation {generation}")
        figure.savefig(
            filepath
        )





def plot_grid(turns):
    filepath = Path(r"C:\Users\Daniel\projects\GameOfLife\testplot.mp4")
    figure, ax = plt.subplots()
    plots = []
    
    counter = 1
    
    for turn in turns:
        generation, grid = turn
        
        plot = ax.pcolormesh(grid)
        ax.set_title(f"Generation {generation}")
        
        plots.append(plot)
        counter += 1
    
    animation = ani.ArtistAnimation(fig=figure, artists=plots, interval=1000)

    return animation
    # writer = ani.FFMpegWriter(
    #     fps=1
    # )
    # animation.save(
    #     filename='test_anim.mp4'
    #     ,writer=writer
    #     )