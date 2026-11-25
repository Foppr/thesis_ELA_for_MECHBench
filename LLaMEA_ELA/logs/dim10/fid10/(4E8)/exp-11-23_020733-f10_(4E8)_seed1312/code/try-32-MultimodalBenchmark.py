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
            result += 0.5 * np.sin(12 * x[i]) * np.cos(7 * x[i]) + 0.25 * np.sin(6 * x[i])**3
            
        # Complex interaction terms between dimensions with exponential scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.2 * np.sin(5 * x[i]) * np.cos(6 * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2) + \
                          0.1 * np.sin(x[i] + x[j])**4
                
        # Higher-order polynomial terms with mixed exponents
        for i in range(self.dim):
            result += 0.15 * x[i]**5 + 0.1 * x[i]**7 + 0.05 * np.exp(2 * x[i]**2)
            
        # Cross-dimensional polynomial terms with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.05 * (x[i]**4) * (x[j]**3) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Structured noise with multiple frequency components and a shifted global minimum
        noise = 0.03 * np.sum(np.sin(25 * x) + np.cos(15 * x) + np.sin(18 * x)**2 + np.cos(9 * x)**3)
        result += noise
        
        # Introduce a perturbed global minimum by adding a sinusoidal offset
        global_offset = 0.3 * np.sum(np.sin(0.5 * x) * np.cos(0.3 * x))
        result += global_offset
        
        # Add a strong exponential barrier near the boundaries to increase difficulty
        barrier = 2.0 * np.sum(np.exp(10 * (np.abs(x) - 5.0)))
        result += barrier
        
        # Final scaling to maintain balanced landscape complexity
        result *= 1.1
        
        return result