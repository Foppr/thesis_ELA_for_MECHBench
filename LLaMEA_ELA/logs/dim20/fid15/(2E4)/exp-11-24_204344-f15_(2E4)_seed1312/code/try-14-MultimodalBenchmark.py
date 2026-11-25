import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Base quadratic term
        quadratic = np.sum(x**2) / self.dim
        
        # Enhanced periodic multimodal component with multiple global minima
        periodic = 0.0
        for i in range(self.dim):
            periodic += 1.5 * np.sin(8 * np.pi * x[i]) ** 2 + 0.7 * np.cos(4 * np.pi * x[i]) ** 2
        
        # Add a basin term with modified coefficients to create a more challenging landscape
        basin = 0.15 * np.sum((x - 1.5)**2)
        
        # Modify noise terms to increase complexity
        noise = 0.08 * np.sum(np.sin(12 * x) * np.cos(6 * x))
        
        # Add a saddle point term with different scaling
        saddle = 0.03 * np.sum(x**4)
        
        # Add cross-dimensional interaction terms
        cross_interaction = 0.05 * np.sum(x[:-1] * x[1:])
        
        return quadratic + periodic + basin + noise + saddle + cross_interaction