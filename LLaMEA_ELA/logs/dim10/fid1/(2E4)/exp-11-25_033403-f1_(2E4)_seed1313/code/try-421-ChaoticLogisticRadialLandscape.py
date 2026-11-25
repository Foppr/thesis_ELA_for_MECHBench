import numpy as np

class ChaoticLogisticRadialLandscape:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic logistic map parameters
        self.logistic_rates = np.random.uniform(3.5, 4.0, dim)
        self.logistic_shifts = np.random.uniform(-1.0, 1.0, dim)
        # Initialize polynomial potentials with varying degrees and coefficients
        self.poly_degrees = np.random.randint(3, 8, dim)
        self.poly_coefficients = np.random.uniform(-3.0, 3.0, dim)
        # Initialize Gaussian radial basis functions
        self.gaussian_centers = np.random.uniform(-5.0, 5.0, (dim, dim))
        self.gaussian_widths = np.random.uniform(0.3, 2.5, dim)
        self.gaussian_weights = np.random.uniform(-1.5, 1.5, dim)
        # Initialize dynamic conditioning parameters
        self.conditioning_factors = np.random.uniform(0.2, 2.5, dim)
        self.conditioning_exponents = np.random.uniform(0.3, 4.0, dim)
        # Initialize cross-dimensional coupling terms
        self.cross_coupling = np.random.uniform(-0.5, 0.5, (dim, dim))
        # Initialize trigonometric components for additional complexity
        self.trig_amplitudes = np.random.uniform(0.3, 3.0, dim)
        self.trig_frequencies = np.random.uniform(0.5, 15.0, dim)
        # Additional harmonic and coupling parameters
        self.harmonic_weights = np.random.uniform(0.05, 0.4, dim)
        self.cross_coupling_strength = np.random.uniform(0.02, 0.3, (dim, dim))
        # New chaotic coupling parameters
        self.chaotic_coupling_strength = np.random.uniform(0.2, 0.8, (dim, dim))
        self.chaotic_exponents = np.random.uniform(1.0, 3.0, (dim, dim))
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Compute chaotic logistic map components
        logistic_terms = 0.0
        for j in range(self.dim):
            logistic_val = self.logistic_rates[j] * np.abs(x[j] - self.logistic_shifts[j]) * (1 - np.abs(x[j] - self.logistic_shifts[j]))
            logistic_terms += np.sin(logistic_val) * np.cos(logistic_val)
        
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
                    cross_terms += self.cross_coupling[i, j] * np.sin(x[i]) * np.cos(x[j])
        
        # Compute trigonometric components
        trig_terms = 0.0
        for j in range(self.dim):
            trig_terms += self.trig_amplitudes[j] * np.sin(self.trig_frequencies[j] * x[j])
        
        # Combine all components with appropriate weights
        total = 1.5 * logistic_terms + 1.2 * poly_terms + 1.1 * gaussian_terms + 0.8 * conditioning_terms + 0.6 * cross_terms + 0.5 * trig_terms
        
        # Add a complex interaction term: multi-scale chaotic coupling with enhanced nonlinearity
        chaotic_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaotic_coupling += self.chaotic_coupling_strength[i, j] * np.sin(3.0 * x[i]) * np.cos(4.0 * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        total += chaotic_coupling
        
        # Add a dynamic harmonic component with time-varying parameters and improved scaling
        harmonic_component = 0.0
        for j in range(self.dim):
            harmonic_component += self.harmonic_weights[j] * np.sin(6.0 * x[j]) * np.cos(5.0 * x[j]) * np.exp(-0.15 * x[j]**2)
        
        total += harmonic_component
        
        # Add a novel cross-dimensional interaction term that improves conditioning
        novel_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                novel_coupling += 0.15 * np.sin(x[i] + x[j]) * np.cos(3.0 * x[i] - x[j]) * (1.0 + 0.15 * (x[i]**2 + x[j]**2))
        
        total += novel_coupling
        
        # Add an additional chaotic interaction term for increased complexity
        extra_chaos = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                extra_chaos += 0.25 * np.sin(2.0 * x[i] + x[j]) * np.cos(x[i] - 2.0 * x[j]) * (x[i]**2 + x[j]**2) * np.exp(-0.02 * (x[i]**2 + x[j]**2))
        
        total += extra_chaos
        
        return total