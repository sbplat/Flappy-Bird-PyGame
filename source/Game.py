"""
Multiplayer Flappy Bird Game

MIT License

Copyright (c) 2021 sbplat

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# Importing the modules
import random
import sys
import time
import pygame

# Defining the RGB colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()  # Initialize pygame

SIZE = (999, 592)  # 1.6875 x 1 (scale)
screen = pygame.display.set_mode(SIZE)  # Set the screen to that size
pygame.display.set_icon(pygame.image.load("./assets/images/icon.png"))  # Icon
pygame.display.set_caption("Flappy Bird")  # Caption

Clock = pygame.time.Clock()  # Setup the clock

# Loading the images
get_ready_image = pygame.image.load("./assets/images/message.png").convert_alpha()
result_image = pygame.image.load("./assets/images/result.png").convert_alpha()
thin_result_image = pygame.image.load(
    "./assets/images/thin-result.png"
).convert_alpha()
gameover_image = pygame.image.load("./assets/images/gameover.png").convert_alpha()
day_background = pygame.image.load("./assets/images/background-day.png").convert()
night_background = pygame.image.load("./assets/images/background-night.png").convert()
base = pygame.image.load("./assets/images/base.png").convert_alpha()
pipe_green = pygame.image.load("./assets/images/pipe-green.png").convert_alpha()
pipe_red = pygame.image.load("./assets/images/pipe-red.png").convert_alpha()
garbage = pygame.image.load("./assets/images/garbage.png").convert_alpha()
retry_image = pygame.image.load("./assets/images/retry.png").convert()
resume_image = pygame.image.load("./assets/images/resume.png").convert()
help_image = pygame.image.load("./assets/images/help.png").convert()

bluebird_downflap = pygame.image.load(
    "./assets/images/bluebird-downflap.png"
).convert_alpha()
bluebird_midflap = pygame.image.load(
    "./assets/images/bluebird-midflap.png"
).convert_alpha()
bluebird_upflap = pygame.image.load(
    "./assets/images/bluebird-upflap.png"
).convert_alpha()

redbird_downflap = pygame.image.load(
    "./assets/images/redbird-downflap.png"
).convert_alpha()
redbird_midflap = pygame.image.load(
    "./assets/images/redbird-midflap.png"
).convert_alpha()
redbird_upflap = pygame.image.load(
    "./assets/images/redbird-upflap.png"
).convert_alpha()

yellowbird_downflap = pygame.image.load(
    "./assets/images/yellowbird-downflap.png"
).convert_alpha()
yellowbird_midflap = pygame.image.load(
    "./assets/images/yellowbird-midflap.png"
).convert_alpha()
yellowbird_upflap = pygame.image.load(
    "./assets/images/yellowbird-upflap.png"
).convert_alpha()

# Transforming the images to the screen size
get_ready_image = pygame.transform.scale(get_ready_image, SIZE)
gameover_image = pygame.transform.scale(
    gameover_image, (gameover_image.get_width() * 3, gameover_image.get_height() * 3)
)
day_background = pygame.transform.scale(day_background, SIZE)
night_background = pygame.transform.scale(night_background, SIZE)
base = pygame.transform.scale(base, SIZE)
pipe_green = pygame.transform.scale(
    pipe_green, (pipe_green.get_width() * 2, pipe_green.get_height() * 2)
)
pipe_red = pygame.transform.scale(
    pipe_red, (pipe_red.get_width() * 2, pipe_red.get_height() * 2)
)
pipe_green_flipped = pygame.transform.rotate(pipe_green, 180)
pipe_red_flipped = pygame.transform.rotate(pipe_red, 180)

bluebird_downflap = pygame.transform.scale(
    bluebird_downflap,
    (bluebird_downflap.get_width() * 2, bluebird_downflap.get_height() * 2),
)
bluebird_midflap = pygame.transform.scale(
    bluebird_midflap,
    (bluebird_midflap.get_width() * 2, bluebird_midflap.get_height() * 2),
)
bluebird_upflap = pygame.transform.scale(
    bluebird_upflap, (bluebird_upflap.get_width() * 2, bluebird_upflap.get_height() * 2)
)

redbird_downflap = pygame.transform.scale(
    redbird_downflap,
    (redbird_downflap.get_width() * 2, redbird_downflap.get_height() * 2),
)
redbird_midflap = pygame.transform.scale(
    redbird_midflap, (redbird_midflap.get_width() * 2, redbird_midflap.get_height() * 2)
)
redbird_upflap = pygame.transform.scale(
    redbird_upflap, (redbird_upflap.get_width() * 2, redbird_upflap.get_height() * 2)
)

yellowbird_downflap = pygame.transform.scale(
    yellowbird_downflap,
    (yellowbird_downflap.get_width() * 2, yellowbird_downflap.get_height() * 2),
)
yellowbird_midflap = pygame.transform.scale(
    yellowbird_midflap,
    (yellowbird_midflap.get_width() * 2, yellowbird_midflap.get_height() * 2),
)
yellowbird_upflap = pygame.transform.scale(
    yellowbird_upflap,
    (yellowbird_upflap.get_width() * 2, yellowbird_upflap.get_height() * 2),
)

blue_birds = [bluebird_downflap, bluebird_midflap, bluebird_upflap]
red_birds = [redbird_downflap, redbird_midflap, redbird_upflap]
yellow_birds = [yellowbird_downflap, yellowbird_midflap, yellowbird_upflap]

def get_font(font_path, size):
    """
    Gets a font and converts it to a pygame font.

    Args:
        font_path(str): The path of the fonts location
        size(int): The size of the font

    Returns:
        font(pygame.font.Font): The font and size converted to a pygame font
    """
    return pygame.font.Font(str(font_path), int(size))  # Returns the font


def draw_text(surface, font, colour, text, x, y):
    """
    Draws text onto the screen.

    Args:
        surface(pygame.display): The screen to draw on
        font(pygame.font.Font): The font to draw with
        colour(RGB tuple): The colour to draw the font with
        text(str): The text to draw
        x(int): The center x coordinate of the text
        y(int): The center y coordinate of the text

    Returns:
        None
    """
    rendered_font = font.render(str(text), True, colour)  # Render the text
    text_rect = rendered_font.get_rect()  # Get the text rect
    text_rect.center = (x, y)  # Change the center
    surface.blit(rendered_font, text_rect)  # Blit the text


def draw_background(surface, is_day):
    """
    Draws the background.

    Args:
        surface(pygame.display): The screen to draw on
        is_day(bool): Whether or not it is day

    Returns:
        None
    """
    surface.fill(WHITE)  # Fills the screen with white
    if is_day:  # Day
        surface.blit(day_background, (0, 0))  # Blit background day

    else:  # Not day
        surface.blit(night_background, (0, 0))  # Blit background night


def draw_base(surface, floor_back_x):
    """
    Draws the scrolling base.

    Args:
        surface(pygame.display): The screen to draw on
        floor_back_x(int): The back x coordinate of the base

    Returns:
        floor_back_x(int): The back x coordinate of the base
    """

    floor_back_x -= 2  # Subtract 2 from the floor back x to keep it scrolling

    if floor_back_x < 0:  # Smaller than zero
        floor_back_x = SIZE[0]  # Sets the x coordinate to the right end of the screen

    surface.blit(
        base, pygame.Rect(floor_back_x, 50, SIZE[0], SIZE[1])
    )  # Blit the right side
    surface.blit(
        base, pygame.Rect(floor_back_x - SIZE[0], 50, SIZE[0], SIZE[1])
    )  # Blit the left side

    return floor_back_x  # Returns the floor_back_x


def draw_bird(surface, birds, birdX, birdY, bird_frame, rotation, animate, bird_image):
    """
    Draws the bird.

    Args:
        surface(pygame.display): The screen to draw the bird on
        birds(list): The set of bird images
        birdX(int): Bird X coordinate
        birdY(int): Bird Y coordinate
        bird_frame(int): The current bird frame
        rotation(int): Bird rotation angle amount
        animate(bool): Whether or not to animate the bird to the next frame
        bird_image(pygame.image): The pygame bird image

    Returns:
        bird_rect(pygame.Rect): The rect of the bird
        bird_frame(int): The current bird frame
        bird_image(pygame.image): The pygame bird image
    """
    if not bird_image:  # Bird image is None
        bird_image = birds[0]  # Sets the bird image to the first in the bird list

    if animate:  # Bird needs to be animated
        bird_frame += 1  # Increase the frame by 1
        bird_frame %= 3  # Modulo the frame so the number loops from 0-2
        bird_image = birds[bird_frame]  # Get the current image from the frame

    rotated_bird = pygame.transform.rotate(bird_image, rotation)  # Rotate the bird
    bird_rect = rotated_bird.get_rect()  # Get the bird rect

    bird_rect.center = (birdX, birdY)  # Change the center

    surface.blit(rotated_bird, bird_rect)  # Blits the new bird to the screen

    return (
        bird_rect,
        bird_frame,
        bird_image,
    )  # Returns bird_rect, bird_frame and bird_image


def draw_pipes(surface, pipes, pipe_assets):
    """
    Draws the pipes.

    Args:
        surface(pygame.display): The screen to draw the bird on
        pipes(list): A list containing the pipe rects
        pipe_assets(list): A list containing the pipe images images (rotated and non-rotated)

    Returns:
        None
    """
    pipe = pipe_assets[0]  # Get the pipe from index 0
    pipe_flipped = pipe_assets[1]  # Get the flipped pipe from index 1

    for pipe_info in pipes:  # Loops through all the pipe sets (up and down pipes)
        pipe_set = pipe_info[0]  # Set the pipe_set to the first index of the list
        bottom_pipe_rect = pipe_set[0]  # Get the bottom pipe
        top_pipe_rect = pipe_set[1]  # Get the top pipe

        surface.blit(
            pipe, bottom_pipe_rect
        )  # Blit the pipe using the bottom_pipe_rect onto the screen
        surface.blit(
            pipe_flipped, top_pipe_rect
        )  # Blit the flipped_pipe using the top_pipe_rect onto the screen


def create_pipes(pipes, pipe_assets):
    """
    Creates the pipes. Generates them randomly and appends them to the pipe list.

    Args:
        pipes(list): A list containing the pipe rects
        pipe_assets(list): A list containing the pipe images images (rotated and non-rotated)

    Returns:
        pipes(list): A list containing the pipe rects
    """
    pipe = pipe_assets[0]  # Get the first index of the list
    pipe_height = random.randint(400, SIZE[1] - 100)  # Generate a random pipe height
    pipeX = SIZE[0] + 50  # Pipe x coordinate

    bottom_pipe_rect = pipe.get_rect()  # Get the pipe rect
    bottom_pipe_rect.midtop = (pipeX, pipe_height)  # Change the midtop coordinates

    top_pipe_rect = pipe.get_rect()  # Get the pipe rect
    top_pipe_rect.midbottom = (
        pipeX,
        pipe_height - 250,
    )  # Change the midbottom coordinates

    score_counted = False  # Set the score counted to False

    pipes.append(
        [[bottom_pipe_rect, top_pipe_rect], score_counted]
    )  # Appends bottom_pipe_rect, top_pipe_rect and score_counted to the pipes list

    return pipes  # Returns the pipes


def remove_pipes(pipes):
    """
    Removes the pipes that are not visible in the screen.

    Args:
        pipes(list): A list containing the pipe rects

    Returns:
        pipes(list): A list containing the pipe rects
    """
    for pipe_info in pipes:  # Loop through all the pipe sets (up and down pipes)
        done = False  # Sets done variable to False
        # We need to have this to break out of our first for loop
        pipe_set = pipe_info[0]
        for pipe in pipe_set:  # Loops through the pipes
            if done:  # If its done, we continue and skip this one
                continue  # Continues to the next pipe and skips the code below

            # Its not done
            if pipe.centerx <= -50:  # Checks if the center is out of the screen
                pipes.remove(pipe_info)  # Remove the pipe from the list
                done = True  # Sets done to True

    return pipes


def move_pipes_back(pipes):
    """
    Moves the pipes backwards according to the speed the background is moving.

    Args:
        pipes(list): A list containing the pipe rects

    Returns:
        pipes(list): A list containing the pipe rects
    """
    for pipe_info in pipes:  # Loops through all the pipe sets (up and down pipes)
        pipe_set = pipe_info[0]  # Set the pipe_set to the first index of the list
        for pipe in pipe_set:  # Loops through the pipes
            pipe.centerx -= 2  # Subtract the pipe center x by 2

    return pipes  # Returns the pipes


def move_pipe_vertically(pipes, up, down):
    """
    Moves the pipes vertically.

    Args:
        pipes(list): A list containing the pipe rects
        up(bool): Up key pressed
        down(bool): Down key pressed

    Returns:
        pipes(list): A list containing the pipe rects
    """
    for pipe_info in pipes:  # Loops through the pipes
        pipe_set = pipe_info[0]  # Set the pipe_set to the first index of the list
        bottom_pipe = pipe_set[0]  # Get the bottom pipe
        top_pipe = pipe_set[1]  # Get the top pipe

        can_up = True  # Sets can_up to True
        can_down = True  # Sets can_down to True

        if (
            top_pipe.centery <= -260
        ):  # Checks if the top pipes centery is less than -260
            top_pipe.centery = -260  # Set the centery to -260 if it is
            can_up = (
                False  # Sets can_up to False to prevent it from going up any higher
            )

        elif (
            bottom_pipe.centery >= 800
        ):  # Checks if the bottom pipes centery is greater than 800
            bottom_pipe.centery = 800  # Set the centery to 800 if it is
            can_down = (
                False  # Sets can_down to False to prevent it from going down any lower
            )

        if down and can_down:  # Down is pressed and can_down is True
            top_pipe.centery += 2  # Increase the top pipe centery by 2
            bottom_pipe.centery += 2  # Increase the bottom pipe centery by 2

        if up and can_up:  # Up is pressed and can_up is True
            top_pipe.centery -= 2  # Decreases the top pipe centery by 2
            bottom_pipe.centery -= 2  # Decreases the bottom pipe centery by 2

    return pipes  # Return the pipe list


def add_items(garbages):
    """
    Adds items/garbage to the garbage list.

    Args:
        garbages(list): A list containing the garbage rects

    Returns:
        garbages(list): A list containing the garbage rects
    """
    garbage_chance = random.randint(0, 600)  # Random number between 0-600
    if garbage_chance == 0:  # Number is 0 (1/601 chance so around 1 garbage per 10s)
        garbageX = SIZE[0] + 50  # Set the garbage x coordinate to SIZE[0] + 50
        # Randomly generate the garbage y coordinate between 100 and SIZE[1]-100
        garbageY = random.randint(100, SIZE[1] - 100)

        garbage_rect = garbage.get_rect()  # Get the garbage rect
        garbage_rect.center = (garbageX, garbageY)  # Set the garbage center coordinates

        garbages.append(
            garbage_rect
        )  # Append the new garbage rect to the garbage rect list

    return garbages  # Return the garbages


def draw_items(surface, garbages):
    """
    Draws items/garbage onto the screen.

    Args:
        surface(pygame.display): The screen to draw the garbage on
        garbages(list): A list containing the garbage rects

    Returns:
        None
    """
    for garbage_rect in garbages:  # Loop through the garbage list
        surface.blit(garbage, garbage_rect)  # Blit the garbage onto the screen


def move_items_back(garbages):
    """
    Moves the items/garbage backwards according to the speed the background is moving.

    Args:
        garbages(list): A list containing the garbage rects

    Returns:
        garbages(list): A list containing the garbage rects
    """
    for garbage_rect in garbages:  # Loops through the garbages
        garbage_rect.centerx -= 2  # Decrease the centerx coordinate by 2

    return garbages  # Returns the garbage list


def remove_items(garbages):
    """
    Removes the items/garbages that are no longer visible on the screen.

    Args:
        garbages(list): A list containing the garbage rects

    Returns:
        garbages(list): A list containing the garbage rects
    """
    for garbage_rect in garbages:  # Loop through all the garbage_rect's
        if garbage_rect.centerx <= -50:  # Checks if the center is out of the screen
            garbages.remove(garbage_rect)  # Remove the garbage item

    return garbages  # Returns the garbage list


def check_death(bird_rect, garbages, pipes):
    """
    Checks if the player/bird is dead.

    Args:
        bird_rect(pygame.Rect): The rect of the bird
        garbages(list): A list containing the garbage rects
        pipes(list): A list containing the pipe rects

    Returns:
        death(bool): Whether or not the bird is dead
    """
    if bird_rect.midbottom[1] > SIZE[1] - 50:  # Bird is touching the ground
        return True  # Returns True (the bird is dead)

    for pipe_info in pipes:  # Loops through the pipes
        pipe_set = pipe_info[0]  # Set the pipe_set to the first index of the list
        bottom_pipe = pipe_set[0]  # Get the bottom pipe
        top_pipe = pipe_set[1]  # Get the top pipe

        if (bottom_pipe.colliderect(bird_rect)) or (
            top_pipe.colliderect(bird_rect)
        ):  # Bottom or top pipe is colliding with the bird
            return True  # Returns True (the bird is dead)

    for garbage_rect in garbages:  # Loop through the garbages
        if garbage_rect.colliderect(bird_rect):  # Garbage is colliding with the bird
            return True  # Returns True (the bird is dead)

    return False  # Returns False (the bird is still alive)


def increase_score(score, pipes, birdX):
    """
    Checks if the player/bird is dead.

    Args:
        score(int): The current player score
        pipes(list): A list containing the pipe rects
        birdX(int): The x coordinate of the bird

    Returns:
        core(int): The current player score
    """
    for pipe_info in pipes:  # Loops through the pipes
        pipe_set = pipe_info[0]  # Set the pipe_set to the first index of the list
        bottom_pipe = pipe_set[0]  # Get the bottom pipe
        score_counted = pipe_info[1]  # Get the top pipe

        if (bottom_pipe.centerx + bottom_pipe.width / 2 <= birdX) and (
            not score_counted
        ):  # Bird passed through the pipe already and
            # also checks to see if the score has not already been counted
            score += 1  # Increase the score by 1
            pipe_info[1] = True  # Set the pipe score counted to True

    return score  # Returns the new score


def draw_score(surface, bird_player_score, start_time):
    """
    Draws the score onto the screen.

    Args:
        surface(pygame.display): The screen to draw on
        bird_player_score(int): The score of the bird player
        start_time(int): The unix timestamp of the time when the game started

    Returns:
        None
    """
    font = get_font("./assets/fonts/04B_19__.ttf", 60)  # Get the 04B_19__ font

    draw_text(
        surface, font, WHITE, str(bird_player_score), 80, 50
    )  # Draws the bird players score

    time_taken = f"{(time.time() - start_time):.2f}"  # Get the total time elapsed

    draw_text(
        surface, font, WHITE, time_taken, SIZE[0] - 100, 50
    )  # Draws the total time elapsed


def get_highscore(score):
    """
    Gets the last saved highscore from the highscore.txt file.

    Args:
        score(int): The score of the bird player

    Returns:
        highscore(int): The all time highscore of this game
    """
    with open("./assets/data/highscore.txt", "r") as file:  # Open the file
        lines = []  # Defines the lines list

        while True:  # Forever loop
            line = file.readline().rstrip(
                "\n"
            )  # Read the line and strip \n from the right side
            if line == "":  # If the line is blank
                break  # Breaks out of the loop
            lines.append(line)  # Appends the line to the list

        highscore = 0  # Defines the highscore variable

        for line in lines:  # Loops through the lines
            try:
                highscore = int(line)  # Converts the line to an integer
                break  # Breaks out of the for loop
            except ValueError:
                continue  # Skips to the next line if its corrupted (cannot convert to int)

        if int(score) > highscore:  # If the current score is higher than the highscore
            save_highscore(int(score))  # Sets the current score as the highscore
            return int(score)  # Returns the current score

        else:  # The highscore is higher
            save_highscore(
                highscore
            )  # Saves the highscore again and erases everything (the file could be corrupted)
            return highscore  # Returns the all time highscore


def save_highscore(highscore):
    """
    Saves the highscore to the highscore.txt file.

    Args:
        highscore(int): The all time highscore

    Returns:
        None
    """
    with open("./assets/data/highscore.txt", "w") as file:  # Open the file
        file.write(
            str(highscore)
        )  # Write the highscore to the file and erases everything else


def blit_help(surface):
    """
    Blits the help menu onto the screen.

    Args:
        surface(pygame.display): The screen to blit the highscore on

    Returns:
        None
    """
    flappy_font_path = "./assets/fonts/FlappyBirdy.ttf"  # Defines the path to the font

    num_font_path = "./assets/fonts/04B_19__.ttf"  # Defines the path to the font

    new_result_image = pygame.transform.scale(
        result_image, SIZE
    )  # Transform the image to the size of the screen
    surface.blit(new_result_image, (0, 0))  # Blit the image

    pygame.draw.circle(
        surface, RED, (SIZE[0] - 80, 80), 30
    )  # Draws a red circle in the top right corner (the exit button)

    draw_text(
        surface, get_font(flappy_font_path, 120), WHITE,
        "How to play",
        SIZE[0] // 2, SIZE[1] // 2 - 200,
    )  # Draws How to play

    draw_text(
        surface, get_font(num_font_path, 33), WHITE,
        "Player 1 is the bird and player 2 is the pipe controller.",
        SIZE[0] // 2, SIZE[1] // 2 - 100,
    )

    draw_text(
        surface, get_font(num_font_path, 33), WHITE,
        "Player 1 Controls:",
        SIZE[0] // 2 - 250, SIZE[1] // 2,
    )

    draw_text(
        surface, get_font(num_font_path, 25), WHITE,
        "Space bar",
        SIZE[0] // 2 - 250, SIZE[1] // 2 + 50,
    )

    draw_text(
        surface, get_font(num_font_path, 33), WHITE,
        "Player 2 Controls:",
        SIZE[0] // 2 + 250, SIZE[1] // 2,
    )

    draw_text(
        surface, get_font(num_font_path, 25), WHITE,
        "Up and down arrow keys",
        SIZE[0] // 2 + 250, SIZE[1] // 2 + 50,
    )

    draw_text(
        surface, get_font(num_font_path, 33), WHITE,
        "Player 1 Objective:",
        SIZE[0] // 2 - 250, SIZE[1] // 2 + 135,
    )

    draw_text(
        surface, get_font(num_font_path, 25), WHITE,
        "Dodge all the pipes and garbage",
        SIZE[0] // 2 - 250, SIZE[1] // 2 + 185,
    )

    draw_text(
        surface, get_font(num_font_path, 25), WHITE,
        "to survive as long as possible.",
        SIZE[0] // 2 - 250, SIZE[1] // 2 + 215,
    )

    draw_text(
        surface, get_font(num_font_path, 33), WHITE,
        "Player 2 Objective:",
        SIZE[0] // 2 + 250, SIZE[1] // 2 + 135,
    )

    draw_text(
        surface, get_font(num_font_path, 25), WHITE,
        "Move the pipes up and down",
        SIZE[0] // 2 + 250, SIZE[1] // 2 + 185,
    )

    draw_text(
        surface, get_font(num_font_path, 25), WHITE,
        "to destroy the bird.",
        SIZE[0] // 2 + 250, SIZE[1] // 2 + 215,
    )


def draw_menu():
    """
    Draws the main menu screen.

    Args:
        None

    Returns:
        None
    """
    help_screen = False  # Defines the variable
    is_day = random.choice([True, False])  # Randomly choose if its day or night
    while True:  # Forever loop
        help_image_rect = help_image.get_rect()  # Get the help button rect
        help_image_rect.center = (
            70,
            SIZE[1] - 50,
        )  # Change the help button rect center

        for event in pygame.event.get():  # Loops through the events
            if event.type == pygame.QUIT:  # If the user closes the window
                pygame.quit()  # Exits pygame
                sys.exit(1)  # Exits the program

            if event.type == pygame.MOUSEBUTTONDOWN:  # Mouse down pressed
                mouse_pos = pygame.mouse.get_pos()  # Get the current mouse position
                if help_image_rect.collidepoint(
                    mouse_pos
                ):  # The mouse click was in the help button
                    help_screen = True  # Sets help_screen to True

                if (abs(mouse_pos[0] - (SIZE[0] - 80)) <= 30) and (
                    abs(mouse_pos[1] - 80) <= 30
                ):  # The red close button was pressed
                    help_screen = False

            if event.type == pygame.KEYDOWN:  # If the user presses a key
                if event.key == pygame.K_ESCAPE:  # If the key pressed is escape
                    if help_screen:  # Help screen is active
                        help_screen = False  # Sets the help screen to False
                    else:  # Help screen is not active
                        pygame.quit()  # Exits pygame
                        sys.exit(1)  # Exits the program

                if event.key == pygame.K_SPACE:  # If the key pressed is space
                    if help_screen:
                        help_screen = False
                    else:
                        draw_game(is_day)  # Draw the game

                if event.key == pygame.K_h:  # H key is pressed
                    help_screen = not help_screen  # Flips the help screen variable

        if help_screen:  # If the user is currently in the help screen
            blit_help(screen)  # Blit the help menu

            pygame.display.flip()  # Flips the display so the user can see
            Clock.tick(60)  # Sets the FPS to 60

            continue  # Continue to the next loop

        draw_background(screen, is_day)  # Draw the background

        screen.blit(get_ready_image, (0, 0))  # Shows the get ready image

        screen.blit(help_image, help_image_rect)  # Blit the help button

        pygame.display.flip()  # Flips the display so the user can see
        Clock.tick(60)  # Sets the FPS to 60


def blit_paused(surface):
    """
    Draws the paused menu screen.

    Args:
        surface(pygame.display): The screen to draw on

    Returns:
        None
    """
    flappy_font_path = "./assets/fonts/FlappyBirdy.ttf"  # Defines the path to the font

    thin_result_image_rect = thin_result_image.get_rect()  # Get the image rect
    thin_result_image_rect.center = (
        SIZE[0] // 2,
        SIZE[1] // 2 + 150,
    )  # Set the image rects center
    surface.blit(thin_result_image, thin_result_image_rect)  # Blit the image

    draw_text(
        surface,
        get_font(flappy_font_path, 250),
        WHITE,
        "Game Paused",
        SIZE[0] // 2,
        SIZE[1] // 2 - 50,
    )  # Draws the text: Game Paused

    resume_image_rect = resume_image.get_rect()  # Get the image rect
    resume_image_rect.center = (
        SIZE[0] // 2 - 110,
        SIZE[1] // 2 + 150,
    )  # Set the image rects center
    surface.blit(resume_image, resume_image_rect)  # Blit the image

    retry_image_rect = retry_image.get_rect()  # Get the image rect
    retry_image_rect.center = (
        SIZE[0] // 2 + 60,
        SIZE[1] // 2 + 150,
    )  # Set the image rects center
    surface.blit(retry_image, retry_image_rect)  # Blit the image


def blit_dead(surface, score, highscore):
    """
    Draws the death screen.

    Args:
        surface(pygame.display): The screen to draw on
        score(int): The player score
        highscore(int): The all time highscore

    Returns:
        None
    """
    flappy_font_path = "./assets/fonts/FlappyBirdy.ttf"  # Defines the path to the font

    num_font_path = "./assets/fonts/04B_19__.ttf"  # Defines the path to the font

    result_image_rect = result_image.get_rect()  # Get the image rect
    result_image_rect.center = (
        SIZE[0] // 2,
        SIZE[1] // 2 + 60,
    )  # Set the image rects center
    surface.blit(result_image, result_image_rect)  # Blit the image

    gameover_image_rect = gameover_image.get_rect()  # Get the image rect
    gameover_image_rect.center = (
        SIZE[0] // 2,
        SIZE[1] // 2 - 200,
    )  # Set the image rects center
    surface.blit(gameover_image, gameover_image_rect)  # Blit the image

    draw_text(
        surface,
        get_font(flappy_font_path, 120),
        WHITE,
        "Score",
        SIZE[0] // 2 - 180,
        SIZE[1] // 2 - 20,
    )  # Draws score

    draw_text(
        surface,
        get_font(num_font_path, 60),
        WHITE,
        score,
        SIZE[0] // 2 - 180,
        SIZE[1] // 2 + 50,
    )  # Draws the score

    draw_text(
        surface,
        get_font(flappy_font_path, 120),
        WHITE,
        "Highscore",
        SIZE[0] // 2 + 120,
        SIZE[1] // 2 - 20,
    )  # Draws highscore

    draw_text(
        surface,
        get_font(num_font_path, 60),
        WHITE,
        highscore,
        SIZE[0] // 2 + 120,
        SIZE[1] // 2 + 50,
    )  # Draws the highscore

    retry_image_rect = retry_image.get_rect()  # Get the image rect
    retry_image_rect.center = (
        SIZE[0] // 2,
        SIZE[1] // 2 + 150,
    )  # Set the image rects center
    surface.blit(retry_image, retry_image_rect)  # Blit the image


def draw_game(is_day):
    """
    Draws the game and contains the game logic.

    Args:
        is_day(bool): Whether or not it is day.

    Returns:
        None
    """
    start_time = time.time()  # Current time

    score = 0  # Sets the score to 0
    highscore = 0

    dead = False  # Bird dead
    paused = False  # Currently paused
    pause_time = 0  # The time when the player paused
    unpause_time = 0  # The time when the player unpaused

    birdX = 200  # Bird X position
    birdY = 120  # Bird Y position
    birds = random.choice(
        [blue_birds, red_birds, yellow_birds]
    )  # Get a random bird colour set
    bird_rect = pygame.Rect(birdX, birdY, 0, 0)  # Bird rect
    flap = []  # Define the flap list
    bird_frame = 0  # Current bird frame
    bird_image = None  # Current bird image
    ANIMATE_BIRD = pygame.USEREVENT + 1  # Animate bird event
    pygame.time.set_timer(ANIMATE_BIRD, 50)  # Set the animate bird event timer

    pipes = []  # Defines the pipe list
    pipe_assets = random.choice(
        [[pipe_green, pipe_green_flipped], [pipe_red, pipe_red_flipped]]
    )  # Random pipe colour list
    CREATE_PIPE = pygame.USEREVENT + 2  # Create pipe event
    pygame.time.set_timer(CREATE_PIPE, 2000)  # Set the create pipe event timer

    garbages = []  # Defines the garbages list

    floor_back_x = SIZE[1]  # Current floor back x coordinate

    up = False  # Defines the variables
    down = False  # Defines the variables
    space_bar = False  # Defines the variables

    while True:  # Forever while loop (using sys.exit to exit)
        bird_animate = False  # Set the bird animtion to False

        for event in pygame.event.get():  # Loops through the events
            if event.type == pygame.QUIT:  # If the user closes the window
                pygame.quit()  # Exits pygame
                sys.exit(1)  # Exits the program

            if event.type == pygame.MOUSEBUTTONDOWN:  # Mouse down button pressed
                mouse_pos = pygame.mouse.get_pos()  # Get current mouse position
                if dead:  # Bird is dead
                    retry_image_rect = (
                        retry_image.get_rect()
                    )  # Get the retry image rect
                    retry_image_rect.center = (
                        SIZE[0] // 2,
                        SIZE[1] // 2 + 150,
                    )  # Change the retry image rect center

                    if retry_image_rect.collidepoint(
                        mouse_pos
                    ):  # Retry image rect is pressed
                        draw_menu()  # Draw the main menu

                if paused:  # Currently paused
                    resume_image_rect = (
                        resume_image.get_rect()
                    )  # Get the resume button rect
                    resume_image_rect.center = (
                        SIZE[0] // 2 - 110,
                        SIZE[1] // 2 + 150,
                    )  # Set the resume button rect center

                    retry_image_rect = (
                        retry_image.get_rect()
                    )  # Get the retry button rect
                    retry_image_rect.center = (
                        SIZE[0] // 2 + 60,
                        SIZE[1] // 2 + 150,
                    )  # Set the retry image rect center

                    if resume_image_rect.collidepoint(
                        mouse_pos
                    ):  # Resume button clicked
                        unpause_time = (
                            time.time()
                        )  # Set the unpause time to the current time
                        time_difference = (
                            unpause_time - pause_time
                        )  # Get the time difference by subtracting the unpause from the pause time
                        start_time += time_difference  # Increase the start time by the time difference
                        paused = False  # Set paused to False

                    if retry_image_rect.collidepoint(mouse_pos):  # Retry button clicked
                        draw_menu()  # Draw the main menu

            if event.type == pygame.KEYDOWN:  # If the user presses a key
                if event.key == pygame.K_ESCAPE:  # If the key pressed is escape
                    if not dead:  # Player not dead
                        if paused:  # Currently paused
                            unpause_time = (
                                time.time()
                            )  # Set the unpause time to the current time
                            time_difference = (
                                unpause_time - pause_time
                            )  # Get the time difference by subtracting the unpause from the pause time
                            start_time += time_difference  # Increase the start time by the time difference
                            paused = False  # Set paused to False
                        else:  # Not paused
                            pause_time = (
                                time.time()
                            )  # Set the pause time to the current time
                            paused = True  # Set paused to True

                if event.key == pygame.K_SPACE:  # If the key pressed is space
                    if paused:  # Currently paused
                        unpause_time = (
                            time.time()
                        )  # Set the unpause time to the current time
                        time_difference = (
                            unpause_time - pause_time
                        )  # Get the time difference by subtracting the unpause from the pause time
                        start_time += time_difference  # Increase the start time by the time difference
                        paused = False  # Set paused to False
                    elif dead:  # Player is dead
                        draw_menu()  # Draw the main menu
                    else:  # In the game
                        space_bar = True  # Sets the space key pressed to True

                if event.key == pygame.K_UP:  # If the key pressed is up
                    up = True  # Sets the up to True

                if event.key == pygame.K_DOWN:  # If the key pressed is down
                    down = True  # Sets the down to True

                if event.key == pygame.K_r:  # R key pressed
                    draw_menu()  # Draw the main menu

                if event.key == pygame.K_p:  # If the key pressed is p
                    if not dead:  # Player not dead
                        if paused:  # Currently paused
                            unpause_time = (
                                time.time()
                            )  # Set the unpause time to the current time
                            time_difference = (
                                unpause_time - pause_time
                            )  # Get the time difference by subtracting the unpause from the pause time
                            start_time += time_difference  # Increase the start time by the time difference
                            paused = False  # Set paused to False
                        else:  # Not paused
                            pause_time = (
                                time.time()
                            )  # Set the pause time to the current time
                            paused = True  # Set paused to True

            if event.type == pygame.KEYUP:  # Key is released
                if event.key == pygame.K_SPACE:  # Space key
                    if (not paused) and (
                        not dead
                    ):  # Not currently paused and player not dead
                        space_bar = False  #  Sets the space bar to False

                if event.key == pygame.K_UP:  # Up arrow key
                    up = False  #  Sets the up to False

                if event.key == pygame.K_DOWN:  # Down arrow key
                    down = False  #  Sets the down to False

            if event.type == ANIMATE_BIRD:  # Animate bird event
                if (not paused) and (
                    not dead
                ):  # Not currently paused and player not dead
                    bird_animate = True  # Sets bird_animate to True

            if event.type == CREATE_PIPE:  # Create pipe event
                if (not paused) and (
                    not dead
                ):  # Not currently paused and player not dead
                    pipes = create_pipes(pipes, pipe_assets)  # Create a pipe

        if paused:  # Currrently paused
            blit_paused(screen)  # Blit the paused screen

            pygame.display.flip()  # Flips the display so the user can see
            Clock.tick(60)  # Sets the FPS to 60

            continue  # Continues to the next loop

        if dead:  # If the bird is dead
            blit_dead(screen, score, highscore)  # Blit the dead screen

            pygame.display.flip()  # Flips the display so the user can see
            Clock.tick(60)  # Sets the FPS to 60

            continue  # Continues to the next loop

        if space_bar:  # Space key pressed
            anti_flap = random.choice([[0], [0], []])  # Random anti flap chance
            # This is to prevent the bird from going to fast suddenly

            flap = (
                anti_flap + list(reversed(range(0, 10))) + [0 for i in range(8)]
            )  # Has a list of many numbers to smoothen the flight

        draw_background(screen, is_day)  # Draws the background
        pipes = move_pipes_back(pipes)  # Move the pipes backwards
        pipes = remove_pipes(pipes)  # Remove the pipes that are out of the screen
        pipes = move_pipe_vertically(pipes, up, down)  # Move the pipes vertically
        draw_pipes(screen, pipes, pipe_assets)  # Draw the pipes
        garbages = add_items(garbages)  # Add a item/garbage
        garbages = move_items_back(garbages)  # Move the items/garbages back
        garbages = remove_items(
            garbages
        )  # Remove the items/garbages that are out of the screen
        draw_items(screen, garbages)  # Draw the items/garbages
        floor_back_x = draw_base(screen, floor_back_x)  # Draws the base (floor)

        dead = check_death(bird_rect, garbages, pipes)  # Checks if the bird is dead

        birdY += 3  # Increase the bird Y coordinate by 3

        try:  # Try to complete the actions
            birdY -= flap[0] * 2  # Change the bird y coordinate (flight)
            flap.pop(0)  # Remove the used one from the flight list
            rotation = 10  # Set rotation to 10
        except IndexError:  # List is empty
            rotation = -10  # Set rotation to -10

        if birdY <= 0:  # Bird y coordinate is less than 0
            birdY = 0  # Set the bird y coordinate to 0

        bird_rect, bird_frame, bird_image = draw_bird(
            screen, birds, birdX, birdY, bird_frame, rotation, bird_animate, bird_image
        )  # Draw the bird

        score = increase_score(
            score, pipes, birdX
        )  # Increase the score if the player passed a pipe
        draw_score(screen, score, start_time)  # Draw the score
        highscore = get_highscore(score)  # Get the highscore

        pygame.display.flip()  # Flips the display so the user can see
        Clock.tick(60)  # Sets the FPS to 60


if __name__ == "__main__":  # The file ran is this file
    draw_menu()  # Draw the main menu
