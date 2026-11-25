import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced fractal component with higher dimensional complexity
        fractal = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multi-scale fractal with varying recursion depths
            scale = 1.0
            nested_sum = 0.0
            for k in range(1, 8):  # Increased nesting levels
                scale *= 0.4
                nested_sum += scale * np.sin(2**(k+2) * xi + k * np.pi/3)
            fractal += nested_sum
        
        # Dynamic phase shifts with temporal coupling
        feedback = 0.0
        for i in range(self.dim):
            if i > 1:
                # Enhanced delayed interaction with multiple previous dimensions
                delay = x_norm[i-1] + 0.4 * x_norm[i-2] - 0.15 * x_norm[i-3] + 0.05 * x_norm[i-4]
                feedback += np.sin(10.0 * delay) * np.exp(-0.3 * delay**2)
            else:
                feedback += np.sin(10.0 * x_norm[i]) * np.exp(-0.3 * x_norm[i]**2)
        
        # Adaptive curvature modulation with dimension-dependent smoothing
        erosion = 0.0
        for i in range(self.dim):
            # Enhanced erosion with variable smoothing factor
            erosion_rate = 0.15 + 0.4 * np.sin(4.0 * x_norm[i]) + 0.25 * np.cos(3.0 * i)
            erosion += erosion_rate * (x_norm[i]**4 - 2.0 * x_norm[i]**2) * np.exp(-0.1 * i)
        
        # Multi-scale interference with frequency modulation
        interference = 0.0
        for i in range(self.dim):
            freq_base = 3.0**(i % 4 + 1)  # Changed base to 3 for different frequency growth
            interference += np.sin(freq_base * x_norm[i]) * np.cos(freq_base * x_norm[i] * 2.0)
        
        # Cross-dimensional coupling with enhanced interaction range
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Increased coupling range
                dist = np.abs(x_norm[i] - x_norm[j])
                strength = np.exp(-dist**2 * (1.5 + 0.3 * (i+j)))  # Modified strength decay
                cross += strength * np.sin(15.0 * dist) * np.cos(5.0 * dist)
        
        # Dynamic scaling with enhanced dimensionality influence
        dynamic_scale = 1.0 + 0.6 * np.sin(self.dim * 0.4) * np.cos(np.mean(x_norm)**2)
        
        # Adaptive weights with improved balance
        weight_fractal = 0.3 + 0.1 * np.sin(self.dim * 0.25)
        weight_feedback = 0.28 + 0.08 * np.cos(self.dim * 0.2)
        weight_erosion = 0.22 + 0.12 * np.tanh(self.dim * 0.07)
        weight_interference = 0.18 + 0.06 * np.sin(self.dim * 0.15)
        weight_cross = 0.02
        
        return dynamic_scale * (weight_fractal * fractal + 
                               weight_feedback * feedback + 
                               weight_erosion * erosion + 
                               weight_interference * interference + 
                               weight_cross * cross)