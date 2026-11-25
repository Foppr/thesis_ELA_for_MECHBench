import numpy as np

class SinusoidalPolynomialBarrierLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Chaotic sinusoidal components with varying frequencies and amplitudes
        self.sin_freqs = 2.0 + 8.0 * np.random.rand(dim)
        self.sin_amps = 0.5 + 3.0 * np.random.rand(dim)
        # Polynomial barrier parameters with varying degrees and coefficients
        self.poly_degrees = 3 + np.random.randint(2, size=dim) * 2
        self.poly_coeffs = 0.1 + 2.0 * np.random.rand(dim)
        # Coupling interactions with non-linear harmonic terms
        self.harmonic_freqs = 1.0 + 5.0 * np.random.rand(dim)
        self.harmonic_amplitudes = 0.3 + 1.7 * np.random.rand(dim)
        # Noise complexity parameters
        self.noise_levels = 0.05 + 0.2 * np.random.rand(dim)
        self.noise_frequencies = 0.5 + 2.0 * np.random.rand(dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic sinusoidal barrier component
        sin_barrier = 0.0
        for i in range(self.dim):
            sin_barrier += self.sin_amps[i] * np.sin(self.sin_freqs[i] * x_norm[i])
        
        # Polynomial barrier with varying degrees
        poly_barrier = 0.0
        for i in range(self.dim):
            poly_barrier += self.poly_coeffs[i] * (x_norm[i]**self.poly_degrees[i])
        
        # Harmonic coupling between dimensions
        harmonic_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_term = self.harmonic_amplitudes[i] * np.cos(self.harmonic_freqs[i] * x_norm[j])
                    harmonic_coupling += coupling_term * np.exp(-0.2 * (x_norm[i]**2 + x_norm[j]**2))
        
        # Noise complexity component
        noise_component = 0.0
        for i in range(self.dim):
            noise_component += self.noise_levels[i] * np.sin(self.noise_frequencies[i] * x_norm[i])
        
        # Combined landscape with chaotic and polynomial interactions
        result = 0.3 * sin_barrier + 0.3 * poly_barrier + 0.3 * harmonic_coupling + 0.1 * noise_component
        
        # Add global conditioning and penalty terms
        condition_penalty = 0.05 * np.sum(x_norm**6)
        return result + condition_penalty + 0.02 * np.sum(np.abs(x_norm)**10)