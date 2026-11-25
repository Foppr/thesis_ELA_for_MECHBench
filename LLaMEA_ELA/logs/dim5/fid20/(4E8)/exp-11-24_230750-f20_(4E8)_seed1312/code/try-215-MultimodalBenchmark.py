import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial coupling with chaotic modulation
        poly_coupling = 0.0
        for i in range(self.dim):
            poly_coupling += (x[i]**4 - 2*x[i]**2 + 1) * np.sin(3 * x[i]) * np.cos(2 * x[i])
        
        # Dynamic sinusoidal modulation with fractal-like self-similarity
        sin_modulation = 0.0
        for scale in [0.5, 1.0, 2.0]:
            sin_modulation += np.sum(np.sin(scale * x) * np.cos(scale * x) * 
                                   np.exp(-0.1 * np.abs(x)) * np.sin(0.5 * np.pi * x))
        
        # Adaptive penalty corridors with exponential scaling
        penalty_corridors = 0.0
        for i in range(self.dim):
            dist_from_center = np.abs(x[i])
            penalty_corridors += (dist_from_center - 3.0)**2 * np.exp(-0.2 * dist_from_center)
        
        # Chaotic component using modified logistic map with time-varying parameter
        chaotic = 0.0
        r_values = [3.5 + 0.1 * np.sin(i) for i in range(self.dim)]
        for i in range(self.dim):
            if i == 0:
                chaotic += x[i] * (r_values[i] * (1 - x[i]))
            else:
                chaotic += x[i] * (r_values[i] * (1 - x[i-1]))
        
        # Radial basis function with adaptive widths and multi-scale interactions
        rbf = 0.0
        centers = np.linspace(-4, 4, 7)
        for center in centers:
            dist = np.sum((x - center) ** 2)
            width = 0.5 + 0.5 * np.sin(center)
            rbf += np.exp(-0.5 * dist / (width**2)) * np.cos(2 * np.pi * dist)
        
        # Improved fitness with adjusted weights and additional complexity
        return 0.4 * poly_coupling + 0.25 * sin_modulation + 0.2 * penalty_corridors + 0.1 * chaotic + 0.05 * rbf