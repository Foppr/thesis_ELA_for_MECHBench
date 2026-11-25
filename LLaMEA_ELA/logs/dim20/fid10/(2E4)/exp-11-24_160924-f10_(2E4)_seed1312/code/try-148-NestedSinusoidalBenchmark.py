import numpy as np

class NestedSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute dynamic phase shifts and frequencies for each dimension
        self.phases = [0.5 * np.pi * np.sin(0.4 * i) for i in range(dim)]
        self.frequencies = [1.0 + 0.5 * np.cos(0.3 * i) for i in range(dim)]
        # Precompute elliptical contour parameters with modified scaling
        self.elliptical_axes = [1.2 + 0.4 * np.sin(0.6 * i) for i in range(dim)]
        self.rotation_angles = [0.3 * np.pi * np.cos(0.5 * i) for i in range(dim)]
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add nested sinusoidal components with varying frequencies and phases
        for i in range(self.dim):
            xi = x[i]
            freq = self.frequencies[i]
            phase = self.phases[i]
            # Nested sinusoidal pattern with multiple harmonics
            result += np.sin(freq * xi + phase) + 0.5 * np.sin(2 * freq * xi + phase) + 0.3 * np.sin(3 * freq * xi + phase)
            
        # Add dynamic elliptical contours with adaptive axes and rotation
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                a = self.elliptical_axes[i]
                b = self.elliptical_axes[j]
                angle = self.rotation_angles[i] + self.rotation_angles[j]
                
                # Rotate coordinates
                cos_a = np.cos(angle)
                sin_a = np.sin(angle)
                xi_rot = xi * cos_a + xj * sin_a
                xj_rot = -xi * sin_a + xj * cos_a
                
                # Elliptical contour with modified scaling
                result += 0.7 * ((xi_rot / a)**2 + (xj_rot / b)**2) * np.exp(-0.15 * (xi_rot**2 + xj_rot**2))
                
        # Add multi-scale sinusoidal interference patterns with altered coupling
        for i in range(self.dim):
            xi = x[i]
            # Add interaction terms between dimensions with varying coupling strengths
            for j in range(self.dim):
                if i != j:
                    coupling = 0.4 * np.sin(0.5 * (i + j)) * np.cos(0.2 * (i - j))
                    result += coupling * np.sin(xi + x[j]) * np.cos(0.5 * (xi - x[j]))
                    
        # Add adaptive noise with dimension-dependent intensity
        for i in range(self.dim):
            xi = x[i]
            noise_intensity = 0.15 + 0.25 * np.sin(0.7 * i)
            result += noise_intensity * np.sin(15.0 * xi) * np.cos(12.0 * xi)
            
        # Add hierarchical nested structures with self-similarity
        for i in range(self.dim):
            xi = x[i]
            # Multiple nested peaks at different scales
            result += 0.9 * np.exp(-0.5 * ((xi - 2.0) / 0.6)**2)
            result += 0.5 * np.exp(-0.5 * ((xi + 1.5) / 1.2)**2)
            result += 0.3 * np.exp(-0.5 * ((xi - 3.0) / 1.8)**2)
            
        # Add dynamic phase coupling between dimensions with modified strength
        for i in range(0, self.dim - 1, 2):
            if i + 1 < self.dim:
                phase_coupling = 0.5 * np.sin(self.phases[i] + self.phases[i+1])
                result += phase_coupling * np.sin(x[i] + x[i+1]) * np.cos(0.3 * (x[i] - x[i+1]))
                
        # Add global scaling factor based on dimensionality
        global_scale = 1.0 + 0.4 * np.sin(0.1 * self.dim)
        result *= global_scale
        
        return result