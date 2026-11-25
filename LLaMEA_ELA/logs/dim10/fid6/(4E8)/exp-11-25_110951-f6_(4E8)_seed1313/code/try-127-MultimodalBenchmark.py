import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced high-frequency trigonometric terms with chaotic modulation
        trig_term = np.sum(np.sin(25 * np.pi * x_norm) * np.cos(20 * np.pi * x_norm) * 
                          (1 + 0.5 * np.sin(10 * np.pi * x_norm)))
        
        # Modified radial basin with multiple exponential decay modes and chaotic peaks
        r = np.sqrt(np.sum(x_norm**2))
        radial_basin = np.exp(-r**2) * (1 + 0.9 * np.sin(12 * r) * np.cos(6 * r) + 
                                       0.5 * np.sin(25 * r))
        
        # Stronger cross-dimensional coupling with chaotic interaction patterns
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += (x_norm[i]**2 + x_norm[i+1]**2) * np.sin(8 * np.pi * (x_norm[i] - x_norm[i+1])) * \
                       (1 + 0.4 * np.cos(5 * np.pi * (x_norm[i] + x_norm[i+1])))
        
        # Increased fractal complexity with non-uniform scaling and chaotic shifts
        fractal = 0.0
        for i in range(self.dim):
            fractal += np.sin(2**(i*1.8) * np.pi * (x_norm[i] + 0.25)) * \
                      np.cos(2**(i//2 + 2) * np.pi * (x_norm[i] - 0.35)) * \
                      (1 + 0.4 * np.sin(2**i * np.pi * x_norm[i]))
        
        # Enhanced conditioning with dimensionality-dependent scaling
        condition = 1.0 + 0.5 * (self.dim - 1) + 0.2 * np.sin(self.dim * np.pi / 4)
        
        # Combine all components with adaptive weights
        return condition * (trig_term + radial_basin + coupling + fractal)