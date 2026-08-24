import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with exponential decay and chaotic modulation
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.exp(-r * (1.0 + 0.3 * np.sin(15 * r))) * (1.0 + 0.4 * np.sin(8 * r))
        
        # Angular components with chaotic interference and multiple frequencies
        angular = 0.0
        for i in range(self.dim):
            freq = (i + 1) * (1.0 + 0.2 * np.sin(i * 3.14159))
            angular += np.sin(freq * x_norm[i]) * np.cos(freq * x_norm[i]) * np.exp(-0.5 * (x_norm[i]**2))
        
        # Additional multimodal term with frequency modulation and chaotic interactions
        periodic = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                periodic += np.sin((i + 1) * (j + 1) * x_norm[i]) * np.cos((i + 1) * (j + 1) * x_norm[j])
        
        # Saddle point component with gradient-based complexity
        saddle = 0.0
        for i in range(self.dim):
            saddle += (x_norm[i]**2 - 0.5 * np.sin(4 * np.pi * x_norm[i]))**2
        
        # Combine all components with adaptive weights
        return 0.25 * radial + 0.35 * angular + 0.25 * periodic + 0.15 * saddle + 1.0