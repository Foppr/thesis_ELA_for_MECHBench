import numpy as np

class NestedOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for nested oscillatory structure
        self.frequencies = np.random.uniform(1.0, 10.0, dim)
        self.amplitudes = np.random.uniform(0.5, 2.0, dim)
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        self.spatial_decay = np.random.uniform(0.1, 1.0, dim)
        self.modulation_depth = np.random.uniform(0.5, 2.0, dim)
        self.interference_strength = np.random.uniform(0.5, 3.0, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] for oscillatory functions
        x_norm = x / 5.0
        
        # Base nested oscillatory component with varying frequencies and amplitudes
        oscillatory_sum = 0.0
        for i in range(self.dim):
            freq = self.frequencies[i]
            amp = self.amplitudes[i]
            phase = self.phase_shifts[i]
            
            # Nested oscillations with harmonic relationships
            nested_term = amp * np.sin(freq * x_norm[i] + phase)
            nested_term += 0.5 * amp * np.sin(2 * freq * x_norm[i] + phase)
            nested_term += 0.3 * amp * np.sin(3 * freq * x_norm[i] + phase)
            
            oscillatory_sum += nested_term
        
        # Spatially varying amplitude gradients with exponential decay
        gradient_sum = 0.0
        for i in range(self.dim):
            decay = self.spatial_decay[i]
            amp_grad = self.amplitudes[i] * np.exp(-decay * np.abs(x_norm[i]))
            gradient_sum += amp_grad * np.cos(x_norm[i])
        
        # Adaptive frequency modulation based on position
        modulation_sum = 0.0
        for i in range(self.dim):
            depth = self.modulation_depth[i]
            mod_freq = self.frequencies[i] * (1 + depth * np.sin(x_norm[i]))
            modulation_sum += np.sin(mod_freq * x_norm[i]) * np.cos(x_norm[i])
        
        # Interference patterns between dimensions
        interference_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):
                strength = self.interference_strength[i]
                interference = strength * np.sin(x_norm[i] + x_norm[j]) * np.cos(x_norm[i] - x_norm[j])
                interference_sum += interference
        
        # Asymmetric basin boundaries with polynomial and exponential components
        boundary_sum = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                boundary_sum += (np.abs(x[i])**1.5 * np.exp(-x[i]**2) + 
                               0.5 * np.sin(x[i]) * np.cos(x[i]))
            else:
                boundary_sum += (x[i]**2 * np.exp(-x[i]) + 
                               0.3 * np.cos(x[i]) * np.sin(x[i]))
        
        # Combined objective function with weighted components
        return (0.4 * oscillatory_sum**2 + 
                0.25 * gradient_sum**2 + 
                0.2 * modulation_sum**2 + 
                0.1 * interference_sum**2 + 
                0.05 * boundary_sum**2)