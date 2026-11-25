import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Radial component with chaotic oscillations
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = 0.5 * r * (1 + 0.3 * np.sin(20 * r) * np.cos(15 * r))
        
        # Angular components with multiple frequency harmonics
        angular_terms = 0
        for i in range(self.dim):
            angle = np.arctan2(x_norm[i], x_norm[(i+1) % self.dim])
            angular_terms += np.sin(12 * angle) * np.cos(8 * angle) * np.sin(5 * angle)
        
        # Chaotic modulation based on distance from center
        chaos_mod = 0.4 * np.exp(-r**2) * np.sin(30 * r)
        
        # Discontinuous gradient components
        discontinuity = 0
        for i in range(self.dim):
            if x_norm[i] > 0.5:
                discontinuity += 0.3 * (x_norm[i] - 0.5)**2
            elif x_norm[i] < -0.5:
                discontinuity += 0.3 * (x_norm[i] + 0.5)**2
        
        # Cross-dimensional interference with non-linear coupling
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x_norm[i] * x_norm[j]) * (x_norm[i]**2 + x_norm[j]**2)
        
        # Shifted global minimum with asymmetric basin
        shift = 0.2
        shift_term = 0.15 * np.sum((x_norm - shift)**4)
        
        # Combine all terms
        result = radial_term + angular_terms + chaos_mod + discontinuity + cross_term + shift_term
        
        return result