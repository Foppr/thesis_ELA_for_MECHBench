import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Global minimum at origin
        result = 0.0
        
        # Create a grid of 16 global minima in 2D space
        grid_centers = []
        for i in range(-2, 3):
            for j in range(-2, 3):
                grid_centers.append([i * 1.5, j * 1.5])
        
        # Add multiple wells with different scales and phases
        for i, center in enumerate(grid_centers):
            if self.dim >= 2:
                dist = np.sum((x[:2] - center)**2)
                # Vary the depth and width of wells based on position
                depth = 0.7 * (1.0 + 0.4 * np.sin(i * 0.5))
                width = 1.2 + 0.3 * np.cos(i * 0.3)
                result += depth * np.exp(-dist / width) * (1.0 + 0.15 * i)
        
        # Add asymmetric attractive forces in different directions
        if self.dim >= 2:
            result += 0.3 * np.sum((x[:2] - np.array([1.5, 1.5]))**4)
            result += 0.2 * np.sum((x[:2] - np.array([-1.5, -1.5]))**3)
        
        # Add chaotic sinusoidal modulations
        for i in range(min(self.dim, 8)):
            result += 0.15 * np.sin(4.0 * x[i] + i * 0.7) * np.cos(3.0 * x[i] + i * 0.3)
        
        # Add a complex higher-order polynomial term
        if self.dim >= 3:
            poly_term = 0.08 * (x[0]**5 + x[1]**4 + x[2]**3)
            result += poly_term
        
        # Add a non-uniform noise pattern based on input coordinates
        noise_pattern = 0.02 * np.sum(np.sin(x) * np.cos(x * 1.5))
        result += noise_pattern
        
        # Add a "banana" shaped valley that is difficult to navigate
        if self.dim >= 2:
            banana_term = 0.4 * (x[0]**2 - x[1])**2 + 0.15 * (x[0] - 2.5)**4
            result += banana_term
        
        # Add a "valley" shaped landscape with varying steepness
        if self.dim >= 2:
            valley_term = 0.25 * np.sum((x[:2] - np.array([0.0, 0.0]))**6) + 0.1 * np.sum(np.abs(x[:2]))
            result += valley_term
        
        # Add a fractal-like pattern with recursive modulation
        if self.dim >= 4:
            fractal_term = 0.05 * np.sum(np.sin(2.0 * x[:4]) * np.cos(1.5 * x[:4]))
            result += fractal_term
        
        return result