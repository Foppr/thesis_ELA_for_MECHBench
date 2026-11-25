import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Base quadratic term for global attraction
        quadratic = np.sum(x_norm ** 2)
        
        # Chaotic sinusoidal oscillations using logistic map for enhanced complexity
        logistic_seq = np.array([0.5])
        for _ in range(self.dim):
            logistic_seq = np.append(logistic_seq, logistic_seq[-1] * 3.8 * (1 - logistic_seq[-1]))
        chaotic = 3 * np.sum(np.sin(logistic_seq[1:self.dim+1] * np.pi * x_norm) ** 2)
        
        # Multiple gaussian peaks with varying heights and widths
        gaussian = 0.3 * np.sum(np.exp(-5 * (x_norm - 0.2) ** 2) + 
                               np.exp(-15 * (x_norm + 0.3) ** 2) +
                               np.exp(-8 * (x_norm - 0.5) ** 2) +
                               np.exp(-12 * (x_norm + 0.6) ** 2))
        
        # Additional saddle point region to increase conditioning difficulty
        saddle = 0.7 * np.sum(np.sin(3 * np.pi * x_norm) * np.cos(2 * np.pi * x_norm))
        
        # Combine all terms with different weights
        return quadratic + chaotic + gaussian + saddle