import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with increased scaling
        result = 1.2 * np.sum(x**2)
        
        # High-frequency chaotic sinusoidal components with varying amplitudes and phases
        for i in range(self.dim):
            result += 1.0 * np.sin(20 * x[i]) * np.cos(12 * x[i]) + 0.8 * np.sin(10 * x[i])**3 + 0.5 * np.cos(15 * x[i])**2
            
        # Complex multi-dimensional interaction terms with stronger exponential scaling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.4 * np.sin(8 * x[i]) * np.cos(9 * x[j]) * np.exp(-0.15 * (x[i] - x[j])**2) + \
                          0.25 * np.sin(x[i] + x[j])**5 + 0.15 * np.cos(2 * x[i] - x[j])**3
                
        # Higher-order polynomial terms with mixed exponents and increased weights
        for i in range(self.dim):
            result += 0.25 * x[i]**6 + 0.2 * x[i]**8 + 0.15 * np.exp(2.5 * x[i]**2) + 0.1 * x[i]**9
            
        # Cross-dimensional polynomial terms with stronger exponential decay and interaction
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.1 * (x[i]**5) * (x[j]**4) * np.exp(-0.08 * (x[i]**2 + x[j]**2)) + \
                          0.08 * (x[i]**3) * (x[j]**6) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                
        # Additional cubic interaction term between dimensions with increased coefficient
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.15 * (x[i] * x[j])**4
                
        # Structured noise with multiple frequency components and a shifted global minimum
        noise = 0.08 * np.sum(np.sin(35 * x) + np.cos(22 * x) + np.sin(25 * x)**2 + np.cos(15 * x)**3)
        result += noise
        
        # Introduce a perturbed global minimum by adding a sinusoidal offset with higher frequency
        global_offset = 0.5 * np.sum(np.sin(0.8 * x) * np.cos(0.5 * x) + 0.3 * np.sin(1.2 * x)**2)
        result += global_offset
        
        # Add a stronger exponential barrier near the boundaries to increase difficulty
        barrier = 3.0 * np.sum(np.exp(15 * (np.abs(x) - 5.0)))
        result += barrier
        
        # Add a chaotic logistic map component for additional complexity
        logistic_component = 0.0
        r = 3.95
        for i in range(self.dim):
            logistic_component += 0.05 * np.sin(r * x[i] * (1 - x[i])) if i < len(x) else 0
        result += logistic_component
        
        # Final scaling to maintain balanced landscape complexity
        result *= 1.2
        
        return result