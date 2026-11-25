import numpy as np

class AdaptiveSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Sinusoidal oscillations with varying frequencies and amplitudes
        sinusoidal = np.sum(np.sin(2 * np.pi * x) * np.cos(3 * np.pi * x) * 
                           (1 + 0.5 * np.sin(0.5 * x**2)))
        
        # Polynomial potential terms with different degrees and coefficients
        polynomial = np.sum(0.1 * x**4 + 0.5 * x**3 - 0.8 * x**2 + 0.3 * x)
        
        # Adaptive penalty regions that change based on distance from origin
        penalty = 0
        for i in range(self.dim):
            dist_from_origin = np.sqrt(np.sum(x**2))
            penalty += 10 * np.exp(-0.1 * (dist_from_origin - 2)**2) * \
                      np.sin(2 * np.pi * dist_from_origin)**3 + \
                      5 * np.exp(-0.05 * (dist_from_origin - 4)**2) * \
                      np.cos(4 * np.pi * dist_from_origin)**2
        
        # Cross-dimensional coupling with adaptive weights based on variable positions
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.5 + 0.5 * np.tanh(0.1 * (x[i] - x[j]))
                cross_coupling += weight * np.sin(x[i] * x[j]) * \
                                np.cos(x[i]**2 + x[j]**2) * \
                                (1 + 0.3 * np.sin(0.7 * (x[i] + x[j])**2))
        
        # Add noise component to increase algorithm robustness testing
        noise = 0.01 * np.random.normal(0, 1)
        
        return 0.8 * (sinusoidal + polynomial + cross_coupling + penalty) + noise