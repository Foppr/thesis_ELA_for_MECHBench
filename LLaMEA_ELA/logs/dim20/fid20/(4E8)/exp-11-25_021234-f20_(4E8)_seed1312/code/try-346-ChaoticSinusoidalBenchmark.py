import numpy as np

class ChaoticSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine-wave interactions with dynamic scaling
        f1 = 0.0
        for i in range(self.dim):
            # Chaotic modulation factor based on position and dimension
            mod_factor = 1.0 + 0.3 * np.sin(0.5 * x[i] + 0.2 * i)
            f1 += mod_factor * np.sin(3.0 * x[i])**2 * np.exp(-0.1 * x[i]**2)
            
        # Dynamic radial conditioning with fractal-like behavior
        f2 = 0.0
        r = np.sqrt(np.sum(x**2))
        for i in range(self.dim):
            # Fractal scaling based on radial distance
            fractal_scale = 1.0 + 0.5 * np.sin(2.0 * r + 0.3 * i)
            f2 += (x[i]**2 / (1.0 + 0.2 * r**2)) * fractal_scale
            
        # Adaptive cross-dimensional couplings with rotational invariance
        f3 = 0.0
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    # Rotational invariant coupling with adaptive strength
                    coupling_strength = 1.0 + 0.4 * np.sin(0.3 * (i - j) + 0.2 * r)
                    rot_invariant = coupling_strength * np.cos(x[i] - x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                    coupling_sum += rot_invariant
            f3 += coupling_sum
            
        # Multi-scale harmonic resonances with time-varying frequencies
        f4 = 0.0
        for i in range(self.dim):
            # Time-varying frequency based on radial position and dimension
            freq = 2.0 + 1.5 * np.sin(0.4 * i + 0.3 * r)
            f4 += np.sin(freq * x[i]) * np.cos(freq * x[i]) * np.exp(-0.05 * x[i]**2)
            
        # Boundary-sensitive potential with exponential decay
        f5 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                boundary_factor = 1.0 + 0.6 * np.sin(0.7 * i)
                f5 += boundary_factor * np.exp(-0.2 * (np.abs(x[i]) - 4.0))
                
        # Polynomial interactions with adaptive coefficients
        f6 = 0.0
        for i in range(self.dim):
            poly_sum = 0.0
            for j in range(i+1, self.dim):
                # Adaptive coefficient based on position and dimension
                coeff = 1.0 + 0.3 * np.sin(0.2 * (i + j) + 0.1 * r)
                interaction = x[i]**2 * x[j]**2
                poly_sum += coeff * interaction * np.exp(-0.03 * (x[i]**2 + x[j]**2))
            f6 += poly_sum
            
        # Fractal-like rotational structure with multi-scale complexity
        f7 = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.4 * np.sin(0.6 * i + 0.3 * r)
            f7 += scale_factor * np.sin(np.pi * x[i] / (1.0 + 0.3 * r))**2
            
        # Phase-shifted harmonic components with chaotic modulation
        f8 = 0.0
        for i in range(self.dim):
            phase_shift = 0.4 * np.sin(0.5 * i + 0.2 * r)
            freq_mod = 1.5 + 0.7 * np.cos(0.3 * i)
            f8 += np.sin(freq_mod * x[i] + phase_shift)**3
            
        # Exponential radial conditioning with adaptive parameters
        f9 = 0.0
        for i in range(self.dim):
            # Adaptive parameter based on position and dimension
            adapt_param = 1.0 + 0.5 * np.sin(0.4 * i + 0.3 * r)
            f9 += adapt_param * np.exp(-0.1 * x[i]**2) * np.cos(2.0 * x[i])**3
            
        # Enhanced chaotic modulation with non-uniform difficulty regions
        f10 = 0.0
        for i in range(self.dim):
            # Non-uniform difficulty factor
            difficulty_factor = 1.0 + 0.8 * np.sin(0.6 * i + 0.4 * r)
            f10 += difficulty_factor * np.sin(2.0 * x[i])**4
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10