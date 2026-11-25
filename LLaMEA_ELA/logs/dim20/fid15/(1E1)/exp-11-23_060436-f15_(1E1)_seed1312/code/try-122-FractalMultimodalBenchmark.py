import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base fractal component with hierarchical structure
        fractal = 0
        for i in range(self.dim):
            # Multi-scale fractal pattern with varying exponents
            scale = 1.0 + 0.5 * np.sin(i * 0.7)
            exponent = 2.0 + 0.8 * np.cos(i * 0.5)
            
            # Fractal-like term with self-similarity
            fractal_term = np.abs(x[i])**exponent * np.exp(-scale * np.abs(x[i]))
            fractal += fractal_term
        
        # Dynamic conditioning component
        conditioning = 0
        for i in range(self.dim):
            # Variable conditioning based on dimension index
            cond_factor = 1.0 + 2.0 * np.sin(i * 0.3) * np.cos(i * 0.4)
            
            # Conditioned quadratic with dynamic scaling
            conditioning += cond_factor * x[i]**2 * (1.0 + 0.1 * np.sin(x[i]))
        
        # Hierarchical multimodal component
        multimodal = 0
        for i in range(self.dim):
            # Multiple peaks with varying heights and widths
            peak_height = 1.0 + 0.5 * np.sin(i * 0.6)
            peak_width = 0.5 + 0.3 * np.cos(i * 0.4)
            
            # Multi-peak function with fractal-like structure
            peak1 = peak_height * np.exp(-0.5 * ((x[i] - 2.0) / peak_width)**2)
            peak2 = peak_height * np.exp(-0.5 * ((x[i] + 2.0) / peak_width)**2)
            peak3 = peak_height * np.exp(-0.5 * ((x[i]) / (peak_width * 0.5))**2)
            
            multimodal += peak1 + peak2 + peak3
        
        # Self-similar interaction component
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited long-range interaction
                # Fractal-like interaction with scale-dependent weights
                scale_weight = 0.5 + 0.3 * np.sin(0.2 * (i + j))
                interaction += scale_weight * np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Dynamic noise component
        noise = 0
        for i in range(self.dim):
            # Dimension-specific noise with varying intensity
            noise_intensity = 0.3 + 0.2 * np.sin(i * 0.8)
            noise += noise_intensity * np.sin(x[i] * (1.0 + 0.1 * np.cos(i)))
        
        # Subspace complexity component
        subspace_complexity = 0
        for i in range(0, self.dim, 2):  # Process pairs of dimensions
            if i + 1 < self.dim:
                # Complex interaction between dimension pairs
                pair_complexity = (np.sin(x[i]) * np.cos(x[i+1]) + 
                                 np.cos(x[i]) * np.sin(x[i+1])) * np.exp(-0.1 * (x[i]**2 + x[i+1]**2))
                subspace_complexity += pair_complexity
        
        # Combine all components with optimized weights
        return (fractal * 0.4 +
                conditioning * 0.3 +
                multimodal * 0.5 +
                interaction * 0.25 +
                noise * 0.15 +
                subspace_complexity * 0.2)