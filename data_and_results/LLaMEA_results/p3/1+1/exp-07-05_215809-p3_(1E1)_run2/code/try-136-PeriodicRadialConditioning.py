import numpy as np

class PeriodicRadialConditioning:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        # Normalize input to [-pi, pi] range
        x_norm = (x - self.bounds.lb) * (2 * np.pi) / (self.bounds.ub - self.bounds.lb) - np.pi
        
        # Radial component with periodic modulation
        r = np.sqrt(np.sum(x**2))
        radial_term = 0.5 * r * (1 + 0.3 * np.sin(3 * r) + 0.2 * np.cos(5 * r))
        
        # Periodic trigonometric components with varying frequencies
        trig_term = 0.0
        for i in range(self.dim):
            freq = 2 + i * 0.5
            trig_term += np.sin(freq * x[i]) * np.cos(freq * x[i]) * np.sin(freq * x[i]**2)
            
        # Adaptive conditioning based on dimension
        conditioning = 0.0
        for i in range(self.dim):
            condition_factor = 1.0 + 0.1 * np.sin(i * 0.3) + 0.05 * np.cos(i * 0.7)
            conditioning += condition_factor * x[i]**2
            
        # Nested local minima with varying depths
        nested_minima = 0.0
        for i in range(self.dim):
            # Create multiple local minima with different positions and depths
            depth = 0.5 + 0.3 * np.sin(i * 0.5)
            position = 1.0 + 0.5 * np.cos(i * 0.3)
            nested_minima += depth * np.exp(-0.5 * (x[i] - position)**2) * np.sin(2 * np.pi * x[i])
            
        # Cross-term interactions with adaptive coupling
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling = 0.3 * np.sin(i * 0.2) * np.cos(j * 0.4)
                cross_terms += coupling * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Fractal-like structure with recursive components
        fractal = 0.0
        for i in range(self.dim):
            fractal += 0.1 * np.sin(7 * x[i]) * np.cos(11 * x[i]) * np.sin(13 * x[i]) * np.cos(17 * x[i])
            
        # Global minimum attraction with polynomial terms
        global_attraction = 0.2 * np.sum(x**4) + 0.1 * np.sum(x**6)
        
        # Combine all components
        f = radial_term + trig_term + conditioning + nested_minima + cross_terms + fractal + global_attraction
        
        return f