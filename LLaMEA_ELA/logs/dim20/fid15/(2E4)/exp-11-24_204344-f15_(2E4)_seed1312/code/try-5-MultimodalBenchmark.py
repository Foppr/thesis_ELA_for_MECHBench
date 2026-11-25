import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Base quadratic term
        quadratic = np.sum(x**2) / self.dim
        
        # Periodic multimodal component with multiple global minima
        periodic = 0.0
        for i in range(self.dim):
            periodic += np.sin(5 * np.pi * x[i]) ** 2
        
        # Add a basin term to create a more challenging landscape
        basin = 0.1 * np.sum((x - 1.0)**2)
        
        # Add sinusoidal interference terms for increased complexity
        interference = 0.0
        for i in range(self.dim):
            interference += 0.5 * np.sin(3 * np.pi * x[i]) * np.cos(2 * np.pi * x[i])
        
        # Add a multi-modal component with higher frequency oscillations
        high_freq = 0.0
        for i in range(self.dim):
            high_freq += np.sin(10 * np.pi * x[i]) ** 2
        
        return quadratic + periodic + basin + interference + high_freq