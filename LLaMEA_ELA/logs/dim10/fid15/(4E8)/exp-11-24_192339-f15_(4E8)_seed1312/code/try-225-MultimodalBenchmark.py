import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal oscillation component with adaptive frequencies
        sin_component = 0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(0.2 * x[i])
            sin_component += np.sin(freq * x[i]) * np.cos(0.3 * x[i]**2)
        
        # Radial basis function with dynamic width and orientation
        rbf_component = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                width = 0.5 + 0.3 * np.sin(0.4 * x[i])
                orientation = np.sin(0.2 * (x[i] + x[j]))
                rbf_component += orientation * np.exp(-0.5 * (dist / width)**2)
        
        # Polynomial interaction with exponential scaling
        poly_component = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                term = (x[i]**2 + x[j]**2) * np.exp(-0.1 * (x[i] - x[j])**2)
                poly_component += term
        
        # Asymmetric coupling with hyperbolic tangent
        asym_component = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                asym_term = (np.tanh(x[i]) - np.tanh(x[j])) * (x[i] + x[j])
                asym_component += asym_term
        
        # Adaptive conditioning based on dimensionality
        cond_factor = 1.0 + 0.2 * np.sin(self.dim * 0.1)
        
        # Fractal-like recursive structure with polynomial scaling
        fractal_component = 0
        for i in range(self.dim):
            fractal_component += (x[i]**3 + 0.5 * x[i]**2) * np.sin(0.5 * x[i])
        
        # Combine all components with appropriate weights
        return cond_factor * (0.4 * sin_component + 0.3 * rbf_component + 
                             0.2 * poly_component + 0.08 * asym_component + 
                             0.02 * fractal_component)