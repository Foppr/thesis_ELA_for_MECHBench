import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like recursive sine-wave component
        result = 0.0
        for i in range(self.dim):
            result += np.sin(2**i * x[i]) * np.cos(3**i * x[i])
            
        # Dynamic harmonic potential with adaptive frequency
        harmonic_pot = 0.0
        for i in range(self.dim):
            freq = 10 * (1 + 0.5 * np.sin(i))
            harmonic_pot += np.sin(freq * x[i]) * np.cos(freq * x[i])
        result += 0.3 * harmonic_pot
        
        # Multi-scale basin structure with recursive conditioning
        basin_structure = 0.0
        for scale in range(1, 5):
            for i in range(self.dim):
                basin_structure += np.sin(scale * x[i]) * np.cos(scale * x[i])
        result += 0.2 * basin_structure
        
        # Adaptive coupling with exponential decay
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                coupling += np.sin(15 * (x[i] + x[j])) * np.exp(-dist)
        result += 0.15 * coupling
        
        # Chaotic gradient modulation with non-linear scaling
        grad_mod = 0.0
        for i in range(self.dim):
            grad_mod += np.sin(20 * x[i])**3 + np.cos(15 * x[i])**3
        result += 0.1 * (grad_mod**2) * np.exp(-0.01 * np.sum(x**2))
        
        # Saddle-point landscape with multi-dimensional harmonic interactions
        saddle = 0.0
        for i in range(self.dim):
            saddle += np.sin(7 * x[i]) * np.cos(9 * x[i])
        result += 0.25 * saddle
        
        # High-order polynomial with cross-dimensional interactions
        poly_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_term += (x[i]**3 + x[j]**3) * np.sin(10 * (x[i] - x[j]))
        result += 0.08 * poly_term
        
        return result