import numpy as np

class ChaoticHybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Chaotic sinusoidal component with varying frequencies and amplitudes
        for i in range(self.dim):
            freq = 2**(i+1)
            amp = 1.0 / (1.0 + i * 0.1)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5) * np.tan(0.1 * x[i]**3)
        
        # Polynomial coupling with chaotic interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j])
                result += 0.5 * coupling * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Fractal-like recursive structure
        for i in range(self.dim):
            result += 0.3 * np.sin(3 * x[i]) * np.cos(7 * x[i]) * np.sin(11 * x[i]**2) * np.cos(13 * x[i]**3)
        
        # Boundary-sensitive exponential terms
        for i in range(self.dim):
            result += 0.4 * np.exp(-np.abs(x[i] - 5.0)) * np.sin(10 * x[i]) + 0.4 * np.exp(-np.abs(x[i] + 5.0)) * np.cos(10 * x[i])
        
        # High-order polynomial with chaotic coefficients
        sum_x = np.sum(x)
        result += 0.2 * (sum_x**7 - 3*sum_x**5 + 2*sum_x**3 - sum_x)
        
        # Multi-scale oscillatory component
        for i in range(self.dim):
            result += 0.15 * np.sin(50 * x[i]) * np.cos(40 * x[i]) * np.sin(30 * x[i]**2) * np.cos(20 * x[i]**3)
        
        # Cross-dimensional interaction with dynamic scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scale = 1.0 + 0.5 * np.sin(x[i] + x[j])
                result += 0.3 * scale * np.sin(2 * x[i]) * np.cos(2 * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Saddle-point enhancement with chaotic perturbation
        for i in range(self.dim):
            result += 0.1 * x[i]**8 - 0.3 * x[i]**7 + 0.2 * x[i]**6 - 0.1 * x[i]**5
        
        return result