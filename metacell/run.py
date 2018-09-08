from metacell.processing.parser import Parser
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def run(filename, n_generations=15, dpi=100, interval=20, save=False):
    p = Parser(filename)
    board = p.create_board()
    fig = plt.figure(dpi=dpi)
    plt.axis("off")
    ims = []
    for i in range(n_generations):
        universe = board.get_state()
        ims.append((plt.imshow(universe, cmap=plt.cm.cubehelix),))
        board.update()
    im_ani = animation.ArtistAnimation(
        fig, ims, interval=interval, repeat_delay=3000, blit=True
    )
    if save:
        im_ani.save(("../media/neuron.gif"), writer="imagemagick")
    plt.show()


run('../boards/neuron.mc', save=True)
