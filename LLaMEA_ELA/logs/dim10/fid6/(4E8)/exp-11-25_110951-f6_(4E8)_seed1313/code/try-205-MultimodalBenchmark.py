import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic gradient components with modified coupling
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.tanh(3 * x_norm[i]) * np.sin(7 * x_norm[i]) + \
                           0.6 * np.tanh(5 * x_norm[i]) * np.cos(10 * x_norm[i]) + \
                           0.4 * np.tanh(x_norm[i]) * np.sin(12 * x_norm[i])
        
        # Multi-scale periodic structures with fractal-like scaling
        periodic_term = 0.0
        for i in range(self.dim):
            periodic_term += np.sin(2 * np.pi * x_norm[i]) + \
                            0.7 * np.sin(3 * np.pi * x_norm[i]) + \
                            0.3 * np.sin(6 * np.pi * x_norm[i]) + \
                            0.1 * np.sin(12 * np.pi * x_norm[i])
        
        # Asymmetric ridge interactions with exponential decay and coupling
        ridge_term = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            k = (i + 2) % self.dim
            ridge_term += np.exp(-0.4 * (x_norm[i] - x_norm[j])**2) * \
                         np.sin(3 * x_norm[i]) * np.cos(4 * x_norm[j]) + \
                         0.4 * np.exp(-0.6 * (x_norm[i] - x_norm[k])**2) * \
                         np.cos(6 * x_norm[i]) * np.sin(3 * x_norm[k])
        
        # Logarithmic barrier functions near boundaries with multi-dimensional coupling
        barrier_term = 0.0
        for i in range(self.dim):
            barrier_term += -np.log(1.0 + np.exp(-x_norm[i])) + \
                           0.5 * np.log(1.0 + x_norm[i]**2) + \
                           0.2 * np.log(1.0 + np.abs(x_norm[i]))
        
        # Non-linear cross-dimensional interactions with fractal-like behavior and coupling
        fractal_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                fractal_term += np.sin(5 * (x_norm[i] + x_norm[j])) * \
                               np.cos(3 * (x_norm[i] - x_norm[j])) + \
                               0.4 * np.sin(2 * (x_norm[i] - x_norm[j])) * \
                               np.cos(6 * (x_norm[i] + x_norm[j]))
        
        # Dynamic phase interference with time-varying components and coupling
        phase_term = 0.0
        for i in range(self.dim):
            phase_term += np.sin(x_norm[i] + np.pi/5) * np.cos(x_norm[i] + np.pi/4) + \
                         0.8 * np.sin(2 * x_norm[i] + np.pi/7) * np.cos(2 * x_norm[i] + np.pi/6) + \
                         0.3 * np.sin(3 * x_norm[i] + np.pi/9) * np.cos(3 * x_norm[i] + np.pi/8)
        
        # Additional high-frequency oscillatory components for increased complexity
        high_freq_term = 0.0
        for i in range(self.dim):
            high_freq_term += 0.5 * np.sin(18 * x_norm[i]) + \
                             0.4 * np.cos(17 * x_norm[i]) + \
                             0.3 * np.sin(22 * x_norm[i])
        
        # Final combined function with weighted contributions
        return 0.22 * chaotic_term + 0.19 * periodic_term + 0.17 * ridge_term + \
               0.13 * barrier_term + 0.14 * fractal_term + 0.09 * phase_term + \
               0.06 * high_freq_term