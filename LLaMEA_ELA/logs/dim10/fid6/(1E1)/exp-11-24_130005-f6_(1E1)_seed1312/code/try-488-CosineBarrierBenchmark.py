import numpy as np

class CosineBarrierBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Radial component with periodic cosine waves
        r = np.sqrt(np.sum(x_scaled**2))
        radial = np.cos(3.0 * r) * np.exp(-0.5 * r**2)
        
        # Angular component with multiple cosine frequencies
        angular = 0.0
        for i in range(self.dim):
            angular += np.cos((i + 1) * np.pi * x_scaled[i]) * np.sin((i + 1) * np.pi * x_scaled[i])
        
        # Multi-frequency periodic pattern with exponential barriers
        periodic = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(i * 0.5)
            periodic += np.cos(freq * x_scaled[i]) * np.exp(-0.1 * np.abs(x_scaled[i]))
            
        # Exponential barrier regions with multiple transition points
        barriers = 0.0
        for i in range(self.dim):
            barriers += 2.0 * np.exp(-5.0 * (x_scaled[i] - 0.3)**2) + \
                       1.5 * np.exp(-3.0 * (x_scaled[i] + 0.4)**2) + \
                       1.0 * np.exp(-7.0 * x_scaled[i]**2)
        
        # Cross-terms with exponential decay and sinusoidal modulation
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                cross_terms += np.sin(2.0 * x_scaled[i]) * np.cos(3.0 * x_scaled[j]) * \
                              np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Combined function with modified weights
        return 1.5 * radial + 2.0 * angular + 1.2 * periodic + 1.8 * barriers + 0.8 * cross_terms