import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with enhanced exponential decay and chaotic modulation
        r = np.sqrt(np.sum(x**2))
        radial_term = np.exp(-r / 3.0) * (1.0 + 0.7 * np.sin(r * 1.5) * np.cos(r * 0.8))
        
        # Higher-order trigonometric wave interference with varying frequencies
        wave_term = 0.0
        for i in range(self.dim):
            wave_term += np.sin(4.0 * x[i]) * np.cos(3.0 * x[i]) * np.sin(2.0 * x[i])
            wave_term += np.cos(5.0 * x[i]) * np.sin(4.0 * x[i]) * np.cos(3.0 * x[i])
        
        # Cross-dimensional cubic interaction terms for increased complexity
        cubic_term = 0.0
        for i in range(self.dim - 2):
            cubic_term += (x[i] * x[i+1] * x[i+2]) ** 2
        
        # Chaotic coupling with radial distance dependence
        chaos_term = 0.0
        for i in range(self.dim - 1):
            diff = x[i] - x[i+1]
            chaos_term += np.sin(x[i] * x[i+1]) * np.exp(-abs(diff) / (1.0 + r / 10.0))
        
        # Angular-based chaotic modulation with radial dependence
        angle_mod = 0.0
        if self.dim >= 2:
            for i in range(self.dim - 1):
                angle_mod += np.arctan2(x[i+1], x[i]) ** 3
        angular_term = 0.4 * np.sin(angle_mod) * np.cos(angle_mod) * np.exp(-r / 8.0)
        
        # Additional radial symmetry breaking term
        symmetry_break = 0.0
        for i in range(self.dim):
            symmetry_break += (x[i] ** 4) * np.sin(0.5 * r)
        
        # Combine all terms with adjusted weights
        result = radial_term + wave_term + 0.6 * cubic_term + 0.5 * chaos_term + angular_term + 0.3 * symmetry_break
        
        return result