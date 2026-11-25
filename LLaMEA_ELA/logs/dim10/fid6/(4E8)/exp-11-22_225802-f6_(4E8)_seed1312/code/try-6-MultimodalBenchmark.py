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
            periodic += np.sin(2 * np.pi * x[i]) * np.cos(0.5 * np.pi * x[i])
            
        # Additional sinusoidal terms for increased complexity
        additional = 0.0
        for i in range(self.dim):
            additional += np.sin(3 * np.pi * x[i])**2 + np.cos(2 * np.pi * x[i])**2
            
        return basin + periodic + additional