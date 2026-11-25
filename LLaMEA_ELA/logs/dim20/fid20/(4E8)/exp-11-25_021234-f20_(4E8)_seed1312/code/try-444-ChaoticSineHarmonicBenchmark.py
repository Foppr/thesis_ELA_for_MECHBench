import numpy as np

class ChaoticSineHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine map component with adaptive scaling
        f1 = 0.0
        for i in range(self.dim):
            # Sine map structure with dimension-dependent scaling
            scale_factor = 3.2 + 0.4 * np.sin(0.6 * i + 0.4 * np.sum(x**2))
            sine_term = np.sin(scale_factor * x[i]) * np.exp(-0.1 * x[i]**2)
            f1 += sine_term
            
        # Radial conditioning with fractal scaling
        f2 = 0.0
        radial_sum = 0.0
        for i in range(self.dim):
            radial_sum += x[i]**2
        radial_term = np.sqrt(radial_sum) / (1.0 + 0.2 * np.sin(0.5 * np.sum(x**2)))
        f2 = radial_term * np.exp(-0.08 * radial_sum)
        
        # Multi-scale harmonic interactions with adaptive coupling
        f3 = 0.0
        for i in range(self.dim):
            # Harmonic components with dynamic frequency modulation
            freq_mod = 1.8 + 0.6 * np.sin(0.5 * i + 0.3 * np.sum(x**2))
            f3 += np.sin(freq_mod * x[i])**2 * np.cos(freq_mod * x[i])**2
            
        # Cross-dimensional coupling with adaptive phase relationships
        f4 = 0.0
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    # Adaptive coupling strength based on distance and dimension
                    coupling_strength = 1.3 + 0.5 * np.sin(0.3 * (i - j) + 0.4 * np.sum(x**2))
                    phase_shift = 0.2 * np.cos(0.4 * (i + j) + 0.3 * np.sum(x**2))
                    coupling_interaction = coupling_strength * np.cos(x[i] + x[j] + phase_shift)
                    coupling_sum += coupling_interaction
            f4 += coupling_sum
            
        # Saddle-point interactions with fractal coupling
        f5 = 0.0
        for i in range(self.dim):
            saddle_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    # Fractal-like coupling strength with distance-dependent modulation
                    dist_factor = 1.1 + 0.3 * np.sin(0.5 * (i - j) + 0.3 * np.sum(x**2))
                    saddle_interaction = dist_factor * np.cos(x[i] - x[j]) * np.exp(-0.04 * (x[i]**2 + x[j]**2))
                    saddle_sum += saddle_interaction
            f5 += saddle_sum
            
        # Boundary-sensitive potential with fractal decay characteristics
        f6 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                boundary_factor = 1.1 + 0.2 * np.cos(0.4 * i + 0.3 * np.sum(x**2))
                f6 += boundary_factor * (np.exp(-0.3 * (np.abs(x[i]) - 4.0)) + 0.5 * np.exp(-0.6 * (np.abs(x[i]) - 4.0)))
                
        # Polynomial interactions with fractal coefficient modulation
        f7 = 0.0
        for i in range(self.dim):
            poly_sum = 0.0
            for j in range(i+1, self.dim):
                # Fractal coefficient based on position and dimension
                coeff = 1.1 + 0.4 * np.sin(0.4 * (i + j) + 0.3 * np.sum(x**2))
                interaction = x[i]**3 * x[j]**2
                poly_sum += coeff * interaction * np.exp(-0.06 * (x[i]**2 + x[j]**2))
            f7 += poly_sum
            
        # Adaptive harmonic components with dynamic phase relationships
        f8 = 0.0
        for i in range(self.dim):
            # Harmonic components with adaptive phase modulation
            phase_mod = 0.3 * np.sin(0.5 * x[i] + 0.3 * i) + 0.2 * np.cos(0.5 * np.sum(x**2))
            f8 += np.sin(2.0 * x[i] + phase_mod)**3 * np.cos(1.5 * x[i] + phase_mod)**3
            
        # Multi-scale gradient complexity with sine modulation
        f9 = 0.0
        for i in range(self.dim):
            # Sine gradient modulation with adaptive eccentricity
            eccentricity = 1.3 + 0.4 * np.sin(0.5 * i + 0.4 * np.sum(x**2))
            f9 += (x[i]**2 / (1.0 + 0.2 * eccentricity)) * np.sin(2.5 * x[i])**2
            
        # Self-similar fractal landscape with sine potential
        f10 = 0.0
        for i in range(self.dim):
            # Fractal pattern with sine potential characteristics
            fractal_scale = 1.1 + 0.3 * np.sin(0.6 * i + 0.4 * np.sum(x**2))
            f10 += fractal_scale * np.cos(fractal_scale * x[i])**2
            
        # Cross-dimensional coupling with sine phase modulation
        f11 = 0.0
        for i in range(self.dim):
            cross_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    phase_shift = 0.5 * np.sin(0.4 * (i + j) + 0.3 * np.sum(x**2))
                    coupling = 1.1 + 0.3 * np.cos(0.5 * (i - j) + 0.4 * np.sum(x**2) + phase_shift)
                    cross_interaction = coupling * x[i] * x[j] * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                    cross_sum += cross_interaction
            f11 += cross_sum
            
        # Adaptive sine gradient with fractal complexity
        f12 = 0.0
        for i in range(self.dim):
            # Fractal gradient structure with sine modulation
            fractal_factor = 1.2 + 0.3 * np.sin(0.5 * i + 0.4 * np.sum(x**2))
            f12 += fractal_factor * np.exp(-0.1 * x[i]**2) * np.sin(2.3 * x[i])**2
            
        # Multi-scale sine resonances with coupling - Modified version
        f13 = 0.0
        for i in range(self.dim):
            # Sine components with coupling and dynamic phase
            freq_mod = 2.0 + 0.5 * np.sin(0.4 * i + 0.4 * np.sum(x**2))
            phase_shift = 0.3 * np.cos(0.5 * x[i] + 0.3 * i) + 0.2 * np.sin(0.5 * np.sum(x**2))
            f13 += np.sin(freq_mod * x[i] + phase_shift)**2 * np.cos(freq_mod * x[i] + phase_shift)**2
            
        # Adding a new term for increased complexity
        f14 = 0.0
        for i in range(self.dim):
            # Additional fractal sine harmonic term with modified coupling
            coupling_strength = 0.8 + 0.3 * np.sin(0.7 * i + 0.3 * np.sum(x**2))
            f14 += coupling_strength * np.sin(1.5 * x[i])**2 * np.cos(1.5 * x[i])**2
            
        # Sine map dynamics for enhanced multimodality
        f15 = 0.0
        for i in range(self.dim):
            # Sine map dynamics with phase modulation
            sine_map = np.sin(3.8 * x[i])
            phase_mod = 0.3 * np.sin(0.4 * i + 0.35 * np.sum(x**2))
            f15 += np.sin(sine_map + phase_mod)**2 * np.exp(-0.08 * x[i]**2)
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14 + f15