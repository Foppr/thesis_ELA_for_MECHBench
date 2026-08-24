import numpy as np

class LabyrinthineEnergyWellBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Base quadratic term with conditioning
        f = 0.5 * np.sum(x**2)
        
        # Add labyrinthine valley structure with exponential energy wells
        valley_term = 0
        for i in range(self.dim):
            # Create asymmetric valleys with exponential depth
            valley_term += np.exp(-0.5 * (x[i] - 2.0)**2) * np.sin(3 * x[i]) + \
                          np.exp(-0.3 * (x[i] + 2.0)**2) * np.cos(2 * x[i])
        f += 2.0 * valley_term
        
        # Add interconnected multi-scale basins
        basin_term = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                # Create basin interactions with varying scales
                basin_term += 0.5 * np.exp(-0.1 * ((x[i] - 1.0)**2 + (x[j] + 1.0)**2)) * \
                             np.sin(2 * x[i] + x[j]) * np.cos(x[i] - 2 * x[j])
        f += basin_term
        
        # Add asymmetric energy wells with exponential scaling
        well_term = 0
        for i in range(self.dim):
            # Create wells with different depths and positions
            well_term += 1.5 * np.exp(-0.2 * (x[i] - 3.0)**2) * \
                        np.sin(4 * x[i]) * np.cos(0.5 * x[i]) + \
                        1.0 * np.exp(-0.3 * (x[i] + 3.0)**2) * \
                        np.cos(3 * x[i]) * np.sin(0.7 * x[i])
        f += well_term
        
        # Add fractal-like self-similar basin structures
        fractal_term = 0
        for i in range(self.dim):
            # Nested basin structures with recursive patterns
            fractal_term += 0.3 * np.exp(-0.1 * (x[i] - 1.5)**2) * \
                           np.sin(6 * x[i]) * np.cos(3 * x[i]) + \
                           0.2 * np.exp(-0.15 * (x[i] + 1.5)**2) * \
                           np.cos(5 * x[i]) * np.sin(2 * x[i])
        f += fractal_term
        
        # Add chaotic basin interactions with non-linear coupling
        chaos_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Create chaotic interactions between dimensions
                chaos_term += 0.4 * np.sin(3 * x[i]) * np.cos(2 * x[j]) * \
                             np.exp(-0.1 * (x[i] - x[j])**2) + \
                             0.3 * np.cos(4 * x[i]) * np.sin(x[j]) * \
                             np.exp(-0.05 * (x[i] + x[j])**2)
        f += chaos_term
        
        # Add asymmetric hill structures to create complex terrain
        hill_term = 0
        for i in range(self.dim):
            # Asymmetric hills with varying heights
            hill_term += 0.8 * np.exp(-0.2 * (x[i] - 2.5)**2) * \
                        np.sin(5 * x[i]) + \
                        0.6 * np.exp(-0.15 * (x[i] + 2.5)**2) * \
                        np.cos(4 * x[i])
        f += hill_term
        
        # Add multi-scale terrain with varying frequencies
        terrain_term = 0
        for i in range(self.dim):
            terrain_term += 0.2 * np.sin(10 * x[i]) * np.cos(8 * x[i]) * \
                           np.exp(-0.05 * x[i]**2) + \
                           0.15 * np.cos(12 * x[i]) * np.sin(6 * x[i]) * \
                           np.exp(-0.03 * x[i]**2)
        f += terrain_term
        
        # Add noise component with non-uniform distribution
        noise_term = 0
        for i in range(self.dim):
            noise_term += 0.05 * np.sin(15 * x[i])**2 + 0.03 * np.cos(10 * x[i])**2
        f += noise_term
        
        # Add dimensional coupling with exponential terms
        coupling_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_term += 0.1 * np.exp(-0.1 * (x[i] - x[j])**2) * \
                                np.sin(3 * x[i] + 2 * x[j]) * \
                                np.cos(2 * x[i] - x[j])
        f += coupling_term
        
        return f