import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic component using sine waves with exponentially decaying amplitudes
        chaotic_term = 0.0
        for i in range(self.dim):
            amplitude = 1.0
            frequency = 2.0
            term = 0.0
            for depth in range(5):  # 5 levels of chaos
                term += amplitude * np.sin(frequency * x_norm[i])
                amplitude *= 0.6  # Exponentially decaying amplitude
                frequency *= 1.8  # Increasing frequency
            chaotic_term += term
        
        # Dynamic conditioning based on dimensionality
        dynamic_cond = 1.0 + 0.5 * np.log(1.0 + self.dim)
        
        # Ruggedness component with multiple sinusoidal interference patterns
        rugged_term = 0.0
        for i in range(self.dim):
            # Multiple overlapping sine waves with different frequencies and phases
            freqs = [1.0, 3.0, 7.0, 11.0]
            phases = [0.0, np.pi/4, np.pi/2, 3*np.pi/4]
            for freq, phase in zip(freqs, phases):
                rugged_term += np.sin(freq * x_norm[i] + phase) * np.exp(-0.1 * (x_norm[i] - 0.5)**2)
        
        # Basin depth variation using polynomial terms
        basin_term = 0.0
        for i in range(self.dim):
            # Varying curvature based on dimension index
            curvature = 1.0 + 0.3 * np.sin(i * np.pi / self.dim)
            basin_term += curvature * (x_norm[i]**2 + 0.1 * x_norm[i]**6)
        
        # Cross-dimensional coupling with rotation-invariance
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Distance-based coupling with chaotic modulation
                dist = np.abs(x_norm[i] - x_norm[j])
                coupling = np.sin(3 * np.pi * dist) * np.exp(-dist**2)
                cross_term += coupling
        
        # Add noise for increased complexity
        noise = 0.05 * np.random.rand()
        
        # Combine all terms with appropriate weights
        result = dynamic_cond * (0.3 * chaotic_term + 0.4 * rugged_term + 
                                0.2 * basin_term + 0.1 * cross_term) + noise
        
        return result