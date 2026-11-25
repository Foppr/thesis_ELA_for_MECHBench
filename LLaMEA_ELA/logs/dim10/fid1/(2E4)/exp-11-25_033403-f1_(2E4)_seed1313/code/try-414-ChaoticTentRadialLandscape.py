import numpy as np

class ChaoticTentRadialLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic tent map parameters
        self.tent_maps = np.random.uniform(0.5, 1.5, dim)
        self.tent_shifts = np.random.uniform(-1.0, 1.0, dim)
        # Initialize polynomial potentials with varying degrees and coefficients
        self.poly_degrees = np.random.randint(2, 6, dim)
        self.poly_coefficients = np.random.uniform(-2.0, 2.0, dim)
        # Initialize Gaussian radial basis functions
        self.gaussian_centers = np.random.uniform(-5.0, 5.0, (dim, dim))
        self.gaussian_widths = np.random.uniform(0.5, 3.0, dim)
        self.gaussian_weights = np.random.uniform(-1.0, 1.0, dim)
        # Initialize dynamic conditioning parameters
        self.conditioning_factors = np.random.uniform(0.1, 2.0, dim)
        self.conditioning_exponents = np.random.uniform(0.5, 3.0, dim)
        # Initialize cross-dimensional coupling terms
        self.cross_coupling = np.random.uniform(-0.3, 0.3, (dim, dim))
        # Initialize trigonometric components for additional complexity
        self.trig_amplitudes = np.random.uniform(0.5, 2.5, dim)
        self.trig_frequencies = np.random.uniform(1.0, 10.0, dim)
        # Additional harmonic and coupling parameters for improved fitness
        self.harmonic_weights = np.random.uniform(0.1, 0.3, dim)
        self.coupling_strengths = np.random.uniform(0.05, 0.2, (dim, dim))
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute chaotic tent map components
        tent_terms = 0.0
        for j in range(self.dim):
            tent_val = self.tent_maps[j] * np.abs(x[j] - self.tent_shifts[j])
            tent_terms += np.sin(tent_val) * np.cos(tent_val)
        
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
        
        # Compute cross-dimensional coupling terms
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    cross_terms += self.cross_coupling[i, j] * np.sin(x[i]) * np.cos(x[j])
        
        # Compute trigonometric components
        trig_terms = 0.0
        for j in range(self.dim):
            trig_terms += self.trig_amplitudes[j] * np.sin(self.trig_frequencies[j] * x[j])
        
        # Combine all components with appropriate weights
        total = 1.3 * tent_terms + 1.0 * poly_terms + 0.9 * gaussian_terms + 0.7 * conditioning_terms + 0.5 * cross_terms + 0.4 * trig_terms
        
        # Add a complex interaction term: multi-scale chaotic coupling with enhanced weights
        chaotic_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaotic_coupling += 0.3 * np.sin(2.0 * x[i]) * np.cos(3.0 * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        total += chaotic_coupling
        
        # Add a dynamic harmonic component with time-varying parameters and improved scaling
        harmonic_component = 0.0
        for j in range(self.dim):
            harmonic_component += self.harmonic_weights[j] * np.sin(5.0 * x[j]) * np.cos(4.0 * x[j]) * np.exp(-0.1 * x[j]**2)
        
        total += harmonic_component
        
        # Add cross-dimensional coupling with enhanced interaction strength
        enhanced_coupling = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    enhanced_coupling += self.coupling_strengths[i, j] * np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.02 * (x[i]**2 + x[j]**2))
        
        total += enhanced_coupling
        
        # Add a global scaling factor to adjust overall fitness landscape
        total *= 0.85
        
        return total