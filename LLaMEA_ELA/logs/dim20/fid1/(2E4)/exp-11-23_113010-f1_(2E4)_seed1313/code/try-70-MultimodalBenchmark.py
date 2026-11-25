import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal-like sinusoidal components with varying frequencies and amplitudes
        fractal_sin = np.sum(np.sin(2 ** (np.arange(1, self.dim + 1)) * np.pi * x_norm) * 
                            np.cos(3 ** (np.arange(1, self.dim + 1)) * np.pi * x_norm))
        
        # Chaotic cross-dimensional coupling using logistic map-like interactions
        chaotic_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaotic_coupling += (x_norm[i] * x_norm[j]) * np.sin(17 * np.pi * (x_norm[i] + x_norm[j]))
        
        # Dynamic saddle structure with time-varying coefficients
        dynamic_saddle = np.sum(x_norm**5 * np.sin(9 * np.pi * x_norm) + 
                               0.6 * x_norm**4 * np.cos(7 * np.pi * x_norm))
        
        # Polynomial basin with adaptive weights and higher-order terms
        poly_basin = np.sum(0.25 * x_norm**8 + 0.35 * x_norm**7 + 0.15 * x_norm**6)
        
        # Multi-scale harmonic components with prime-based frequencies
        multi_harmonic = np.sum(np.sin(19 * np.pi * x_norm**4) * 
                               np.cos(13 * np.pi * x_norm**4) + 
                               np.sin(23 * np.pi * x_norm**5) * 
                               np.cos(17 * np.pi * x_norm**5))
        
        # Add noise and scale the function
        noise = 0.005 * np.random.random()
        
        return 1.2 * fractal_sin + 0.9 * chaotic_coupling + 0.6 * dynamic_saddle + \
               0.5 * poly_basin + 0.4 * multi_harmonic + noise