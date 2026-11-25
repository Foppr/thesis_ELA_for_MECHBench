import numpy as np

class ChaoticPolynomialRidgeLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize polynomial components
        self.poly_degrees = np.random.randint(2, 5, dim)
        self.poly_coeffs = np.random.uniform(-1.0, 1.0, (3, dim))
        # Initialize chaotic sinusoidal modulations
        self.chaos_freqs = np.random.uniform(1.0, 5.0, dim)
        self.chaos_amplitudes = np.random.uniform(0.5, 2.0, dim)
        self.chaos_phase = np.random.uniform(0, 2*np.pi, dim)
        # Initialize elliptical ridge structures
        self.ridge_centers = np.random.uniform(-4.0, 4.0, (4, dim))
        self.ridge_axes = np.random.uniform(0.5, 3.0, (4, dim))
        self.ridge_heights = np.random.uniform(1.0, 4.0, 4)
        # Initialize adaptive scaling
        self.adaptive_weights = np.random.uniform(0.1, 2.0, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute polynomial potential
        poly_potential = 0.0
        for j in range(self.dim):
            term = self.poly_coeffs[0, j] * (x[j]**self.poly_degrees[j])
            if self.poly_degrees[j] > 2:
                term += self.poly_coeffs[1, j] * (x[j]**(self.poly_degrees[j]-1))
            if self.poly_degrees[j] > 3:
                term += self.poly_coeffs[2, j] * (x[j]**(self.poly_degrees[j]-2))
            poly_potential += term
            
        # Add chaotic sinusoidal modulation
        chaos_modulation = 0.0
        for j in range(self.dim):
            chaos_modulation += self.chaos_amplitudes[j] * np.sin(self.chaos_freqs[j] * x[j] + self.chaos_phase[j])
            
        # Add elliptical ridge contributions
        ridge_potential = 0.0
        for i in range(4):
            ridge_dist = 0.0
            for j in range(self.dim):
                ridge_dist += ((x[j] - self.ridge_centers[i, j]) / self.ridge_axes[i, j])**2
            ridge_val = np.exp(-0.5 * ridge_dist)
            ridge_potential += self.ridge_heights[i] * ridge_val
            
        # Add adaptive weighted terms
        weight_terms = 0.0
        for j in range(self.dim):
            weight_terms += self.adaptive_weights[j] * x[j]**3
            
        # Combine all components
        total = poly_potential + chaos_modulation + ridge_potential + 0.1 * weight_terms
        
        return total