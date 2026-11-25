import numpy as np

class ChaoticEllipticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Dynamic parameters that scale with dimensionality
        self.elliptic_factors = np.logspace(0.5, 2.0, min(15, dim))
        self.saddle_strengths = np.linspace(0.8, 3.5, min(12, dim))
        self.chaotic_params = np.random.uniform(0.1, 0.9, min(10, dim))
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Elliptic valley components with dynamic scaling
        elliptic_term = 0.0
        for i in range(min(len(self.elliptic_factors), self.dim)):
            factor = self.elliptic_factors[i]
            # Asymmetric elliptic shape with varying eccentricity
            ellipse_val = factor * (x_norm[i] ** 2) + 0.3 * (x_norm[i] ** 4)
            elliptic_term += ellipse_val
            
        # Saddle-point corridors with dynamic strength
        saddle_term = 0.0
        for i in range(min(len(self.saddle_strengths), self.dim)):
            strength = self.saddle_strengths[i]
            # Asymmetric saddle with chaotic modulation
            saddle_val = strength * x_norm[i] * np.sin(5.0 * x_norm[i])
            saddle_term += saddle_val
            
        # Chaotic interaction terms between dimensions
        chaotic_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                # Dynamic coupling with chaotic modulation
                modulator = np.sin(self.chaotic_params[i % len(self.chaotic_params)] * 
                                 x_norm[j] * (i + 1))
                coupling = 0.25 * (x_norm[i] ** 2) * (x_norm[j] ** 2) * modulator
                chaotic_term += coupling
                
        # Multi-scale optima clustering with dynamic positioning
        cluster_term = 0.0
        for i in range(self.dim):
            # Create clustered minima with varying distances
            cluster_pos = 2.5 * np.sin(0.5 * (i + 1) * np.pi / self.dim)
            distance = x_norm[i] - cluster_pos
            cluster_val = 0.8 * (distance ** 4) + 0.3 * (distance ** 6)
            cluster_term += cluster_val
            
        # Combine all terms with adaptive weights
        result = 0.7 * elliptic_term + 0.5 * saddle_term + 0.4 * chaotic_term + 0.3 * cluster_term
        
        # Add dynamic noise with time-varying amplitude
        noise_amplitude = 0.02 * (1.0 + 0.05 * self.dim)
        noise = noise_amplitude * np.random.randn()
        
        return result + noise