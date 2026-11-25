import numpy as np

class QuaternionSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic quaternion-based rotational dynamics with adaptive frequency
        f1 = 0.0
        for i in range(self.dim):
            # Chaos-inducing quaternion-like rotation with time-dependent frequency
            freq = 1.0 + 0.3 * np.sin(0.5 * i + 0.2 * np.sum(x**2))
            angle = freq * x[i] + 0.4 * np.sin(0.7 * i)
            rot_factor = np.cos(angle)**2 + np.sin(angle)**2
            f1 += rot_factor * np.sin(3.0 * x[i])**2 * np.exp(-0.08 * x[i]**2)
            
        # Adaptive radial conditioning with chaotic modulation
        f2 = 0.0
        r = np.sqrt(np.sum(x**2))
        for i in range(self.dim):
            # Radial conditioning with chaotic parameter modulation
            rad_param = 1.0 + 0.5 * np.sin(0.3 * i + 0.4 * r + 0.2 * np.cos(r))
            f2 += (x[i]**2 / (1.0 + 0.2 * r**2)) * np.cos(rad_param * x[i])**2
            
        # Multi-scale saddle-point interactions with chaotic coupling
        f3 = 0.0
        for i in range(self.dim):
            saddle_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    # Chaotic coupling strength with phase modulation
                    coupling_strength = 1.0 + 0.4 * np.sin(0.3 * (i - j) + 0.2 * r + 0.1 * np.sin(r))
                    saddle_interaction = coupling_strength * np.cos(x[i] + x[j]) * np.exp(-0.03 * (x[i]**2 + x[j]**2))
                    saddle_sum += saddle_interaction
            f3 += saddle_sum
            
        # Multi-scale harmonic resonances with chaotic phase relationships
        f4 = 0.0
        for i in range(self.dim):
            # Chaotic phase modulation based on position and radial distance
            phase_mod = np.sin(0.6 * x[i] + 0.3 * i) + 0.4 * np.cos(0.5 * r) + 0.2 * np.sin(r)
            f4 += np.sin(2.5 * x[i] + phase_mod)**2 * np.cos(1.8 * x[i] + phase_mod)**2
            
        # Boundary-sensitive potential with chaotic decay
        f5 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                boundary_factor = 1.0 + 0.3 * np.sin(0.7 * i + 0.3 * r)
                f5 += boundary_factor * (np.exp(-0.25 * (np.abs(x[i]) - 4.0)) + 0.6 * np.exp(-0.5 * (np.abs(x[i]) - 4.0)))
                
        # Polynomial interactions with chaotic coefficients
        f6 = 0.0
        for i in range(self.dim):
            poly_sum = 0.0
            for j in range(i+1, self.dim):
                # Chaotic coefficient based on position and dimension
                coeff = 1.0 + 0.5 * np.sin(0.4 * (i + j) + 0.3 * r + 0.2 * np.cos(r))
                interaction = x[i]**3 * x[j]**3
                poly_sum += coeff * interaction * np.exp(-0.03 * (x[i]**2 + x[j]**2))
            f6 += poly_sum
            
        # Fractal-like structure with chaotic rotational symmetry
        f7 = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.4 * np.sin(0.8 * i + 0.5 * r + 0.3 * np.cos(r))
            f7 += scale_factor * np.cos(np.pi * x[i] / (1.0 + 0.3 * r))**3
            
        # Chaotic harmonic components with phase-shifted modulation
        f8 = 0.0
        for i in range(self.dim):
            phase_shift = 0.4 * np.sin(0.7 * i + 0.3 * r) + 0.2 * np.cos(0.5 * r) + 0.1 * np.sin(r)
            freq_mod = 2.5 + 0.9 * np.sin(0.6 * i + 0.4 * r)
            f8 += np.sin(freq_mod * x[i] + phase_shift)**4
            
        # Chaotic radial conditioning with quaternion-based parameters
        f9 = 0.0
        for i in range(self.dim):
            # Chaotic parameter based on position and dimension
            adapt_param = 1.0 + 0.7 * np.sin(0.6 * i + 0.4 * r + 0.3 * np.cos(r))
            f9 += adapt_param * np.exp(-0.12 * x[i]**2) * np.sin(1.8 * x[i])**2
            
        # Enhanced chaotic rotational complexity with multi-dimensional coupling
        f10 = 0.0
        for i in range(self.dim):
            # Chaotic difficulty factor with radial modulation
            difficulty_factor = 1.0 + 0.8 * np.sin(0.9 * i + 0.6 * r + 0.4 * np.cos(r))
            f10 += difficulty_factor * np.cos(2.5 * x[i])**3
            
        # Add improved gradient structure with additional chaotic components
        f11 = 0.0
        for i in range(self.dim):
            # Enhanced gradient complexity through higher-order chaotic interactions
            grad_complexity = 1.0 + 0.6 * np.sin(0.8 * i + 0.5 * r + 0.3 * np.cos(r) + 0.2 * np.sin(2.0 * r))
            f11 += grad_complexity * np.sin(4.0 * x[i])**2 * np.exp(-0.1 * x[i]**2)
            
        # Cross-dimensional coupling with chaotic phase shifts
        f12 = 0.0
        for i in range(self.dim):
            cross_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    phase_shift = 0.5 * np.sin(0.4 * (i + j) + 0.3 * r)
                    coupling = 1.0 + 0.3 * np.cos(0.6 * (i - j) + 0.2 * r + phase_shift)
                    cross_interaction = coupling * x[i] * x[j] * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                    cross_sum += cross_interaction
            f12 += cross_sum
            
        # Modified chaotic components for improved benchmark characteristics
        f13 = 0.0
        for i in range(self.dim):
            # Slight modification to coupling strengths and phase shifts
            mod_coupling = 1.0 + 0.45 * np.sin(0.35 * (i - self.dim//2) + 0.25 * r + 0.15 * np.sin(r))
            f13 += mod_coupling * np.cos(x[i] + 0.5 * x[(i+1)%self.dim]) * np.exp(-0.04 * (x[i]**2 + x[(i+1)%self.dim]**2))
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11 + f12 + f13