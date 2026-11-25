import numpy as np

class FractalRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.t = 0.0
        
    def f(self, x):
        self.t += 0.01
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like terrain with self-similar structures
        result = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Multi-scale fractal components with varying exponents
            result += (xi**2 + 0.1 * np.sin(10.0 * xi) + 0.05 * np.sin(50.0 * xi))**2
            
        # Dynamic ridge structures with time-varying curvature
        ridge_strength = 1.0 + 0.3 * np.sin(0.5 * self.t)
        for i in range(self.dim):
            xi = x[i]
            # Ridge-like terms with variable width and height
            result += ridge_strength * np.exp(-xi**2/2.0) * np.cos(3.0 * xi + 0.2 * self.t)
            
        # Elliptic shaping with time-varying eccentricity
        eccentricity = 0.5 + 0.4 * np.sin(0.7 * self.t)
        for i in range(self.dim):
            xi = x[i]
            # Elliptical basin terms with varying axes
            result += eccentricity * (xi**2) * np.exp(-xi**2/4.0)
            
        # Complex valley and peak connectivity with chaotic modulation
        chaos_factor = 0.8 + 0.3 * np.cos(0.9 * self.t)
        for i in range(self.dim):
            xi = x[i]
            # Chaotic valley terms with multiple local minima
            result += chaos_factor * (xi**4 - 2.0 * xi**2) * np.sin(2.0 * xi + 0.1 * self.t)
            
        # Interaction terms with dynamic coupling strength
        coupling = 0.6 + 0.2 * np.sin(0.6 * self.t)
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                # Coupled interaction with fractal-like dependence
                diff = x[i] - x[j]
                result += coupling * np.exp(-diff**2/0.3) * np.sin(5.0 * diff + 0.3 * self.t)
                
        # Modified interaction terms with enhanced chaos
        for i in range(self.dim):
            xi = x[i]
            # Enhanced chaotic modulation with higher frequency components
            result += 0.5 * np.sin(10.0 * xi + 0.5 * self.t) * np.cos(7.0 * xi + 0.4 * self.t)
            
        # Time-varying elliptic shaping with adaptive parameters
        shape_factor = 1.2 + 0.3 * np.sin(0.8 * self.t)
        result += shape_factor * np.sum((x**2) * np.exp(-x**2/5.0))
        
        return result