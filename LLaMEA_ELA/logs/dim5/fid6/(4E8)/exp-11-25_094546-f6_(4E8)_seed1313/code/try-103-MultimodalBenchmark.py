import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced hyperchaotic fractal component with improved self-similarity
        fractal = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            # Increased nesting levels and modified scaling
            scale = 1.0
            nested_sum = 0.0
            for k in range(1, 8):  # Increased to 7 levels of nesting
                scale *= 0.45  # Reduced scaling factor for more complex structure
                nested_sum += scale * np.sin(2**(k+2) * xi + k * np.pi/3)
            fractal += nested_sum
        
        # Modified time-delayed feedback with enhanced memory effects
        feedback = 0.0
        for i in range(self.dim):
            if i > 1:
                # Enhanced delayed interaction with previous dimensions
                delay = x_norm[i-1] + 0.4 * x_norm[i-2] - 0.15 * x_norm[i-3]
                feedback += np.sin(10.0 * delay) * np.exp(-0.3 * delay**2)
            else:
                feedback += np.sin(10.0 * x_norm[i]) * np.exp(-0.3 * x_norm[i]**2)
        
        # Improved adaptive landscape erosion with enhanced roughness
        erosion = 0.0
        for i in range(self.dim):
            # Enhanced erosion rate based on position and dimension
            erosion_rate = 0.15 + 0.4 * np.sin(3.5 * x_norm[i]) + 0.25 * np.cos(2.5 * i)
            erosion += erosion_rate * (x_norm[i]**4 - 2.5 * x_norm[i]**2)
        
        # Refined multi-scale interference patterns with adjusted frequency growth
        interference = 0.0
        for i in range(self.dim):
            freq_base = 2.0**(i % 4 + 1)  # Increased frequency base variation
            interference += np.sin(freq_base * x_norm[i]) * np.cos(freq_base * x_norm[i] * 1.3)
        
        # Enhanced cross-dimensional coupling with modified interaction strengths and range
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased coupling range
                dist = np.abs(x_norm[i] - x_norm[j])
                strength = np.exp(-dist**2 * (2.0 + 0.4 * (i+j)))  # Further increased decay rate
                cross += strength * np.sin(18.0 * dist) * np.cos(6.0 * dist)  # Increased frequencies
        
        # Enhanced dynamic scaling factor based on dimensionality and position
        dynamic_scale = 1.0 + 0.6 * np.sin(self.dim * 0.4) * np.cos(np.mean(x_norm)**2)
        
        # Combined components with refined weights to improve balance and reduce bias
        weight_fractal = 0.38 + 0.05 * np.sin(self.dim * 0.3)
        weight_feedback = 0.27 + 0.12 * np.cos(self.dim * 0.2)
        weight_erosion = 0.22 + 0.13 * np.tanh(self.dim * 0.08)
        weight_interference = 0.16 + 0.04 * np.sin(self.dim * 0.15)
        weight_cross = 0.12  # Increased cross-weight for better balance
        
        return dynamic_scale * (weight_fractal * fractal + 
                               weight_feedback * feedback + 
                               weight_erosion * erosion + 
                               weight_interference * interference + 
                               weight_cross * cross)