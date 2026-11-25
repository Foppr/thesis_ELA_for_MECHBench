import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Main chaotic component with saddle-like structure
        chaotic = 0.0
        for i in range(self.dim):
            # Saddle point structure with hyperbolic tangent
            chaotic += np.tanh(x_scaled[i] * 3.0) * np.sin(x_scaled[i] * 2.0)
            
        # Embedded periodic orbits with varying frequencies
        periodic = 0.0
        for i in range(self.dim):
            # Multiple periodic components with different periods
            period1 = 2.0 + 0.5 * np.sin(i * 0.3)
            period2 = 3.0 + 0.3 * np.cos(i * 0.4)
            
            periodic += np.sin(x_scaled[i] * 2.0 * np.pi / period1) * \
                       np.cos(x_scaled[i] * 2.0 * np.pi / period2)
        
        # Multi-scale interaction terms with fractal-like behavior
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                # Fractal-like interaction with scaling factor
                scale_factor = 1.0 / (1.0 + np.abs(i - j))
                interaction += scale_factor * np.sin(x_scaled[i] * x_scaled[j]) * \
                              np.cos(x_scaled[i] + x_scaled[j])
        
        # Discontinuous regions with step functions
        discontinuous = 0.0
        for i in range(self.dim):
            # Step function with multiple thresholds
            threshold1 = np.sin(i * 0.5)
            threshold2 = np.cos(i * 0.3)
            
            step1 = 1.0 if x_scaled[i] > threshold1 else 0.0
            step2 = 1.0 if x_scaled[i] < threshold2 else 0.0
            
            discontinuous += step1 * np.exp(-x_scaled[i]**2) + step2 * np.exp(-(x_scaled[i]-1.0)**2)
        
        # Central attraction with repulsion zones
        attraction = 0.0
        for i in range(self.dim):
            # Distance-based attraction with exponential decay
            dist = np.abs(x_scaled[i])
            attraction += np.exp(-dist) * np.sin(dist * 5.0)
            
        # Combined function with modified weights
        return 0.8 * chaotic + 0.6 * periodic + 0.4 * interaction + 0.3 * discontinuous + 0.5 * attraction