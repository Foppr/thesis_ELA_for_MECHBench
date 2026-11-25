import numpy as np

class FractalEllipticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-based self-similarity pattern with adaptive scaling
        f1 = 0.0
        for i in range(self.dim):
            # Self-similar fractal structure with dimension-dependent scaling
            scale_factor = 1.0 + 0.3 * np.sin(0.5 * i + 0.2 * np.sum(x**2))
            fractal_term = np.sin(scale_factor * x[i])**2 + 0.5 * np.cos(scale_factor * x[i])**2
            f1 += fractal_term * np.exp(-0.1 * x[i]**2)
            
        # Adaptive elliptic potential with dynamic eccentricity
        f2 = 0.0
        for i in range(self.dim):
            # Elliptic potential with time-varying eccentricity
            eccentricity = 1.0 + 0.4 * np.sin(0.3 * i + 0.2 * np.sum(x**2))
            f2 += (x[i]**2 / (1.0 + 0.3 * eccentricity)) * np.exp(-0.05 * x[i]**2)
            
        # Dynamic gradient modulation with multi-scale harmonic components
        f3 = 0.0
        for i in range(self.dim):
            # Multi-scale harmonic components with dynamic frequency modulation
            freq_mod = 1.0 + 0.6 * np.sin(0.4 * i + 0.3 * np.sum(x**2))
            f3 += np.sin(freq_mod * x[i])**2 * np.cos(freq_mod * x[i])**2
            
        # Cross-dimensional coupling with adaptive phase relationships
        f4 = 0.0
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    # Adaptive coupling strength based on distance and dimension
                    coupling_strength = 1.0 + 0.5 * np.sin(0.2 * (i - j) + 0.3 * np.sum(x**2))
                    phase_shift = 0.4 * np.cos(0.3 * (i + j) + 0.2 * np.sum(x**2))
                    coupling_interaction = coupling_strength * np.cos(x[i] + x[j] + phase_shift)
                    coupling_sum += coupling_interaction
            f4 += coupling_sum
            
        # Multi-scale saddle-point interactions with fractal coupling
        f5 = 0.0
        for i in range(self.dim):
            saddle_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    # Fractal-like coupling strength with distance-dependent modulation
                    dist_factor = 1.0 + 0.3 * np.sin(0.5 * (i - j) + 0.2 * np.sum(x**2))
                    saddle_interaction = dist_factor * np.cos(x[i] - x[j]) * np.exp(-0.02 * (x[i]**2 + x[j]**2))
                    saddle_sum += saddle_interaction
            f5 += saddle_sum
            
        # Boundary-sensitive potential with fractal decay characteristics
        f6 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                boundary_factor = 1.0 + 0.4 * np.cos(0.3 * i + 0.2 * np.sum(x**2))
                f6 += boundary_factor * (np.exp(-0.3 * (np.abs(x[i]) - 4.0)) + 0.5 * np.exp(-0.6 * (np.abs(x[i]) - 4.0)))
                
        # Polynomial interactions with fractal coefficient modulation
        f7 = 0.0
        for i in range(self.dim):
            poly_sum = 0.0
            for j in range(i+1, self.dim):
                # Fractal coefficient based on position and dimension
                coeff = 1.0 + 0.6 * np.sin(0.3 * (i + j) + 0.2 * np.sum(x**2))
                interaction = x[i]**4 * x[j]**2
                poly_sum += coeff * interaction * np.exp(-0.04 * (x[i]**2 + x[j]**2))
            f7 += poly_sum
            
        # Adaptive elliptic harmonics with dynamic phase relationships
        f8 = 0.0
        for i in range(self.dim):
            # Harmonic components with adaptive phase modulation
            phase_mod = 0.3 * np.sin(0.5 * x[i] + 0.2 * i) + 0.2 * np.cos(0.4 * np.sum(x**2))
            f8 += np.sin(2.0 * x[i] + phase_mod)**3 * np.cos(1.5 * x[i] + phase_mod)**3
            
        # Multi-scale gradient complexity with elliptic modulation
        f9 = 0.0
        for i in range(self.dim):
            # Elliptic gradient modulation with adaptive eccentricity
            eccentricity = 1.0 + 0.5 * np.sin(0.4 * i + 0.3 * np.sum(x**2))
            f9 += (x[i]**2 / (1.0 + 0.4 * eccentricity)) * np.sin(3.0 * x[i])**2
            
        # Self-similar fractal landscape with elliptic potential
        f10 = 0.0
        for i in range(self.dim):
            # Fractal pattern with elliptic potential characteristics
            fractal_scale = 1.0 + 0.4 * np.sin(0.6 * i + 0.3 * np.sum(x**2))
            f10 += fractal_scale * np.cos(fractal_scale * x[i])**2
            
        # Cross-dimensional coupling with elliptic phase modulation
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
            
        # Adaptive elliptic gradient with fractal complexity - Modified version
        f12 = 0.0
        for i in range(self.dim):
            # Fractal gradient structure with elliptic modulation - Slight modification to coefficients
            fractal_factor = 1.0 + 0.5 * np.sin(0.5 * i + 0.3 * np.sum(x**2))
            f12 += fractal_factor * np.exp(-0.1 * x[i]**2) * np.sin(2.5 * x[i])**2
            
        # Multi-scale harmonic resonances with elliptic coupling - Modified version
        f13 = 0.0
        for i in range(self.dim):
            # Harmonic components with elliptic coupling and dynamic phase - Slight modification to frequencies
            freq_mod = 2.0 + 0.7 * np.sin(0.4 * i + 0.3 * np.sum(x**2))
            phase_shift = 0.3 * np.cos(0.5 * x[i] + 0.2 * i) + 0.2 * np.sin(0.4 * np.sum(x**2))
            f13 += np.sin(freq_mod * x[i] + phase_shift)**2 * np.cos(freq_mod * x[i] + phase_shift)**2
            
        # Adding a new term for increased complexity
        f14 = 0.0
        for i in range(self.dim):
            # Additional fractal harmonic term with modified coupling
            coupling_strength = 0.8 + 0.3 * np.sin(0.6 * i + 0.2 * np.sum(x**2))
            f14 += coupling_strength * np.sin(1.5 * x[i])**2 * np.cos(1.5 * x[i])**2
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14