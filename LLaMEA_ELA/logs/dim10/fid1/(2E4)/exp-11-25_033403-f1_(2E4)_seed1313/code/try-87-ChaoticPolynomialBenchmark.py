import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.poly_degree = 4
        self.sin_frequency = 3.0
        self.radial_factor = 2.0
        self.conditioning_base = 1.5
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with adaptive conditioning
        poly_term = 0.0
        for i in range(self.dim):
            scale = self.conditioning_base ** (i / self.dim)
            poly_term += scale * (x[i] ** self.poly_degree + 0.3 * x[i] ** 6 + 0.1 * x[i] ** 8)
        
        # Sinusoidal radial component with chaotic modulation
        r = np.sqrt(np.sum(x**2))
        sin_radial = np.sin(self.sin_frequency * r) * np.cos(0.5 * r) * np.exp(-0.1 * r)
        radial_term = self.radial_factor * r * sin_radial
        
        # Cross-dimensional interaction with chaotic coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.sin(x[i] * x[j]) * np.cos(0.3 * x[i] + 0.7 * x[j])
                cross_term += interaction * (1 + 0.2 * np.sin(2 * i * j))
        
        # Enhanced harmonic components with varying frequencies and phase shifts
        harmonic_term = 0.0
        for i in range(self.dim):
            freq = self.sin_frequency * (1 + 0.5 * np.sin(i))
            phase_shift = 0.3 * np.cos(i)
            harmonic_term += np.sin(freq * x[i] + phase_shift) * np.cos(0.8 * freq * x[i] + phase_shift)
        
        # Modified barrier terms with enhanced exponential scaling
        barrier_term = 0.0
        for i in range(self.dim):
            barrier = np.exp(2.5 * np.abs(x[i])) * (1 + 0.4 * np.sin(5 * x[i]))
            barrier_term += barrier
            
        # Chaotic noise component with enhanced variability
        noise = 0.08 * np.sum(np.sin(12 * x) ** 2 + 0.5 * np.cos(9 * x) ** 2)
        
        # Global scaling factor with enhanced chaotic variation
        global_scale = 1.0 + 0.3 * np.sin(0.4 * r) * np.cos(0.2 * r)
        
        # Add a new deceptive quadratic component
        deceptive_term = 0.0
        for i in range(self.dim):
            deceptive_term += 0.5 * (x[i] - 2.0)**2 * (1 + 0.1 * np.sin(3 * x[i]))
        
        # Combine all terms
        total = poly_term + radial_term + cross_term + harmonic_term + barrier_term + noise + deceptive_term
        
        return total * global_scale