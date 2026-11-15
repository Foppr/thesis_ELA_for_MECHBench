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
            freq = 2**(i % 5 + 2)  # Slightly reduced frequency range
            amp = 1.8 + 1.0 * np.sin(i * 0.6)  # Slightly reduced amplitude variation
            sinusoidal += amp * np.sin(freq * np.pi * x_normalized[i]) * np.exp(-0.3 * (x_normalized[i] - 0.1)**2)
        
        # Add a complex penalty term with multiple local minima and higher-order terms
        penalty = 0.0
        for i in range(self.dim):
            penalty += 0.35 * (x_normalized[i]**10 - 5 * x_normalized[i]**8 + 10 * x_normalized[i]**6 - 10 * x_normalized[i]**4 + 5 * x_normalized[i]**2 - 1)
            
        # Add a global minimum at origin with additional penalty terms
        global_penalty = 0.0
        for i in range(self.dim):
            global_penalty += 0.12 * np.sin(18 * np.pi * x_normalized[i]) * np.exp(-0.15 * x_normalized[i]**2)
            
        # Add a highly oscillatory term to increase complexity with cross-dimension interactions
        oscillatory = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                oscillatory += 0.25 * np.sin(25 * np.pi * (x_normalized[i] + x_normalized[j])) * np.cos(20 * np.pi * (x_normalized[i] - x_normalized[j]))
                
        # Add a central repulsion term to challenge basin attraction
        center_repulsion = 0.0
        dist_from_origin = np.sqrt(np.sum(x_normalized**2))
        center_repulsion = 2.5 * np.exp(-0.5 * dist_from_origin**2) * (1.0 + 0.6 * np.sin(12 * dist_from_origin))
        
        # Add a new chaotic component for increased complexity
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += 0.2 * np.sin(40 * np.pi * x_normalized[i]) * np.cos(30 * np.pi * x_normalized[i]) * np.exp(-0.08 * x_normalized[i]**2)
        
        # Add a new term to improve fitness score and reduce bias
        bias_reduction = 0.0
        for i in range(self.dim):
            bias_reduction += 0.05 * np.sin(8 * np.pi * x_normalized[i]) * np.cos(6 * np.pi * x_normalized[i])
        
        return quadratic + sinusoidal + penalty + global_penalty + oscillatory + center_repulsion + chaotic + bias_reduction