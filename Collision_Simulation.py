import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Collision Simulation')

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Circle properties
circle_radius = 20
num_circles = 5

# Create a list of circles
circles = []
for _ in range(num_circles):
    circle_pos = [random.randint(circle_radius, width - circle_radius), random.randint(circle_radius, height - circle_radius)]
    circle_speed = [random.choice([-2, 2]), random.choice([-2, 2])]
    circle_color = random.choice([RED, BLUE, GREEN, YELLOW])
    circles.append({'pos': circle_pos, 'speed': circle_speed, 'color': circle_color})

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move circles
    for circle in circles:
        circle['pos'][0] += circle['speed'][0]
        circle['pos'][1] += circle['speed'][1]

        # Bounce off walls
        if circle['pos'][0] <= circle_radius or circle['pos'][0] >= width - circle_radius:
            circle['speed'][0] = -circle['speed'][0]
        if circle['pos'][1] <= circle_radius or circle['pos'][1] >= height - circle_radius:
            circle['speed'][1] = -circle['speed'][1]

    # Collision detection
    for i in range(len(circles)):
        for j in range(i + 1, len(circles)):
            circle1 = circles[i]
            circle2 = circles[j]
            distance = ((circle1['pos'][0] - circle2['pos'][0]) ** 2 + (circle1['pos'][1] - circle2['pos'][1]) ** 2) ** 0.5
            if distance < 2 * circle_radius:
                circle1['speed'][0] = -circle1['speed'][0]
                circle1['speed'][1] = -circle1['speed'][1]
                circle2['speed'][0] = -circle2['speed'][0]
                circle2['speed'][1] = -circle2['speed'][1]

    # Clear screen
    screen.fill(WHITE)

    # Draw circles
    for circle in circles:
        pygame.draw.circle(screen, circle['color'], (int(circle['pos'][0]), int(circle['pos'][1])), circle_radius)

    # Update display
    pygame.display.flip()

    # Frame rate
    clock.tick(60)

pygame.quit()