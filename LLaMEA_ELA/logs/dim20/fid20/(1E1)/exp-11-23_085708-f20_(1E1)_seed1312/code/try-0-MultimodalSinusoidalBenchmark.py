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
        
        # Additional sinusoidal terms for more complexity
        for i in range(self.dim):
            sinusoidal_term += 0.5 * np.sin(0.8 * x[i]) * np.cos(0.4 * x[i])
            
        return quadratic_term + sinusoidal_term + 2.0