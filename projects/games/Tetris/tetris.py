import turtle
import time
import random

wn = turtle.Screen()
wn.title("Tetris by Daniel L.")
wn.bgcolor("NavajoWhite2")
wn.setup(width=800, height=800)  # Wider screen to accommodate instructions
wn.tracer(0)

delay = 0.1

class Shape():
    def __init__(self):
        self.x = 5
        self.y = 0
        self.color = random.randint(1, 7)
        
        # Block Shapes
        square = [[1,1],
                  [1,1]]

        horizontal_line = [[1,1,1,1]]

        vertical_line = [[1],
                         [1],
                         [1],
                         [1]]

        left_l = [[1,0,0,0],
                  [1,1,1,1]]
                   
        right_l = [[0,0,0,1],
                   [1,1,1,1]]
                   
        left_s = [[1,1,0],
                  [0,1,1]]
                  
        right_s = [[0,1,1],
                   [1,1,0]]
                  
        t = [[0,1,0],
             [1,1,1]]

        shapes = [square, horizontal_line, vertical_line, left_l, right_l, left_s, right_s, t]

        self.shape = random.choice(shapes)
        self.height = len(self.shape)
        self.width = len(self.shape[0])

    def move_left(self, grid):
        if self.x > 0:
            if grid[self.y][self.x - 1] == 0:
                self.erase_shape(grid)
                self.x -= 1
        
    def move_right(self, grid):
        if self.x < 12 - self.width:
            if grid[self.y][self.x + self.width] == 0:
                self.erase_shape(grid)
                self.x += 1
    
    def draw_shape(self, grid):
        for y in range(self.height):
            for x in range(self.width):
                if(self.shape[y][x]==1):
                    grid[self.y + y][self.x + x] = self.color
                
    def erase_shape(self, grid):
        for y in range(self.height):
            for x in range(self.width):
                if(self.shape[y][x]==1):
                    grid[self.y + y][self.x + x] = 0
                    
    def can_move(self, grid):
        result = True
        for x in range(self.width):
            if(self.shape[self.height-1][x] == 1):
                if(grid[self.y + self.height][self.x + x] != 0):
                    result = False
        return result
    
    def rotate(self, grid):
        self.erase_shape(grid)
        rotated_shape = []
        for x in range(len(self.shape[0])):
            new_row = []
            for y in range(len(self.shape)-1, -1, -1):
                new_row.append(self.shape[y][x])
            rotated_shape.append(new_row)
        
        right_side = self.x + len(rotated_shape[0])
        if right_side < len(grid[0]):     
            self.shape = rotated_shape
            self.height = len(self.shape)
            self.width = len(self.shape[0])

grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Create the drawing pen
pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.shape("square")
pen.setundobuffer(None)

# Create instruction pen
instruction_pen = turtle.Turtle()
instruction_pen.penup()
instruction_pen.speed(0)
instruction_pen.hideturtle()
instruction_pen.color("black")

def draw_instructions():
    instruction_pen.clear()
    instruction_pen.goto(-350, 300)
    instruction_pen.write("HOW TO PLAY", align="left", font=("Arial", 20, "bold"))
    
    instructions = [
        "Controls:",
        "A or Left Arrow: Move Left",
        "D or Right Arrow: Move Right",
        "Space or Up Arrow: Rotate",
        "",
        "Game Rules:",
        "- Complete rows to score points",
        "- Each row = 10 points",
        "- Game ends when blocks",
        "  reach the top",
        "",
        "Current Score:"
    ]
    
    y_pos = 250
    for line in instructions:
        instruction_pen.goto(-350, y_pos)
        instruction_pen.write(line, align="left", font=("Arial", 14, "normal"))
        y_pos -= 30
    
    # Draw arrow indicators
    instruction_pen.goto(-350, -200)
    instruction_pen.write("←   →   ↑", align="left", font=("Arial", 24, "bold"))
    instruction_pen.goto(-350, -230)
    instruction_pen.write("Move  Rotate", align="left", font=("Arial", 14, "normal"))

def draw_grid(pen, grid):
    pen.clear()
    top = 230
    left = -110
    
    colors = ["black", "lightblue", "blue", "orange", "yellow", "green", "purple", "red"]
    
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            screen_x = left + (x * 20)
            screen_y = top - (y * 20)
            color_number = grid[y][x]
            color = colors[color_number]
            pen.color(color)
            pen.goto(screen_x, screen_y)
            pen.stamp()

def check_grid(grid):
    y = 23
    while y > 0:
        is_full = True
        for x in range(0, 12):
            if grid[y][x] == 0:
                is_full = False
                y -= 1
                break
        if is_full:
            global score
            score += 10
            for copy_y in range(y, 0, -1):
                for copy_x in range(0, 12):
                    grid[copy_y][copy_x] = grid[copy_y-1][copy_x]

def draw_score(pen, score):
    pen.color("blue")
    pen.hideturtle()
    pen.goto(-350, -300)  # Moved to left side
    pen.write("Score: {}".format(score), move=False, align="left", font=("Arial", 24, "normal"))

# Create the initial shape
shape = Shape()
grid[shape.y][shape.x] = shape.color

# Set up key bindings
wn.listen()
wn.onkeypress(lambda: shape.move_left(grid), "a")
wn.onkeypress(lambda: shape.move_left(grid), "Left")
wn.onkeypress(lambda: shape.move_right(grid), "d")
wn.onkeypress(lambda: shape.move_right(grid), "Right")
wn.onkeypress(lambda: shape.rotate(grid), "space")
wn.onkeypress(lambda: shape.rotate(grid), "Up")

# Initialize score
score = 0

# Draw initial screen
draw_instructions()
draw_score(pen, score)

# Main game loop
while True:
    wn.update()

    # Move the shape
    if shape.y == 23 - shape.height + 1:
        shape = Shape()
        check_grid(grid)
    elif shape.can_move(grid):
        shape.erase_shape(grid)
        shape.y += 1
        shape.draw_shape(grid)
    else:
        shape = Shape()
        check_grid(grid)
        
    # Check if game over (block reached top)
    for x in range(12):
        if grid[0][x] != 0:
            pen.goto(-110, 230)
            pen.color("red")
            pen.write("GAME OVER", font=("Arial", 36, "bold"))
            time.sleep(3)
            # Reset game
            for y in range(len(grid)):
                for x in range(len(grid[0])):
                    grid[y][x] = 0
            score = 0
            shape = Shape()
            break
        
    # Draw the screen
    draw_grid(pen, grid)
    draw_score(pen, score)
    draw_instructions()
    
    time.sleep(delay)
    
wn.mainloop()