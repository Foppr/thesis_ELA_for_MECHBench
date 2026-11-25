import numpy as np

class ExponentialRBFBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Exponential barrier parameters with varying steepness
        self.barrier_centers = np.random.uniform(-4.0, 4.0, (dim, 8))
        self.barrier_steepness = np.random.uniform(1.0, 15.0, (dim, 8))
        # Radial basis function parameters with different widths
        self.rbf_centers = np.random.uniform(-4.5, 4.5, (dim, 6))
        self.rbf_widths = np.random.uniform(0.5, 3.0, (dim, 6))
        # Spectral decomposition components with varying frequencies
        self.spectral_freqs = np.random.uniform(0.1, 5.0, dim)
        self.spectral_amplitudes = np.random.uniform(-2.0, 2.0, dim)
        # Multi-scale interaction coefficients
        self.scale_factors = np.random.uniform(0.5, 3.0, (dim, dim))
        # Adaptive conditioning with exponential scaling
        self.conditioning_exponents = np.random.uniform(1.0, 4.0, dim)
        # Phase shifts for spectral components
        self.spectral_phases = np.random.uniform(0, 2*np.pi, dim)
        # Polynomial terms for additional curvature
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, (dim, 4))
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Exponential barrier functions with multiple centers
        barrier_energy = 0.0
        for i in range(self.dim):
            for j in range(8):
                dist = abs(x[i] - self.barrier_centers[i, j])
                barrier_energy += self.barrier_steepness[i, j] * np.exp(-dist / (1.0 + 0.1 * dist))
                
        # Radial basis functions with different widths
        rbf_energy = 0.0
        for i in range(self.dim):
            for j in range(6):
                dist_sq = np.sum((x - self.rbf_centers[:, j]) ** 2)
                rbf_energy += np.exp(-dist_sq / (2.0 * self.rbf_widths[i, j] ** 2))
                
        # Spectral decomposition with cosine and sine components
        spectral_energy = 0.0
        for i in range(self.dim):
            spectral_energy += self.spectral_amplitudes[i] * np.cos(self.spectral_freqs[i] * x[i] + self.spectral_phases[i])
            
        # Multi-scale interaction terms
        interaction_energy = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = abs(x[i] - x[j])
                interaction_energy += self.scale_factors[i, j] * np.exp(-dist ** 2 / (2.0 * (1.0 + dist)))
                
        # Adaptive conditioning with exponential scaling
        conditioning_energy = 0.0
        for i in range(self.dim):
            conditioning_energy += self.conditioning_exponents[i] * (x[i] ** self.conditioning_exponents[i])
            
        # Polynomial curvature terms
        poly_energy = 0.0
        for i in range(self.dim):
            for j in range(4):
                poly_energy += self.poly_coeffs[i, j] * (x[i] ** (j + 1))
                
        # Combine all components with weighted sum
        total = 0.25 * barrier_energy + 0.20 * rbf_energy + 0.15 * spectral_energy + 0.20 * interaction_energy + 0.10 * conditioning_energy + 0.10 * poly_energy
        
        return total