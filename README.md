# Bouncing Balls Physics Simulation

A small 2D physics sandbox built with Python and pygame. Click anywhere in the window to spawn a ball and watch it fall, bounce off the floor and walls, and collide with other balls.

This project was created as a hands-on way to learn object-oriented programming and basic game physics.

Features
Spawn balls with a mouse click, each with a random color
Gravity-driven motion using delta-time (frame-rate independent)
Energy loss on bounce (floor restitution of 0.8) and floor friction
Collisions with the floor and with the left and right walls
Ball-to-ball collisions with:
positional correction (overlapping balls are pushed apart)
impulse-based velocity resolution with adjustable elasticity
multiple solver iterations per frame (10) for more stable stacking
Object-oriented design: all ball behavior lives in a Ball class
Requirements
Python 3.9+
pygame-ce 2.5.2 or newer

The code uses pygame.mouse.get_just_pressed(), which is available in pygame-ce (the community edition) but not in the original pygame package.

Installation
bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

pip install pygame-ce
Usage
bash
python main.py
Action	Result
Left mouse click	Spawn a ball at the cursor position
Close window	Quit the simulation
How It Works
The Ball class

Each ball stores its position, velocity, acceleration, radius and color. On every frame, gravity(dt) performs a simple Euler integration:

v += a * dt
pos += v * dt

Then it resolves collisions with the boundaries: the floor reflects the vertical velocity and reduces it by 20%, while the walls clamp the ball's position inside the play area.

Ball-to-ball collisions

For every pair of balls, the simulation:

Computes the distance between centers and checks for overlap.
Separates the balls along the collision normal so they no longer overlap.
Resolves velocities along the normal using an impulse, assuming equal masses. The e parameter controls elasticity (0 = balls stick together, 1 = perfectly elastic bounce).

This is repeated 10 times per frame to improve stability when many balls are piled up.

Configuration

Tweak these values at the top of main.py or in the code to change the behavior:

Parameter	Location	Default	Description
g	top of file	900	Gravity acceleration (pixels/s²)
floor_y	top of file	600	Y-coordinate of the floor
wall_x	top of file	1200	X-coordinate of the right wall
radius	Ball.__init__	36	Ball radius in pixels
e	collision loop	0.3	Ball-to-ball elasticity
FPS cap	clock.tick(...)	120	Maximum frames per second
Project Structure
.
├── main.py       # Simulation: Ball class, game loop, collision handling
└── README.md
Ideas for Future Improvements
Different masses and radii for balls
Mouse interaction (drag and throw balls)
Rolling friction and air resistance
Spatial partitioning (grid) for better performance with many balls
Keyboard controls to reset the scene or change gravity
