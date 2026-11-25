import numpy as np

class RotatedHyperEllipsoidalRBF:
    def __init__(self, dim):
        self.dim = dim
        # Initialize rotated hyper-ellipsoidal components with random rotation matrices
        self.rotation_matrices = []
        for _ in range(3):
            # Generate random orthogonal matrix for rotation
            A = np.random.randn(dim, dim)
            Q, _ = np.linalg.qr(A)
            self.rotation_matrices.append(Q)
        
        # Initialize hyper-ellipsoidal parameters
        self.ellipsoid_centers = np.random.uniform(-4.0, 4.0, (3, dim))
        self.ellipsoid_axes = np.random.uniform(0.5, 3.0, (3, dim))
        self.ellipsoid_weights = np.random.uniform(0.5, 2.0, 3)
        
        # Initialize radial basis function parameters
        self.rbf_centers = np.random.uniform(-4.0, 4.0, (5, dim))
        self.rbf_widths = np.random.uniform(0.5, 2.0, 5)
        self.rbf_weights = np.random.uniform(-1.0, 1.0, 5)
        
        # Initialize noise modulation parameters
        self.noise_amplitudes = np.random.uniform(0.1, 0.5, dim)
        self.noise_frequencies = np.random.uniform(1.0, 5.0, dim)
        
        # Initialize adaptive conditioning factors
        self.conditioning_factors = np.random.uniform(0.1, 2.0, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute rotated hyper-ellipsoidal components
        hyper_ellipsoid = 0.0
        for i in range(3):
            rotated_x = self.rotation_matrices[i] @ (x - self.ellipsoid_centers[i])
            dist_squared = np.sum((rotated_x / self.ellipsoid_axes[i]) ** 2)
            hyper_ellipsoid += self.ellipsoid_weights[i] * np.exp(-0.5 * dist_squared)
        
        # Compute radial basis function components
        rbf = 0.0
        for i in range(5):
            diff = x - self.rbf_centers[i]
            dist_squared = np.sum(diff ** 2)
            rbf += self.rbf_weights[i] * np.exp(-0.5 * dist_squared / (self.rbf_widths[i] ** 2))
        
        # Add noise modulation
        noise = 0.0
        for j in range(self.dim):
            noise += self.noise_amplitudes[j] * np.sin(self.noise_frequencies[j] * x[j])
        
        # Apply adaptive conditioning
        conditioning = 0.0
        for j in range(self.dim):
            conditioning += self.conditioning_factors[j] * (x[j] ** 2)
        
        # Combine all components with appropriate weights
        total = 0.7 * hyper_ellipsoid + 0.6 * rbf + 0.3 * noise + 0.2 * conditioning
        
        # Add a new component: cross-dimensional interaction with sine modulation
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_interaction += np.sin(x[i] * x[j]) * (1.0 + 0.1 * np.cos(x[i] + x[j]))
        
        # Add a new component: polynomial with mixed even/odd terms
        poly_terms = 0.0
        for j in range(self.dim):
            if j % 2 == 0:
                poly_terms += 0.5 * (x[j] ** 4) + 0.3 * (x[j] ** 2)
            else:
                poly_terms += 0.4 * (x[j] ** 3) + 0.2 * x[j]
        
        # Final combination with refined weights
        total = 0.8 * hyper_ellipsoid + 0.7 * rbf + 0.25 * noise + 0.15 * conditioning + 0.2 * cross_interaction + 0.1 * poly_terms
        
        return total