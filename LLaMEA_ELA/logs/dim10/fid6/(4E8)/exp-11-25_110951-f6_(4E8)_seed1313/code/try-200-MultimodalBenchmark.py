import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic gradient components with modified fractal basins
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.tanh(4 * x_norm[i]) * np.sin(9 * x_norm[i]) + \
                           0.6 * np.tanh(7 * x_norm[i]) * np.cos(11 * x_norm[i]) + \
                           0.3 * np.sinh(2 * x_norm[i]) * np.cos(5 * x_norm[i])
        
        # Multi-scale periodic structures with increased spectral complexity
        periodic_term = 0.0
        for i in range(self.dim):
            periodic_term += np.sin(2 * np.pi * x_norm[i]) + \
                            0.7 * np.sin(4 * np.pi * x_norm[i]) + \
                            0.3 * np.sin(8 * np.pi * x_norm[i]) + \
                            0.1 * np.sin(16 * np.pi * x_norm[i])
        
        # Asymmetric ridge interactions with exponential decay and dynamic coupling
        ridge_term = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 2) % self.dim
            ridge_term += np.exp(-0.3 * (x_norm[i] - x_norm[j])**2) * \
                         np.sin(4 * x_norm[i]) * np.cos(3 * x_norm[j]) + \
                         0.5 * np.exp(-0.7 * (x_norm[i] - x_norm[k])**2) * \
                         np.cos(2 * x_norm[i]) * np.sin(5 * x_norm[k])
        
        # Logarithmic barrier functions near boundaries with multi-dimensional coupling
        barrier_term = 0.0
        for i in range(self.dim):
            barrier_term += -np.log(1.0 + np.exp(-x_norm[i])) + \
                           0.5 * np.log(1.0 + x_norm[i]**2) + \
                           0.2 * np.log(1.0 + np.abs(x_norm[i])**3)
        
        # Non-linear cross-dimensional interactions with fractal-like behavior and enhanced complexity
        fractal_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                fractal_term += np.sin(7 * (x_norm[i] + x_norm[j])) * \
                               np.cos(4 * (x_norm[i] - x_norm[j])) + \
                               0.5 * np.cos(3 * (x_norm[i] + x_norm[j])) * \
                               np.sin(6 * (x_norm[i] - x_norm[j]))
        
        # Dynamic phase interference with time-varying components and additional harmonics
        phase_term = 0.0
        for i in range(self.dim):
            phase_term += np.sin(x_norm[i] + np.pi/4) * np.cos(x_norm[i] + np.pi/3) + \
                         0.8 * np.sin(2 * x_norm[i] + np.pi/6) * np.cos(2 * x_norm[i] + np.pi/5) + \
                         0.3 * np.sin(3 * x_norm[i] + np.pi/8) * np.cos(4 * x_norm[i] + np.pi/7)
        
        # Additional cross-dimensional coupling terms with mutated frequency parameters
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited range for complexity
                coupling_term += np.sin(2 * np.pi * (x_norm[i] + x_norm[j])) * \
                               np.cos(3 * np.pi * (x_norm[i] - x_norm[j])) * \
                               np.exp(-0.5 * (x_norm[i] - x_norm[j])**2)
        
        # Final combined function with weighted contributions
        return 0.2 * chaotic_term + 0.18 * periodic_term + 0.18 * ridge_term + \
               0.12 * barrier_term + 0.15 * fractal_term + 0.1 * phase_term + \
               0.07 * coupling_term