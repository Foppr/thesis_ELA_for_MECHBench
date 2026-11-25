import numpy as np

class TentRadialHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map dynamics with radial conditioning
        f1 = 0.0
        for i in range(self.dim):
            # Tent map with dynamic parameter based on position
            r = 1.5 + 0.5 * np.sin(0.3 * i + 0.2 * np.sum(x**2))
            if x[i] < 0.5:
                tent_value = r * x[i]
            else:
                tent_value = r * (1.0 - x[i])
            f1 += tent_value * np.exp(-0.1 * x[i]**2)
            
        # Radial conditioning with multi-scale harmonic components
        f2 = 0.0
        radius = np.sqrt(np.sum(x**2))
        for i in range(self.dim):
            # Harmonic radial component with varying frequency
            freq = 2.0 + 1.0 * np.sin(0.4 * i + 0.3 * radius)
            f2 += np.sin(freq * x[i])**2 * np.cos(freq * x[i])**2
            
        # Multi-scale harmonic interactions with dynamic coupling
        f3 = 0.0
        for i in range(self.dim):
            interaction_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    # Dynamic coupling strength based on distance and dimension
                    coupling_strength = 1.0 + 0.6 * np.sin(0.3 * (i - j) + 0.2 * radius)
                    freq_mod = 1.0 + 0.4 * np.cos(0.5 * (i + j) + 0.3 * radius)
                    interaction = coupling_strength * np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[j])
                    interaction_sum += interaction
            f3 += interaction_sum
            
        # Cross-dimensional harmonic resonances with adaptive phase shifts
        f4 = 0.0
        for i in range(self.dim):
            resonance_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    phase_shift = 0.5 * np.sin(0.2 * (i + j) + 0.3 * radius)
                    freq_mod = 1.0 + 0.3 * np.cos(0.4 * (i - j) + 0.2 * radius)
                    resonance = np.sin(freq_mod * x[i] + phase_shift) * np.cos(freq_mod * x[j] + phase_shift)
                    resonance_sum += resonance
            f4 += resonance_sum
            
        # Fractal-like radial potential with chaotic modulation
        f5 = 0.0
        for i in range(self.dim):
            # Radial fractal structure with chaotic scaling factor
            scale_factor = 1.0 + 0.4 * np.sin(0.5 * i + 0.3 * radius)
            radial_term = np.sin(scale_factor * x[i])**2 + 0.5 * np.cos(scale_factor * x[i])**2
            f5 += radial_term * np.exp(-0.05 * x[i]**2)
            
        # Boundary-sensitive chaotic potential with harmonic decay
        f6 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                boundary_factor = 1.0 + 0.3 * np.cos(0.4 * i + 0.2 * radius)
                f6 += boundary_factor * (np.exp(-0.2 * (np.abs(x[i]) - 4.0)) + 0.3 * np.exp(-0.5 * (np.abs(x[i]) - 4.0)))
                
        # Multi-scale saddle-point interactions with chaotic coupling
        f7 = 0.0
        for i in range(self.dim):
            saddle_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    # Chaotic coupling strength with distance-dependent modulation
                    dist_factor = 1.0 + 0.5 * np.sin(0.4 * (i - j) + 0.2 * radius)
                    saddle_interaction = dist_factor * np.cos(x[i] - x[j]) * np.exp(-0.03 * (x[i]**2 + x[j]**2))
                    saddle_sum += saddle_interaction
            f7 += saddle_sum
            
        # Adaptive radial harmonics with chaotic phase modulation
        f8 = 0.0
        for i in range(self.dim):
            # Harmonic components with chaotic phase modulation
            phase_mod = 0.4 * np.sin(0.3 * x[i] + 0.2 * i) + 0.3 * np.cos(0.5 * radius)
            f8 += np.sin(3.0 * x[i] + phase_mod)**2 * np.cos(2.0 * x[i] + phase_mod)**2
            
        # Multi-scale gradient complexity with chaotic modulation
        f9 = 0.0
        for i in range(self.dim):
            # Chaotic gradient structure with radial modulation
            chaos_factor = 1.0 + 0.6 * np.sin(0.4 * i + 0.3 * radius)
            f9 += chaos_factor * np.exp(-0.1 * x[i]**2) * np.sin(2.0 * x[i])**2
            
        # Self-similar chaotic landscape with radial harmonic potential
        f10 = 0.0
        for i in range(self.dim):
            # Chaotic pattern with radial harmonic characteristics
            chaos_scale = 1.0 + 0.5 * np.sin(0.6 * i + 0.3 * radius)
            f10 += chaos_scale * np.cos(chaos_scale * x[i])**2
            
        # Cross-dimensional coupling with chaotic phase relationships
        f11 = 0.0
        for i in range(self.dim):
            cross_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    phase_shift = 0.4 * np.sin(0.3 * (i + j) + 0.2 * radius)
                    coupling = 1.0 + 0.5 * np.cos(0.5 * (i - j) + 0.3 * radius + phase_shift)
                    cross_interaction = coupling * x[i] * x[j] * np.exp(-0.04 * (x[i]**2 + x[j]**2))
                    cross_sum += cross_interaction
            f11 += cross_sum
            
        # Adaptive chaotic gradient with harmonic complexity
        f12 = 0.0
        for i in range(self.dim):
            # Harmonic gradient structure with chaotic modulation
            chaos_factor = 1.0 + 0.4 * np.sin(0.5 * i + 0.3 * radius)
            f12 += chaos_factor * np.exp(-0.1 * x[i]**2) * np.sin(2.5 * x[i])**2
            
        # Multi-scale chaotic resonances with radial coupling
        f13 = 0.0
        for i in range(self.dim):
            # Harmonic components with radial coupling and chaotic phase
            freq_mod = 2.0 + 0.8 * np.sin(0.4 * i + 0.3 * radius)
            phase_shift = 0.3 * np.cos(0.6 * x[i] + 0.2 * i) + 0.2 * np.sin(0.5 * radius)
            f13 += np.sin(freq_mod * x[i] + phase_shift)**2 * np.cos(freq_mod * x[i] + phase_shift)**2
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13