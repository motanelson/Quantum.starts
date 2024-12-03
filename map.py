import pygame
import os
import sys

# Constants
TILE_SIZE = 32  # Each tile is 32x32 pixels
WINDOW_TITLE = "Tile Map Viewer"

def load_map(file_path):
    """
    Load a map from a text file. Each letter represents a tile.
    """
    try:
        with open(file_path, "r") as f:
            map_data = f.readlines()
        return [line.strip() for line in map_data]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

def load_tile_images(tile_directory):
    """
    Load tile images from the specified directory.
    Each letter (a-z) must have a corresponding .bmp file.
    """
    tiles = {}
    for char in "abcdefghijklmnopqrstuvwxyz":
        tile_path = os.path.join(tile_directory, f"{char}.bmp")
        if os.path.exists(tile_path):
            tiles[char] = pygame.image.load(tile_path)
        else:
            print(f"Warning: Missing tile image for '{char}' at {tile_path}")
    return tiles

def render_map(screen, map_data, tiles):
    """
    Render the tile map on the screen.
    """
    for y, line in enumerate(map_data):
        for x, char in enumerate(line):
            if char in tiles:
                screen.blit(tiles[char], (x * TILE_SIZE, y * TILE_SIZE))

def main():
    # Initialize pygame
    pygame.init()

    # Load map and tiles
    map_file = input("Enter the path to the .txt file: ")
    map_data = load_map(map_file)

    tile_directory = input("Enter the directory containing tile images: ")
    tiles = load_tile_images(tile_directory)

    # Calculate window size based on the map dimensions
    map_width = max(len(line) for line in map_data)
    map_height = len(map_data)
    window_width = map_width * TILE_SIZE
    window_height = map_height * TILE_SIZE

    # Create the window
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption(WINDOW_TITLE)

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill((0, 0, 0))

        # Render the map
        render_map(screen, map_data, tiles)

        # Update the display
        pygame.display.flip()

    # Quit pygame
    pygame.quit()

if __name__ == "__main__":
    main()

