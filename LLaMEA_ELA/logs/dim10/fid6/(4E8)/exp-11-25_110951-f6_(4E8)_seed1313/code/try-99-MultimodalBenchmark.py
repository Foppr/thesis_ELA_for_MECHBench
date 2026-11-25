import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced high-frequency trigonometric terms with chaotic modulation
        trig_term = np.sum(np.sin(15 * np.pi * x_norm) * np.cos(12 * np.pi * x_norm) * 
                          (1 + 0.3 * np.sin(7 * np.pi * x_norm)))
        
        # Modified radial basin with multiple exponential decay modes and chaotic peaks
        r = np.sqrt(np.sum(x_norm**2))
        radial_basin = np.exp(-r**2) * (1 + 0.7 * np.sin(8 * r) * np.cos(4 * r) + 
                                       0.3 * np.sin(15 * r))
        
        # Stronger cross-dimensional coupling with chaotic interaction patterns
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += (x_norm[i]**2 + x_norm[i+1]**2) * np.sin(5 * np.pi * (x_norm[i] - x_norm[i+1])) * \
                       (1 + 0.2 * np.cos(3 * np.pi * (x_norm[i] + x_norm[i+1])))
        
        # Increased fractal complexity with non-uniform scaling and chaotic shifts
        fractal = 0.0
        for i in range(self.dim):
            fractal += np.sin(2**(i*1.5) * np.pi * (x_norm[i] + 0.15)) * \
                      np.cos(2**(i//3 + 1) * np.pi * (x_norm[i] - 0.25)) * \
                      (1 + 0.25 * np.sin(2**i * np.pi * x_norm[i]))
        
        # Enhanced conditioning with dimensionality-dependent scaling
        condition = 1.0 + 0.3 * (self.dim - 1) + 0.1 * np.sin(self.dim * np.pi / 4)
        
        # Combine all components with adaptive weights
        return condition * (trig_term + radial_basin + coupling + fractal)