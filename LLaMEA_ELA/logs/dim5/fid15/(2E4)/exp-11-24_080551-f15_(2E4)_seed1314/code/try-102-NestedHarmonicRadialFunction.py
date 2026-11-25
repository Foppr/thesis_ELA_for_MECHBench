import numpy as np

class NestedHarmonicRadialFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Base harmonic oscillation with nested frequencies
        result = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(i * 0.3)
            amp = 1.0 + 0.5 * np.cos(i * 0.7)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
            
        # Radial basis function with adaptive centers and widths
        for i in range(self.dim):
            center = np.sin(i * 0.5) + 0.5 * np.cos(i * 0.3)
            width = 1.0 + 0.3 * np.sin(i * 0.8)
            radial_term = np.exp(-width * (x[i] - center)**2)
            result += 0.5 * radial_term
            
        # Nested harmonic interactions with varying coupling strengths
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                coupling = 0.3 + 0.2 * np.sin(i * j * 0.2)
                freq_ratio = 1.0 + 0.5 * np.cos(i + j)
                interaction = np.sin(freq_ratio * x[i]) * np.cos(freq_ratio * x[j])
                result += coupling * interaction
                
        # Multi-scale radial components with different decay rates
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = abs(x[i] - x[j])
                radial_decay = np.exp(-0.5 * dist**2) + 0.3 * np.exp(-dist)
                result += 0.2 * radial_decay
                
        # Adaptive conditioning with dynamic scaling
        condition_factor = 1.0
        for i in range(self.dim):
            condition_factor *= (1.0 + 0.2 * np.abs(x[i]))
        result *= condition_factor
        
        # High-frequency modulated components
        for i in range(self.dim):
            mod_freq = 10.0 + 5.0 * np.sin(i * 0.4)
            mod_amp = 0.8 + 0.2 * np.cos(i * 0.6)
            result += mod_amp * np.sin(mod_freq * x[i]) * np.cos(mod_freq * x[i] * 0.3)
            
        # Polynomial coupling with exponential weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_term = (x[i]**2) * (x[j]**3) + (x[j]**2) * (x[i]**3)
                weight = np.exp(-0.1 * (x[i]**2 + x[j]**2))
                result += 0.15 * poly_term * weight
                
        # Nested harmonic with varying amplitudes and phases
        for i in range(self.dim):
            amp = 1.5 + 0.5 * np.sin(i * 0.9)
            phase = 0.5 * np.cos(i * 0.4)
            result += amp * np.sin(x[i] + phase)**3
            
        # Cross-dimensional coupling with distance-dependent weights
        total_dist = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                total_dist += abs(x[i] - x[j])
                
        weight_factor = 1.0 / (1.0 + 0.1 * total_dist)
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x[i] * x[j]) * np.cos(x[i] + x[j])
                result += 0.25 * coupling * weight_factor
                
        return result