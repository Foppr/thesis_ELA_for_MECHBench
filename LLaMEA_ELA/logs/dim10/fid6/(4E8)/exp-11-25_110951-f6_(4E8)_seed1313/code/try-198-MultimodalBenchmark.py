import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic gradient components with enhanced hyperbolic tangent modulations
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += 1.2 * np.tanh(4 * x_norm[i]) * np.sin(8 * x_norm[i]) + \
                           0.7 * np.tanh(6 * x_norm[i]) * np.cos(10 * x_norm[i])
        
        # Multi-scale periodic structures with altered amplitudes and frequencies
        periodic_term = 0.0
        for i in range(self.dim):
            periodic_term += 1.2 * np.sin(3 * np.pi * x_norm[i]) + \
                            0.9 * np.sin(6 * np.pi * x_norm[i]) + \
                            0.4 * np.sin(12 * np.pi * x_norm[i])
        
        # Asymmetric ridge interactions with modified exponential decay
        ridge_term = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            ridge_term += np.exp(-0.3 * (x_norm[i] - x_norm[j])**2) * \
                         np.sin(4 * x_norm[i]) * np.cos(3 * x_norm[j])
        
        # Logarithmic barrier functions near boundaries with multi-dimensional coupling
        barrier_term = 0.0
        for i in range(self.dim):
            barrier_term += -np.log(1.0 + np.exp(-x_norm[i])) + \
                           0.6 * np.log(1.0 + x_norm[i]**2)
        
        # Non-linear cross-dimensional interactions with enhanced fractal-like behavior
        fractal_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                fractal_term += 1.5 * np.sin(6 * (x_norm[i] + x_norm[j])) * \
                               np.cos(4 * (x_norm[i] - x_norm[j]))
        
        # Dynamic phase interference with increased complexity
        phase_term = 0.0
        for i in range(self.dim):
            phase_term += 1.3 * np.sin(x_norm[i] + np.pi/5) * np.cos(x_norm[i] + np.pi/4) + \
                         1.1 * np.sin(2.5 * x_norm[i] + np.pi/7) * np.cos(2.5 * x_norm[i] + np.pi/6)
        
        # Final combined function with adjusted weighted contributions
        return 0.3 * chaotic_term + 0.25 * periodic_term + 0.18 * ridge_term + \
               0.12 * barrier_term + 0.15 * fractal_term + 0.05 * phase_term