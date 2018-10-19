
# Author: Pierce Brooks

import gridster as g

width = 5
height = 5
grid = g.make_grid(width, height)
guy = g.make_guy(5)

print("   * Prepare to move up next!")
g.put_guy_on_grid_at(2, 2, guy, grid)
g.draw_grid(grid)

print("   * Prepare to move right next!")
g.move_guy_up(guy)
g.draw_grid(grid)

print("   * Prepare to move down next!")
g.move_guy_right(guy)
g.draw_grid(grid)

print("   * Prepare to move left next!")
g.move_guy_down(guy)
g.draw_grid(grid)

print("   * We're done!")
g.move_guy_left(guy)
g.draw_grid(grid)

print("   * Bye!")
