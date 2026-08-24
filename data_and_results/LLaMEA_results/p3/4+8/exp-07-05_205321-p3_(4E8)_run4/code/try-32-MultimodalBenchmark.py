import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with exponential decay and modified frequency
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.exp(-2.0 * r) * (1.0 + 0.3 * np.sin(15 * r))
        
        # Angular components with increased harmonic complexity
        angular = 0.0
        for i in range(self.dim):
            angular += np.sin((i + 1) * np.pi * x_norm[i]) * np.cos((i + 2) * np.pi * x_norm[i])
        
        # Additional multimodal term with shifted periodicity
        periodic = np.sum(np.sin(4 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm) * np.exp(-0.5 * r))
        
        # Shifted global minimum component
        shift = np.sum((x_norm + 0.2)**2) * 0.1
        
        # Combine all components
        return 0.4 * radial + 0.3 * angular + 0.2 * periodic + 0.1 * shift + 0.8