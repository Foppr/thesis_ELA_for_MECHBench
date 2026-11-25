import numpy as np

class MultiModalSymmetricBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with polynomial growth
        r = np.sqrt(np.sum(x**2))
        radial_term = 0.1 * r**4 + 0.3 * r**3 - 0.2 * r**2 + 0.5 * r
        
        # Trigonometric coupling with varying frequencies
        trig_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                angle = np.arctan2(x[j], x[i])
                trig_coupling += np.sin(3 * angle) * np.cos(5 * angle) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Multi-modal component with multiple peaks
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += np.sin(2 * np.pi * x[i]) * np.cos(3 * np.pi * x[i]) + \
                         0.5 * np.sin(4 * np.pi * x[i])**2 + \
                         0.3 * np.cos(6 * np.pi * x[i])**3
        
        # Adaptive penalty based on distance from center
        penalty = 0.0
        for i in range(self.dim):
            dist_from_center = np.abs(x[i])
            penalty += 2.0 * np.exp(-0.5 * (dist_from_center - 2.0)**2) + \
                      1.5 * np.exp(-0.3 * (dist_from_center - 4.0)**2)
        
        # Cross-dimensional interaction with symmetry
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x[i] * x[j]) / (1.0 + np.abs(x[i] - x[j]))
        
        # Boundary attraction term
        boundary_attraction = 0.0
        for i in range(self.dim):
            boundary_attraction += 0.2 * (5.0 - np.abs(x[i]))**3
        
        # Final function value
        result = radial_term + trig_coupling + multimodal + penalty + cross_term + boundary_attraction
        
        return result