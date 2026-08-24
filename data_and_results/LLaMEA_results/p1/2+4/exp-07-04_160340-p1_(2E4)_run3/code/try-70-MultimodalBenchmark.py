import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_global = np.zeros(dim)
    
    def f(self, x):
        x = np.array(x)
        
        # Normalize to [-5, 5] domain
        x_norm = x / 5.0
        
        # Create hexagonal lattice structure for global minima
        hex_positions = []
        for i in range(-2, 3):
            for j in range(-2, 3):
                if (i + j) % 2 == 0:
                    hex_positions.append([i * 1.5, j * 1.5])
        
        # Calculate distance to each hexagonal minimum
        penalty = 0.0
        for pos in hex_positions:
            dist = np.sum((x_norm - np.array(pos))**2)
            penalty += np.exp(-dist / 0.5)
        
        # Add periodic sinusoidal components
        periodic_term = 0.0
        for i in range(self.dim):
            periodic_term += np.sin(2 * np.pi * x[i]) + 0.5 * np.sin(4 * np.pi * x[i])
        
        # Add chaotic gradient field using a modified sine map
        chaotic_field = 0.0
        for i in range(self.dim):
            chaotic_field += np.sin(10 * x[i]) * np.cos(7 * x[i]) + 0.3 * np.sin(17 * x[i])
        
        # Add nested structure with varying scales
        nested_term = 0.0
        for i in range(self.dim):
            nested_term += 0.1 * np.sin(50 * x[i]) * np.cos(30 * x[i])
        
        # Combine all components
        result = penalty + 0.5 * np.sum(x**2) + periodic_term + chaotic_field + nested_term
        
        # Add small noise for robustness
        noise = 0.001 * np.sum(np.random.randn(self.dim) * x)
        result += noise
        
        return result