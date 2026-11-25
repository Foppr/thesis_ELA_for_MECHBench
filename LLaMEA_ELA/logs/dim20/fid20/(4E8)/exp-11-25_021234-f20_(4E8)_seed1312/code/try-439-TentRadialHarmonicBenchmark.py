import numpy as np

class TentRadialHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map dynamics with radial conditioning and improved convergence
        f1 = 0.0
        for i in range(self.dim):
            # Tent map with dynamic parameter based on position and dimension
            r = 1.8 + 0.2 * np.sin(0.3 * i + 0.2 * np.sum(x**2))
            if x[i] < 0.5:
                tent_value = r * x[i]
            else:
                tent_value = r * (1.0 - x[i])
            f1 += tent_value * np.exp(-0.05 * x[i]**2)
            
        # Radial conditioning with multi-scale harmonic components and better scaling
        f2 = 0.0
        radius = np.sqrt(np.sum(x**2))
        for i in range(self.dim):
            # Harmonic radial component with varying frequency and adaptive scaling
            freq = 1.5 + 1.5 * np.sin(0.4 * i + 0.3 * radius)
            f2 += np.sin(freq * x[i])**2 * np.cos(freq * x[i])**2 * (1.0 + 0.1 * np.sin(0.2 * radius))
            
        # Multi-scale harmonic interactions with dynamic coupling and improved stability
        f3 = 0.0
        for i in range(self.dim):
            interaction_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    # Dynamic coupling strength based on distance and dimension with better normalization
                    coupling_strength = 1.2 + 0.4 * np.sin(0.3 * (i - j) + 0.2 * radius)
                    freq_mod = 1.5 + 0.3 * np.cos(0.5 * (i + j) + 0.3 * radius)
                    interaction = coupling_strength * np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[j])
                    interaction_sum += interaction
            f3 += interaction_sum * (1.0 + 0.05 * np.cos(0.1 * i))
            
        # Cross-dimensional harmonic resonances with adaptive phase shifts and improved complexity
        f4 = 0.0
        for i in range(self.dim):
            resonance_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    phase_shift = 0.3 * np.sin(0.2 * (i + j) + 0.3 * radius)
                    freq_mod = 1.2 + 0.3 * np.cos(0.4 * (i - j) + 0.2 * radius)
                    resonance = np.sin(freq_mod * x[i] + phase_shift) * np.cos(freq_mod * x[j] + phase_shift)
                    resonance_sum += resonance
            f4 += resonance_sum * (1.0 + 0.1 * np.sin(0.3 * i))
            
        # Fractal-like radial potential with chaotic modulation and improved stability
        f5 = 0.0
        for i in range(self.dim):
            # Radial fractal structure with chaotic scaling factor and better convergence
            scale_factor = 1.2 + 0.3 * np.sin(0.5 * i + 0.3 * radius)
            radial_term = np.sin(scale_factor * x[i])**2 + 0.4 * np.cos(scale_factor * x[i])**2
            f5 += radial_term * np.exp(-0.03 * x[i]**2)
            
        # Boundary-sensitive chaotic potential with harmonic decay and improved robustness
        f6 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                boundary_factor = 1.0 + 0.2 * np.cos(0.4 * i + 0.2 * radius)
                f6 += boundary_factor * (np.exp(-0.15 * (np.abs(x[i]) - 4.0)) + 0.2 * np.exp(-0.3 * (np.abs(x[i]) - 4.0)))
                
        # Multi-scale saddle-point interactions with chaotic coupling and improved gradient structure
        f7 = 0.0
        for i in range(self.dim):
            saddle_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    # Chaotic coupling strength with distance-dependent modulation
                    dist_factor = 1.0 + 0.4 * np.sin(0.4 * (i - j) + 0.2 * radius)
                    saddle_interaction = dist_factor * np.cos(x[i] - x[j]) * np.exp(-0.02 * (x[i]**2 + x[j]**2))
                    saddle_sum += saddle_interaction
            f7 += saddle_sum * (1.0 + 0.05 * np.sin(0.2 * i))
            
        # Adaptive radial harmonics with chaotic phase modulation and improved complexity
        f8 = 0.0
        for i in range(self.dim):
            # Harmonic components with chaotic phase modulation and better scaling
            phase_mod = 0.3 * np.sin(0.3 * x[i] + 0.2 * i) + 0.2 * np.cos(0.5 * radius)
            f8 += np.sin(2.5 * x[i] + phase_mod)**2 * np.cos(1.5 * x[i] + phase_mod)**2
            
        # Multi-scale gradient complexity with chaotic modulation and improved convergence
        f9 = 0.0
        for i in range(self.dim):
            # Chaotic gradient structure with radial modulation and better stability
            chaos_factor = 1.0 + 0.5 * np.sin(0.4 * i + 0.3 * radius)
            f9 += chaos_factor * np.exp(-0.08 * x[i]**2) * np.sin(1.5 * x[i])**2
            
        # Self-similar chaotic landscape with radial harmonic potential and improved robustness
        f10 = 0.0
        for i in range(self.dim):
            # Chaotic pattern with radial harmonic characteristics and better convergence
            chaos_scale = 1.0 + 0.4 * np.sin(0.6 * i + 0.3 * radius)
            f10 += chaos_scale * np.cos(chaos_scale * x[i])**2
            
        # Cross-dimensional coupling with chaotic phase relationships and improved stability
        f11 = 0.0
        for i in range(self.dim):
            cross_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    phase_shift = 0.3 * np.sin(0.3 * (i + j) + 0.2 * radius)
                    coupling = 1.0 + 0.4 * np.cos(0.5 * (i - j) + 0.3 * radius + phase_shift)
                    cross_interaction = coupling * x[i] * x[j] * np.exp(-0.03 * (x[i]**2 + x[j]**2))
                    cross_sum += cross_interaction
            f11 += cross_sum * (1.0 + 0.05 * np.sin(0.2 * i))
            
        # Adaptive chaotic gradient with harmonic complexity and improved convergence
        f12 = 0.0
        for i in range(self.dim):
            # Harmonic gradient structure with chaotic modulation and better scaling
            chaos_factor = 1.0 + 0.3 * np.sin(0.5 * i + 0.3 * radius)
            f12 += chaos_factor * np.exp(-0.07 * x[i]**2) * np.sin(2.0 * x[i])**2
            
        # Multi-scale chaotic resonances with radial coupling and improved gradient structure
        f13 = 0.0
        for i in range(self.dim):
            # Harmonic components with radial coupling and chaotic phase
            freq_mod = 1.8 + 0.6 * np.sin(0.4 * i + 0.3 * radius)
            phase_shift = 0.2 * np.cos(0.6 * x[i] + 0.2 * i) + 0.1 * np.sin(0.5 * radius)
            f13 += np.sin(freq_mod * x[i] + phase_shift)**2 * np.cos(freq_mod * x[i] + phase_shift)**2
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13