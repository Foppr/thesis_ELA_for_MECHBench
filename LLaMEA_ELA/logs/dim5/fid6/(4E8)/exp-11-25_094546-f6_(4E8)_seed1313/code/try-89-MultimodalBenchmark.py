import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Hyperchaotic fractal component with nested self-similarity
        fractal = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Nested fractal pattern with recursive scaling
            scale = 1.0
            nested_sum = 0.0
            for k in range(1, 6):  # 5 levels of nesting
                scale *= 0.5
                nested_sum += scale * np.sin(2**(k+1) * xi + k * np.pi/4)
            fractal += nested_sum
        
        # Time-delayed feedback with memory effects
        feedback = 0.0
        for i in range(self.dim):
            if i > 2:
                # Delayed interaction with previous dimensions
                delay = x_norm[i-1] + 0.3 * x_norm[i-2] - 0.1 * x_norm[i-3]
                feedback += np.sin(8.0 * delay) * np.exp(-0.5 * delay**2)
            else:
                feedback += np.sin(8.0 * x_norm[i]) * np.exp(-0.5 * x_norm[i]**2)
        
        # Adaptive landscape erosion with dimension-dependent roughness
        erosion = 0.0
        for i in range(self.dim):
            # Varying erosion rate based on position and dimension
            erosion_rate = 0.1 + 0.3 * np.sin(3.0 * x_norm[i]) + 0.2 * np.cos(2.0 * i)
            erosion += erosion_rate * (x_norm[i]**4 - 2.0 * x_norm[i]**2)
        
        # Multi-scale interference patterns with exponential frequency growth
        interference = 0.0
        for i in range(self.dim):
            freq_base = 2.0**(i % 3 + 1)
            interference += np.sin(freq_base * x_norm[i]) * np.cos(freq_base * x_norm[i] * 1.5)
        
        # Cross-dimensional coupling with modified interaction strength and range
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Reduced coupling range
                dist = np.abs(x_norm[i] - x_norm[j])
                strength = np.exp(-dist**2 * (1.5 + 0.3 * (i+j)))  # Increased decay rate
                cross += strength * np.sin(15.0 * dist) * np.cos(5.0 * dist)  # Modified frequencies
        
        # Dynamic scaling factor based on dimensionality and position
        dynamic_scale = 1.0 + 0.5 * np.sin(self.dim * 0.35) * np.cos(np.mean(x_norm)**2)
        
        # Combine all components with adaptive weights
        weight_fractal = 0.35 + 0.08 * np.sin(self.dim * 0.25)
        weight_feedback = 0.25 + 0.1 * np.cos(self.dim * 0.18)
        weight_erosion = 0.2 + 0.15 * np.tanh(self.dim * 0.06)
        weight_interference = 0.15 + 0.05 * np.sin(self.dim * 0.12)
        weight_cross = 0.08  # Increased cross-weight
        
        return dynamic_scale * (weight_fractal * fractal + 
                               weight_feedback * feedback + 
                               weight_erosion * erosion + 
                               weight_interference * interference + 
                               weight_cross * cross)