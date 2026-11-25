import numpy as np

class ChaoticPolynomialSpectralLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic tent map parameters
        self.tent_params = np.random.uniform(1.5, 3.0, dim)
        # Initialize polynomial deformation coefficients
        self.poly_coeffs = np.random.uniform(-0.5, 0.5, (3, dim))
        # Initialize spectral filtering components with random frequencies
        self.spectral_freqs = np.random.uniform(0.5, 2.0, dim)
        self.spectral_amps = np.random.uniform(0.1, 1.0, dim)
        # Initialize dynamic frequency modulation parameters
        self.modulation_freqs = np.random.uniform(0.1, 0.5, dim)
        self.modulation_ampls = np.random.uniform(0.05, 0.2, dim)
        # Initialize anisotropic scaling matrix
        self.scaling_matrix = np.random.uniform(0.5, 2.0, (dim, dim))
        # Initialize cross-dimensional interaction weights
        self.interaction_weights = np.random.uniform(-0.3, 0.3, (dim, dim))
        # Initialize periodic harmonic components
        self.harmonic_freqs = np.random.uniform(1.0, 4.0, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute chaotic tent map components
        tent_terms = 0.0
        for j in range(self.dim):
            # Tent map: f(x) = mu * min(x, 1-x) for x in [0,1]
            scaled_x = (x[j] + 5.0) / 10.0  # Map to [0,1]
            tent_val = self.tent_params[j] * min(scaled_x, 1.0 - scaled_x)
            tent_terms += tent_val
        
        # Compute polynomial deformation terms
        poly_terms = 0.0
        for j in range(self.dim):
            poly_val = (self.poly_coeffs[0,j] * x[j]**2 + 
                       self.poly_coeffs[1,j] * x[j]**3 + 
                       self.poly_coeffs[2,j] * x[j]**4)
            poly_terms += poly_val
        
        # Compute spectral filtering components
        spec_terms = 0.0
        for j in range(self.dim):
            spec_val = self.spectral_amps[j] * np.sin(self.spectral_freqs[j] * x[j])
            spec_terms += spec_val
        
        # Compute dynamic frequency modulation
        mod_terms = 0.0
        for j in range(self.dim):
            mod_val = self.modulation_ampls[j] * np.sin(self.modulation_freqs[j] * x[j])
            mod_terms += mod_val
        
        # Apply anisotropic scaling
        scaled_x = np.dot(self.scaling_matrix, x)
        scale_terms = 0.0
        for j in range(self.dim):
            scale_terms += scaled_x[j]**2
        
        # Compute cross-dimensional interactions
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_terms += self.interaction_weights[i,j] * x[i] * x[j]
        
        # Compute periodic harmonic components
        harm_terms = 0.0
        for j in range(self.dim):
            harm_val = np.sin(self.harmonic_freqs[j] * x[j])
            harm_terms += harm_val
        
        # Combine all components with appropriate weights
        total = 1.5 * tent_terms + 1.0 * poly_terms + 0.8 * spec_terms + 0.6 * mod_terms + 0.4 * scale_terms + 0.3 * cross_terms + 0.2 * harm_terms
        
        return total