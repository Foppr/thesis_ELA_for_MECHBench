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
            freq = 2**(i % 6 + 3)  # Increased frequency range
            amp = 2.0 + 1.2 * np.sin(i * 0.7)  # Increased amplitude variation
            sinusoidal += amp * np.sin(freq * np.pi * x_normalized[i]) * np.exp(-0.4 * (x_normalized[i] - 0.2)**2)
        
        # Add a complex penalty term with multiple local minima and higher-order terms
        penalty = 0.0
        for i in range(self.dim):
            penalty += 0.4 * (x_normalized[i]**10 - 5 * x_normalized[i]**8 + 10 * x_normalized[i]**6 - 10 * x_normalized[i]**4 + 5 * x_normalized[i]**2 - 1)
            
        # Add a global minimum at origin with additional penalty terms
        global_penalty = 0.0
        for i in range(self.dim):
            global_penalty += 0.15 * np.sin(20 * np.pi * x_normalized[i]) * np.exp(-0.2 * x_normalized[i]**2)
            
        # Add a highly oscillatory term to increase complexity with cross-dimension interactions
        oscillatory = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                oscillatory += 0.3 * np.sin(30 * np.pi * (x_normalized[i] + x_normalized[j])) * np.cos(25 * np.pi * (x_normalized[i] - x_normalized[j]))
                
        # Add a central repulsion term to challenge basin attraction
        center_repulsion = 0.0
        dist_from_origin = np.sqrt(np.sum(x_normalized**2))
        center_repulsion = 3.0 * np.exp(-0.6 * dist_from_origin**2) * (1.0 + 0.7 * np.sin(15 * dist_from_origin))
        
        # Introduce a new chaotic component to increase complexity and improve fitness score
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += 0.3 * np.sin(35 * np.pi * x_normalized[i]) * np.cos(30 * np.pi * x_normalized[i]) * np.exp(-0.25 * x_normalized[i]**2)
            
        # Add a cross-dimensional interaction term with varying weights
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.15 * (i + 1) * (j + 1) / (self.dim * (self.dim + 1) / 2)
                cross_interaction += weight * np.sin(15 * np.pi * (x_normalized[i]**2 + x_normalized[j]**2)) * np.exp(-0.15 * (x_normalized[i] - x_normalized[j])**2)
        
        # Add a new fractal-like component for enhanced multimodality
        fractal = 0.0
        for i in range(self.dim):
            fractal += 0.2 * np.sin(50 * np.pi * x_normalized[i]) * np.cos(40 * np.pi * x_normalized[i]) * np.exp(-0.3 * x_normalized[i]**2) + 0.1 * np.sin(60 * np.pi * x_normalized[i])
            
        # Add a dynamic interaction term that changes with dimensionality
        dynamic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dynamic_interaction += 0.1 * np.sin(5 * np.pi * (x_normalized[i] + x_normalized[j])) * np.cos(3 * np.pi * (x_normalized[i] - x_normalized[j])) * np.exp(-0.05 * (i - j)**2)
        
        return quadratic + sinusoidal + penalty + global_penalty + oscillatory + center_repulsion + chaotic + cross_interaction + fractal + dynamic_interaction