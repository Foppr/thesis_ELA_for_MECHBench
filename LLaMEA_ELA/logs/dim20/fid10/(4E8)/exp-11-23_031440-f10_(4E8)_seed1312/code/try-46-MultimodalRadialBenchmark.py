import numpy as np

class MultimodalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Convert to numpy array and ensure correct shape
        x = np.array(x)
        
        # Radial term with dynamic conditioning
        r = np.sqrt(np.sum(x**2))
        radial_term = 0.5 * r**2 * (1 + 0.1 * np.sin(5 * r))
        
        # Polynomial interactions with varying degrees
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += x[i]**4 - 2 * x[i]**2 + 0.5 * x[i]**6
            
        # Radial symmetry with multiple minima
        radial_minima = 0.0
        for i in range(self.dim):
            radial_minima += np.sin(2 * np.pi * x[i]) * np.cos(2 * np.pi * x[i])
            
        # Dynamic conditioning based on distance from origin
        condition_factor = 1 + 0.5 * np.exp(-0.1 * r**2)
        
        # Cross-terms with varying coupling strengths
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += 0.3 * np.sin(3 * (x[i] + x[j])) * np.cos(3 * (x[i] - x[j]))
                
        # Add noise component with multiple frequencies
        noise = 0.05 * np.sum(np.sin(10 * x) + np.cos(7 * x) + 0.3 * np.sin(15 * x))
        
        return condition_factor * (radial_term + poly_term + radial_minima + cross_term + noise)