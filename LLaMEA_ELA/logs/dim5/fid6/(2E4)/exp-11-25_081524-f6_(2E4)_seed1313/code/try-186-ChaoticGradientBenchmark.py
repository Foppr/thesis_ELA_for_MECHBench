import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic gradient components using logistic map modulation
        chaotic = 0.0
        for i in range(self.dim):
            # Logistic map with parameter that varies by dimension
            r = 3.8 + 0.1 * np.sin(0.3 * i)
            x_mod = (x[i] + 5.0) / 10.0  # Normalize to [0,1]
            chaotic += r * x_mod * (1 - x_mod) * np.sin(x[i] * 2.0)
        
        # Polynomial coupling with varying exponents
        poly_coupling = 0.0
        for i in range(self.dim):
            exp_factor = 2.0 + 0.5 * np.cos(0.4 * i)
            poly_coupling += (x[i]**exp_factor) * np.cos(x[i] * 0.5)
        
        # Saddle point structure with harmonic oscillations
        saddle = 0.0
        for i in range(self.dim):
            # Time-varying harmonic potential
            t = 1.0 + 0.2 * np.sin(0.1 * i + 1.0)
            saddle += x[i]**2 * np.cos(x[i] * t) * np.exp(-0.1 * x[i]**2)
        
        # Cross-dimensional interaction with dynamic coupling strength
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Dynamic coupling based on coordinate values
                coupling_strength = 0.5 + 0.3 * np.sin(x[i] + x[j])
                cross_interaction += coupling_strength * np.sin((x[i] - x[j]) * 1.2)
        
        # Combine all components with dynamic weights
        result = 0.3 * chaotic + 0.4 * poly_coupling + 0.2 * saddle + 0.1 * cross_interaction
        
        # Add dimension-dependent scaling factor
        scaling = 1.0 + 0.1 * np.sqrt(self.dim)
        
        return result * scaling