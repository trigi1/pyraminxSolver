# pyraminxSolver
Solves a pyraminx puzzle in the fewest moves possible

How to input the scramble:
- The input should be a 36-character long string (each character representing a sticker on the pyraminx)
- You can use any 4 lowercase letters to represent the 4 colors on the puzzle (such as r, g, b, y for red, green, blue, yellow)
- The first 9 characters should be the 9 stickers on the front face from left to right, top to bottom
- The next 9 characters should be the 9 stickers on the left face from left to right, top to bottom with the same bottom face as before
- The next 9 characters should be the 9 stickers on the right face from left to right, top to bottom with the same bottom face as before
- The final 9 characters should be the 9 stickers on the bottom face from left to right, top to bottom with the new bottom face being the front face

Examples (with starting green front, yellow bottom, red left, blue right):
- "gggggggggrrrrrrrrrbbbbbbbbbyyyyyyyyy" is solved
- "bbbbgggggggggrrrrrrrrrbbbbbyyyyyyyyy" is the pyraminx after a U move
- "gggyggrggrrrbrrrrrbgbbbbbbbyyyyyygyy" is the pyraminx after the moves L R' L' R
