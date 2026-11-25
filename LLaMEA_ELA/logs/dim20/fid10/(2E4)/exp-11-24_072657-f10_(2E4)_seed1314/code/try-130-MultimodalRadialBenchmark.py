import numpy as np

class MultimodalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial polynomial potential with varying exponents
        r_squared = np.sum(x_norm**2)
        radial_potential = np.sum((1.0 + 0.3 * r_squared) * (x_norm**4 + 0.5 * x_norm**6))
        
        # Sinusoidal oscillations with dimension-dependent frequencies
        freqs = 2.0 + 0.8 * np.arange(self.dim)
        sin_term = np.sum(np.sin(freqs * np.pi * x_norm) * np.cos(freqs * np.pi * x_norm**2))
        
        # Cross-dimensional coupling with interaction weights
        cross_coupling = 0.0
        for i in range(self.dim - 1):
            weight = 0.5 + 0.3 * np.sin(0.7 * i)
            cross_coupling += weight * (x_norm[i]**2 + x_norm[i+1]**2) * np.sin(x_norm[i] * x_norm[i+1])
        
        # Mixed polynomial and trigonometric terms with chaotic modulation
        mixed_term = np.sum((x_norm**3 + 0.7 * x_norm**5) * np.cos(3.0 * x_norm) * np.sin(2.5 * x_norm))
        
        # Additional chaotic multi-modal structure
        chaotic_structure = 0.0
        for i in range(self.dim):
            chaotic_structure += np.sin(4.0 * x_norm[i] + 0.5 * np.cos(3.0 * x_norm[i]))
        
        # Combine all terms with dimensionality scaling
        dim_scaling = 1.0 + 0.2 * np.log(self.dim + 1)
        
        result = (radial_potential + 0.8 * sin_term + 0.6 * cross_coupling + 
                 0.7 * mixed_term + 0.5 * chaotic_structure) * dim_scaling
        
        # Add small random noise for robustness
        noise = 0.001 * np.random.random()
        
        return result + noise