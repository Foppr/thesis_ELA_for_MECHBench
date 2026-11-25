import numpy as np

class ChaoticCubicSplineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for spline control
        self.c1 = 2.0 + np.sin(np.arange(dim) * np.pi / (dim + 1)) * 1.5
        self.c2 = 1.0 + np.cos(np.arange(dim) * np.pi / (dim + 2)) * 0.8
        self.c3 = 0.5 + np.sin(np.arange(dim) * np.pi / (dim + 3)) * 0.5
        # Adaptive frequency for chaotic modulation
        self.freq = 3.0 + np.arange(dim) * 0.3
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Initialize cubic spline components
        spline_sum = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            # Chaotic cubic spline with periodic boundary conditions
            spline_term = (self.c1[i] * xi**3 + 
                          self.c2[i] * xi**2 + 
                          self.c3[i] * xi)
            # Add chaotic modulation based on frequency
            chaotic_mod = np.sin(self.freq[i] * xi) * np.cos(self.freq[i] * xi)
            spline_sum += spline_term * chaotic_mod
        
        # Add periodic boundary term with adaptive scaling
        boundary_term = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            # Periodic boundary effect with adaptive gradient
            grad_factor = 1.0 + 0.5 * np.sin(xi * np.pi)
            boundary_term += grad_factor * np.sin(2 * np.pi * xi) ** 2
        
        # Multi-dimensional interaction with chaotic coupling
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Coupling between dimensions with chaotic phase shift
                phase_shift = np.sin(self.freq[i] * x_scaled[j]) * np.cos(self.freq[j] * x_scaled[i])
                interaction_term += phase_shift * (x_scaled[i]**2 + x_scaled[j]**2)
        
        # Adaptive exponential penalty for large values
        penalty_term = 0.0
        for i in range(self.dim):
            xi = x_scaled[i]
            # Exponential penalty with chaotic scaling factor
            penalty_factor = np.exp(0.5 * self.c1[i] * xi**2)
            penalty_term += penalty_factor
        
        # Add a chaotic noise component for additional complexity
        noise_component = 0.0
        for i in range(self.dim):
            noise_component += np.sin(5 * x_scaled[i]) * np.cos(3 * x_scaled[i])
        
        # Combine all components with adaptive weights
        return 0.3 * spline_sum + 0.25 * boundary_term + 0.2 * interaction_term + 0.15 * penalty_term + 0.1 * noise_component