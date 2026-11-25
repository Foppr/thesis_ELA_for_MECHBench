import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.a = 0.5
        self.b = 2.0
        self.c = 1.5
        
    def f(self, x):
        # Handle dimension mismatch
        if len(x) < self.dim:
            raise ValueError("Dimension mismatch: input has fewer dimensions than expected")
        elif len(x) > self.dim:
            x = x[:self.dim]
        
        # Scale input to [-5, 5] range if needed
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial basin term - creates a smooth but curved landscape
        poly_term = np.sum(x**4) * 0.1
        
        # Trigonometric modulations - introduces multiple local minima
        trig_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Multiple sine and cosine components with different frequencies
            trig_term += (np.sin(xi * self.a) + np.cos(xi * self.b) + 
                         np.sin(xi * self.c) * np.cos(xi * self.a)) * np.exp(-0.1 * xi**2)
        
        # Exponential interaction terms - creates complex correlations between variables
        exp_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                diff = x[i] - x[j]
                exp_term += np.exp(-0.5 * diff**2) * np.sin(x[i] + x[j]) * (x[i]**2 + x[j]**2)
        
        # Chaotic component using a modified sine map
        chaotic_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Apply a chaotic sine map with parameter control
            chaotic_component = np.sin(xi * np.pi) * np.exp(-0.1 * xi**2)
            chaotic_term += chaotic_component * np.cos(xi * self.b + i * 0.7)
        
        # Combine all terms with proper scaling
        return poly_term + 0.8 * trig_term + 0.2 * exp_term + 0.5 * chaotic_term