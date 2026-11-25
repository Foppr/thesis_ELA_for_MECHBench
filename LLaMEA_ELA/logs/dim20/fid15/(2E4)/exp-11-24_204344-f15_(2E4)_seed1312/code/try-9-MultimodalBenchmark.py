import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Base quadratic term
        quadratic = np.sum(x**2) / self.dim
        
        # Complex periodic multimodal component with multiple global minima
        periodic = 0.0
        for i in range(self.dim):
            periodic += np.sin(7 * np.pi * x[i]) ** 2 + 0.5 * np.cos(3 * np.pi * x[i]) ** 2
        
        # Add a basin term to create a more challenging landscape
        basin = 0.1 * np.sum((x - 1.0)**2)
        
        # Add noise terms to increase complexity
        noise = 0.05 * np.sum(np.sin(10 * x) * np.cos(5 * x))
        
        # Add a saddle point term to create additional difficulty
        saddle = 0.02 * np.sum(x**4)
        
        return quadratic + periodic + basin + noise + saddle