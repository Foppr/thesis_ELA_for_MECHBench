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
            # Multi-scale fractal with varying recursion depths and improved scaling
            scale = 1.0
            nested_sum = 0.0
            for k in range(1, 10):  # Increased nesting levels for more complexity
                scale *= 0.35
                nested_sum += scale * np.sin(2**(k+3) * xi + k * np.pi/4)
            fractal += nested_sum
        
        # Dynamic phase shifts with temporal coupling and enhanced feedback
        feedback = 0.0
        for i in range(self.dim):
            if i > 2:
                # Enhanced delayed interaction with multiple previous dimensions
                delay = x_norm[i-1] + 0.3 * x_norm[i-2] - 0.1 * x_norm[i-3] + 0.03 * x_norm[i-4]
                feedback += np.sin(12.0 * delay) * np.exp(-0.25 * delay**2)
            else:
                feedback += np.sin(8.0 * x_norm[i]) * np.exp(-0.2 * x_norm[i]**2)
        
        # Adaptive curvature modulation with dimension-dependent smoothing
        erosion = 0.0
        for i in range(self.dim):
            # Enhanced erosion with variable smoothing factor and improved modulation
            erosion_rate = 0.2 + 0.35 * np.sin(5.0 * x_norm[i]) + 0.2 * np.cos(4.0 * i)
            erosion += erosion_rate * (x_norm[i]**4 - 2.0 * x_norm[i]**2) * np.exp(-0.15 * i)
        
        # Multi-scale interference with frequency modulation and improved coupling
        interference = 0.0
        for i in range(self.dim):
            freq_base = 4.0**(i % 5 + 1)  # Changed base to 4 for different frequency growth
            interference += np.sin(freq_base * x_norm[i]) * np.cos(freq_base * x_norm[i] * 2.5)
        
        # Cross-dimensional coupling with enhanced interaction range and modified strength
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Increased coupling range
                dist = np.abs(x_norm[i] - x_norm[j])
                strength = np.exp(-dist**2 * (1.8 + 0.25 * (i+j)))  # Modified strength decay
                cross += strength * np.sin(18.0 * dist) * np.cos(6.0 * dist)
        
        # Dynamic scaling with enhanced dimensionality influence and improved balance
        dynamic_scale = 1.0 + 0.55 * np.sin(self.dim * 0.35) * np.cos(np.mean(x_norm)**2)
        
        # Adaptive weights with improved balance and reduced systematic biases
        weight_fractal = 0.32 + 0.08 * np.sin(self.dim * 0.3)
        weight_feedback = 0.27 + 0.1 * np.cos(self.dim * 0.15)
        weight_erosion = 0.23 + 0.11 * np.tanh(self.dim * 0.08)
        weight_interference = 0.16 + 0.07 * np.sin(self.dim * 0.2)
        weight_cross = 0.02
        
        return dynamic_scale * (weight_fractal * fractal + 
                               weight_feedback * feedback + 
                               weight_erosion * erosion + 
                               weight_interference * interference + 
                               weight_cross * cross)