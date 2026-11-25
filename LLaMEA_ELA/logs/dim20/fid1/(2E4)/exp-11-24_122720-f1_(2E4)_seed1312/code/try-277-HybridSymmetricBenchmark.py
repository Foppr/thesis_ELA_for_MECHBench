import numpy as np

class HybridSymmetricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Parameters for radial symmetry and oscillatory components
        self.oscillation_freq = [2.0 + 0.5 * np.sin(i * np.pi / (dim + 1)) for i in range(dim)]
        self.symmetry_order = [3 + int(np.floor((i + 1) / 2)) for i in range(dim)]
        self.penalty_strength = 1.0 + 0.3 * np.log(dim + 1)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with symmetric oscillations
        radial = np.sum(x**2)
        radial_term = 0.5 * radial + 0.1 * np.sin(np.sqrt(radial) * np.pi)
        
        # Sinusoidal oscillations in each dimension
        oscillation = 0
        for i in range(self.dim):
            freq = self.oscillation_freq[i]
            osc = np.sin(freq * x[i]) * np.cos(freq * x[i])
            oscillation += osc
            
        # Radial symmetry with varying orders
        symmetry = 0
        for i in range(self.dim):
            order = self.symmetry_order[i]
            sym = np.cos(order * np.arctan2(x[i], x[(i + 1) % self.dim]))
            symmetry += sym
            
        # Conditional quadratic penalty based on distance from origin
        penalty = 0
        dist_from_origin = np.sqrt(radial)
        for i in range(self.dim):
            if abs(x[i]) > 3.0:
                penalty += self.penalty_strength * (x[i] - 3.0)**2
                
        # Combine all components with dimensionally adaptive weights
        result = 1.5 * radial_term + 1.0 * oscillation + 0.8 * symmetry + penalty
        
        # Add a global scaling factor based on problem dimensionality
        scale_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        result *= scale_factor
        
        return result