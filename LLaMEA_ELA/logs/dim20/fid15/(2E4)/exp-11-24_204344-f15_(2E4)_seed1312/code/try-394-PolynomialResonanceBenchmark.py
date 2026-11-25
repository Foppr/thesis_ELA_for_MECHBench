import numpy as np

class PolynomialResonanceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Polynomial chaos expansion coefficients
        self.poly_coeffs = np.random.randn(dim, 8)
        # Radial basis function centers and widths
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (15, dim))
        self.rbf_widths = np.random.uniform(0.5, 3.0, 15)
        # Stochastic resonance parameters
        self.resonance_freqs = np.random.uniform(0.1, 2.0, dim)
        self.resonance_amplitudes = np.random.uniform(0.5, 2.0, dim)
        self.noise_levels = np.random.uniform(0.1, 1.0, dim)
        # Dynamic fitness modulation
        self.modulation_freqs = np.random.uniform(0.01, 0.1, dim)
        self.modulation_amplitudes = np.random.uniform(0.1, 0.5, dim)
        
    def f(self, x):
        x = np.array(x)
        
        # Polynomial chaos expansion component
        poly_term = 0.0
        for i in range(self.dim):
            coeffs = self.poly_coeffs[i]
            xi = x[i]
            # Evaluate polynomial chaos expansion with Hermite polynomials
            poly_term += (coeffs[0] + coeffs[1]*xi + coeffs[2]*xi**2 + coeffs[3]*xi**3 + 
                         coeffs[4]*xi**4 + coeffs[5]*xi**5 + coeffs[6]*xi**6 + coeffs[7]*xi**7)
        
        # Radial basis function interpolation component
        rbf_term = 0.0
        for i in range(15):  # 15 RBF centers
            center = self.rbf_centers[i]
            width = self.rbf_widths[i]
            distance = np.sum((x - center)**2)
            rbf_term += np.exp(-distance / (2 * width**2))
        
        # Stochastic resonance component with dynamic coupling
        resonance_term = 0.0
        for i in range(self.dim):
            freq = self.resonance_freqs[i]
            amp = self.resonance_amplitudes[i]
            noise = self.noise_levels[i]
            
            # Add stochastic resonance effect
            resonance = amp * np.sin(freq * x[i]) + noise * np.random.randn()
            resonance_term += resonance * np.cos(x[i] * 0.5)
        
        # Dynamic fitness modulation based on time-like parameter
        mod_term = 0.0
        t = np.sum(x) * 0.01  # Time-like parameter
        for i in range(self.dim):
            freq = self.modulation_freqs[i]
            amp = self.modulation_amplitudes[i]
            mod_term += amp * np.sin(freq * t + x[i])
        
        # Combine all components with nonlinear weighting
        total = 0.3 * poly_term + 0.4 * rbf_term + 0.2 * resonance_term + 0.1 * mod_term
        
        # Add a global scaling factor based on distance from origin
        dist_from_origin = np.linalg.norm(x)
        global_scale = 1.0 + 0.3 * np.sin(dist_from_origin * 0.5) * np.cos(dist_from_origin * 0.2)
        
        return total * global_scale