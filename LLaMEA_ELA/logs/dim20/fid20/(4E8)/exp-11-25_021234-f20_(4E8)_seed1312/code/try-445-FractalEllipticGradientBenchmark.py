import numpy as np

class FractalEllipticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-based logistic map pattern with enhanced chaotic dynamics
        f1 = 0.0
        for i in range(self.dim):
            # Logistic map with dimension-dependent control parameter
            r = 3.9 + 0.1 * np.sin(0.7 * i + 0.3 * np.sum(x**2))
            logistic_term = r * x[i] * (1.0 - x[i]**2)
            f1 += logistic_term * np.exp(-0.08 * x[i]**2)
            
        # Adaptive elliptic potential with enhanced eccentricity modulation
        f2 = 0.0
        for i in range(self.dim):
            # Elliptic potential with enhanced dynamic eccentricity
            eccentricity = 1.5 + 0.6 * np.sin(0.4 * i + 0.3 * np.sum(x**2))
            f2 += (x[i]**2 / (1.0 + 0.4 * eccentricity)) * np.exp(-0.07 * x[i]**2)
            
        # Dynamic gradient modulation with multi-scale chaotic components
        f3 = 0.0
        for i in range(self.dim):
            # Chaotic frequency modulation with enhanced complexity
            freq_mod = 1.5 + 0.8 * np.sin(0.5 * i + 0.4 * np.sum(x**2))
            f3 += np.sin(freq_mod * x[i])**3 * np.cos(freq_mod * x[i])**3
            
        # Cross-dimensional coupling with enhanced phase relationships
        f4 = 0.0
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    # Enhanced coupling strength based on position and dimension
                    coupling_strength = 1.5 + 0.7 * np.sin(0.3 * (i - j) + 0.4 * np.sum(x**2))
                    phase_shift = 0.6 * np.cos(0.4 * (i + j) + 0.3 * np.sum(x**2))
                    coupling_interaction = coupling_strength * np.cos(x[i] + x[j] + phase_shift)
                    coupling_sum += coupling_interaction
            f4 += coupling_sum
            
        # Multi-scale saddle-point interactions with enhanced fractal coupling
        f5 = 0.0
        for i in range(self.dim):
            saddle_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    # Enhanced fractal-like coupling strength with distance-dependent modulation
                    dist_factor = 1.5 + 0.4 * np.sin(0.6 * (i - j) + 0.3 * np.sum(x**2))
                    saddle_interaction = dist_factor * np.cos(x[i] - x[j]) * np.exp(-0.03 * (x[i]**2 + x[j]**2))
                    saddle_sum += saddle_interaction
            f5 += saddle_sum
            
        # Boundary-sensitive potential with enhanced fractal decay characteristics
        f6 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                boundary_factor = 1.5 + 0.5 * np.cos(0.4 * i + 0.3 * np.sum(x**2))
                f6 += boundary_factor * (np.exp(-0.4 * (np.abs(x[i]) - 4.0)) + 0.7 * np.exp(-0.8 * (np.abs(x[i]) - 4.0)))
                
        # Polynomial interactions with enhanced fractal coefficient modulation
        f7 = 0.0
        for i in range(self.dim):
            poly_sum = 0.0
            for j in range(i+1, self.dim):
                # Enhanced fractal coefficient based on position and dimension
                coeff = 1.5 + 0.8 * np.sin(0.4 * (i + j) + 0.3 * np.sum(x**2))
                interaction = x[i]**5 * x[j]**3
                poly_sum += coeff * interaction * np.exp(-0.06 * (x[i]**2 + x[j]**2))
            f7 += poly_sum
            
        # Enhanced elliptic harmonics with dynamic phase relationships
        f8 = 0.0
        for i in range(self.dim):
            # Harmonic components with enhanced phase modulation
            phase_mod = 0.5 * np.sin(0.6 * x[i] + 0.3 * i) + 0.3 * np.cos(0.5 * np.sum(x**2))
            f8 += np.sin(3.0 * x[i] + phase_mod)**4 * np.cos(2.0 * x[i] + phase_mod)**4
            
        # Enhanced multi-scale gradient complexity with elliptic modulation
        f9 = 0.0
        for i in range(self.dim):
            # Elliptic gradient modulation with enhanced eccentricity
            eccentricity = 1.5 + 0.7 * np.sin(0.5 * i + 0.4 * np.sum(x**2))
            f9 += (x[i]**2 / (1.0 + 0.5 * eccentricity)) * np.sin(4.0 * x[i])**3
            
        # Enhanced self-similar fractal landscape with elliptic potential
        f10 = 0.0
        for i in range(self.dim):
            # Enhanced fractal pattern with elliptic potential characteristics
            fractal_scale = 1.5 + 0.5 * np.sin(0.7 * i + 0.4 * np.sum(x**2))
            f10 += fractal_scale * np.cos(fractal_scale * x[i])**3
            
        # Enhanced cross-dimensional coupling with elliptic phase modulation
        f11 = 0.0
        for i in range(self.dim):
            cross_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    phase_shift = 0.7 * np.sin(0.4 * (i + j) + 0.3 * np.sum(x**2))
                    coupling = 1.5 + 0.5 * np.cos(0.5 * (i - j) + 0.4 * np.sum(x**2) + phase_shift)
                    cross_interaction = coupling * x[i] * x[j] * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                    cross_sum += cross_interaction
            f11 += cross_sum
            
        # Enhanced adaptive elliptic gradient with fractal complexity
        f12 = 0.0
        for i in range(self.dim):
            # Enhanced fractal gradient structure with elliptic modulation
            fractal_factor = 1.5 + 0.6 * np.sin(0.6 * i + 0.4 * np.sum(x**2))
            f12 += fractal_factor * np.exp(-0.15 * x[i]**2) * np.sin(3.0 * x[i])**3
            
        # Enhanced multi-scale harmonic resonances with elliptic coupling
        f13 = 0.0
        for i in range(self.dim):
            # Enhanced harmonic components with elliptic coupling and dynamic phase
            freq_mod = 2.5 + 0.9 * np.sin(0.5 * i + 0.4 * np.sum(x**2))
            phase_shift = 0.4 * np.cos(0.6 * x[i] + 0.3 * i) + 0.3 * np.sin(0.5 * np.sum(x**2))
            f13 += np.sin(freq_mod * x[i] + phase_shift)**3 * np.cos(freq_mod * x[i] + phase_shift)**3
            
        # Enhanced additional fractal harmonic term with modified coupling
        f14 = 0.0
        for i in range(self.dim):
            # Additional enhanced fractal harmonic term with modified coupling
            coupling_strength = 1.2 + 0.4 * np.sin(0.7 * i + 0.3 * np.sum(x**2))
            f14 += coupling_strength * np.sin(2.0 * x[i])**3 * np.cos(2.0 * x[i])**3
            
        # Additional chaotic fractal component with enhanced complexity
        f15 = 0.0
        for i in range(self.dim):
            # Chaotic fractal component with additional nonlinear interactions
            chaos_factor = 2.0 + 0.8 * np.sin(0.8 * i + 0.4 * np.sum(x**2))
            f15 += chaos_factor * np.sin(chaos_factor * x[i])**2 * np.cos(chaos_factor * x[i])**2
            
        # Improved convergence properties with enhanced regularization
        regularization = 0.01 * np.sum(x**4)
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13 + f14 + f15 + regularization