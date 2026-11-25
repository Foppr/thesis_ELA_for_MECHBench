import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with enhanced exponential decay and chaotic modulation
        r = np.sqrt(np.sum(x**2))
        radial_term = np.exp(-r / 2.0) * (1.0 + 0.9 * np.sin(r * 2.0) * np.cos(r * 0.7))
        
        # Higher-order trigonometric wave interference with varying frequencies
        wave_term = 0.0
        for i in range(self.dim):
            wave_term += np.sin(6.0 * x[i]) * np.cos(3.5 * x[i]) * np.sin(2.5 * x[i])
            wave_term += np.cos(7.0 * x[i]) * np.sin(4.5 * x[i]) * np.cos(3.5 * x[i])
        
        # Cross-dimensional cubic interaction terms for increased complexity
        cubic_term = 0.0
        for i in range(self.dim - 2):
            cubic_term += (x[i] * x[i+1] * x[i+2]) ** 4
        
        # Chaotic coupling with radial distance dependence
        chaos_term = 0.0
        for i in range(self.dim - 1):
            diff = x[i] - x[i+1]
            chaos_term += np.sin(x[i] * x[i+1]) * np.exp(-abs(diff) / (2.0 + r / 10.0))
        
        # Angular-based chaotic modulation with radial dependence
        angle_mod = 0.0
        if self.dim >= 2:
            for i in range(self.dim - 1):
                angle_mod += np.arctan2(x[i+1], x[i]) ** 5
        angular_term = 0.6 * np.sin(angle_mod) * np.cos(angle_mod) * np.exp(-r / 8.0)
        
        # Additional radial symmetry breaking term with higher-order polynomial
        symmetry_break = 0.0
        for i in range(self.dim):
            symmetry_break += (x[i] ** 6) * np.sin(0.7 * r)
        
        # Novel quartic cross-dimensional coupling
        quartic_term = 0.0
        for i in range(self.dim - 3):
            quartic_term += (x[i] * x[i+1] * x[i+2] * x[i+3]) ** 2.5
        
        # Combined with additional sinusoidal modulation
        final_mod = 0.0
        for i in range(self.dim):
            final_mod += np.sin(2.5 * x[i]) * np.cos(1.8 * x[i]) * np.exp(-r / 3.5)
        
        # Combine all terms with adjusted weights
        result = radial_term + wave_term + 0.8 * cubic_term + 0.7 * chaos_term + angular_term + 0.5 * symmetry_break + 0.4 * quartic_term + 0.3 * final_mod
        
        return result