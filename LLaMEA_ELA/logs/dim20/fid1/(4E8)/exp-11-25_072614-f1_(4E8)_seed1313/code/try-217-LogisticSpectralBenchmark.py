import numpy as np

class LogisticSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters
        self.r_values = np.random.uniform(3.5, 4.0, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Logistic map chaotic dynamics
        logistic_term = 0.0
        for i in range(self.dim):
            r = self.r_values[i]
            x_i = (x[i] + 5.0) / 10.0  # Normalize to [0, 1]
            x_i = r * x_i * (1 - x_i)
            logistic_term += x_i**2
        
        # Spectral decomposition using discrete cosine transform
        dct_term = 0.0
        for i in range(self.dim):
            # Apply DCT-like transformation with varying frequencies
            freq = 2 * np.pi * (i + 1) / self.dim
            dct_term += np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Adaptive ridge penalty based on dimensionality and input values
        ridge_penalty = 0.0
        for i in range(self.dim):
            ridge_penalty += (x[i]**2 + 0.1 * np.sin(x[i])**2) / (1.0 + 0.01 * self.dim)
        
        # Cross-dimensional interaction with sine coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[i] - x[j]) * np.cos(x[i] + x[j])
        
        # Dynamic conditioning with exponential scaling
        cond_term = 0.0
        for i in range(self.dim):
            cond_term += np.exp(0.1 * np.abs(x[i])) * np.sin(0.5 * x[i])**2
        
        # Multi-scale fractal-like structure with recursive sine waves
        fractal_term = 0.0
        for i in range(self.dim):
            scale = 1.0
            for k in range(1, 6):  # Up to 5 scales
                scale *= 0.5
                fractal_term += scale * np.sin(2**k * x[i])
        
        # Combine all terms with varying weights
        total = 0.25 * logistic_term + 0.20 * dct_term + 0.15 * ridge_penalty + 0.20 * cross_term + 0.10 * cond_term + 0.10 * fractal_term
        
        return total