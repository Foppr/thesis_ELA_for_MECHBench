import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic behavior
        self.a = 3.9
        self.b = 0.1
        self.c = 0.5
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Chaotic component using logistic map with multi-dimensional coupling
        chaotic = 0.0
        for i in range(self.dim):
            # Logistic map with parameter dependence
            param = 3.8 + 0.1 * np.sin(x_scaled[i] * 2.0)
            chaotic += (param * x_scaled[i] * (1 - x_scaled[i])) ** 2
        
        # Multi-modal component with embedded saddle points
        multimodal = 0.0
        for i in range(self.dim):
            # Multiple quadratic wells with varying depths and positions
            well_depth = 1.0 + 0.5 * np.sin(i * 0.3)
            well_position = np.cos(i * 0.4) * 0.7
            multimodal += well_depth * (x_scaled[i] - well_position)**2 * \
                         (1 + 0.3 * np.sin(5 * x_scaled[i]))
        
        # Saddle point component with gradient discontinuities
        saddle = 0.0
        for i in range(self.dim):
            # Gradient discontinuity at specific points
            discontinuity_point = np.sin(i * 0.2) * 0.5
            if x_scaled[i] < discontinuity_point:
                saddle += (x_scaled[i] - discontinuity_point)**3
            else:
                saddle += (x_scaled[i] - discontinuity_point)**2
            
            # Add saddle point potential
            saddle += 0.2 * np.sin(3 * x_scaled[i]) * np.cos(2 * x_scaled[i])
        
        # Cross-term interaction with chaotic coupling
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Chaotic coupling between dimensions
                coupling_strength = 0.3 * (1 + np.sin(x_scaled[i] + x_scaled[j]))
                cross_terms += coupling_strength * np.sin(x_scaled[i] * x_scaled[j])
        
        # Gradient discontinuity landscape with piecewise linear regions
        gradient_discontinuity = 0.0
        for i in range(self.dim):
            # Piecewise function with sharp transitions
            if x_scaled[i] < -0.3:
                gradient_discontinuity += 2 * x_scaled[i]**2 + 0.1
            elif x_scaled[i] < 0.3:
                gradient_discontinuity += 0.5 * x_scaled[i]**3
            else:
                gradient_discontinuity += 2 * (x_scaled[i] - 0.3)**2 + 0.2
        
        # Combined function with modified weights and chaotic scaling
        return 1.2 * chaotic + 0.8 * multimodal + 1.5 * saddle + 0.7 * cross_terms + 0.9 * gradient_discontinuity