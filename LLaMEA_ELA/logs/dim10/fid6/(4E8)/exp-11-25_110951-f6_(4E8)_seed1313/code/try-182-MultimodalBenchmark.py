import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic gradient components with hyperbolic tangent modulations
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.tanh(3 * x_norm[i]) * np.sin(7 * x_norm[i]) + \
                           0.5 * np.tanh(5 * x_norm[i]) * np.cos(9 * x_norm[i])
        
        # Multi-scale periodic structures with varying amplitudes
        periodic_term = 0.0
        for i in range(self.dim):
            periodic_term += np.sin(2 * np.pi * x_norm[i]) + \
                            0.7 * np.sin(4 * np.pi * x_norm[i]) + \
                            0.3 * np.sin(8 * np.pi * x_norm[i])
        
        # Asymmetric ridge interactions with exponential decay
        ridge_term = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            ridge_term += np.exp(-0.5 * (x_norm[i] - x_norm[j])**2) * \
                         np.sin(3 * x_norm[i]) * np.cos(2 * x_norm[j])
        
        # Logarithmic barrier functions near boundaries with multi-dimensional coupling
        barrier_term = 0.0
        for i in range(self.dim):
            barrier_term += -np.log(1.0 + np.exp(-x_norm[i])) + \
                           0.5 * np.log(1.0 + x_norm[i]**2)
        
        # Non-linear cross-dimensional interactions with fractal-like behavior
        fractal_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                fractal_term += np.sin(5 * (x_norm[i] + x_norm[j])) * \
                               np.cos(3 * (x_norm[i] - x_norm[j]))
        
        # Dynamic phase interference with time-varying components
        phase_term = 0.0
        for i in range(self.dim):
            phase_term += np.sin(x_norm[i] + np.pi/4) * np.cos(x_norm[i] + np.pi/3) + \
                         0.8 * np.sin(2 * x_norm[i] + np.pi/6) * np.cos(2 * x_norm[i] + np.pi/5)
        
        # Final combined function with weighted contributions
        return 0.25 * chaotic_term + 0.2 * periodic_term + 0.15 * ridge_term + \
               0.15 * barrier_term + 0.15 * fractal_term + 0.1 * phase_term