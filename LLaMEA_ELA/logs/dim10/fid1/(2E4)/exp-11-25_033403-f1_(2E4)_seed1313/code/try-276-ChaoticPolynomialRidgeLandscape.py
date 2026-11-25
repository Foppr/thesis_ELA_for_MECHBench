import numpy as np

class ChaoticPolynomialRidgeLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize polynomial components with higher order terms
        self.poly_degrees = np.random.randint(3, 7, dim)
        self.poly_coeffs = np.random.uniform(-2.0, 2.0, (5, dim))
        # Initialize chaotic sinusoidal modulations with more complex patterns
        self.chaos_freqs = np.random.uniform(2.0, 8.0, dim)
        self.chaos_amplitudes = np.random.uniform(1.0, 3.0, dim)
        self.chaos_phase = np.random.uniform(0, 2*np.pi, dim)
        # Initialize elliptical ridge structures with more complex geometry
        self.ridge_centers = np.random.uniform(-4.5, 4.5, (6, dim))
        self.ridge_axes = np.random.uniform(0.3, 4.0, (6, dim))
        self.ridge_heights = np.random.uniform(0.5, 5.0, 6)
        # Initialize fractal-like components
        self.fractal_freqs = np.random.uniform(0.5, 3.0, dim)
        self.fractal_amplitudes = np.random.uniform(0.1, 1.5, dim)
        # Initialize adaptive scaling with more complex weights
        self.adaptive_weights = np.random.uniform(-1.0, 3.0, dim)
        # Additional noise parameters
        self.noise_level = np.random.uniform(0.01, 0.2)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute polynomial potential with higher order terms
        poly_potential = 0.0
        for j in range(self.dim):
            term = self.poly_coeffs[0, j] * (x[j]**self.poly_degrees[j])
            if self.poly_degrees[j] > 3:
                term += self.poly_coeffs[1, j] * (x[j]**(self.poly_degrees[j]-1))
            if self.poly_degrees[j] > 4:
                term += self.poly_coeffs[2, j] * (x[j]**(self.poly_degrees[j]-2))
            if self.poly_degrees[j] > 5:
                term += self.poly_coeffs[3, j] * (x[j]**(self.poly_degrees[j]-3))
            if self.poly_degrees[j] > 6:
                term += self.poly_coeffs[4, j] * (x[j]**(self.poly_degrees[j]-4))
            poly_potential += term
            
        # Add chaotic sinusoidal modulation
        chaos_modulation = 0.0
        for j in range(self.dim):
            chaos_modulation += self.chaos_amplitudes[j] * np.sin(self.chaos_freqs[j] * x[j] + self.chaos_phase[j])
            
        # Add elliptical ridge contributions
        ridge_potential = 0.0
        for i in range(6):
            ridge_dist = 0.0
            for j in range(self.dim):
                ridge_dist += ((x[j] - self.ridge_centers[i, j]) / self.ridge_axes[i, j])**2
            ridge_val = np.exp(-0.5 * ridge_dist)
            ridge_potential += self.ridge_heights[i] * ridge_val
            
        # Add fractal-like components
        fractal_potential = 0.0
        for j in range(self.dim):
            fractal_potential += self.fractal_amplitudes[j] * np.sin(self.fractal_freqs[j] * x[j]) * np.cos(self.fractal_freqs[j] * x[j])
            
        # Add adaptive weighted terms
        weight_terms = 0.0
        for j in range(self.dim):
            weight_terms += self.adaptive_weights[j] * x[j]**4
            
        # Add noise component
        noise = np.random.normal(0, self.noise_level)
        
        # Combine all components
        total = poly_potential + chaos_modulation + ridge_potential + fractal_potential + 0.15 * weight_terms + noise
        
        return total