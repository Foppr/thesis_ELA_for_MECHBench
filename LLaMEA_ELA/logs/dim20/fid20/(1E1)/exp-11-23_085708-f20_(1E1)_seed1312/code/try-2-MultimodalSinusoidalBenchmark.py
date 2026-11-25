import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Quadratic basin term - creates a broad minimum region
        quadratic_term = 0.1 * np.sum(x**2)
        
        # Sinusoidal grid terms - creates multiple local minima
        sinusoidal_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                sinusoidal_term += np.sin(0.5 * (x[i] + x[j])) * np.cos(0.3 * (x[i] - x[j]))
        
        # Additional high-frequency sinusoidal terms for increased complexity
        for i in range(self.dim):
            sinusoidal_term += 1.0 * np.sin(2.0 * x[i]) * np.cos(1.5 * x[i])
            
        # Add a chaotic component with exponential modulation
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.exp(-0.1 * np.abs(x[i])) * np.sin(3.0 * x[i])
        
        return quadratic_term + sinusoidal_term + chaotic_term + 3.0