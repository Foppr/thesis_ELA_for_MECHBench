import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        self.coeffs = np.random.uniform(-1, 1, dim)
        self.poly_exponents = np.random.randint(2, 6, dim)
        self.logistic_r = np.random.uniform(3.5, 4.0, dim)
        self.oscillation_freq = np.random.uniform(1.0, 5.0, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        f_val = 0.0
        
        # Base quadratic term
        f_val += np.sum(x**2) * 0.1
        
        # Sinusoidal oscillations with varying frequencies
        for i in range(self.dim):
            f_val += 0.5 * np.sin(self.oscillation_freq[i] * x[i]) * np.cos(2 * x[i])
            
        # Polynomial interactions with random exponents
        for i in range(self.dim):
            f_val += 0.3 * (x[i]**self.poly_exponents[i]) * np.sin(3 * x[i])
            
        # Logistic map chaotic modulation
        for i in range(self.dim):
            logistic_val = x[i]
            for _ in range(10):
                logistic_val = self.logistic_r[i] * logistic_val * (1 - logistic_val)
            f_val += 0.2 * logistic_val * np.cos(4 * x[i])
            
        # Cross-variable polynomial interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.1 * (x[i]**2) * (x[j]**3) * np.sin(2 * (x[i] + x[j]))
                
        # Global multimodal component with multiple peaks
        f_val += 0.4 * np.prod(np.sin(0.5 * x + np.pi/4)) + 0.3 * np.sum(np.cos(3 * x))
        
        return f_val