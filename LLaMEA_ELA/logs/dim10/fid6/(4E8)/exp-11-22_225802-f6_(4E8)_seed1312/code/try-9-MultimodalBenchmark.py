import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Quadratic basin term - global minimum at origin
        basin = 0.1 * np.sum(x**2)
        
        # Multimodal periodic terms with multiple global minima
        periodic = 0.0
        for i in range(self.dim):
            periodic += np.sin(2 * np.pi * x[i]) * np.cos(0.5 * np.pi * x[i]) + 0.5 * np.sin(4 * np.pi * x[i])**2
            
        # Additional sinusoidal terms with different frequencies for increased complexity
        additional = 0.0
        for i in range(self.dim):
            additional += 0.3 * np.sin(3 * np.pi * x[i])**2 + 0.7 * np.cos(2.5 * np.pi * x[i])**2
            
        # Cross-terms to introduce interactions between dimensions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += 0.1 * np.sin(np.pi * x[i]) * np.cos(np.pi * x[j])
                
        return basin + periodic + additional + cross_term