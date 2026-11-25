import numpy as np

class ChaoticRadialSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic radial basis parameters
        self.radial_centers = np.random.uniform(-3.0, 3.0, (min(15, dim), dim))
        self.radial_widths = np.logspace(0.5, 2.0, min(15, dim))
        self.radial_amplitudes = np.random.uniform(1.0, 5.0, min(15, dim))
        # Dynamic gradient modulation parameters
        self.gradient_scales = np.logspace(0.5, 3.0, min(10, dim))
        self.gradient_exponents = np.random.uniform(1.5, 4.0, min(10, dim))
        # Adaptive dimensionality scaling
        self.dimension_weights = np.logspace(-1.0, 1.0, min(8, dim))
        # Saddle-point modulation parameters
        self.saddle_frequencies = np.logspace(1.0, 2.5, min(12, dim))
        self.saddle_amplitudes = np.random.uniform(0.5, 2.0, min(12, dim))
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic radial basis functions with dynamic modulation
        for i in range(min(len(self.radial_centers), self.dim)):
            center = self.radial_centers[i]
            width = self.radial_widths[i % len(self.radial_widths)]
            amplitude = self.radial_amplitudes[i % len(self.radial_amplitudes)]
            
            # Radial distance with chaotic scaling
            distances = np.sqrt(np.sum((x_norm - center)**2, axis=-1, keepdims=True))
            radial_term = amplitude * np.exp(-width * distances) * np.sin(distances)
            result += np.sum(radial_term)
            
        # Dynamic gradient modulation with adaptive scaling
        gradient_term = 0.0
        for i in range(self.dim):
            scale = self.gradient_scales[i % len(self.gradient_scales)]
            exponent = self.gradient_exponents[i % len(self.gradient_exponents)]
            weight = self.dimension_weights[i % len(self.dimension_weights)]
            
            # Adaptive gradient modulation with chaotic behavior
            modulated_gradient = np.abs(x_norm[i])**exponent * np.cos(scale * x_norm[i])
            gradient_term += weight * modulated_gradient
            
        # Saddle-point regions with frequency modulation
        saddle_term = 0.0
        for i in range(self.dim):
            freq = self.saddle_frequencies[i % len(self.saddle_frequencies)]
            amp = self.saddle_amplitudes[i % len(self.saddle_amplitudes)]
            
            # Saddle-point with harmonic modulation
            saddle_contribution = amp * (x_norm[i]**2) * np.sin(freq * x_norm[i])
            saddle_term += saddle_contribution
            
        # Cross-dimensional coupling with chaotic interaction
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                # Chaotic coupling between dimensions
                coupling_strength = np.sin(x_norm[i] * x_norm[j]) * np.cos(x_norm[i] + x_norm[j])
                coupling_term += coupling_strength
                
        # Adaptive dimensionality scaling with chaotic weighting
        scaling_term = 0.0
        for i in range(self.dim):
            weight = self.dimension_weights[i % len(self.dimension_weights)]
            scaling_term += weight * np.exp(-np.abs(x_norm[i]))
            
        # Combine all components with chaotic weighting
        result = 0.3 * result + 0.4 * gradient_term + 0.2 * saddle_term + 0.1 * coupling_term + 0.05 * scaling_term
        
        return result