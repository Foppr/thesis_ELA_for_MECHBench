import numpy as np

class AdaptiveRidgeAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        np.random.seed(42)
        # Initialize parameters for each dimension
        self.attractor_centers = np.random.uniform(-3.0, 3.0, dim)
        self.attractor_strengths = np.random.uniform(1.0, 5.0, dim)
        self.ridge_parameters = np.random.uniform(0.5, 2.0, dim)
        self.noise_levels = np.random.uniform(0.01, 0.1, dim)
        self.frequency_modulators = np.random.uniform(0.5, 2.0, dim)
        # Additional chaotic and fractal parameters
        self.fractal_dimensions = np.random.uniform(1.1, 1.9, dim)
        self.saddle_strengths = np.random.uniform(0.5, 3.0, dim)
        self.coupling_exponents = np.random.uniform(0.5, 1.5, dim)
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Add chaotic attractor contributions with fractal modulation
        for i in range(self.dim):
            xi = x[i]
            center = self.attractor_centers[i]
            strength = self.attractor_strengths[i]
            ridge_param = self.ridge_parameters[i]
            fractal_dim = self.fractal_dimensions[i]
            
            # Fractal-like attractor with chaotic modulation
            distance = np.abs(xi - center)
            fractal_term = strength * np.exp(-0.5 * (distance / (1.0 + 0.1 * xi**2))**fractal_dim)
            
            # Add ridge-like gradient flow component with fractal scaling
            ridge_component = ridge_param * np.sin(3.0 * xi) * np.cos(2.0 * xi) * np.tanh(xi)
            
            result += fractal_term + ridge_component
            
        # Add chaotic saddle point contributions
        for i in range(self.dim):
            xi = x[i]
            saddle_strength = self.saddle_strengths[i]
            # Chaotic saddle point with exponential decay
            saddle_term = saddle_strength * np.exp(-0.5 * xi**2) * np.sin(10.0 * xi)
            result += saddle_term
            
        # Add cross-dimensional coupling with adaptive fractal coupling
        for i in range(self.dim):
            xi = x[i]
            for j in range(i+1, self.dim):
                xj = x[j]
                
                # Fractal-based coupling strength
                coupling_strength = 0.5 * (1.0 + np.sin(0.3 * (i - j))) * (1.0 + 0.2 * np.sin(xi + xj))
                
                # Fractal coupling with power law interaction
                exponent = self.coupling_exponents[i] * self.coupling_exponents[j]
                cross_term = coupling_strength * np.power(np.abs(xi - xj), exponent) * np.cos(0.5 * (xi + xj))
                result += cross_term
                
        # Add dimensionally adaptive noise with fractal characteristics
        for i in range(self.dim):
            xi = x[i]
            noise_level = self.noise_levels[i] * (1.0 + 0.2 * np.sin(0.7 * i)) * (1.0 + 0.1 * np.cos(xi))
            noise_component = noise_level * np.sin(10.0 * xi + 0.5 * i) * np.cos(5.0 * xi)
            result += noise_component
            
        # Add frequency-dependent modulation for enhanced complexity with fractal scaling
        freq_mod = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq_mod += self.frequency_modulators[i] * np.sin(4.0 * xi + 0.3 * i) * np.tanh(xi)
        result += 0.1 * freq_mod**2
        
        # Add global scaling with non-linear transformation and fractal influence
        global_scale = 1.0 + 0.3 * np.tanh(np.sum(x) / self.dim) * np.prod(np.cos(x / 5.0))
        result *= global_scale
        
        # Add chaotic perturbation to increase algorithmic bias - improved version
        chaotic_perturbation = 0.05 * np.sum(np.sin(100.0 * x) * np.cos(50.0 * x) * np.exp(-0.1 * np.sum(x**2)))
        result += chaotic_perturbation
        
        # Add enhanced multi-modal structure with better fitness discrimination
        multimodal_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Add multiple local minima with varying depths
            multimodal_term += (xi**4 - 16*xi**2 + 5*xi) * np.cos(0.5 * xi)
        result += 0.3 * multimodal_term
        
        return result