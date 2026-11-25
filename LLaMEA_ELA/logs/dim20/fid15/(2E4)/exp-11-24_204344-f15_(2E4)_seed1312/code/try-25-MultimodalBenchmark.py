import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Base quadratic term with exponential scaling
        quadratic = np.exp(np.sum(x**2) / self.dim) - 1.0
        
        # Exponentially scaled periodic multimodal component with multiple global minima
        periodic = 0.0
        for i in range(self.dim):
            periodic += 2.0 * np.exp(2.0 * np.sin(10 * np.pi * x[i]) ** 2) + 1.2 * np.cos(5 * np.pi * x[i]) ** 2
        
        # Complex basin term with exponential modification
        basin = 0.2 * np.exp(0.5 * np.sum((x - 2.0)**2))
        
        # Enhanced noise terms with higher frequency components
        noise = 0.1 * np.sum(np.sin(20 * x) * np.cos(10 * x) * np.exp(-0.1 * x**2))
        
        # Saddle point term with higher-order polynomial
        saddle = 0.05 * np.sum(x**6)
        
        # Stronger cross-dimensional interaction terms
        cross_interaction = 0.1 * np.sum(x[:-1] ** 2 * x[1:] ** 2)
        
        return quadratic + periodic + basin + noise + saddle + cross_interaction