import numpy as np

class AdaptiveRidgeAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for each dimension
        self.ridge_centers = np.random.uniform(-3.0, 3.0, dim)
        self.ridge_heights = np.random.uniform(1.0, 4.0, dim)
        self.ridge_widths = np.random.uniform(0.5, 2.0, dim)
        self.asymmetry_params = np.random.uniform(0.1, 1.5, dim)
        self.modulation_frequencies = np.random.uniform(1.0, 5.0, dim)
        self.coupling_strengths = np.random.uniform(0.5, 2.5, dim)
        self.dynamic_exponents = np.random.uniform(0.5, 2.0, dim)
        self.periodic_amplitudes = np.random.uniform(0.5, 2.0, dim)
        self.noise_magnitudes = np.random.uniform(0.01, 0.1, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add ridge-like contributions with asymmetric modulation
        for i in range(self.dim):
            xi = x[i]
            center = self.ridge_centers[i]
            height = self.ridge_heights[i]
            width = self.ridge_widths[i]
            asymmetry = self.asymmetry_params[i]
            
            # Asymmetric ridge structure with exponential decay
            ridge_term = height * np.exp(-0.5 * ((xi - center) / width)**2) * (1.0 + asymmetry * np.sin(xi))
            result += ridge_term
            
        # Add periodic gradient modulation with dynamic frequency
        for i in range(self.dim):
            xi = x[i]
            freq = self.modulation_frequencies[i]
            amp = self.periodic_amplitudes[i]
            
            # Periodic modulation that varies with input position
            modulation = amp * np.sin(freq * xi + 0.5 * np.sin(2.0 * xi))
            result += modulation
            
        # Add cross-dimensional coupling with dynamic strength based on position
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                
                # Dynamic coupling strength that adapts to input values
                coupling_strength = self.coupling_strengths[i] * (1.0 + 0.3 * np.sin(xi + xj)) * np.exp(-0.1 * (xi**2 + xj**2))
                exponent = self.dynamic_exponents[i] * self.dynamic_exponents[j]
                
                # Coupling with asymmetric interaction
                coupling_term = coupling_strength * np.abs(xi - xj)**exponent * np.cos(0.5 * (xi + xj))
                result += coupling_term
                
        # Add noise components that vary with dimension and input position
        for i in range(self.dim):
            xi = x[i]
            noise_magnitude = self.noise_magnitudes[i] * (1.0 + 0.2 * np.sin(xi))
            noise_component = noise_magnitude * np.cos(10.0 * xi + i) * np.tanh(xi)
            result += noise_component
            
        # Add global scaling based on input position and dimension
        global_scale = 1.0 + 0.3 * np.sin(np.sum(x) / self.dim) * np.cos(np.sum(x**2) / (self.dim * 25.0))
        result *= global_scale
        
        # Add asymmetric multimodal structure with dynamic parameters
        multimodal_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Multi-scale multimodal with varying polynomial degrees and trigonometric components
            multimodal_term += (xi**4 - 10*xi**2 + 5) * np.sin(0.8 * xi) * np.cos(0.3 * xi)
        result += 0.5 * multimodal_term
        
        # Add dynamic ridge interaction terms
        ridge_interaction = 0.0
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xi, xj = x[i], x[j]
                # Dynamic ridge interaction with position-dependent strength
                interaction_strength = 0.5 * (1.0 + np.cos(xi + xj)) * np.exp(-0.05 * (xi**2 + xj**2))
                interaction_term = interaction_strength * (xi**2 + xj**2) * np.sin(0.6 * (xi - xj))
                ridge_interaction += interaction_term
        result += 0.2 * ridge_interaction
        
        return result