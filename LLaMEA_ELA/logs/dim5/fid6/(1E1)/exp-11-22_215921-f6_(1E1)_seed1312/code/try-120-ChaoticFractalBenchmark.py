import numpy as np

class ChaoticFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Logistic map chaotic component with parameter modulation
        logistic = 0.0
        r_params = 3.9 + 0.1 * np.sin(2 * np.pi * x_norm[:-1])
        for i in range(len(x_norm)-1):
            logistic += (r_params[i] * x_norm[i] * (1 - x_norm[i])) ** 2
        
        # Fractal basin boundaries with self-similar structure
        fractal = np.sum(np.abs(x_norm[:-1] - x_norm[1:]) ** 1.5 * 
                        np.exp(-0.5 * (x_norm[:-1]**2 + x_norm[1:]**2)))
        
        # Cross-dimensional interference patterns with wave superposition
        interference = 0.0
        for i in range(len(x_norm)):
            for j in range(i+1, len(x_norm)):
                interference += np.sin(5 * (x_norm[i] - x_norm[j])) * np.cos(3 * (x_norm[i] + x_norm[j]))
        
        # Multi-scale periodic modulation with dynamic frequency
        multi_freq = 0.0
        for i in range(len(x_norm)):
            freq = 2 ** (i % 3) * (1 + 0.5 * np.sin(4 * np.pi * x_norm[i]))
            multi_freq += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i])
        
        # Asymmetric Gaussian valleys with fractal geometry
        gaussian_valleys = 0.0
        for i in range(len(x_norm)):
            gaussian_valleys += np.exp(-2 * (x_norm[i] - np.sin(3 * x_norm[i]))**2) * \
                              np.exp(-0.5 * (x_norm[i]**2))
        
        # Dimension-dependent coupling with recursive scaling
        coupling = 1.0 + 0.3 * np.log(self.dim + 1)
        
        # Combine all terms with adaptive weighting
        return coupling * (logistic + fractal + interference + multi_freq + gaussian_valleys)