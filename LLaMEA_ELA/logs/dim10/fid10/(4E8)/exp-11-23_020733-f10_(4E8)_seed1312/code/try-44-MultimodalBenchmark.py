import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with slight scaling
        result = 0.8 * np.sum(x**2)
        
        # High-frequency sinusoidal components with varying amplitudes
        for i in range(self.dim):
            result += 0.6 * np.sin(15 * x[i]) * np.cos(8 * x[i]) + 0.3 * np.sin(7 * x[i])**3
            
        # Complex interaction terms between dimensions with exponential scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.25 * np.sin(6 * x[i]) * np.cos(7 * x[j]) * np.exp(-0.12 * (x[i] - x[j])**2) + \
                          0.12 * np.sin(x[i] + x[j])**4
                
        # Higher-order polynomial terms with mixed exponents
        for i in range(self.dim):
            result += 0.18 * x[i]**5 + 0.12 * x[i]**7 + 0.06 * np.exp(2.2 * x[i]**2)
            
        # Cross-dimensional polynomial terms with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.06 * (x[i]**4) * (x[j]**3) * np.exp(-0.06 * (x[i]**2 + x[j]**2))
                
        # Additional cubic interaction term between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.08 * (x[i] * x[j])**3
                
        # Structured noise with multiple frequency components and a shifted global minimum
        noise = 0.04 * np.sum(np.sin(28 * x) + np.cos(17 * x) + np.sin(20 * x)**2 + np.cos(10 * x)**3)
        result += noise
        
        # Introduce a perturbed global minimum by adding a sinusoidal offset
        global_offset = 0.35 * np.sum(np.sin(0.6 * x) * np.cos(0.35 * x))
        result += global_offset
        
        # Add a strong exponential barrier near the boundaries to increase difficulty
        barrier = 2.2 * np.sum(np.exp(11 * (np.abs(x) - 5.0)))
        result += barrier
        
        # Final scaling to maintain balanced landscape complexity
        result *= 1.12
        
        return result