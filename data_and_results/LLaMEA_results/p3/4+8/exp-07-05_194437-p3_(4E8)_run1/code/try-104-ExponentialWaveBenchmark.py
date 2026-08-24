import numpy as np

class ExponentialWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Precompute random coefficients for wave interference
        self.wave_coeffs = np.random.uniform(0.5, 2.0, dim)
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        self.decay_rates = np.random.uniform(0.1, 0.5, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay potential component
        decay_potential = 0.0
        for i in range(self.dim):
            decay_potential += np.exp(-self.decay_rates[i] * np.abs(x[i])) * np.sin(self.wave_coeffs[i] * x[i] + self.phase_shifts[i])
        
        # Trigonometric wave interference component
        wave_interference = 0.0
        for i in range(self.dim):
            wave_interference += np.cos(self.wave_coeffs[i] * x[i] + self.phase_shifts[i]) * np.sin(self.wave_coeffs[i] * x[i] * 2 + self.phase_shifts[i] * 2)
        
        # Cross-dimensional coupling through adaptive conditioning
        conditioning = 1.0
        for i in range(self.dim):
            conditioning *= (1.0 + 0.1 * np.sin(x[i] * 0.5) * np.cos(x[i] * 0.3))
        
        # Multi-scale periodic component
        periodic_component = 0.0
        for i in range(self.dim):
            period = 2.0 + 1.5 * np.sin(0.2 * i)
            periodic_component += np.sin(2.0 * np.pi * x[i] / period) * np.cos(3.0 * x[i] / period)
        
        # Boundary penalty with exponential decay
        boundary_penalty = 0.0
        for i in range(self.dim):
            dist_from_bound = 5.0 - np.abs(x[i])
            if dist_from_bound < 0:
                boundary_penalty += 5.0 * np.exp(dist_from_bound**2)
        
        # Combine all components
        result = decay_potential + wave_interference * conditioning + periodic_component + boundary_penalty
        
        # Add adaptive noise based on problem dimension
        noise = 0.0
        for i in range(self.dim):
            noise += 0.02 * np.sin(10.0 * x[i] + i) * np.cos(5.0 * x[i] + i)
        result += noise
        
        # Final scaling with chaotic modulation
        final_scale = 1.0 + 0.05 * np.sin(0.1 * self.dim) * np.cos(0.05 * self.dim)
        result *= final_scale
        
        return result