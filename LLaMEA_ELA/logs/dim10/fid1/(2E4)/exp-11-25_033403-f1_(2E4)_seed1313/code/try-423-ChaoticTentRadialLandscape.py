import numpy as np

class ChaoticTentRadialLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic tent map parameters with increased complexity
        self.tent_maps = np.random.uniform(0.8, 2.0, dim)
        self.tent_shifts = np.random.uniform(-1.5, 1.5, dim)
        self.tent_nonlinearities = np.random.uniform(0.5, 3.0, dim)
        # Initialize polynomial potentials with higher degrees and coefficients
        self.poly_degrees = np.random.randint(3, 8, dim)
        self.poly_coefficients = np.random.uniform(-3.0, 3.0, dim)
        # Initialize Gaussian radial basis functions with more centers
        self.gaussian_centers = np.random.uniform(-5.0, 5.0, (dim, dim))
        self.gaussian_widths = np.random.uniform(0.3, 4.0, dim)
        self.gaussian_weights = np.random.uniform(-1.5, 1.5, dim)
        # Initialize dynamic conditioning parameters with more variation
        self.conditioning_factors = np.random.uniform(0.05, 3.0, dim)
        self.conditioning_exponents = np.random.uniform(0.3, 4.0, dim)
        # Initialize cross-dimensional coupling terms with enhanced complexity
        self.cross_coupling = np.random.uniform(-0.5, 0.5, (dim, dim))
        self.cross_coupling_strength = np.random.uniform(0.1, 0.4, (dim, dim))
        # Initialize trigonometric components with higher frequencies
        self.trig_amplitudes = np.random.uniform(0.3, 3.0, dim)
        self.trig_frequencies = np.random.uniform(2.0, 15.0, dim)
        # Additional harmonic and coupling parameters with increased complexity
        self.harmonic_weights = np.random.uniform(0.05, 0.5, dim)
        self.harmonic_frequencies = np.random.uniform(3.0, 8.0, dim)
        # Novel higher-order coupling terms
        self.higher_order_couplings = np.random.uniform(-0.2, 0.2, (dim, dim, dim))
        # Multi-scale chaotic parameters
        self.multi_scale_factors = np.random.uniform(0.1, 1.0, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute chaotic tent map components with higher nonlinearity
        tent_terms = 0.0
        for j in range(self.dim):
            tent_val = self.tent_maps[j] * np.abs(x[j] - self.tent_shifts[j])
            tent_terms += np.sin(tent_val * self.tent_nonlinearities[j]) * np.cos(tent_val * self.tent_nonlinearities[j])
        
        # Compute polynomial potential terms
        poly_terms = 0.0
        for j in range(self.dim):
            poly_terms += self.poly_coefficients[j] * (x[j] ** self.poly_degrees[j])
        
        # Compute Gaussian radial basis functions
        gaussian_terms = 0.0
        for j in range(self.dim):
            gaussian_sum = 0.0
            for k in range(self.dim):
                diff = x[k] - self.gaussian_centers[j, k]
                gaussian_sum += np.exp(-0.5 * (diff**2) / (self.gaussian_widths[j]**2))
            gaussian_terms += self.gaussian_weights[j] * gaussian_sum
        
        # Compute dynamic conditioning terms
        conditioning_terms = 0.0
        for j in range(self.dim):
            conditioning_terms += self.conditioning_factors[j] * (np.abs(x[j]) ** self.conditioning_exponents[j])
        
        # Compute cross-dimensional coupling terms with enhanced interaction
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_terms += self.cross_coupling[i, j] * np.sin(x[i]) * np.cos(x[j]) * (1.0 + self.cross_coupling_strength[i, j] * x[i]**2)
        
        # Compute trigonometric components
        trig_terms = 0.0
        for j in range(self.dim):
            trig_terms += self.trig_amplitudes[j] * np.sin(self.trig_frequencies[j] * x[j])
        
        # Combine all components with appropriate weights
        total = 1.5 * tent_terms + 1.2 * poly_terms + 1.1 * gaussian_terms + 0.8 * conditioning_terms + 0.6 * cross_terms + 0.5 * trig_terms
        
        # Add a complex interaction term: multi-scale chaotic coupling with enhanced nonlinearity
        chaotic_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaotic_coupling += 0.4 * np.sin(2.5 * x[i]) * np.cos(3.5 * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2)) * self.multi_scale_factors[i] * self.multi_scale_factors[j]
        
        total += chaotic_coupling
        
        # Add a dynamic harmonic component with time-varying parameters and improved scaling
        harmonic_component = 0.0
        for j in range(self.dim):
            harmonic_component += self.harmonic_weights[j] * np.sin(self.harmonic_frequencies[j] * x[j]) * np.cos(4.0 * x[j]) * np.exp(-0.15 * x[j]**2)
        
        total += harmonic_component
        
        # Add a novel cross-dimensional interaction term that improves conditioning with higher-order effects
        novel_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                novel_coupling += 0.15 * np.sin(x[i] + x[j]) * np.cos(2.0 * x[i] - x[j]) * (1.0 + 0.15 * (x[i]**2 + x[j]**2)) * np.exp(-0.02 * (x[i]**3 + x[j]**3))
        
        total += novel_coupling
        
        # Add higher-order coupling terms
        higher_order_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                for k in range(j+1, self.dim):
                    if i != j and i != k:
                        higher_order_terms += self.higher_order_couplings[i, j, k] * np.sin(x[i]) * np.cos(x[j]) * np.sin(x[k])
        
        total += higher_order_terms
        
        return total