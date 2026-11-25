import numpy as np

class MultimodalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial basin term for global convergence
        polynomial = 0.1 * np.sum(x**4)
        
        # Trigonometric multimodal component with multiple peaks
        trigonometric = 0.0
        for i in range(self.dim):
            trigonometric += np.sin(2 * np.pi * x[i]) * np.cos(3 * np.pi * x[i])
            trigonometric += 0.5 * np.sin(5 * x[i]) * np.cos(2 * x[i])
            
        # Radial basis function component with multiple centers
        radial = 0.0
        centers = np.linspace(-4, 4, min(5, self.dim))
        for i in range(len(centers)):
            if i < self.dim:
                radial += np.exp(-0.5 * ((x[i] - centers[i]) / 1.5)**2)
                
        # Cross-dimensional interaction terms
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited interaction
                if j < self.dim:
                    interaction += 0.3 * np.sin(x[i]) * np.cos(x[j]) * (x[i] - x[j])**2
                    
        # Add noise for increased complexity
        noise = 0.02 * np.sum(np.sin(15 * x) + np.cos(15 * x))
        
        return polynomial + trigonometric + radial + interaction + noise