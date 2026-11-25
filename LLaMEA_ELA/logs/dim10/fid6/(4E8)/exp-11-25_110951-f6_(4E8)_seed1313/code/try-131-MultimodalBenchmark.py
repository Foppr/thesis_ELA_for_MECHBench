import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced high-frequency trigonometric terms with chaotic modulation and phase shifts
        trig_term = np.sum(np.sin(30 * np.pi * x_norm) * np.cos(25 * np.pi * x_norm) * 
                          (1 + 0.6 * np.sin(15 * np.pi * x_norm)) * 
                          np.exp(-0.5 * np.sum(x_norm**2)))
        
        # Modified radial basin with multiple exponential decay modes, chaotic peaks and multi-scale structure
        r = np.sqrt(np.sum(x_norm**2))
        radial_basin = np.exp(-r**2) * (1 + 0.8 * np.sin(15 * r) * np.cos(7 * r) + 
                                       0.4 * np.sin(30 * r) * np.cos(12 * r) + 
                                       0.3 * np.sin(50 * r))
        
        # Stronger cross-dimensional coupling with chaotic interaction patterns and variable coupling strength
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += (x_norm[i]**2 + x_norm[i+1]**2) * np.sin(10 * np.pi * (x_norm[i] - x_norm[i+1])) * \
                       (1 + 0.5 * np.cos(6 * np.pi * (x_norm[i] + x_norm[i+1])) + 
                        0.3 * np.sin(8 * np.pi * (x_norm[i] - x_norm[i+1])))
        
        # Increased fractal complexity with non-uniform scaling, chaotic shifts and multi-scale interactions
        fractal = 0.0
        for i in range(self.dim):
            fractal += np.sin(2**(i*2.0) * np.pi * (x_norm[i] + 0.3)) * \
                      np.cos(2**(i//2 + 3) * np.pi * (x_norm[i] - 0.4)) * \
                      (1 + 0.5 * np.sin(2**i * np.pi * x_norm[i]) * 
                       np.cos(2**(i+1) * np.pi * x_norm[i]))
        
        # Enhanced conditioning with dimensionality-dependent scaling and adaptive difficulty factors
        condition = 1.0 + 0.6 * (self.dim - 1) + 0.3 * np.sin(self.dim * np.pi / 3) + \
                   0.2 * np.cos(self.dim * np.pi / 5)
        
        # Add a global structure with multiple basins and enhanced landscape complexity
        global_structure = 0.0
        for i in range(0, self.dim, 2):
            if i+1 < self.dim:
                global_structure += np.sin(5 * np.pi * x_norm[i]) * np.cos(5 * np.pi * x_norm[i+1]) * \
                                  (1 + 0.4 * np.sin(3 * np.pi * (x_norm[i] + x_norm[i+1])))
        
        # Combine all components with adaptive weights and improved balance
        return condition * (trig_term + radial_basin + coupling + fractal + global_structure)