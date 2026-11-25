import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.poly_degree = 4
        self.sin_frequency = 2.5
        self.radial_factor = 1.5
        self.conditioning_base = 1.3
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with modified conditioning
        poly_term = 0.0
        for i in range(self.dim):
            scale = self.conditioning_base ** (i / self.dim)
            poly_term += scale * (0.8 * x[i] ** self.poly_degree + 0.2 * x[i] ** 6 + 0.05 * x[i] ** 8)
        
        # Sinusoidal radial component with modified frequency
        r = np.sqrt(np.sum(x**2))
        sin_radial = np.sin(self.sin_frequency * r) * np.cos(0.4 * r) * np.exp(-0.15 * r)
        radial_term = self.radial_factor * r * sin_radial
        
        # Cross-dimensional interaction with modified coupling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = np.sin(0.8 * x[i] * x[j]) * np.cos(0.2 * x[i] + 0.8 * x[j])
                cross_term += interaction * (1 + 0.3 * np.sin(1.5 * i * j))
        
        # Harmonic components with altered frequencies
        harmonic_term = 0.0
        for i in range(self.dim):
            freq = self.sin_frequency * (1 + 0.3 * np.sin(i))
            phase_shift = 0.2 * np.cos(i)
            harmonic_term += np.sin(freq * x[i] + phase_shift) * np.cos(0.7 * freq * x[i] + phase_shift)
        
        # Modified barrier terms with different scaling
        barrier_term = 0.0
        for i in range(self.dim):
            barrier = np.exp(3.0 * np.abs(x[i])) * (1 + 0.3 * np.sin(4 * x[i]))
            barrier_term += barrier
            
        # Chaotic noise component with modified amplitude
        noise = 0.06 * np.sum(np.sin(10 * x) ** 2 + 0.4 * np.cos(7 * x) ** 2)
        
        # Global scaling factor with different chaotic variation
        global_scale = 1.0 + 0.2 * np.sin(0.3 * r) * np.cos(0.15 * r)
        
        # Add a new deceptive quadratic component with modified parameters
        deceptive_term = 0.0
        for i in range(self.dim):
            deceptive_term += 0.3 * (x[i] - 1.5)**2 * (1 + 0.15 * np.sin(2.5 * x[i]))
        
        # Combine all terms
        total = poly_term + radial_term + cross_term + harmonic_term + barrier_term + noise + deceptive_term
        
        return total * global_scale