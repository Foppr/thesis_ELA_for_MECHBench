import numpy as np

class RadialChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Cluster centers for radial basis functions with dynamic positioning
        self.cluster_centers = np.random.uniform(-5.0, 5.0, (dim, 8))
        # Adaptive correlation matrices between dimensions
        self.correlation_matrices = []
        for _ in range(8):
            corr = np.random.rand(dim, dim)
            corr = (corr + corr.T) / 2
            np.fill_diagonal(corr, 1.0)
            self.correlation_matrices.append(corr)
        # Polynomial degree for each dimension
        self.poly_degrees = np.random.randint(3, 10, dim)
        # Trigonometric frequency modifiers
        self.freq_modifiers = np.random.uniform(0.5, 3.0, dim)
        # Adaptive conditioning factors
        self.conditioning_factors = np.random.uniform(0.1, 4.0, dim)
        # Radial basis function widths with variation
        self.rbf_widths = np.random.uniform(0.5, 3.0, 8)
        # Hybrid interaction coefficients
        self.hybrid_coeffs = np.random.uniform(-2.0, 2.0, (dim, dim))
        # Dynamic phase shifts for trigonometric components
        self.phase_shifts = np.random.uniform(0, 4*np.pi, dim)
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Radial basis function components with adaptive cluster centers and correlation
        rbf_energy = 0.0
        for i in range(8):
            center = self.cluster_centers[:, i]
            diff = x - center
            weighted_diff = np.dot(diff, self.correlation_matrices[i])
            distance_sq = np.sum(weighted_diff ** 2)
            rbf_energy += np.exp(-distance_sq / (2 * self.rbf_widths[i] ** 2))
            
        # Polynomial components with adaptive degrees and conditioning
        poly_energy = 0.0
        for i in range(self.dim):
            poly_energy += self.conditioning_factors[i] * (x[i] ** self.poly_degrees[i])
            
        # Trigonometric components with dynamic frequency modifiers and phase shifts
        trig_energy = 0.0
        for i in range(self.dim):
            trig_energy += np.sin(self.freq_modifiers[i] * x[i] + self.phase_shifts[i]) ** 2
            
        # Hybrid polynomial-trigonometric interactions between dimensions
        hybrid_energy = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                hybrid_energy += self.hybrid_coeffs[i, j] * (x[i] ** 2) * np.cos(x[j])
                
        # Combine all components with weighted sum and dynamic scaling
        total = 0.30 * rbf_energy + 0.25 * poly_energy + 0.25 * trig_energy + 0.20 * hybrid_energy
        
        return -total