import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with logistic map scaling
        result = 0.7 * np.sum(x**2)
        
        # Chaotic sinusoidal components with logistic map modulation
        for i in range(self.dim):
            logistic_factor = 1.0 / (1.0 + np.exp(-5.0 * (x[i] - 0.5)))
            result += 0.6 * np.sin(15 * x[i]) * np.cos(8 * x[i]) * logistic_factor + \
                      0.3 * np.sin(7 * x[i])**4 * (1.0 - logistic_factor)
            
        # Enhanced interaction terms with asymmetric saddle points
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                asym_factor = np.abs(x[i] - x[j]) / (np.abs(x[i]) + np.abs(x[j]) + 1e-8)
                result += 0.25 * np.sin(4 * x[i]) * np.cos(5 * x[j]) * asym_factor + \
                          0.15 * np.sin(x[i] + x[j])**3 * (1.0 - asym_factor)
                
        # Higher-order polynomial terms with chaotic weights
        for i in range(self.dim):
            chaotic_weight = 0.5 + 0.5 * np.sin(10 * x[i])
            result += 0.2 * x[i]**6 * chaotic_weight + 0.15 * x[i]**8 * (1.0 - chaotic_weight) + \
                      0.08 * np.exp(3 * x[i]**2)
            
        # Cross-dimensional terms with exponential decay and chaotic modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaotic_mod = 0.5 + 0.5 * np.sin(5 * (x[i] + x[j]))
                result += 0.08 * (x[i]**5) * (x[j]**4) * np.exp(-0.03 * (x[i]**2 + x[j]**2)) * chaotic_mod
                
        # Structured noise with chaotic frequency components and global minimum perturbation
        noise = 0.04 * np.sum(np.sin(30 * x) + np.cos(20 * x) + np.sin(25 * x)**2 + np.cos(12 * x)**3)
        result += noise
        
        # Perturbed global minimum with chaotic offset
        global_offset = 0.4 * np.sum(np.sin(0.7 * x) * np.cos(0.4 * x) * np.exp(-0.5 * x**2))
        result += global_offset
        
        # Modified boundary barriers with chaotic strength
        barrier_strength = 1.5 + 0.5 * np.sin(8 * x)
        barrier = np.sum(barrier_strength * np.exp(12 * (np.abs(x) - 5.0)))
        result += barrier
        
        # Final scaling to maintain balanced landscape complexity
        result *= 1.2
        
        return result