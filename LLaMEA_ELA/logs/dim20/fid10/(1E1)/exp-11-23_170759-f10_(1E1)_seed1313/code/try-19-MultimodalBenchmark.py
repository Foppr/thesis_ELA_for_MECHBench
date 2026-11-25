import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Global minimum at origin
        result = 0.0
        
        # Create a grid of 25 global minima in 2D space
        grid_centers = []
        for i in range(-2, 3):
            for j in range(-2, 3):
                grid_centers.append([i * 2.0, j * 2.0])
        
        # Add multiple wells with different scales and phases
        for i, center in enumerate(grid_centers):
            if self.dim >= 2:
                dist = np.sum((x[:2] - center)**2)
                # Vary the depth and width of wells based on position
                depth = 0.8 * (1.0 + 0.5 * np.sin(i * 0.6))
                width = 1.5 + 0.4 * np.cos(i * 0.4)
                result += depth * np.exp(-dist / width) * (1.0 + 0.2 * i)
        
        # Add asymmetric attractive forces in different directions
        if self.dim >= 2:
            result += 0.4 * np.sum((x[:2] - np.array([2.0, 2.0]))**4)
            result += 0.3 * np.sum((x[:2] - np.array([-2.0, -2.0]))**3)
        
        # Add chaotic sinusoidal modulations
        for i in range(min(self.dim, 10)):
            result += 0.2 * np.sin(5.0 * x[i] + i * 0.8) * np.cos(3.0 * x[i] + i * 0.4)
        
        # Add a complex higher-order polynomial term
        if self.dim >= 3:
            poly_term = 0.1 * (x[0]**5 + x[1]**4 + x[2]**3 + x[0]*x[1]*x[2]**2)
            result += poly_term
        
        # Add a non-uniform noise pattern based on input coordinates
        noise_pattern = 0.03 * np.sum(np.sin(x) * np.cos(x) * np.exp(-x**2 / 60))
        result += noise_pattern
        
        # Add a "banana" shaped valley that is difficult to navigate
        if self.dim >= 2:
            banana_term = 0.5 * (x[0]**2 - x[1])**2 + 0.2 * (x[0] - 3.0)**4
            result += banana_term
        
        # Add a new feature: a saddle point landscape with multiple local minima
        if self.dim >= 2:
            saddle_term = 0.4 * (x[0]**2 - x[1]**2) + 0.2 * (x[0] * x[1])**2
            result += saddle_term
            
        # Add a periodic component with varying frequency and amplitude
        if self.dim >= 1:
            periodic_term = 0.3 * np.sum(np.sin(7.0 * x) * np.cos(5.0 * x))
            result += periodic_term
        
        # Add a new twist: a fractal-like structure with self-similar patterns
        if self.dim >= 2:
            fractal_term = 0.15 * (np.sin(x[0] * 12) + np.cos(x[1] * 12))**2 + \
                          0.08 * (np.sin(x[0] * 6) * np.cos(x[1] * 6))**3
            result += fractal_term
            
        # Add a cross-shaped valley structure
        if self.dim >= 2:
            cross_term = 0.3 * (np.abs(x[0]) + np.abs(x[1]))**1.7
            result += cross_term
            
        # Add a new feature: a "canyon" shaped landscape with steep gradients
        if self.dim >= 2:
            canyon_term = 0.25 * np.exp(-0.5 * ((x[0] - 1.0)**2 + (x[1] - 1.0)**2)) * \
                         np.sin(3.0 * x[0]) * np.cos(3.0 * x[1])
            result += canyon_term
            
        # Add a multi-scale sinusoidal modulation
        if self.dim >= 1:
            multiscale_term = 0.18 * np.sum(np.sin(10.0 * x) + 0.5 * np.sin(20.0 * x))
            result += multiscale_term
            
        return result