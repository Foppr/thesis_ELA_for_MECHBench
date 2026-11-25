import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Polynomial chaos expansion component with Hermite polynomials
        chaos_term = 0.0
        for i in range(self.dim):
            # Use third-order Hermite polynomial H3(x) = 4x^3 - 3x
            h3_x = 4 * x_norm[i]**3 - 3 * x_norm[i]
            chaos_term += h3_x**2
        
        # Stochastic harmonic potential with varying frequencies and amplitudes
        harmonic_potential = 0.0
        for i in range(self.dim):
            freq = 2**(i + 1) * (1 + 0.5 * np.sin(i * np.pi / self.dim))
            amp = 1.0 + 0.3 * np.cos(i * np.pi / self.dim)
            harmonic_potential += amp * np.sin(freq * x_norm[i])**2
        
        # Cross-dimensional coupling with asymmetric interaction weights
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                # Asymmetric coupling coefficient
                coupling_ij = (i + 1) * np.exp(-0.1 * (j - i)) * np.cos(np.pi * (i + j) / self.dim)
                coupling_ji = (j + 1) * np.exp(-0.1 * (j - i)) * np.sin(np.pi * (i + j) / self.dim)
                cross_coupling += coupling_ij * x_norm[i]**2 * x_norm[j] + coupling_ji * x_norm[j]**2 * x_norm[i]
        
        # Multi-scale fractal-like structure with sine-cosine modulation
        fractal_structure = 0.0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.5 * np.sin(3 * np.pi * x_norm[i])
            fractal_structure += scale_factor * (np.abs(x_norm[i])**1.7 + 0.3 * np.cos(5 * x_norm[i]))
        
        # Asymmetric noise component with dimensionality-dependent strength
        noise_strength = 0.1 / (1 + 0.1 * self.dim)
        noise = noise_strength * np.random.random() * np.sin(2**(self.dim + 3) * x_norm[0])
        
        # Combine components with dynamic scaling factors
        total = 0.8 * chaos_term + 0.6 * harmonic_potential + 0.4 * cross_coupling + 0.5 * fractal_structure + noise
        
        # Apply dimensionality-dependent penalty for better conditioning
        dim_penalty = 1.0 + 0.05 * np.log(self.dim + 1)
        
        return total * dim_penalty