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
            periodic += 2.0 * np.sin(10 * np.pi * x[i]) ** 2 + 1.2 * np.cos(5 * np.pi * x[i]) ** 2
        
        # Add a basin term with modified coefficients to create a more challenging landscape
        basin = 0.2 * np.sum((x - 2.0)**2)
        
        # Modify noise terms to increase complexity
        noise = 0.1 * np.sum(np.sin(15 * x) * np.cos(8 * x))
        
        # Add a saddle point term with different scaling
        saddle = 0.04 * np.sum(x**4)
        
        # Add cross-dimensional interaction terms with higher coupling strength
        cross_interaction = 0.1 * np.sum(x[:-1] * x[1:] * (x[:-1]**2 + x[1:]**2))
        
        # Add a new hyper-peak term to increase multimodality
        hyper_peak = 0.3 * np.sum(np.sin(20 * x) ** 4)
        
        return quadratic + periodic + basin + noise + saddle + cross_interaction + hyper_peak