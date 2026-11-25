import numpy as np

class ChaoticHybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Enhanced chaotic sinusoidal component with higher frequencies and amplitudes
        for i in range(self.dim):
            freq = 3**(i+1)
            amp = 1.5 / (1.0 + i * 0.2)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7) * np.tan(0.15 * x[i]**3)
        
        # Stronger polynomial coupling with chaotic interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = (x[i]**3 + x[j]**3) * np.sin(x[i] * x[j]) * np.cos(0.5 * x[i] * x[j])
                result += 0.7 * coupling * np.exp(-0.15 * (x[i] - x[j])**2)
        
        # Enhanced fractal-like recursive structure with higher frequency components
        for i in range(self.dim):
            result += 0.5 * np.sin(5 * x[i]) * np.cos(9 * x[i]) * np.sin(13 * x[i]**2) * np.cos(17 * x[i]**3) * np.sin(23 * x[i]**4)
        
        # Increased boundary-sensitive exponential terms
        for i in range(self.dim):
            result += 0.6 * np.exp(-np.abs(x[i] - 5.0)) * np.sin(15 * x[i]) + 0.6 * np.exp(-np.abs(x[i] + 5.0)) * np.cos(15 * x[i])
        
        # Higher-order polynomial with more chaotic coefficients
        sum_x = np.sum(x)
        result += 0.3 * (sum_x**9 - 4*sum_x**7 + 3*sum_x**5 - sum_x**3)
        
        # Enhanced multi-scale oscillatory component
        for i in range(self.dim):
            result += 0.25 * np.sin(70 * x[i]) * np.cos(60 * x[i]) * np.sin(50 * x[i]**2) * np.cos(40 * x[i]**3) * np.sin(30 * x[i]**4)
        
        # Enhanced cross-dimensional interaction with dynamic scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                scale = 1.5 + 0.8 * np.sin(x[i] + x[j]) * np.cos(0.5 * x[i] - x[j])
                result += 0.5 * scale * np.sin(3 * x[i]) * np.cos(3 * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Saddle-point enhancement with more complex chaotic perturbation
        for i in range(self.dim):
            result += 0.15 * x[i]**9 - 0.4 * x[i]**8 + 0.3 * x[i]**7 - 0.2 * x[i]**6 + 0.1 * x[i]**5
        
        # Additional chaotic coupling between all dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    result += 0.2 * np.sin(x[i] * x[j] * x[k]) * np.cos(0.3 * x[i]**2 + 0.4 * x[j]**2 + 0.5 * x[k]**2)
        
        return result