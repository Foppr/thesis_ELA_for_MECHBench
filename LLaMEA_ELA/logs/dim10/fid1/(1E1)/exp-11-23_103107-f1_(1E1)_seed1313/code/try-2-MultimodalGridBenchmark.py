import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Quadratic basin term - global minimum at origin
        basin = 0.1 * np.sum(x**2)
        
        # Multimodal grid terms with shifted minima and modified interactions
        grid_terms = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    # Shifted grid pattern with different frequencies
                    grid_terms += np.sin(2 * (x[i] - x[j])**2) * np.cos(1.5 * x[i]**2 + 0.5 * x[j]**2)
        
        # Additional harmonic terms with altered coefficients
        harmonic = 0
        for i in range(self.dim):
            harmonic += 0.5 * np.sin(4 * x[i]) * np.cos(1.2 * x[i])
            
        return basin + grid_terms + harmonic