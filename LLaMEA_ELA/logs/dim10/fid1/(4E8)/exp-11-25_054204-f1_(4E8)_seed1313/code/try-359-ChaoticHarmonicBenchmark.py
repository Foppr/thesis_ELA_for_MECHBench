import numpy as np

class ChaoticHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute spherical harmonic coefficients
        self.harmonic_coeffs = np.array([np.sin(i * 0.7) * np.cos(i * 0.5) for i in range(1, dim + 1)])
        # Initialize chaotic parameters
        self.chebyshev_params = np.array([0.8 + 0.2 * np.sin(i * 0.3) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base spherical term
        f1 = np.sum(x**2)
        
        # Chaotic tent map component with adaptive scaling
        f2 = 0.0
        for i in range(self.dim):
            # Tent map dynamics with parameter modulation
            tent_map = 1.0 - 2.0 * abs(x[i] - np.mean(x))
            chaotic_factor = 0.5 + 0.5 * np.tanh(2.0 * x[i])
            f2 += chaotic_factor * tent_map * np.sin(3.0 * x[i])
        
        # Spherical harmonic interactions with dynamic exponents
        f3 = 0.0
        for i in range(self.dim):
            # Spherical harmonic expansion with variable degree
            degree = int(1 + abs(x[i]) % 4)
            harmonic_term = np.sum([self.harmonic_coeffs[j] * np.sin((j+1) * x[i]) 
                                  for j in range(min(degree, self.dim))])
            f3 += harmonic_term * np.exp(-0.5 * (x[i]**2))
        
        # Chebyshev polynomial chaos with adaptive weights
        f4 = 0.0
        for i in range(self.dim):
            cheby_poly = np.cos(self.chebyshev_params[i] * np.arccos(np.clip(x[i]/5.0, -1.0, 1.0)))
            f4 += self.chebyshev_params[i] * cheby_poly * np.cos(2.0 * x[i])
        
        # Adaptive gradient modulation with fractal-like scaling
        f5 = 0.0
        for i in range(self.dim):
            grad_mod = 1.0 + 0.3 * np.sin(x[i] * 0.5) * np.cos(x[i] * 0.7)
            f5 += grad_mod * np.sin(2.0 * x[i]) * np.exp(-0.1 * abs(x[i]))
        
        # Multi-scale radial interaction with chaotic coupling
        f6 = 0.0
        for i in range(self.dim):
            radial_dist = np.sum((x - x[i])**2)
            chaotic_coupling = np.sin(0.3 * np.sum(x)) * np.cos(0.4 * x[i])
            f6 += 0.8 * np.exp(-radial_dist / (1.0 + 0.5 * abs(x[i]))) * chaotic_coupling
        
        # Dynamically scaled polynomial with harmonic modulation
        f7 = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.2 * np.sin(i * 0.4) * np.cos(i * 0.6)
            f7 += scale_factor * (x[i]**3) * np.sin(2.5 * x[i])
        
        # Fractal-inspired radial component with variable dimensionality
        f8 = 0.0
        for i in range(self.dim):
            fractal_dim = 1.5 + 0.5 * np.sin(i * 0.2)
            f8 += np.exp(-np.sum(x**2) / (2.0 * fractal_dim)) * np.cos(3.0 * x[i])
        
        # Cross-dimensional chaotic interaction with phase modulation
        f9 = 0.0
        for i in range(self.dim - 1):
            phase_shift = 0.5 * np.sin(i * 0.8 + np.sum(x) * 0.1)
            interaction = np.sin(x[i] + x[i+1] + phase_shift) * np.cos(0.3 * (x[i] - x[i+1]))
            f9 += interaction * np.exp(-0.2 * abs(x[i] - x[i+1]))
        
        # Adaptive power-law scaling with chaotic frequency modulation
        f10 = 0.0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.4 * np.sin(0.5 * x[i] + i * 0.3)
            f10 += freq_mod * (x[i]**2.5) * np.exp(-0.3 * abs(x[i]))
        
        # Multi-peak chaotic component with dynamic positioning
        f11 = 0.0
        for i in range(self.dim):
            peak_pos = 3.0 * np.sin(i * 0.6 + np.sum(x) * 0.2)
            f11 += 0.7 * np.exp(-((x[i] - peak_pos)**2) / 1.5) * np.sin(4.0 * x[i])
        
        # Final scaling factor based on chaotic dynamics and dimensionality
        chaos_factor = 1.0 + 0.5 * np.sin(np.sum(x) * 0.3) * np.cos(np.sum(x) * 0.7)
        scale_factor = chaos_factor * (1.0 + 0.3 * np.log(self.dim + 1))
        
        # Final function with all components
        return scale_factor * (f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10 + f11)