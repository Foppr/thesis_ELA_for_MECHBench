import numpy as np

class ChaoticHyperEllipsoidalLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize polynomial potential components with higher variation
        self.poly_degrees = np.random.randint(2, 8, dim)
        self.poly_coeffs = np.random.uniform(-3.0, 3.0, dim)
        # Initialize chaotic sine-wave modulations with stronger chaos
        self.chaos_freqs = np.random.uniform(4.0, 10.0, dim)
        self.chaos_amplitudes = np.random.uniform(1.0, 3.0, dim)
        # Initialize hyper-ellipsoidal structures with more complex centers and axes
        self.ellipsoid_centers = np.random.uniform(-4.5, 4.5, (7, dim))
        self.ellipsoid_axes = np.random.uniform(0.5, 4.0, (7, dim))
        self.ellipsoid_weights = np.random.uniform(0.3, 2.5, 7)
        # Initialize momentum-based gradient steering parameters with adaptive scaling
        self.momentum_params = np.random.uniform(0.05, 1.2, dim)
        self.steering_magnitude = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute polynomial potential with cross-terms for non-separability
        poly_potential = 0.0
        for j in range(self.dim):
            poly_potential += self.poly_coeffs[j] * (x[j] ** self.poly_degrees[j])
        # Add cross-terms between dimensions for increased complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_potential += 0.1 * self.poly_coeffs[i] * self.poly_coeffs[j] * x[i] * x[j]
        
        # Add chaotic sine-wave modulation with double chaotics
        chaos_modulation = 0.0
        for j in range(self.dim):
            chaos_modulation += self.chaos_amplitudes[j] * np.sin(self.chaos_freqs[j] * x[j] + 
                                                                  np.sin(self.chaos_freqs[j] * x[j] + 
                                                                         np.cos(self.chaos_freqs[j] * x[j])))
        
        # Add hyper-ellipsoidal structures with overlapping and varying scales
        ellipsoid_potential = 0.0
        for i in range(7):
            ell_dist = 0.0
            for j in range(self.dim):
                ell_dist += ((x[j] - self.ellipsoid_centers[i, j]) / self.ellipsoid_axes[i, j])**2
            ellipsoid_potential += self.ellipsoid_weights[i] * np.exp(-0.3 * ell_dist)
        
        # Add momentum-based gradient steering with additional nonlinear terms
        steering_terms = 0.0
        for j in range(self.dim):
            steering_terms += self.steering_magnitude[j] * x[j] * np.sin(self.momentum_params[j] * x[j]) + \
                             0.2 * self.steering_magnitude[j] * np.cos(self.momentum_params[j] * x[j])
        
        # Combine all components with dynamic weighting
        total = 0.6 * poly_potential + 1.5 * chaos_modulation + ellipsoid_potential + 0.4 * steering_terms
        
        return total