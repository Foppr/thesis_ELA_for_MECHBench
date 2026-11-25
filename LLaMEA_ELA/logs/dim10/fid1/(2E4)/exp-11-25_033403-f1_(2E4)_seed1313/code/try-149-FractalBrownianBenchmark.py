import numpy as np

class FractalBrownianBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize fractal parameters
        self.hurst_params = np.random.uniform(0.1, 0.9, dim)
        self.fractal_amplitudes = np.random.uniform(1.0, 5.0, dim)
        self.rotation_matrices = []
        for _ in range(dim):
            # Generate random rotation matrices
            theta = np.random.uniform(0, 2*np.pi)
            c, s = np.cos(theta), np.sin(theta)
            self.rotation_matrices.append(np.array([[c, -s], [s, c]]))
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal Brownian motion component
        fbm_term = 0.0
        for i in range(self.dim):
            hurst = self.hurst_params[i]
            amplitude = self.fractal_amplitudes[i]
            
            # Generate fractal noise using fractional Brownian motion
            # Simplified version using multiple sine waves with different frequencies
            freqs = np.logspace(0, 3, num=10)
            fbm_sum = 0.0
            for j, freq in enumerate(freqs):
                phase = np.random.uniform(0, 2*np.pi)
                fbm_sum += amplitude * (1.0 / (freq + 1)) * np.sin(freq * x[i] + phase) * (freq ** (-hurst))
            fbm_term += fbm_sum
            
        # Multi-scale geometric features
        geometry_term = 0.0
        scales = [0.5, 1.0, 2.0, 4.0]
        for scale in scales:
            scale_sum = 0.0
            for i in range(self.dim):
                # Create self-similar geometric patterns using trigonometric functions
                scale_sum += np.sin(scale * x[i]) * np.cos(scale * x[i])
            geometry_term += scale_sum / len(scales)
            
        # Rotation-based interaction terms
        rotation_term = 0.0
        for i in range(self.dim):
            # Apply rotation to create non-separability
            if self.dim >= 2:
                # Simple 2D rotation interaction
                if i + 1 < self.dim:
                    x_rotated = np.dot(self.rotation_matrices[i], np.array([x[i], x[i+1]]))
                    rotation_term += (x_rotated[0]**2 + x_rotated[1]**2) * np.sin(x[i] * x[i+1])
                    
        # Multi-fractal dimensionality with varying roughness
        roughness_term = 0.0
        for i in range(self.dim):
            hurst = self.hurst_params[i]
            # Create roughness using Hurst parameter effects
            roughness_term += (1.0 - hurst) * np.abs(x[i])**2 + hurst * np.sin(x[i])**2
            
        # Boundary effect with fractal scaling
        boundary_term = 0.0
        for i in range(self.dim):
            # Fractal-like boundary behavior
            boundary_term += np.exp(-0.5 * (x[i] - 5.0)**2) + np.exp(-0.5 * (x[i] + 5.0)**2)
            
        # Combine all components with adaptive weighting
        total = 0.4 * fbm_term + 0.3 * geometry_term + 0.2 * rotation_term + 0.1 * roughness_term + 0.3 * boundary_term
        
        return total