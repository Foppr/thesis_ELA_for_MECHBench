import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.poly_degree = 4
        self.radial_decay = 0.3
        self.coupling_strength = 1.5
        self.chaos_factor = 0.8
        self.dimensionality_modifier = 2.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial potential component
        poly_sum = 0
        for i in range(self.dim):
            poly_sum += (x[i] ** self.poly_degree) * np.cos(0.5 * x[i])
            
        # Radial symmetry component with exponential decay
        radial_sum = 0
        center = np.zeros(self.dim)
        for i in range(self.dim):
            radial_sum += np.exp(-self.radial_decay * (x[i] - center[i]) ** 2)
            
        # Chaotic coupling terms using logistic map-like behavior
        chaos_sum = 0
        for i in range(self.dim):
            chaotic_val = np.sin(self.chaos_factor * x[i])
            for j in range(i+1, self.dim):
                coupling = np.sin(self.coupling_strength * (x[i] + x[j]))
                chaos_sum += chaotic_val * coupling
                
        # Dimensionality-dependent scaling and modulation
        dim_factor = self.dimensionality_modifier * np.log(self.dim + 1)
        
        # Add noise with chaotic pattern
        noise = 0
        for i in range(self.dim):
            noise += np.random.normal(0, 0.1) * np.sin(i * np.pi / (self.dim + 1))
            
        # Cross-term interactions with sinusoidal modulation
        cross_sum = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
                cross_sum += interaction
                
        # Combine all components
        result = dim_factor * (poly_sum + radial_sum + cross_sum) + chaos_sum + noise
        
        return result + 0.01 * self.dim