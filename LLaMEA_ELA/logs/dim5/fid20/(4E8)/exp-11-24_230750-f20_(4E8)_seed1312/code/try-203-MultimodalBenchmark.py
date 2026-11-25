import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic sine-cosine interaction with altered polynomial exponents
        chaotic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                term = np.sin(x[i]) * np.cos(x[j]) * (x[i]**3 + x[j]**2)
                chaotic_interaction += term / (1.0 + np.abs(x[i] - x[j]))
        
        # Modified radial basis function with adjusted widths and polynomial exponents
        rbf = 0.0
        centers = np.random.uniform(-4, 4, (7, self.dim))
        for center in centers:
            dist = np.sum((x - center) ** 2)
            width = 0.5 + 0.5 * np.sin(dist)
            rbf += np.exp(-width * dist) * np.cos(2 * np.pi * dist ** 1.5)
        
        # Dynamic penalty landscape with varying severity and non-linear scaling
        penalty = 0.0
        for i in range(self.dim):
            penalty += (np.abs(x[i]) - 3.0) ** 4 * np.exp(-0.2 * x[i]**2) + \
                      0.1 * np.sin(5 * x[i]) * np.cos(3 * x[i])
        
        # Multi-scale sinusoidal modulation with adaptive amplitude and phase
        multiscale = 0.0
        scales = [0.2, 0.6, 1.2, 2.0]
        for scale in scales:
            phase_shift = np.sin(scale * np.sum(x))
            multiscale += np.sum(np.sin(scale * x + phase_shift) * 
                               np.cos(scale * x + phase_shift) * 
                               np.exp(-0.1 * np.abs(x)))
        
        # Polynomial coupling with chaotic modulation
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_coupling += (x[i] ** 2.5) * (x[j] ** 1.8) * np.sin(x[i] + x[j])
        
        # Combined fitness with weighted components
        return 0.3 * chaotic_interaction + 0.3 * rbf + 0.25 * penalty + 0.1 * multiscale + 0.05 * poly_coupling