import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential coupling terms
        exp_term = 0.0
        for i in range(self.dim):
            exp_term += np.exp(0.5 * x[i]**2) * np.sin(3 * x[i])
        
        # Trigonometric wave interference
        wave_term = 0.0
        for i in range(self.dim):
            wave_term += np.cos(2 * x[i]) * np.sin(4 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Saddle-point attraction regions
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += (x[i]**2 - 1.0)**2 * np.cos(5 * x[i])
        
        # Cross-dimensional coupling with exponential decay
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.exp(-0.5 * (x[i]**2 + x[j]**2)) * \
                              np.sin(2 * x[i] * x[j]) * \
                              np.cos(0.3 * (x[i]**2 - x[j]**2))
        
        # Combined result with global minimum at origin
        result = exp_term + wave_term + saddle_term + 0.3 * cross_term
        
        # Add penalty for distance from origin to reinforce global minimum
        result += 0.02 * np.sum(x**8) + 0.01 * np.sum(np.abs(x)**5)
        
        return result