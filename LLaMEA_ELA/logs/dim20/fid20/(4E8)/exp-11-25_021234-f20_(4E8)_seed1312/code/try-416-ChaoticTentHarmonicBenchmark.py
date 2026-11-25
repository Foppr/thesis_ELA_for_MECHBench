import numpy as np

class ChaoticTentHarmonicBenchmark:
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
            tent_val = param * np.abs(x[i]) if x[i] < 0.5 else (1 - param) * np.abs(x[i])
            f1 += tent_val * np.exp(-0.1 * x[i]**2)
            
        # Radial conditioning with multi-scale harmonic components
        f2 = 0.0
        radius = np.sqrt(np.sum(x**2))
        for i in range(self.dim):
            # Harmonic radial components with dynamic frequency
            freq_mod = 1.0 + 0.6 * np.sin(0.4 * i + 0.3 * radius)
            f2 += (x[i]**2 / (1.0 + 0.3 * freq_mod)) * np.cos(freq_mod * x[i])**2
            
        # Multi-scale harmonic interactions with adaptive coupling
        f3 = 0.0
        for i in range(self.dim):
            harmonic_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    # Adaptive coupling strength based on position and dimension
                    coupling_strength = 1.0 + 0.4 * np.sin(0.2 * (i - j) + 0.3 * radius)
                    phase_shift = 0.5 * np.cos(0.3 * (i + j) + 0.2 * radius)
                    harmonic_interaction = coupling_strength * np.sin(x[i] + x[j] + phase_shift)**2
                    harmonic_sum += harmonic_interaction
            f3 += harmonic_sum
            
        # Saddle-point interactions with chaotic modulation
        f4 = 0.0
        for i in range(self.dim):
            saddle_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    # Chaotic coupling strength with distance-dependent modulation
                    dist_factor = 1.0 + 0.3 * np.sin(0.5 * (i - j) + 0.2 * radius)
                    saddle_interaction = dist_factor * np.tan(x[i] - x[j]) * np.exp(-0.02 * (x[i]**2 + x[j]**2))
                    saddle_sum += saddle_interaction
            f4 += saddle_sum
            
        # Boundary-sensitive potential with chaotic decay
        f5 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                boundary_factor = 1.0 + 0.4 * np.cos(0.3 * i + 0.2 * radius)
                f5 += boundary_factor * (np.exp(-0.3 * (np.abs(x[i]) - 4.0)) + 0.5 * np.exp(-0.6 * (np.abs(x[i]) - 4.0)))
                
        # Polynomial interactions with chaotic coefficient modulation
        f6 = 0.0
        for i in range(self.dim):
            poly_sum = 0.0
            for j in range(i+1, self.dim):
                # Chaotic coefficient based on position and dimension
                coeff = 1.0 + 0.6 * np.sin(0.3 * (i + j) + 0.2 * radius)
                interaction = x[i]**3 * x[j]**2
                poly_sum += coeff * interaction * np.exp(-0.04 * (x[i]**2 + x[j]**2))
            f6 += poly_sum
            
        # Chaotic harmonic resonances with radial modulation
        f7 = 0.0
        for i in range(self.dim):
            # Harmonic components with chaotic phase modulation
            phase_mod = 0.3 * np.sin(0.5 * x[i] + 0.2 * i) + 0.2 * np.cos(0.4 * radius)
            f7 += np.sin(2.0 * x[i] + phase_mod)**3 * np.cos(1.5 * x[i] + phase_mod)**3
            
        # Multi-scale gradient complexity with chaotic modulation
        f8 = 0.0
        for i in range(self.dim):
            # Chaotic gradient structure with radial modulation
            chaos_factor = 1.0 + 0.5 * np.sin(0.5 * i + 0.3 * radius)
            f8 += chaos_factor * np.exp(-0.1 * x[i]**2) * np.cos(2.5 * x[i])**2
            
        # Tent map landscape with harmonic potential
        f9 = 0.0
        for i in range(self.dim):
            # Tent map pattern with harmonic potential characteristics
            tent_scale = 1.0 + 0.4 * np.sin(0.6 * i + 0.3 * radius)
            f9 += tent_scale * np.sin(tent_scale * x[i])**2
            
        # Cross-dimensional coupling with chaotic phase modulation
        f10 = 0.0
        for i in range(self.dim):
            cross_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    phase_shift = 0.5 * np.sin(0.3 * (i + j) + 0.2 * radius)
                    coupling = 1.0 + 0.4 * np.tan(0.4 * (i - j) + 0.3 * radius + phase_shift)
                    cross_interaction = coupling * x[i] * x[j] * np.exp(-0.03 * (x[i]**2 + x[j]**2))
                    cross_sum += cross_interaction
            f10 += cross_sum
            
        # Chaotic elliptic gradient with harmonic complexity
        f11 = 0.0
        for i in range(self.dim):
            # Harmonic gradient structure with chaotic modulation
            chaos_factor = 1.0 + 0.5 * np.cos(0.5 * i + 0.3 * radius)
            f11 += chaos_factor * np.exp(-0.1 * x[i]**2) * np.sin(2.0 * x[i])**2
            
        # Multi-scale chaotic resonances with harmonic coupling
        f12 = 0.0
        for i in range(self.dim):
            # Harmonic components with chaotic coupling and dynamic phase
            freq_mod = 2.0 + 0.7 * np.sin(0.4 * i + 0.3 * radius)
            phase_shift = 0.3 * np.cos(0.5 * x[i] + 0.2 * i) + 0.2 * np.sin(0.4 * radius)
            f12 += np.sin(freq_mod * x[i] + phase_shift)**2 * np.cos(freq_mod * x[i] + phase_shift)**2
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12