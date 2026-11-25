import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced fractal component with higher dimensional complexity and increased recursion
        fractal = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Multi-scale fractal with varying recursion depths and additional harmonics
            scale = 1.0
            nested_sum = 0.0
            for k in range(1, 12):  # Increased nesting levels
                scale *= 0.35
                nested_sum += scale * np.sin(2**(k+3) * xi + k * np.pi/4)
            fractal += nested_sum
        
        # Dynamic phase shifts with enhanced temporal coupling and feedback loops
        feedback = 0.0
        for i in range(self.dim):
            if i > 2:
                # Enhanced delayed interaction with more complex previous dimension dependencies
                delay = x_norm[i-1] + 0.5 * x_norm[i-2] - 0.2 * x_norm[i-3] + 0.08 * x_norm[i-4] + 0.03 * x_norm[i-5]
                feedback += np.sin(12.0 * delay) * np.exp(-0.4 * delay**2)
            else:
                feedback += np.sin(12.0 * x_norm[i]) * np.exp(-0.4 * x_norm[i]**2)
        
        # Adaptive curvature modulation with dimension-dependent smoothing and additional nonlinearity
        erosion = 0.0
        for i in range(self.dim):
            # Enhanced erosion with variable smoothing factor and additional sine component
            erosion_rate = 0.2 + 0.5 * np.sin(5.0 * x_norm[i]) + 0.3 * np.cos(4.0 * i) + 0.1 * np.sin(2.0 * i)
            erosion += erosion_rate * (x_norm[i]**5 - 2.5 * x_norm[i]**3 + 1.0 * x_norm[i]) * np.exp(-0.15 * i)
        
        # Multi-scale interference with frequency modulation and enhanced cross-talk
        interference = 0.0
        for i in range(self.dim):
            freq_base = 4.0**(i % 5 + 1)  # Changed base to 4 for different frequency growth
            interference += np.sin(freq_base * x_norm[i]) * np.cos(freq_base * x_norm[i] * 2.5) + 0.1 * np.sin(freq_base * x_norm[i] * 3.0)
        
        # Cross-dimensional coupling with enhanced interaction range and modified strength
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+7, self.dim)):  # Increased coupling range
                dist = np.abs(x_norm[i] - x_norm[j])
                strength = np.exp(-dist**2 * (2.0 + 0.4 * (i+j)))  # Modified strength decay
                cross += strength * np.sin(20.0 * dist) * np.cos(7.0 * dist) + 0.05 * np.sin(10.0 * dist)
        
        # Dynamic scaling with enhanced dimensionality influence and additional harmonic
        dynamic_scale = 1.0 + 0.8 * np.sin(self.dim * 0.5) * np.cos(np.mean(x_norm)**2) * np.exp(-0.05 * self.dim)
        
        # Adaptive weights with improved balance and additional sinusoidal modulation
        weight_fractal = 0.35 + 0.15 * np.sin(self.dim * 0.3)
        weight_feedback = 0.3 + 0.12 * np.cos(self.dim * 0.25)
        weight_erosion = 0.25 + 0.15 * np.tanh(self.dim * 0.08)
        weight_interference = 0.15 + 0.08 * np.sin(self.dim * 0.2)
        weight_cross = 0.03 + 0.02 * np.cos(self.dim * 0.1)
        
        return dynamic_scale * (weight_fractal * fractal + 
                               weight_feedback * feedback + 
                               weight_erosion * erosion + 
                               weight_interference * interference + 
                               weight_cross * cross)