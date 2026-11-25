import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Global minimum at origin
        result = 0.0
        
        # Create a grid of 36 global minima in 2D space
        grid_centers = []
        for i in range(-3, 4):
            for j in range(-3, 4):
                grid_centers.append([i * 1.5, j * 1.5])
        
        # Add multiple wells with different scales and phases
        for i, center in enumerate(grid_centers):
            if self.dim >= 2:
                dist = np.sum((x[:2] - center)**2)
                # Vary the depth and width of wells based on position
                depth = 1.0 * (1.0 + 0.3 * np.sin(i * 0.7))
                width = 1.2 + 0.5 * np.cos(i * 0.5)
                result += depth * np.exp(-dist / width) * (1.0 + 0.15 * i)
        
        # Add asymmetric attractive forces in different directions
        if self.dim >= 2:
            result += 0.3 * np.sum((x[:2] - np.array([1.5, 1.5]))**4)
            result += 0.25 * np.sum((x[:2] - np.array([-1.5, -1.5]))**3)
        
        # Add chaotic sinusoidal modulations
        for i in range(min(self.dim, 12)):
            result += 0.25 * np.sin(6.0 * x[i] + i * 0.9) * np.cos(4.0 * x[i] + i * 0.5)
        
        # Add a complex higher-order polynomial term
        if self.dim >= 3:
            poly_term = 0.12 * (x[0]**6 + x[1]**5 + x[2]**4 + x[0]*x[1]*x[2]**3)
            result += poly_term
        
        # Add a non-uniform noise pattern based on input coordinates
        noise_pattern = 0.04 * np.sum(np.sin(x) * np.cos(x) * np.exp(-x**2 / 70))
        result += noise_pattern
        
        # Add a "banana" shaped valley that is difficult to navigate
        if self.dim >= 2:
            banana_term = 0.6 * (x[0]**2 - x[1])**2 + 0.25 * (x[0] - 2.5)**4
            result += banana_term
        
        # Add a new feature: a saddle point landscape with multiple local minima
        if self.dim >= 2:
            saddle_term = 0.5 * (x[0]**2 - x[1]**2) + 0.3 * (x[0] * x[1])**2
            result += saddle_term
            
        # Add a periodic component with varying frequency and amplitude
        if self.dim >= 1:
            periodic_term = 0.35 * np.sum(np.sin(8.0 * x) * np.cos(6.0 * x))
            result += periodic_term
        
        # Add a new twist: a fractal-like structure with self-similar patterns
        if self.dim >= 2:
            fractal_term = 0.2 * (np.sin(x[0] * 15) + np.cos(x[1] * 15))**2 + \
                          0.1 * (np.sin(x[0] * 7) * np.cos(x[1] * 7))**3
            result += fractal_term
            
        # Add a cross-shaped valley structure
        if self.dim >= 2:
            cross_term = 0.35 * (np.abs(x[0]) + np.abs(x[1]))**1.8
            result += cross_term
            
        # Add a new feature: a "canyon" shaped landscape with steep gradients
        if self.dim >= 2:
            canyon_term = 0.3 * np.exp(-0.5 * ((x[0] - 1.2)**2 + (x[1] - 1.2)**2)) * \
                         np.sin(4.0 * x[0]) * np.cos(4.0 * x[1])
            result += canyon_term
            
        # Add a multi-scale sinusoidal modulation
        if self.dim >= 1:
            multiscale_term = 0.2 * np.sum(np.sin(12.0 * x) + 0.6 * np.sin(24.0 * x))
            result += multiscale_term
            
        # Add a new feature: a "valley" landscape with multiple local minima
        if self.dim >= 2:
            valley_term = 0.2 * (x[0] - x[1])**4 + 0.15 * np.exp(-0.5 * ((x[0] + 1.0)**2 + (x[1] + 1.0)**2))
            result += valley_term
            
        # Add a new feature: a "peaks" landscape with multiple local maxima
        if self.dim >= 2:
            peaks_term = -0.18 * np.exp(-0.5 * ((x[0] - 2.0)**2 + (x[1] - 2.0)**2)) - \
                        0.12 * np.exp(-0.5 * ((x[0] + 2.0)**2 + (x[1] + 2.0)**2))
            result += peaks_term
            
        # Add a new feature: a "spiral" structure
        if self.dim >= 2:
            spiral_term = 0.1 * np.exp(-0.1 * (x[0]**2 + x[1]**2)) * np.sin(5.0 * np.arctan2(x[1], x[0]))
            result += spiral_term
            
        return result