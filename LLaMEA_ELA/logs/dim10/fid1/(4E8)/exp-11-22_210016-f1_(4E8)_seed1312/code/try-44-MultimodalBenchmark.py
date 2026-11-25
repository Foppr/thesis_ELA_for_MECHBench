import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with enhanced exponential decay and chaotic modulation
        r = np.sqrt(np.sum(x**2))
        radial_term = np.exp(-r / 2.5) * (1.0 + 0.8 * np.sin(r * 1.7) * np.cos(r * 0.9))
        
        # Higher-order trigonometric wave interference with varying frequencies
        wave_term = 0.0
        for i in range(self.dim):
            wave_term += np.sin(5.0 * x[i]) * np.cos(4.0 * x[i]) * np.sin(3.0 * x[i])
            wave_term += np.cos(6.0 * x[i]) * np.sin(5.0 * x[i]) * np.cos(4.0 * x[i])
        
        # Cross-dimensional cubic interaction terms for increased complexity
        cubic_term = 0.0
        for i in range(self.dim - 2):
            cubic_term += (x[i] * x[i+1] * x[i+2]) ** 3
        
        # Chaotic coupling with radial distance dependence
        chaos_term = 0.0
        for i in range(self.dim - 1):
            diff = x[i] - x[i+1]
            chaos_term += np.sin(x[i] * x[i+1]) * np.exp(-abs(diff) / (1.5 + r / 12.0))
        
        # Angular-based chaotic modulation with radial dependence
        angle_mod = 0.0
        if self.dim >= 2:
            for i in range(self.dim - 1):
                angle_mod += np.arctan2(x[i+1], x[i]) ** 4
        angular_term = 0.5 * np.sin(angle_mod) * np.cos(angle_mod) * np.exp(-r / 9.0)
        
        # Additional radial symmetry breaking term with higher-order polynomial
        symmetry_break = 0.0
        for i in range(self.dim):
            symmetry_break += (x[i] ** 5) * np.sin(0.6 * r)
        
        # Novel quartic cross-dimensional coupling
        quartic_term = 0.0
        for i in range(self.dim - 3):
            quartic_term += (x[i] * x[i+1] * x[i+2] * x[i+3]) ** 2
        
        # Combined with additional sinusoidal modulation
        final_mod = 0.0
        for i in range(self.dim):
            final_mod += np.sin(2.0 * x[i]) * np.cos(1.5 * x[i]) * np.exp(-r / 4.0)
        
        # Combine all terms with adjusted weights
        result = radial_term + wave_term + 0.7 * cubic_term + 0.6 * chaos_term + angular_term + 0.4 * symmetry_break + 0.3 * quartic_term + 0.2 * final_mod
        
        return result