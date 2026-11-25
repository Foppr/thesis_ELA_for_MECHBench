import numpy as np

class FractalEllipticValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Fractal hierarchy parameters
        self.fractal_depth = min(4, max(1, int(np.log2(dim) + 1)))
        self.hierarchy_scale = 1.0 + 0.5 * np.random.rand(self.fractal_depth)
        self.hierarchy_offset = np.random.uniform(-2.0, 2.0, (self.fractal_depth, dim))
        # Elliptic contour parameters
        self.ellipse_axes = 1.0 + 2.0 * np.random.rand(dim)
        self.ellipse_rotation = np.random.uniform(0, 2*np.pi, dim)
        # Time-variant conditioning
        self.time_phase = np.random.rand()
        self.time_scale = 1.0 + 0.3 * np.sin(0.2 * self.time_phase)
        # Noise injection parameters
        self.noise_level = 0.1 + 0.2 * np.random.rand()
        self.noise_freq = 0.5 + 0.5 * np.random.rand()
        
    def f(self, x):
        # Clip input to bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal hierarchical structure
        fractal_value = 0.0
        for depth in range(self.fractal_depth):
            scale = self.hierarchy_scale[depth]
            offset = self.hierarchy_offset[depth]
            # Nested transformation with scaling and shifting
            nested_x = (x - offset) / scale
            # Apply elliptic contour at each level
            ellipse_term = 0.0
            for i in range(self.dim):
                rotated_coord = nested_x[i] * np.cos(self.ellipse_rotation[i]) - \
                               nested_x[(i+1) % self.dim] * np.sin(self.ellipse_rotation[i])
                ellipse_term += (rotated_coord / self.ellipse_axes[i])**2
            fractal_value += np.exp(-0.5 * ellipse_term)
        
        # Time-variant elliptic contours
        time_ellipse = 0.0
        for i in range(self.dim):
            # Dynamic axis scaling based on time
            dynamic_axis = self.ellipse_axes[i] * (1.0 + 0.2 * np.sin(self.time_phase + 0.1 * i))
            # Elliptic shape with rotation and scaling
            rotated_x = x[i] * np.cos(self.ellipse_rotation[i]) - \
                       x[(i+1) % self.dim] * np.sin(self.ellipse_rotation[i])
            time_ellipse += (rotated_x / dynamic_axis)**2
        
        # Adaptive noise injection
        noise_injection = 0.0
        for i in range(self.dim):
            # Spatially varying noise with frequency modulation
            noise_freq_mod = self.noise_freq * (1.0 + 0.1 * np.sin(0.3 * x[i]))
            noise_injection += self.noise_level * np.sin(noise_freq_mod * x[i])
        
        # Combined fitness landscape
        # Create nested valleys with varying conditioning
        valley_term = 0.0
        for i in range(self.dim):
            # Quadratic valley with varying steepness
            valley_width = 1.0 + 0.5 * np.sin(0.2 * x[i])
            valley_term += (x[i] / valley_width)**2
        
        # Asymmetric conditioning and scaling
        cond_scaling = 0.0
        for i in range(self.dim):
            # Adaptive scaling based on position and dimension
            adaptive_scale = 1.0 + 0.3 * np.sin(0.5 * x[i] + 0.1 * i)
            cond_scaling += adaptive_scale * np.abs(x[i])**1.5
        
        # Combine all components with dynamic weights
        weight1 = 0.3 + 0.1 * np.sin(self.time_phase)
        weight2 = 0.4 + 0.1 * np.cos(self.time_phase)
        weight3 = 0.2 + 0.05 * np.sin(0.3 * self.dim)
        weight4 = 0.1 + 0.05 * np.cos(0.2 * self.dim)
        
        return (weight1 * fractal_value + 
                weight2 * time_ellipse + 
                weight3 * valley_term + 
                weight4 * cond_scaling + 
                noise_injection)