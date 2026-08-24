import numpy as np

class ChaoticCrossDimensionalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.alpha = 2.0
        self.beta = 3.0
        self.gamma = 0.5
        self.delta = 1.5
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with exponential decay and polynomial terms
        r = np.sqrt(np.sum(x**2))
        radial_term = np.exp(-self.alpha * r) + self.beta * r**3 + self.gamma * r**4
        
        # Sinusoidal oscillations with varying frequencies and amplitudes
        sin_term = 0
        for i in range(self.dim):
            freq = (i + 1) * np.pi
            sin_term += np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7) * np.exp(-0.1 * x[i]**2)
        
        # Cross-dimensional chaotic interaction using a modified logistic map
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.sin(self.delta * x[i] * x[j]) * np.cos(self.delta * x[i] * x[j] * 0.3)
                cross_term += interaction * (1.0 + 0.2 * np.sin(x[i] + x[j]))
        
        # Polynomial radial interaction with chaotic modulation
        poly_radial = 0
        for i in range(self.dim):
            poly_radial += (x[i]**2 + x[i]**3) * np.sin(self.gamma * r)
        
        # Combined chaotic oscillation with exponential weighting
        chaotic_osc = 0
        for i in range(self.dim):
            chaotic_osc += np.exp(-self.beta * np.abs(x[i])) * np.sin(self.delta * x[i] * np.log(np.abs(x[i]) + 1e-8))
        
        # Final objective value with weighted components
        return (0.8 * radial_term + 
                1.5 * sin_term + 
                0.7 * cross_term + 
                0.6 * poly_radial + 
                0.9 * chaotic_osc)