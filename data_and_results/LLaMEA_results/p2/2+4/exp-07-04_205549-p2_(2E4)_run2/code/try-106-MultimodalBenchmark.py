import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        quadratic = np.sum(x_norm**2)
        
        # Nested sinusoidal components with varying frequencies and amplitudes
        nested_sine = 0.0
        for i in range(self.dim):
            freq = 2**(i % 5 + 2)  # Increasing frequencies
            amp = 1.5 + 0.8 * np.sin(i * 0.5)  # Varying amplitudes
            nested_sine += amp * np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i])
        
        # Radial component with multiple peaks
        radial = 0.0
        r = np.sqrt(np.sum(x_norm**2))
        for i in range(1, 6):
            radial += 0.5 * np.sin(i * 10 * r) * np.exp(-0.5 * (r - i/5)**2)
        
        # Cross-dimensional coupling with chaotic interactions
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += 0.3 * np.sin(20 * np.pi * (x_norm[i]**2 + x_norm[j]**2)) * np.cos(15 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Chaotic component with exponential decay
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += 0.4 * np.sin(50 * np.pi * x_norm[i]) * np.cos(40 * np.pi * x_norm[i]) * np.exp(-0.3 * x_norm[i]**2)
        
        # Multi-scale oscillatory term
        multiscale = 0.0
        for i in range(self.dim):
            multiscale += 0.2 * np.sin(30 * np.pi * x_norm[i]) * np.cos(25 * np.pi * x_norm[i]) * np.sin(20 * np.pi * x_norm[i]**2)
        
        # Sharp transition component
        sharp_transitions = 0.0
        for i in range(self.dim):
            sharp_transitions += 0.3 * np.tanh(10 * x_norm[i]) * np.exp(-0.5 * x_norm[i]**2)
        
        # High-frequency noise component
        noise = 0.0
        for i in range(self.dim):
            noise += 0.1 * np.sin(100 * np.pi * x_norm[i]) * np.cos(90 * np.pi * x_norm[i])
        
        # Global structure with multiple valleys
        global_structure = 0.0
        for i in range(self.dim):
            global_structure += 0.25 * np.sin(15 * np.pi * x_norm[i]) * np.cos(12 * np.pi * x_norm[i]) * np.exp(-0.4 * x_norm[i]**2)
        
        # Combined function
        return quadratic + nested_sine + radial + coupling + chaotic + multiscale + sharp_transitions + noise + global_structure