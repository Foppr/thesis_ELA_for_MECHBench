import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.alpha = 0.8
        self.beta = 2.5
        self.gamma = 1.8
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal oscillations component
        sin_component = 0.0
        for i in range(self.dim):
            sin_component += np.sin(self.alpha * x[i]) * np.cos(self.beta * x[i])
            
        # Gaussian peaks with adaptive widths
        gaussian_peaks = 0.0
        for i in range(self.dim):
            gaussian_peaks += np.exp(-0.5 * ((x[i] - 1.0) ** 2) / (0.3 + 0.2 * i)) + \
                              np.exp(-0.5 * ((x[i] + 1.0) ** 2) / (0.3 + 0.2 * i))
            
        # Logarithmic barriers
        log_barrier = 0.0
        for i in range(self.dim):
            log_barrier += np.log(1.0 + np.abs(x[i]) ** self.gamma)
            
        # Adaptive conditioning with dimension-dependent scaling
        conditioning = 0.0
        for i in range(self.dim):
            conditioning += (i + 1) * (x[i] ** 2)
            
        # Cross-dimensional interaction with cubic coupling
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += (x[i] * x[j]) ** 3
                
        # Asymmetric exponential penalty
        exp_penalty = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                exp_penalty += np.exp(-x[i]) - 1.0
            else:
                exp_penalty += np.exp(x[i]) - 1.0
                
        return 0.3 * sin_component + 0.4 * gaussian_peaks + 0.1 * log_barrier + \
               0.15 * conditioning + 0.1 * cross_interaction + 0.25 * exp_penalty