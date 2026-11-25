import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced fractal component with higher dimensional complexity and improved nesting
        fractal = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            scale = 1.0
            nested_sum = 0.0
            for k in range(1, 10):  # Increased nesting levels for more complexity
                scale *= 0.35
                nested_sum += scale * np.sin(2**(k+3) * xi + k * np.pi/4)
            fractal += nested_sum
        
        # Dynamic phase shifts with enhanced temporal coupling and feedback
        feedback = 0.0
        for i in range(self.dim):
            if i > 2:
                delay = x_norm[i-1] + 0.35 * x_norm[i-2] - 0.18 * x_norm[i-3] + 0.07 * x_norm[i-4]
                feedback += np.sin(12.0 * delay) * np.exp(-0.25 * delay**2)
            else:
                feedback += np.sin(12.0 * x_norm[i]) * np.exp(-0.25 * x_norm[i]**2)
        
        # Adaptive curvature modulation with enhanced smoothing and dimension coupling
        erosion = 0.0
        for i in range(self.dim):
            erosion_rate = 0.2 + 0.35 * np.sin(4.5 * x_norm[i]) + 0.2 * np.cos(3.5 * i)
            erosion += erosion_rate * (x_norm[i]**4 - 2.0 * x_norm[i]**2) * np.exp(-0.12 * i)
        
        # Multi-scale interference with frequency modulation and enhanced interaction
        interference = 0.0
        for i in range(self.dim):
            freq_base = 4.0**(i % 5 + 1)  # Changed base to 4 for different frequency growth
            interference += np.sin(freq_base * x_norm[i]) * np.cos(freq_base * x_norm[i] * 2.5)
        
        # Cross-dimensional coupling with enhanced interaction range and variable strength
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Increased coupling range
                dist = np.abs(x_norm[i] - x_norm[j])
                strength = np.exp(-dist**2 * (1.7 + 0.25 * (i+j)))  # Modified strength decay
                cross += strength * np.sin(18.0 * dist) * np.cos(6.0 * dist)
        
        # Dynamic scaling with enhanced dimensionality influence and improved balance
        dynamic_scale = 1.0 + 0.7 * np.sin(self.dim * 0.35) * np.cos(np.mean(x_norm)**2)
        
        # Adaptive weights with better balance and reduced systematic bias
        weight_fractal = 0.32 + 0.12 * np.sin(self.dim * 0.3)
        weight_feedback = 0.27 + 0.09 * np.cos(self.dim * 0.25)
        weight_erosion = 0.21 + 0.13 * np.tanh(self.dim * 0.08)
        weight_interference = 0.17 + 0.07 * np.sin(self.dim * 0.18)
        weight_cross = 0.03
        
        return dynamic_scale * (weight_fractal * fractal + 
                               weight_feedback * feedback + 
                               weight_erosion * erosion + 
                               weight_interference * interference + 
                               weight_cross * cross)