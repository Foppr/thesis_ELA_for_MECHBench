import numpy as np

class ChaoticInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Spherical basin component
        sphere = 0.1 * np.sum(x**2)
        
        # Logistic map chaotic component with parameter dependence
        logistic = 0.0
        r = 3.9  # Chaos-inducing parameter
        for i in range(self.dim):
            if i == 0:
                x_prev = x[-1]
            else:
                x_prev = x[i-1]
            logistic += np.sin(r * x_prev * (1 - x_prev)) * np.cos(x[i])
        
        # Fractal-like interference pattern using multiple frequencies
        fractal = 0.0
        for i in range(self.dim):
            fractal += np.sin(2**i * x[i]) * np.cos(3**i * x[(i + 1) % self.dim])
            fractal += 0.5 * np.sin(5 * x[i]) * np.sin(7 * x[(i + 2) % self.dim])
        
        # Multi-scale oscillatory component with varying amplitudes
        oscillatory = 0.0
        for i in range(self.dim):
            oscillatory += (1.0 / (i + 1)) * np.sin(10 * x[i]) * np.cos(8 * x[(i + 1) % self.dim])
            oscillatory += (1.0 / (i + 1)**2) * np.sin(15 * x[i]) * np.cos(12 * x[(i + 2) % self.dim])
        
        # Cross-term interaction with non-separability
        cross_terms = 0.0
        for i in range(self.dim):
            cross_terms += 0.3 * x[i] * np.sin(x[(i + 1) % self.dim]) * np.cos(x[(i + 2) % self.dim])
            cross_terms += 0.2 * x[i]**2 * np.sin(2 * x[(i + 1) % self.dim])
        
        # Global structure with multiple local minima
        global_structure = 0.0
        for i in range(self.dim):
            global_structure += (x[i] - 1)**4 + (x[i] + 1)**4
            
        # Add noise to create ruggedness
        noise = 0.05 * np.sum(np.random.randn(self.dim))
        
        return sphere + 1.5 * logistic + 1.2 * fractal + 0.8 * oscillatory + 0.6 * cross_terms + 1.0 * global_structure + noise