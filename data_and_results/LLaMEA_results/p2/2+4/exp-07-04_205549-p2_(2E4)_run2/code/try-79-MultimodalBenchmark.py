import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term for conditioning
        quadratic = np.sum(x_norm**2)
        
        # Sinusoidal components with dynamic frequencies and amplitudes
        sinusoidal = 0.0
        for i in range(self.dim):
            freq = 2**(i % 5 + 2)
            amp = 1.5 + 0.8 * np.sin(i * 0.5)
            sinusoidal += amp * np.sin(freq * np.pi * x_norm[i]) * np.exp(-0.5 * x_norm[i]**2)
        
        # Exponential penalty with multiple local minima
        exp_penalty = 0.0
        for i in range(self.dim):
            exp_penalty += 0.3 * np.exp(-2.0 * (x_norm[i] - 0.2)**2) * np.sin(10 * np.pi * x_norm[i])
            
        # Cross-dimensional interaction with varying coupling strength
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.5 + 0.3 * np.sin(i * 0.4) * np.cos(j * 0.3)
                cross_interaction += coupling * np.sin(20 * np.pi * (x_norm[i] + x_norm[j])) * np.cos(15 * np.pi * (x_norm[i] - x_norm[j]))
        
        # Chaotic component with nested structure
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += 0.4 * np.sin(60 * np.pi * x_norm[i]) * np.cos(50 * np.pi * x_norm[i]) * np.exp(-0.3 * x_norm[i]**2)
            
        # Multi-scale sinusoidal modulation
        multiscale = 0.0
        for i in range(self.dim):
            multiscale += 0.25 * np.sin(40 * np.pi * x_norm[i]) * np.cos(30 * np.pi * x_norm[i]) * np.sin(20 * np.pi * x_norm[i])
        
        # Dynamic scaling factor based on dimension
        scale_factor = 1.0 + 0.2 * np.sin(self.dim * 0.3)
        
        # Ruggedness enhancement through polynomial terms
        ruggedness = 0.0
        for i in range(self.dim):
            ruggedness += 0.1 * (x_norm[i]**8 - 4 * x_norm[i]**6 + 6 * x_norm[i]**4 - 4 * x_norm[i]**2 + 1)
            
        # Global minimum attraction with repulsion
        attraction = 0.0
        dist = np.sqrt(np.sum(x_norm**2))
        attraction = 2.0 * np.exp(-0.4 * dist**2) * (1.0 + 0.5 * np.sin(10 * dist))
        
        # Add all components together with dynamic scaling
        result = scale_factor * (quadratic + sinusoidal + exp_penalty + cross_interaction + chaotic + multiscale + ruggedness + attraction)
        
        return result