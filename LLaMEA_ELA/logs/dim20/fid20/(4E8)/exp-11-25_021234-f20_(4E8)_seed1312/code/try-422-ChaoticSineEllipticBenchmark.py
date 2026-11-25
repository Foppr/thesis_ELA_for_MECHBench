import numpy as np

class ChaoticSineEllipticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine-wave pattern with adaptive frequency modulation
        f1 = 0.0
        for i in range(self.dim):
            # Chaotic frequency modulation using sine-wave dynamics
            freq_mod = 1.0 + 0.6 * np.sin(0.5 * i + 0.3 * np.sum(x**2))
            f1 += np.sin(freq_mod * x[i])**3 + 0.5 * np.cos(freq_mod * x[i])**3
            
        # Adaptive elliptic potential with dynamic eccentricity
        f2 = 0.0
        for i in range(self.dim):
            # Elliptic potential with time-varying eccentricity
            eccentricity = 1.0 + 0.5 * np.sin(0.4 * i + 0.2 * np.sum(x**2))
            f2 += (x[i]**2 / (1.0 + 0.4 * eccentricity)) * np.exp(-0.05 * x[i]**2)
            
        # Dynamic gradient modulation with chaotic phase relationships
        f3 = 0.0
        for i in range(self.dim):
            # Chaotic phase modulation with multi-scale harmonic components
            phase_mod = 0.4 * np.sin(0.6 * x[i] + 0.2 * i) + 0.3 * np.cos(0.5 * np.sum(x**2))
            f3 += np.sin(2.0 * x[i] + phase_mod)**2 * np.cos(1.5 * x[i] + phase_mod)**2
            
        # Cross-dimensional coupling with chaotic coupling strength
        f4 = 0.0
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    # Chaotic coupling strength based on position and dimension
                    coupling_strength = 1.0 + 0.6 * np.sin(0.3 * (i - j) + 0.4 * np.sum(x**2))
                    phase_shift = 0.5 * np.cos(0.4 * (i + j) + 0.3 * np.sum(x**2))
                    coupling_interaction = coupling_strength * np.cos(x[i] + x[j] + phase_shift)
                    coupling_sum += coupling_interaction
            f4 += coupling_sum
            
        # Multi-scale saddle-point interactions with chaotic coupling
        f5 = 0.0
        for i in range(self.dim):
            saddle_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    # Chaotic-like coupling strength with distance-dependent modulation
                    dist_factor = 1.0 + 0.4 * np.sin(0.6 * (i - j) + 0.3 * np.sum(x**2))
                    saddle_interaction = dist_factor * np.cos(x[i] - x[j]) * np.exp(-0.03 * (x[i]**2 + x[j]**2))
                    saddle_sum += saddle_interaction
            f5 += saddle_sum
            
        # Boundary-sensitive potential with chaotic decay characteristics
        f6 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                boundary_factor = 1.0 + 0.5 * np.cos(0.4 * i + 0.3 * np.sum(x**2))
                f6 += boundary_factor * (np.exp(-0.4 * (np.abs(x[i]) - 4.0)) + 0.6 * np.exp(-0.7 * (np.abs(x[i]) - 4.0)))
                
        # Polynomial interactions with chaotic coefficient modulation
        f7 = 0.0
        for i in range(self.dim):
            poly_sum = 0.0
            for j in range(i+1, self.dim):
                # Chaotic coefficient based on position and dimension
                coeff = 1.0 + 0.7 * np.sin(0.4 * (i + j) + 0.3 * np.sum(x**2))
                interaction = x[i]**3 * x[j]**3
                poly_sum += coeff * interaction * np.exp(-0.05 * (x[i]**2 + x[j]**2))
            f7 += poly_sum
            
        # Chaotic elliptic harmonics with dynamic phase relationships
        f8 = 0.0
        for i in range(self.dim):
            # Harmonic components with chaotic phase modulation
            phase_mod = 0.4 * np.sin(0.6 * x[i] + 0.3 * i) + 0.3 * np.cos(0.5 * np.sum(x**2))
            f8 += np.sin(3.0 * x[i] + phase_mod)**3 * np.cos(2.0 * x[i] + phase_mod)**3
            
        # Multi-scale gradient complexity with chaotic modulation
        f9 = 0.0
        for i in range(self.dim):
            # Chaotic gradient modulation with elliptic characteristics
            eccentricity = 1.0 + 0.6 * np.sin(0.5 * i + 0.4 * np.sum(x**2))
            f9 += (x[i]**2 / (1.0 + 0.5 * eccentricity)) * np.sin(3.5 * x[i])**2
            
        # Chaotic fractal landscape with elliptic potential
        f10 = 0.0
        for i in range(self.dim):
            # Chaotic pattern with elliptic potential characteristics
            chaotic_scale = 1.0 + 0.5 * np.sin(0.7 * i + 0.4 * np.sum(x**2))
            f10 += chaotic_scale * np.cos(chaotic_scale * x[i])**3
            
        # Cross-dimensional coupling with chaotic phase modulation
        f11 = 0.0
        for i in range(self.dim):
            cross_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    phase_shift = 0.6 * np.sin(0.4 * (i + j) + 0.3 * np.sum(x**2))
                    coupling = 1.0 + 0.5 * np.cos(0.5 * (i - j) + 0.4 * np.sum(x**2) + phase_shift)
                    cross_interaction = coupling * x[i] * x[j] * np.exp(-0.04 * (x[i]**2 + x[j]**2))
                    cross_sum += cross_interaction
            f11 += cross_sum
            
        # Chaotic elliptic gradient with multi-scale complexity
        f12 = 0.0
        for i in range(self.dim):
            # Chaotic gradient structure with elliptic modulation
            chaotic_factor = 1.0 + 0.6 * np.sin(0.6 * i + 0.4 * np.sum(x**2))
            f12 += chaotic_factor * np.exp(-0.15 * x[i]**2) * np.sin(3.0 * x[i])**3
            
        # Multi-scale chaotic resonances with elliptic coupling
        f13 = 0.0
        for i in range(self.dim):
            # Harmonic components with chaotic coupling and dynamic phase
            freq_mod = 2.5 + 0.8 * np.sin(0.5 * i + 0.4 * np.sum(x**2))
            phase_shift = 0.4 * np.cos(0.6 * x[i] + 0.3 * i) + 0.3 * np.sin(0.5 * np.sum(x**2))
            f13 += np.sin(freq_mod * x[i] + phase_shift)**3 * np.cos(freq_mod * x[i] + phase_shift)**3
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13