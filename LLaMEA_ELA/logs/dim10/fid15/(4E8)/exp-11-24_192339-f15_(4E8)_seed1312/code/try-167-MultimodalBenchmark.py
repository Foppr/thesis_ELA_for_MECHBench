import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with sinusoidal modulation
        r = np.sqrt(np.sum(x**2))
        radial = r * (1.0 + 0.3 * np.sin(5.0 * r))
        
        # Sinusoidal oscillations in each dimension
        sin_component = 0
        for i in range(self.dim):
            sin_component += np.sin(7.0 * x[i]) * np.cos(3.0 * x[i])
        
        # Cross-dimensional quadratic interactions with varying coupling strengths
        quad_cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.5 + 0.5 * np.sin(0.5 * (i + j))
                quad_cross += coupling * (x[i] - x[j])**2
        
        # Multi-scale radial basis functions with varying centers and widths
        rbfs = 0
        for i in range(self.dim):
            center = 2.0 * np.cos(0.3 * i)
            width = 0.8 + 0.4 * np.sin(0.4 * i)
            rbfs += np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Asymmetric polynomial terms with exponential scaling
        poly_term = 0
        for i in range(self.dim):
            poly_term += (x[i]**3 + x[i]**4) * np.exp(-0.1 * np.abs(x[i]))
        
        # Global conditioning factor based on dimensionality
        cond_factor = 1.0 + 0.5 * np.log(self.dim + 1)
        
        # Combine all components with appropriate weights
        return cond_factor * (0.4 * radial + 0.3 * sin_component + 0.2 * quad_cross + 0.1 * rbfs) + poly_term