import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Global minimum at origin
        result = 0.0
        
        # Create a grid of 9 global minima in 2D space
        grid_centers = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                grid_centers.append([i * 2.5, j * 2.5])
        
        # Add multiple wells with different scales and phases
        for i, center in enumerate(grid_centers):
            if self.dim >= 2:
                dist = np.sum((x[:2] - center)**2)
                # Vary the depth and width of wells based on position
                depth = 0.5 * (1.0 + 0.3 * np.sin(i))
                width = 1.0 + 0.2 * np.cos(i)
                result += depth * np.exp(-dist / width) * (1.0 + 0.1 * i)
        
        # Add asymmetric attractive forces in different directions
        if self.dim >= 2:
            result += 0.2 * np.sum((x[:2] - np.array([1.0, 1.0]))**4)
            result += 0.15 * np.sum((x[:2] - np.array([-1.0, -1.0]))**3)
        
        # Add chaotic sinusoidal modulations
        for i in range(min(self.dim, 6)):
            result += 0.1 * np.sin(3.0 * x[i] + i) * np.cos(2.0 * x[i] + i * 0.5)
        
        # Add a complex higher-order polynomial term
        if self.dim >= 3:
            poly_term = 0.05 * (x[0]**4 + x[1]**3 + x[2]**2)
            result += poly_term
        
        # Add a non-uniform noise pattern based on input coordinates
        noise_pattern = 0.01 * np.sum(np.sin(x) * np.cos(x))
        result += noise_pattern
        
        # Add a "banana" shaped valley that is difficult to navigate
        if self.dim >= 2:
            banana_term = 0.3 * (x[0]**2 - x[1])**2 + 0.1 * (x[0] - 2.0)**4
            result += banana_term
        
        # Add a new feature: a saddle point landscape with multiple local minima
        if self.dim >= 2:
            saddle_term = 0.25 * (x[0]**2 - x[1]**2) + 0.1 * (x[0] * x[1])**2
            result += saddle_term
            
        # Add a periodic component with varying frequency and amplitude
        if self.dim >= 1:
            periodic_term = 0.15 * np.sum(np.sin(5.0 * x) * np.cos(3.0 * x))
            result += periodic_term
        
        return result