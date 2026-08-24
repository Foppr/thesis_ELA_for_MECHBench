import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_normalized = x / 5.0
        
        # Base quadratic term with conditioning
        quadratic = np.sum(x_normalized**2)
        
        # Multiple sinusoidal components with varying frequencies and amplitudes
        sinusoidal = 0.0
        for i in range(self.dim):
            freq = 2**(i % 7 + 2)  # Increased frequency range
            amp = 2.5 + 1.5 * np.sin(i * 0.8)  # Increased amplitude variation
            sinusoidal += amp * np.sin(freq * np.pi * x_normalized[i]) * np.exp(-0.5 * (x_normalized[i] - 0.1)**2)
        
        # Add a complex penalty term with multiple local minima and higher-order terms
        penalty = 0.0
        for i in range(self.dim):
            penalty += 0.5 * (x_normalized[i]**12 - 6 * x_normalized[i]**10 + 15 * x_normalized[i]**8 - 20 * x_normalized[i]**6 + 15 * x_normalized[i]**4 - 6 * x_normalized[i]**2 + 1)
            
        # Add a global minimum at origin with additional penalty terms
        global_penalty = 0.0
        for i in range(self.dim):
            global_penalty += 0.2 * np.sin(25 * np.pi * x_normalized[i]) * np.exp(-0.3 * x_normalized[i]**2)
            
        # Add a highly oscillatory term to increase complexity with cross-dimension interactions
        oscillatory = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                oscillatory += 0.4 * np.sin(35 * np.pi * (x_normalized[i] + x_normalized[j])) * np.cos(30 * np.pi * (x_normalized[i] - x_normalized[j]))
                
        # Add a central repulsion term to challenge basin attraction
        center_repulsion = 0.0
        dist_from_origin = np.sqrt(np.sum(x_normalized**2))
        center_repulsion = 4.0 * np.exp(-0.7 * dist_from_origin**2) * (1.0 + 0.8 * np.sin(20 * dist_from_origin))
        
        # Add a new chaotic component for increased complexity with adaptive modulation
        chaotic = 0.0
        for i in range(self.dim):
            adaptive_freq = 60 + 20 * np.sin(i * 0.5)
            chaotic += 0.3 * np.sin(adaptive_freq * np.pi * x_normalized[i]) * np.cos(adaptive_freq * 0.5 * np.pi * x_normalized[i]) * np.exp(-0.15 * x_normalized[i]**2)
        
        # Add a new term for increased multimodality with non-separable interactions
        multimodal = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                multimodal += 0.25 * np.sin(40 * np.pi * x_normalized[i] * x_normalized[j]) * np.exp(-0.3 * (x_normalized[i]**2 + x_normalized[j]**2))
        
        return quadratic + sinusoidal + penalty + global_penalty + oscillatory + center_repulsion + chaotic + multimodal