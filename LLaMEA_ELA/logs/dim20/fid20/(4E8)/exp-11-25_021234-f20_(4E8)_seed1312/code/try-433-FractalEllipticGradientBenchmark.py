import numpy as np

class FractalEllipticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-based self-similarity pattern with multi-scale complexity
        f1 = 0.0
        for i in range(self.dim):
            # Self-similar fractal component with dimension-dependent scaling
            scale_factor = 1.0 + 0.3 * np.sin(0.5 * i + 0.2 * np.sum(x**2))
            fractal_term = scale_factor * np.sin(3.0 * x[i] + 0.1 * np.sum(x**2))**2
            f1 += fractal_term
            
        # Adaptive elliptic potential with dynamic conditioning
        f2 = 0.0
        for i in range(self.dim):
            # Elliptic potential with adaptive eccentricity
            eccentricity = 1.0 + 0.5 * np.cos(0.4 * i + 0.3 * np.sum(x**2))
            elliptic_term = x[i]**2 * eccentricity + 0.1 * x[i]**4
            f2 += elliptic_term
            
        # Dynamic gradient modulation with phase shifts
        f3 = 0.0
        for i in range(self.dim):
            # Phase-shifted gradient component with dynamic amplitude
            amplitude = 1.0 + 0.4 * np.sin(0.6 * i + 0.2 * np.sum(x**2))
            phase_shift = 0.3 * np.cos(0.5 * x[i] + 0.1 * i)
            gradient_term = amplitude * np.sin(x[i] + phase_shift)**2
            f3 += gradient_term
            
        # Modified coupling strengths with chaotic modulation
        f4 = 0.0
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    # Chaotic coupling strength based on position and dimension
                    coupling_strength = 1.0 + 0.6 * np.sin(0.4 * (i + j) + 0.3 * np.sum(x**2))
                    interaction = coupling_strength * x[i] * x[j] * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                    coupling_sum += interaction
            f4 += coupling_sum
            
        # Phase shift modulation with radial dependence
        f5 = 0.0
        for i in range(self.dim):
            phase_mod = 0.5 * np.sin(0.3 * x[i] + 0.2 * np.sum(x**2))
            radial_factor = 1.0 + 0.3 * np.cos(0.4 * np.sum(x**2))
            f5 += radial_factor * np.cos(x[i] + phase_mod)**2
            
        # Multi-scale harmonic interactions with frequency modulation
        f6 = 0.0
        for i in range(self.dim):
            freq_mod = 2.0 + 0.8 * np.sin(0.5 * i + 0.3 * np.sum(x**2))
            harmonic_term = np.sin(freq_mod * x[i])**2 * np.cos(freq_mod * x[i])**2
            f6 += harmonic_term
            
        # Adaptive elliptic potential with radial coupling
        f7 = 0.0
        r = np.sqrt(np.sum(x**2))
        for i in range(self.dim):
            eccentricity = 1.0 + 0.4 * np.sin(0.3 * i + 0.2 * r)
            elliptic_term = x[i]**2 * eccentricity + 0.1 * x[i]**4
            f7 += elliptic_term
            
        # Chaotic gradient structure with multi-scale complexity
        f8 = 0.0
        for i in range(self.dim):
            chaotic_factor = 1.0 + 0.5 * np.sin(0.4 * i + 0.3 * np.sum(x**2))
            gradient_term = chaotic_factor * np.exp(-0.1 * x[i]**2) * np.sin(2.0 * x[i])**2
            f8 += gradient_term
            
        # Fractal self-similarity with radial modulation
        f9 = 0.0
        for i in range(self.dim):
            fractal_factor = 1.0 + 0.3 * np.cos(0.5 * x[i] + 0.2 * i)
            radial_mod = 1.0 + 0.4 * np.sin(0.3 * np.sum(x**2))
            f9 += fractal_factor * radial_mod * np.sin(3.0 * x[i])**2
            
        # Multi-scale coupling with dynamic phase shifts
        f10 = 0.0
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    phase_shift = 0.4 * np.sin(0.3 * (i + j) + 0.2 * np.sum(x**2))
                    coupling = 1.0 + 0.5 * np.cos(0.4 * (i - j) + 0.3 * np.sum(x**2) + phase_shift)
                    interaction = coupling * x[i] * x[j] * np.exp(-0.04 * (x[i]**2 + x[j]**2))
                    coupling_sum += interaction
            f10 += coupling_sum
            
        # Adaptive elliptic with harmonic modulation
        f11 = 0.0
        for i in range(self.dim):
            eccentricity = 1.0 + 0.6 * np.sin(0.5 * i + 0.3 * np.sum(x**2))
            harmonic_mod = 1.0 + 0.4 * np.cos(0.4 * x[i] + 0.2 * i)
            f11 += eccentricity * harmonic_mod * (x[i]**2 + 0.1 * x[i]**4)
            
        # Chaotic coupling with radial potential
        f12 = 0.0
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    coupling_strength = 1.0 + 0.7 * np.sin(0.3 * (i + j) + 0.2 * np.sum(x**2))
                    interaction = coupling_strength * x[i] * x[j] * np.exp(-0.03 * (x[i]**2 + x[j]**2))
                    coupling_sum += interaction
            f12 += coupling_sum
            
        # Fractal gradient with dynamic modulation
        f13 = 0.0
        for i in range(self.dim):
            fractal_factor = 1.0 + 0.5 * np.sin(0.6 * i + 0.3 * np.sum(x**2))
            gradient_term = fractal_factor * np.exp(-0.1 * x[i]**2) * np.sin(2.5 * x[i])**2
            f13 += gradient_term
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13