import numpy as np

class FractalBrownianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize fractal parameters
        self.hurst_params = np.random.uniform(0.1, 0.9, dim)
        self.fractal_amplitudes = np.random.uniform(0.5, 2.0, dim)
        self.frequency_scales = np.random.uniform(0.5, 3.0, dim)
        self.rotation_angles = np.random.uniform(0, 2*np.pi, dim)
        self.transformation_weights = np.random.uniform(0.1, 1.0, dim)
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal Brownian motion component with adaptive roughness
        fbm_term = 0.0
        for i in range(self.dim):
            hurst = self.hurst_params[i]
            amplitude = self.fractal_amplitudes[i]
            frequency = self.frequency_scales[i]
            
            # Generate fractal noise using fractional Brownian motion characteristics
            fbm_value = amplitude * np.sin(frequency * x[i]) * (1.0 + hurst * np.cos(2.0 * frequency * x[i]))
            fbm_term += fbm_value
            
        # Multi-scale geometric patterns with self-similarity
        geometry_term = 0.0
        scales = [1.0, 2.0, 3.0, 4.0]
        for scale in scales:
            scale_sum = 0.0
            for i in range(self.dim):
                # Create self-similar geometric structures
                geom_val = np.sin(scale * x[i]) * np.cos(scale * x[i])
                scale_sum += geom_val
            geometry_term += scale_sum / len(scales)
            
        # Rotation-invariant feature extraction
        rotation_term = 0.0
        for i in range(self.dim):
            angle = self.rotation_angles[i]
            # Apply rotational transformation to create orientation-dependent features
            rotated_val = x[i] * np.cos(angle) - x[(i+1) % self.dim] * np.sin(angle)
            rotation_term += rotated_val**2
            
        # Adaptive transformation weighting
        transform_term = 0.0
        for i in range(self.dim):
            weight = self.transformation_weights[i]
            # Apply weighted transformations with exponential decay
            transform_term += weight * np.exp(-0.1 * x[i]**2) * np.sin(x[i])
            
        # Boundary influence with fractal scaling
        boundary_term = 0.0
        for i in range(self.dim):
            # Simulate boundary effects with fractal scaling
            boundary_val = (1.0 + np.exp(-x[i])) * (1.0 - np.exp(-x[i]))
            boundary_term += boundary_val
            
        # Combine all components with adaptive weighting
        total = 0.4 * fbm_term + 0.3 * geometry_term + 0.2 * rotation_term + 0.5 * transform_term + 0.3 * boundary_term
        
        return total