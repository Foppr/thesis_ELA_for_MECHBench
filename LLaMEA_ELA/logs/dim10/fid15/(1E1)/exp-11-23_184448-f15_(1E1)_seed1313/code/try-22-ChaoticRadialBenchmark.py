import numpy as np

class ChaoticRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term for conditioning
        base_term = np.sum(x**2) / (2.0 * self.dim)
        
        # Radial basis function component with chaotic centers
        rbf_term = 0.0
        for i in range(self.dim):
            # Chaotic center positions
            center = 3.0 * np.sin(i * np.pi / (self.dim + 1))
            # Radial distance from center
            r = np.abs(x[i] - center)
            # RBF with chaotic width
            width = 0.5 + 0.3 * np.cos(i * np.pi / (self.dim + 2))
            rbf_term += np.exp(-r**2 / (2.0 * width**2))
        
        # Sinusoidal oscillation component with cross-dimensional coupling
        sin_term = 0.0
        for i in range(self.dim):
            # Chaotic frequency modulation
            freq = 1.0 + 2.0 * np.sin(i * np.pi / (self.dim + 3))
            sin_term += np.sin(freq * x[i])
            
        # Cross-dimensional coupling with chaotic interaction weights
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic coupling weight
                weight = 0.4 + 0.3 * np.sin(i * j * np.pi / (self.dim + 1))
                coupling_term += weight * x[i] * x[j]
        
        # Chaotic perturbation term with multiple frequencies
        perturbation_term = 0.0
        for i in range(self.dim):
            # Multiple chaotic frequencies
            freqs = [1.0, 2.0, 3.0, 4.0]
            for f in freqs:
                perturbation_term += np.sin(f * x[i] + f * np.cos(x[i]))
        
        # Adaptive basin structure with chaotic depth
        basin_term = 0.0
        for i in range(self.dim):
            # Chaotic basin depth
            depth = 0.3 + 0.4 * np.sin(i * np.pi / (self.dim + 4))
            # Basin with exponential penalty
            distance = np.abs(x[i])
            basin_term += depth * distance * np.exp(-distance)
        
        # Dimensionality scaling factor
        dim_scale = 1.0 + 0.2 * np.log(self.dim + 1)
        
        return dim_scale * (base_term + 0.3 * rbf_term + 0.2 * sin_term + 
                           0.25 * coupling_term + 0.15 * perturbation_term + 
                           0.1 * basin_term)