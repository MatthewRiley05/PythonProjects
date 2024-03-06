from matplotlib.figure import Figure
import numpy as np
import math as Math
from hkb_diamondsquare import DiamondSquare as DS
from perlin_noise import PerlinNoise
from opensimplex import OpenSimplex
from matplotlib.colors import BoundaryNorm, LinearSegmentedColormap, Normalize
import random
from multiprocessing import Pool, cpu_count

numWorkers = cpu_count()
size = 100
scale = 1
mix = 0.3

colors = [
    '#9BC3D9',  # Deep ocean blue
    '#B4D9E4',  # Light ocean blue
    '#E8D8B1',  # Golden sand
    '#A9D9C2',  # Light green
    '#5B7F6F',  # Dark green
    '#8D6D53',  # Rich brown
    '#F2F2F2',  # White snow
]

diamondSquare = LinearSegmentedColormap.from_list("mycmap", colors)
perlin = LinearSegmentedColormap.from_list("mycmap", colors)
simplex = LinearSegmentedColormap.from_list("mycmap", colors)


# Define the color boundaries
#                                DO    LOB   GS    LG   DG    RB    WS
boundsDiamondSquare = np.array([0, 0.55, 0.6, 0.65, 0.68, 0.75, 0.8, 1])
normDiaomondSquare = BoundaryNorm(boundsDiamondSquare, diamondSquare.N)

boundsPerlin = np.array([0, 0.15, 0.18, 0.25, 0.3, 0.35, 0.45, 1])
normPerlin = BoundaryNorm(boundsPerlin, perlin.N)

boundsSimplex = np.array([0, 0.6, 0.63, 0.67, 0.71, 0.76, 0.8, 1])
normSimplex = BoundaryNorm(boundsSimplex, simplex.N)

def lerp(a, b, t):
    return a * (1 - t) + b * t



### Diamond Square ###
def generateDiamondSquare():
    global size, scale, mix
    noise = DS.diamond_square(shape=(size, size),
                              min_height=0,
                              max_height=1,
                              roughness=scale / 1.5,)

    elevation = []
    for y in range(size):
        elevation.append([0] * size)
        for x in range(size):
            nx = 2 * x / size - 1
            ny = 2 * y / size - 1
            d = 1 - (1 - nx**2) * (1 - ny**2)
            e =     1 * noise[y][x] \
                    +  0.5 * noise[y][x] \
                    + 0.25 * noise[y][x]
            e = lerp(e / (1 + 0.5 + 0.25), 1 - d, mix)
            elevation[y][x] = Math.pow(abs(e), 1)

    noiseMap = elevation

    # Normalize the noiseMap
    min_val = min(map(min, noiseMap))
    max_val = max(map(max, noiseMap))
    for y in range(size):
        for x in range(size):
            noiseMap[y][x] = (noiseMap[y][x] - min_val) / (max_val - min_val)

    # Apply a moving average filter to the noiseMap
    for y in range(1, size - 1):
        for x in range(1, size - 1):
            noiseMap[y][x] = (noiseMap[y - 1][x] + noiseMap[y + 1][x] + noiseMap[y][x - 1] + noiseMap[y][x + 1]) / 4
            
    # Create a new figure and axes
    fig = Figure(figsize=(12, 12), dpi=100)
    fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
    ax = fig.add_subplot(111)

    # Plot the noise array
    ax.imshow(noiseMap, cmap=diamondSquare, norm=normDiaomondSquare, interpolation='none')
    ax.axis('tight')
    ax.axis('off')
    return fig


### Perlin Noise ###
def generate_noise(args):
    x, y, size, scale, mix, seed = args
    noise = PerlinNoise(octaves=10, seed=seed)
    nx = 2 * x / size - 1
    ny = 2 * y / size - 1
    d = 1 - (1 - nx**2) * (1 - ny**2)
    e =     1 * noise(((scale * 0.2) * nx, (scale * 0.2) * ny)) \
            +  0.5 * noise(((scale * 0.4) * nx, (scale * 0.4) * ny)) \
            + 0.25 * noise(((scale * 0.8) * nx, (scale * 0.8) * ny))
    e = lerp(e / (1 + 0.5 + 0.25), 1 - d, mix)
    return Math.pow(abs(e), 1)

def generatePerlin():   
    global size, scale, mix
    seed = random.randint(0, 1000)

    # Create a list of all points in the grid
    points = [(x, y, size, scale, mix, seed) for x in range(size) for y in range(size)]

    # Create a pool of workers
    with Pool(numWorkers) as p:
        # Use map to apply the generate_noise function to each point
        elevation = np.array(p.map(generate_noise, points)).reshape(size, size)

    noiseMap = elevation

    # Create a new figure and axes
    fig = Figure(figsize=(12, 12), dpi=100)
    fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
    ax = fig.add_subplot(111)

    # Plot the noise array
    ax.imshow(noiseMap, cmap=perlin, norm=normPerlin, interpolation='none')
    ax.axis('tight')
    ax.axis('off')
    return fig



### OpenSimplex Noise ###
def openSimplexNoise(nx, ny, gen):
    return gen.noise2(nx, ny) / 2.0 + 0.5

def calculate_elevation(args):
    x, y, gen, size, scale, mix = args
    nx = 2 * x / size - 1
    ny = 2 * y / size - 1
    d = 1 - (1 - nx**2) * (1 - ny**2)
    e =     1 * openSimplexNoise((scale * 2) * nx, (scale * 2) * ny, gen) \
            +  0.5 * openSimplexNoise((scale * 8) * nx, (scale * 8) * ny, gen) \
            + 0.25 * openSimplexNoise((scale * 16) * nx, (scale * 16) * ny, gen)
    e = lerp(e / (1 + 0.5 + 0.25), 1 - d, mix)
    return y, x, Math.pow(abs(e), 1)

def generateOpenSimplex():
    seed = random.randint(0, 1000)
    gen = OpenSimplex(seed)
    
    global size, scale, mix

    elevation = [[0] * size for _ in range(size)]

    with Pool(numWorkers) as p:
        results = p.map(calculate_elevation, [(x, y, gen, size, scale, mix) for y in range(size) for x in range(size)])

    for result in results:
        y, x, e = result
        elevation[y][x] = e

    noiseMap = elevation

    # Create a new figure and axes
    fig = Figure(figsize=(12, 12), dpi=100)
    fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
    ax = fig.add_subplot(111)

    # Plot the noise array
    ax.imshow(noiseMap, cmap=simplex, norm=normSimplex, interpolation='none')
    ax.axis('tight')
    ax.axis('off')
    return fig