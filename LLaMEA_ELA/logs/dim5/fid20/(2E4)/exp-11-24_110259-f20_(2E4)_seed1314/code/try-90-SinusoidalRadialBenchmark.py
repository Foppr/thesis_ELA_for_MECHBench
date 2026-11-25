import numpy as np

class SinusoidalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Generate random parameters for radial basis functions
        self.rbf_centers = np.random.uniform(-5.0, 5.0, (10, dim))
        self.rbf_widths = np.random.uniform(0.5, 3.0, 10)
        self.rbf_weights = np.random.uniform(-2.0, 2.0, 10)
        
        # Sinusoidal components with varying frequencies and amplitudes
        self.sin_frequencies = np.random.uniform(1.0, 8.0, dim)
        self.sin_amplitudes = np.random.uniform(0.5, 3.0, dim)
        
        # Conditioning parameters
        self.conditioning_factors = np.random.uniform(0.1, 10.0, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] for sinusoidal components
        x_normalized = x / 5.0
        
        # Sinusoidal oscillation component
        sin_component = 0.0
        for i in range(self.dim):
            freq = self.sin_frequencies[i]
            amp = self.sin_amplitudes[i]
            cond = self.conditioning_factors[i]
            sin_component += amp * np.sin(freq * x_normalized[i] * cond) * np.cos(freq * x_normalized[i] * cond)
        
        # Radial basis function component
        rbf_component = 0.0
        for i in range(10):
            center = self.rbf_centers[i]
            width = self.rbf_widths[i]
            weight = self.rbf_weights[i]
            
            # Calculate squared Euclidean distance
            dist_sq = np.sum((x_normalized - center)**2)
            rbf_value = weight * np.exp(-dist_sq / (2 * width**2))
            rbf_component += rbf_value
        
        # Cross-term interactions between dimensions
        cross_component = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Adaptive interaction strength based on dimension indices
                interaction_strength = 0.5 * (1.0 + np.sin(0.5 * (i + j)))
                cross_component += interaction_strength * np.sin(x_normalized[i]) * np.cos(x_normalized[j])
        
        # Polynomial conditioning component
        poly_component = np.sum((x_normalized**2) * self.conditioning_factors)
        
        # Combine all components with adaptive weighting
        result = 0.3 * sin_component + 0.4 * rbf_component + 0.2 * cross_component + 0.1 * poly_component
        
        # Add noise for robustness
        noise = 0.001 * np.random.randn()
        
        return result + noise