import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Base quadratic term
        quadratic = np.sum(x**2) / self.dim
        
        # Enhanced periodic multimodal component with altered frequencies and amplitudes
        periodic = 0.0
        for i in range(self.dim):
            periodic += 2.5 * np.sin(12 * np.pi * x[i]) ** 2 + 0.7 * np.cos(6 * np.pi * x[i]) ** 2
        
        # Add a basin term with modified coefficients to create a more challenging landscape
        basin = 0.3 * np.sum((x - 1.5)**2)
        
        # Modify noise terms to increase complexity
        noise = 0.15 * np.sum(np.sin(18 * x) * np.cos(9 * x))
        
        # Add a saddle point term with different scaling
        saddle = 0.05 * np.sum(x**4)
        
        # Add cross-dimensional interaction terms
        cross_interaction = 0.07 * np.sum(x[:-1] * x[1:])
        
        return quadratic + periodic + basin + noise + saddle + cross_interaction