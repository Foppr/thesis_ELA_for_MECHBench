import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic terms with varying scales and higher-order polynomial
        result = 0.0
        for i in range(self.dim):
            result += (x[i] - 1.2)**2 + (x[i] + 1.2)**2 + 0.03 * x[i]**4 + 0.001 * x[i]**6
        
        # Enhanced exponentially scaled interaction terms with stronger coupling and sinusoidal modulation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction_strength = np.exp(1.5 * (i + j)) * (1.0 + 0.7 * np.sin(i * j)) * (1.0 + 0.3 * np.cos(i + j))
                result += interaction_strength * (x[i] - x[j])**2
        
        # Add multiple saddle point structures with multi-frequency sinusoidal modulation
        for i in range(self.dim):
            result += 0.8 * np.sin(3.0 * x[i]) * np.cos(2.0 * x[i]) * np.sin(0.5 * x[i]) + 0.2 * np.sin(5.0 * x[i])
        
        # Add a highly curved global minimum with asymmetric basin structure
        result += 0.002 * np.sum(x**2) + 0.0005 * np.sum(x**6) + 0.0001 * np.sum(x**8)
        
        # Add a complex periodic component with multiple frequencies and chaotic modulation
        periodic_term = 0.0
        for i in range(self.dim):
            periodic_term += np.sin(4.0 * x[i]) * np.cos(3.0 * x[i]) * np.sin(1.5 * x[i]) * np.cos(0.7 * x[i])
        result += 0.2 * periodic_term
        
        # Add a shifted global minimum with additional perturbation terms and chaotic scaling
        result += 0.6 * np.sum((x - 0.3)**2) + 0.05 * np.sum(np.sin(2.0 * x)**2) + 0.02 * np.sum(np.sin(3.0 * x)**3)
        
        # Add a secondary multimodal structure with local minima and fractal-like characteristics
        for i in range(self.dim):
            result += 0.3 * np.sin(5.0 * x[i]) * np.cos(4.0 * x[i]) + 0.2 * np.sin(7.0 * x[i]) + 0.1 * np.sin(9.0 * x[i])**2
        
        # Add a novel chaotic component with dimensionality-dependent scaling
        chaotic_term = 0.0
        for i in range(self.dim):
            chaotic_term += np.sin(x[i] * np.pi * (i + 1)) * np.cos(x[i] * np.pi * (i + 1) * 0.5)
        result += 0.1 * chaotic_term * np.exp(-0.1 * self.dim)
        
        # Add a dimensional complexity factor to increase challenge with higher dimensions
        result += 0.05 * self.dim * np.sum(np.abs(x)**3)
        
        return result