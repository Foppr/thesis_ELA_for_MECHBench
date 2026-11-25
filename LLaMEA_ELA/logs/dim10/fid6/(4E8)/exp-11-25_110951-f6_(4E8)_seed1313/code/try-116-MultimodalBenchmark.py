import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced high-frequency trigonometric terms with chaotic modulation and cubic interactions
        trig_term = np.sum(np.sin(25 * np.pi * x_norm) * np.cos(20 * np.pi * x_norm) * 
                          (1 + 0.5 * np.sin(12 * np.pi * x_norm) + 0.2 * x_norm**3))
        
        # Modified radial basin with multiple exponential decay modes, chaotic peaks and cubic corrections
        r = np.sqrt(np.sum(x_norm**2))
        radial_basin = np.exp(-r**2) * (1 + 0.9 * np.sin(12 * r) * np.cos(6 * r) + 
                                       0.5 * np.sin(25 * r) + 0.3 * r**3)
        
        # Stronger cross-dimensional coupling with chaotic interaction patterns and cubic terms
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += (x_norm[i]**2 + x_norm[i+1]**2 + 0.3 * x_norm[i]**3 * x_norm[i+1]) * \
                       np.sin(9 * np.pi * (x_norm[i] - x_norm[i+1])) * \
                       (1 + 0.4 * np.cos(5 * np.pi * (x_norm[i] + x_norm[i+1])) + 
                        0.2 * x_norm[i]**2 * x_norm[i+1]**2)
        
        # Increased fractal complexity with non-uniform scaling, chaotic shifts and cubic components
        fractal = 0.0
        for i in range(self.dim):
            fractal += np.sin(2**(i*1.8) * np.pi * (x_norm[i] + 0.25)) * \
                      np.cos(2**(i//2 + 2) * np.pi * (x_norm[i] - 0.35)) * \
                      (1 + 0.4 * np.sin(2**i * np.pi * x_norm[i]) + 0.15 * x_norm[i]**3)
        
        # Enhanced conditioning with dimensionality-dependent scaling and cubic correction
        condition = 1.0 + 0.5 * (self.dim - 1) + 0.2 * np.sin(self.dim * np.pi / 4) + 0.1 * (self.dim - 1)**3
        
        # Combine all components with adaptive weights
        return condition * (trig_term + radial_basin + coupling + fractal)