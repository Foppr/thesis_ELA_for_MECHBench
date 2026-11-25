import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced chaotic component with multi-frequency interference
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += (np.sin(15 * np.pi * x_norm[i]) * np.cos(7 * np.pi * x_norm[i]) + 
                       np.sin(8 * np.pi * x_norm[i]) * np.cos(12 * np.pi * x_norm[i]))
        
        # Higher-order polynomial potential with variable coefficients
        poly_potential = np.sum(0.8 * x_norm**6 + 0.4 * x_norm**5 + 0.3 * x_norm**4 + 
                               0.2 * x_norm**3 + 0.1 * x_norm**2)
        
        # Complex wave interference with frequency modulation
        wave_sum = 0.0
        for i in range(self.dim):
            freq_mod = 1 + 0.5 * np.sin(0.5 * np.pi * x_norm[i])
            wave_sum += np.sin(4 * np.pi * x_norm[i] * freq_mod * (i + 1)) * np.cos(6 * np.pi * x_norm[i] * freq_mod * (i + 1))
        
        # Advanced cross-dimensional coupling with adaptive weights
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.0 / (1.0 + np.exp(-5 * (x_norm[i] - x_norm[j])**2))
                cross_coupling += weight * np.exp(-abs(x_norm[i] - x_norm[j])) * np.sin(np.pi * (x_norm[i] + x_norm[j]))
        
        # Asymmetric saddle point structure with dynamic curvature
        saddle = 0.0
        for i in range(self.dim):
            curvature = 1.0 + 0.3 * np.sin(2 * np.pi * x_norm[i])
            saddle += x_norm[i]**2 * curvature * np.cos(6 * np.pi * x_norm[i])
        
        # Stochastic perturbation with adaptive noise scaling
        noise = 0.05 * np.random.random() * (1.0 + 0.5 * np.mean(np.abs(x_norm)))
        
        # Adaptive scaling factors based on dimensionality
        scale_factors = [1.2 + 0.1 * i for i in range(self.dim)]
        adaptive_scale = np.mean(scale_factors)
        
        return adaptive_scale * (1.8 * chaotic + 0.9 * poly_potential + 0.7 * wave_sum + 
                               0.5 * cross_coupling + 0.4 * saddle) + noise