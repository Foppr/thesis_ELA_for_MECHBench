import numpy as np

class MultiModalRadialLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Radial component with multiple periodic basis functions
        r = np.sqrt(np.sum(x_scaled**2))
        radial = np.sum(0.5 * np.exp(-0.5 * (x_scaled - 0.3)**2) + 
                       0.3 * np.exp(-0.3 * (x_scaled + 0.4)**2) + 
                       0.2 * np.exp(-0.1 * (x_scaled - 0.6)**2))
        
        # Sine-cosine coupling terms between dimensions
        coupling = 0.0
        for i in range(self.dim - 1):
            coupling += np.sin(2 * np.pi * x_scaled[i]) * np.cos(3 * np.pi * x_scaled[i+1]) + \
                       0.5 * np.cos(4 * np.pi * x_scaled[i]) * np.sin(5 * np.pi * x_scaled[i+1])
        
        # Adaptive dimensionality scaling with frequency modulation
        adaptive = 0.0
        for i in range(self.dim):
            freq = 2 + 0.5 * np.sin(0.5 * i)
            adaptive += np.sin(freq * x_scaled[i])**2 + 0.3 * np.cos(freq * x_scaled[i])**2
        
        # Multi-scale periodic component with varying wavelengths
        periodic = 0.0
        for i in range(self.dim):
            periodic += np.sin(10 * np.pi * x_scaled[i]) * np.cos(8 * np.pi * x_scaled[i]) + \
                       0.7 * np.sin(15 * np.pi * x_scaled[i]) * np.cos(12 * np.pi * x_scaled[i]) + \
                       0.4 * np.sin(20 * np.pi * x_scaled[i]) * np.cos(18 * np.pi * x_scaled[i])
        
        # Cross-dimensional interaction with polynomial coupling
        cross_dim = 0.0
        for i in range(self.dim - 2):
            cross_dim += (x_scaled[i] + x_scaled[i+1])**2 * (x_scaled[i+2] - x_scaled[i])**2
        
        # Fractal-like self-similarity with nested periodic components
        fractal = 0.0
        for i in range(self.dim):
            fractal += np.sin(3 * np.pi * x_scaled[i]) * np.cos(7 * np.pi * x_scaled[i]) + \
                      0.6 * np.sin(9 * np.pi * x_scaled[i]) * np.cos(14 * np.pi * x_scaled[i]) + \
                      0.3 * np.sin(21 * np.pi * x_scaled[i]) * np.cos(35 * np.pi * x_scaled[i])
        
        # Adaptive noise component with dimension-dependent amplitude
        noise = 0.0
        for i in range(self.dim):
            noise += 0.1 * np.sin(50 * np.pi * x_scaled[i]) * np.cos(45 * np.pi * x_scaled[i]) + \
                    0.05 * np.sin(75 * np.pi * x_scaled[i]) * np.cos(60 * np.pi * x_scaled[i])
        
        # Combine all components with optimized weights
        return 0.3 * radial + 0.25 * coupling + 0.2 * adaptive + 0.15 * periodic + 0.1 * cross_dim + 0.08 * fractal + 0.05 * noise