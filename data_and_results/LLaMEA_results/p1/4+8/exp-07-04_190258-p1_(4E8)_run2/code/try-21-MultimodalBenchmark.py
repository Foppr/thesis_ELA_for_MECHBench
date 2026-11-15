import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Multimodal component with chaotic perturbations and saddle points
        multimodal = 0
        for i in range(self.dim):
            # Add chaotic sinusoidal modulation
            chaotic_term = np.sin(x[i]) * np.exp(-0.05 * (x[i] - 1)**2)
            # Add saddle point contribution
            saddle_term = 0.5 * (x[i] - 2)**2 * np.sin(0.5 * x[i])
            multimodal += chaotic_term + saddle_term
        
        # Additional asymmetric quadratic terms
        asymmetric = 0
        for i in range(self.dim):
            if x[i] >= 0:
                asymmetric += 0.2 * (x[i] - 1.5)**2
            else:
                asymmetric += 0.3 * (x[i] + 1.5)**2
        
        # Add coupling between dimensions for increased complexity
        coupling = 0
        for i in range(self.dim - 1):
            coupling += 0.1 * np.sin(x[i]) * np.cos(x[i+1])
        
        return sphere + multimodal + asymmetric + coupling