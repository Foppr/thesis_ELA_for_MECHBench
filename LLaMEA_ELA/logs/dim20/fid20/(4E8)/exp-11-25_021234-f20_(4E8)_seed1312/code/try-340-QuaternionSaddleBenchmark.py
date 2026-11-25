import numpy as np

class QuaternionSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quaternion-based rotational dynamics with time-varying parameters
        f1 = 0.0
        for i in range(self.dim):
            # Generate quaternion components based on position
            q_real = np.cos(0.5 * x[i])
            q_imag1 = np.sin(0.5 * x[i]) * np.cos(x[(i+1) % self.dim])
            q_imag2 = np.sin(0.5 * x[i]) * np.sin(x[(i+1) % self.dim])
            q_imag3 = 0.5 * np.sin(x[i]) * np.cos(0.3 * i)
            
            # Quaternion norm squared
            quat_norm_sq = q_real**2 + q_imag1**2 + q_imag2**2 + q_imag3**2
            
            # Spherical harmonic contribution
            f1 += quat_norm_sq * np.exp(-0.1 * x[i]**2)
            
        # Saddle-point harmonic interactions with elliptic conditioning
        f2 = 0.0
        for i in range(self.dim):
            # Elliptic scaling factors
            a = 1.0 + 0.5 * np.sin(0.4 * i)
            b = 1.0 + 0.3 * np.cos(0.3 * i)
            
            # Saddle-point harmonic term
            saddle_term = (x[i]**2 - a**2) * (x[i]**2 - b**2)
            f2 += saddle_term * np.exp(-0.05 * x[i]**2)
            
        # Time-varying elliptic conditioning with chaotic modulation
        f3 = 0.0
        r = np.sqrt(np.sum(x**2))
        for i in range(self.dim):
            # Chaotic modulation of elliptic parameters
            mod_a = 1.0 + 0.4 * np.sin(0.5 * i + 0.3 * r)
            mod_b = 1.0 + 0.3 * np.cos(0.4 * i + 0.2 * r)
            
            # Elliptic quadratic form
            elliptic_term = (x[i]**2 / mod_a**2) + (x[(i+1) % self.dim]**2 / mod_b**2)
            f3 += elliptic_term * np.exp(-0.1 * x[i]**2)
            
        # Multi-scale harmonic resonances with adaptive coupling
        f4 = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.3 * i + 0.2 * r)
            amp = 1.2 + 0.8 * np.cos(0.4 * i + 0.1 * r)
            
            # Resonant harmonic interaction
            f4 += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Cross-dimensional coupling with rotational invariance
        f5 = 0.0
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    # Rotational invariant coupling
                    rot_invariant = np.cos(x[i] - x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                    coupling_sum += rot_invariant
            f5 += coupling_sum * np.exp(-0.1 * x[i]**2)
            
        # Boundary-sensitive saddle potentials
        f6 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                boundary_factor = 1.0 + 0.5 * np.sin(0.6 * i)
                f6 += boundary_factor * (np.abs(x[i]) - 4.0)**3
            
        # Adaptive polynomial interactions with rotational symmetry
        f7 = 0.0
        for i in range(self.dim):
            poly_sum = 0.0
            for j in range(i+1, self.dim):
                # Rotational symmetric interaction coefficient
                coeff = 1.0 + 0.3 * np.sin(0.2 * (i - j) + 0.1 * r)
                interaction = x[i]**3 * x[j]**3
                poly_sum += coeff * interaction * np.exp(-0.02 * (x[i]**2 + x[j]**2))
            f7 += poly_sum
            
        # Fractal-like rotational structure with multi-scale complexity
        f8 = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.4 * np.sin(0.5 * i + 0.3 * r)
            f8 += scale_factor * np.sin(np.pi * x[i] / (1.0 + 0.2 * r))**3
            
        # Time-varying phase-shifted harmonic components
        f9 = 0.0
        for i in range(self.dim):
            phase_shift = 0.5 * np.sin(0.4 * i + 0.2 * r)
            freq_mod = 1.5 + 0.8 * np.cos(0.3 * i)
            f9 += np.sin(freq_mod * x[i] + phase_shift)**2
            
        # Exponential radial conditioning with rotational modulation
        f10 = 0.0
        for i in range(self.dim):
            modulator = 1.0 + 0.4 * np.sin(0.5 * i + 0.3 * r)
            f10 += modulator * np.exp(-0.1 * x[i]**2) * np.cos(2.0 * x[i])**2
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10