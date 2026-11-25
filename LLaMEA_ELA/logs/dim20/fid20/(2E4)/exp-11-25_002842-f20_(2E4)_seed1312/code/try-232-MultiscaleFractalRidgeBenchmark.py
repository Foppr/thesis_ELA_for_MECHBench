import numpy as np

class MultiscaleFractalRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize multiscale fractal parameters
        self.fractal_dimensions = np.random.uniform(1.1, 2.9, dim)
        self.ridge_widths = np.random.uniform(0.5, 3.0, dim)
        self.spectral_bands = np.random.uniform(0.1, 2.0, (dim, 4))
        self.adaptive_scaling = np.random.uniform(0.5, 2.0, dim)
        self.coupling_strengths = np.random.uniform(0.3, 1.5, (dim, dim))
        self.frequency_modulators = np.random.uniform(0.8, 2.5, dim)
        self.smoothness_parameters = np.random.uniform(0.1, 1.0, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Initialize result
        result = 0.0
        
        # Multiscale fractal ridge components
        for i in range(self.dim):
            # Fractal ridge with adaptive width and spectral band modulation
            ridge_value = 0.0
            
            # Multiple frequency bands
            for j in range(4):
                freq = self.spectral_bands[i, j] * (1.0 + 0.5 * np.sin(x_norm[i]))
                amp = 1.0 / (1.0 + np.exp(-self.frequency_modulators[i] * (x_norm[i] - 0.5)))
                ridge_value += amp * np.sin(freq * x_norm[i]) * np.exp(-0.5 * (x_norm[i] / self.ridge_widths[i])**2)
            
            # Fractal dimension scaling
            fractal_scaling = np.power(np.abs(x_norm[i]), self.fractal_dimensions[i])
            
            # Adaptive smoothing parameter
            smooth_param = self.smoothness_parameters[i]
            ridge_value *= np.exp(-smooth_param * x_norm[i]**2)
            
            result += ridge_value * fractal_scaling * self.adaptive_scaling[i]
        
        # Cross-dimensional coupling with spectral band interactions
        coupling_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Spectral band coupling between dimensions
                coupling_strength = self.coupling_strengths[i, j] * np.cos(x_norm[i] - x_norm[j])
                
                # Frequency interaction term
                freq_interaction = np.sin(self.spectral_bands[i, 0] * x_norm[i]) * \
                                  np.cos(self.spectral_bands[j, 1] * x_norm[j])
                
                # Distance-based coupling
                distance_factor = np.exp(-0.5 * (x_norm[i] - x_norm[j])**2)
                
                coupling_terms += coupling_strength * freq_interaction * distance_factor
        
        # Add coupling terms to main result
        result += 0.5 * coupling_terms
        
        # Add noise component for enhanced complexity
        noise = np.random.normal(0, 0.1, self.dim)
        noise_component = np.sum(noise * np.sin(x_norm))
        
        return result + noise_component