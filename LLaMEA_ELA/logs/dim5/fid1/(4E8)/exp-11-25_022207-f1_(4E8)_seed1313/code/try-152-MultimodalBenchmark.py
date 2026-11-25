import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basis function component with varying widths
        rbf_sum = 0.0
        for i in range(1, min(6, self.dim + 1)):
            center = np.sin(i * np.pi / 6) * np.ones(self.dim)
            width = 0.5 + 0.3 * np.sin(i * np.pi / 4)
            rbf_sum += np.exp(-np.sum(((x_norm - center) / width)**2))
        
        # Sinusoidal modulation with frequency scaling
        sin_mod = np.sum(np.sin(2 * np.pi * x_norm) * 
                        np.cos(3 * np.pi * x_norm) * 
                        (1 + 0.3 * np.sin(5 * np.pi * x_norm)))
        
        # Asymmetric polynomial interactions with cross-terms
        poly_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_interaction += (x_norm[i]**3 + 0.5 * x_norm[i]**2) * \
                                  (x_norm[j]**4 + 0.3 * x_norm[j]**3) * \
                                  np.exp(-0.2 * (x_norm[i] - x_norm[j])**2)
        
        # Cross-dimensional coupling with exponential decay
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += np.exp(-0.5 * (x_norm[i]**2 + x_norm[j]**2)) * \
                           np.sin(4 * (x_norm[i] - x_norm[j]))
        
        # Saddle-point enhancing component
        saddle = 0.0
        for i in range(self.dim):
            saddle += (x_norm[i]**2 - 1)**2 * (1 + 0.4 * np.cos(6 * x_norm[i]))
        
        # Asymmetric quartic with harmonic perturbation
        quartic = np.sum((x_norm**4 + 0.3 * x_norm**3) * 
                        (1 + 0.2 * np.sin(7 * x_norm)) * 
                        np.exp(-0.15 * np.abs(x_norm)))
        
        # Global scaling and combination
        return 1.2 * (rbf_sum + sin_mod + poly_interaction + coupling + saddle + quartic)