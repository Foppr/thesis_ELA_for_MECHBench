import numpy as np

class TentRadialHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map dynamics with parameter modulation
        f1 = 0.0
        for i in range(self.dim):
            # Tent map with time-varying parameter
            param = 1.5 + 0.5 * np.sin(0.3 * i + 0.2 * np.sum(x**2))
            tent_value = param * np.abs(x[i]) if x[i] < 0.5 else (1 - param) * np.abs(x[i])
            f1 += tent_value * np.exp(-0.1 * x[i]**2)
            
        # Radial conditioning with multi-scale harmonic components
        f2 = 0.0
        r = np.sqrt(np.sum(x**2))
        for i in range(self.dim):
            # Radial harmonic interactions with dimension-dependent scaling
            scale_factor = 1.0 + 0.4 * np.sin(0.4 * i + 0.3 * r)
            radial_term = x[i]**2 * scale_factor * np.exp(-0.05 * r**2)
            f2 += radial_term
            
        # Multi-scale harmonic interactions with chaotic coupling
        f3 = 0.0
        for i in range(self.dim):
            # Chaotic coupling strength based on position and dimension
            coupling_strength = 1.0 + 0.6 * np.sin(0.5 * i + 0.4 * np.sum(x**2))
            harmonic_term = coupling_strength * np.sin(2.0 * x[i])**2 * np.cos(1.5 * x[i])**2
            f3 += harmonic_term
            
        # Cross-dimensional chaotic coupling with phase modulation
        f4 = 0.0
        for i in range(self.dim):
            cross_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    # Chaotic phase shift based on dimension and position
                    phase_shift = 0.3 * np.sin(0.4 * (i + j) + 0.2 * np.sum(x**2))
                    coupling = 1.0 + 0.5 * np.cos(0.3 * (i - j) + 0.3 * np.sum(x**2) + phase_shift)
                    cross_interaction = coupling * x[i] * x[j] * np.exp(-0.03 * (x[i]**2 + x[j]**2))
                    cross_sum += cross_interaction
            f4 += cross_sum
            
        # Saddle-point interactions with chaotic modulation
        f5 = 0.0
        for i in range(self.dim):
            saddle_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    # Chaotic coupling strength with distance dependence
                    dist_factor = 1.0 + 0.3 * np.sin(0.6 * (i - j) + 0.2 * np.sum(x**2))
                    saddle_interaction = dist_factor * np.cos(x[i] - x[j]) * np.exp(-0.02 * (x[i]**2 + x[j]**2))
                    saddle_sum += saddle_interaction
            f5 += saddle_sum
            
        # Boundary-sensitive potential with chaotic decay
        f6 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                # Chaotic boundary factor
                boundary_factor = 1.0 + 0.4 * np.cos(0.3 * i + 0.2 * np.sum(x**2))
                f6 += boundary_factor * (np.exp(-0.3 * (np.abs(x[i]) - 4.0)) + 0.5 * np.exp(-0.6 * (np.abs(x[i]) - 4.0)))
                
        # Polynomial interactions with chaotic coefficient modulation
        f7 = 0.0
        for i in range(self.dim):
            poly_sum = 0.0
            for j in range(i+1, self.dim):
                # Chaotic coefficient based on position and dimension
                coeff = 1.0 + 0.6 * np.sin(0.3 * (i + j) + 0.2 * np.sum(x**2))
                interaction = x[i]**4 * x[j]**2
                poly_sum += coeff * interaction * np.exp(-0.04 * (x[i]**2 + x[j]**2))
            f7 += poly_sum
            
        # Chaotic harmonic resonances with radial modulation
        f8 = 0.0
        for i in range(self.dim):
            # Harmonic components with chaotic phase modulation
            phase_mod = 0.3 * np.sin(0.5 * x[i] + 0.2 * i) + 0.2 * np.cos(0.4 * np.sum(x**2))
            f8 += np.sin(2.0 * x[i] + phase_mod)**3 * np.cos(1.5 * x[i] + phase_mod)**3
            
        # Multi-scale chaotic gradient complexity
        f9 = 0.0
        for i in range(self.dim):
            # Chaotic gradient structure with radial modulation
            chaotic_factor = 1.0 + 0.5 * np.sin(0.5 * i + 0.3 * np.sum(x**2))
            f9 += chaotic_factor * np.exp(-0.1 * x[i]**2) * np.sin(2.5 * x[i])**2
            
        # Tent map with radial potential
        f10 = 0.0
        for i in range(self.dim):
            # Tent map pattern with radial characteristics
            tent_scale = 1.0 + 0.4 * np.sin(0.6 * i + 0.3 * np.sum(x**2))
            f10 += tent_scale * np.cos(tent_scale * x[i])**2
            
        # Chaotic cross-dimensional coupling with radial phase modulation
        f11 = 0.0
        for i in range(self.dim):
            cross_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    phase_shift = 0.5 * np.sin(0.3 * (i + j) + 0.2 * np.sum(x**2))
                    coupling = 1.0 + 0.4 * np.cos(0.4 * (i - j) + 0.3 * np.sum(x**2) + phase_shift)
                    cross_interaction = coupling * x[i] * x[j] * np.exp(-0.03 * (x[i]**2 + x[j]**2))
                    cross_sum += cross_interaction
            f11 += cross_sum
            
        # Chaotic elliptic gradient with harmonic modulation
        f12 = 0.0
        for i in range(self.dim):
            # Chaotic gradient structure with harmonic modulation
            chaotic_factor = 1.0 + 0.5 * np.sin(0.5 * i + 0.3 * np.sum(x**2))
            f12 += chaotic_factor * np.exp(-0.1 * x[i]**2) * np.sin(2.5 * x[i])**2
            
        # Multi-scale chaotic harmonic resonances with radial coupling
        f13 = 0.0
        for i in range(self.dim):
            # Harmonic components with chaotic coupling and dynamic phase
            freq_mod = 2.0 + 0.7 * np.sin(0.4 * i + 0.3 * np.sum(x**2))
            phase_shift = 0.3 * np.cos(0.5 * x[i] + 0.2 * i) + 0.2 * np.sin(0.4 * np.sum(x**2))
            f13 += np.sin(freq_mod * x[i] + phase_shift)**2 * np.cos(freq_mod * x[i] + phase_shift)**2
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13