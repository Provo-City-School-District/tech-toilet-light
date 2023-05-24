# tech-toilet-light



##optimizations made:

- The wheel function now uses modulo (%) to ensure pos is always within 0-255, avoiding repeated checks.
- The rainbow_cycle function's inner loop now uses the optimized wheel function directly to set the pixel colors, reducing function calls.
- The set_pixels function combines setting pixel colors, showing the pixels, and adding a delay into a single function call, avoiding repetitive code.
- The range in the rainbow_cycle function has been changed to 256 for smoother color transition.
- The conditions for checking the values of bathroom1 and bathroom2 have been simplified using not operator instead of comparing with 0.