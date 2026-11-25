import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term with adaptive conditioning
        quad_term = np.sum(x_norm**2)
        
        # Chaotic trigonometric components with varying frequencies
        trig_term = 0
        for i in range(self.dim):
            trig_term += (np.sin(10 * x_norm[i]) * np.cos(7 * x_norm[i]) + 
                         0.5 * np.sin(15 * x_norm[i]) * np.cos(12 * x_norm[i]) +
                         0.3 * np.sin(20 * x_norm[i]) * np.cos(18 * x_norm[i]))
        
        # Polynomial coupling terms creating complex interaction
        poly_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling for complexity control
                poly_coupling += (x_norm[i]**3 + x_norm[j]**3) * np.sin(5 * (x_norm[i] - x_norm[j])**2)
        
        # Saddle point inducing term with hyperbolic tangent
        saddle_term = 0
        for i in range(self.dim):
            saddle_term += np.tanh(3 * x_norm[i]) * np.cos(8 * x_norm[i])
        
        # Adaptive scaling based on dimensionality
        scale_factor = 1.0 + 2.0 * np.log(self.dim + 1)
        
        # Additional chaotic noise with exponential decay
        noise = np.sum(np.exp(-np.abs(x_norm)) * np.sin(25 * x_norm) ** 3)
        
        # Combined landscape with modified global structure
        return scale_factor * (quad_term + 0.5 * trig_term + 0.3 * poly_coupling + 
                              0.4 * saddle_term + 0.1 * noise)