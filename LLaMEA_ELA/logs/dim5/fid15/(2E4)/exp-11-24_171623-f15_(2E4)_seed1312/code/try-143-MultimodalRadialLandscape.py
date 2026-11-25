import numpy as np

class MultimodalRadialLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Chaotic radial basis function components with dynamic centers
        rb_sum = 0.0
        for i in range(min(7, self.dim)):
            center = np.sin(i * np.pi / max(1, self.dim - 1)) * np.cos(i * np.pi / (self.dim + 1))
            width = 0.3 + 0.7 * np.abs(np.sin(i * np.pi / (self.dim + 2)))
            rb_sum += np.exp(-0.5 * np.sum((x_norm - center)**2) / (width**2)) * np.cos(i * x_norm[i])
        
        # Hyperbolic sinusoidal oscillations with chaotic frequencies
        sin_sum = 0.0
        for i in range(self.dim):
            freq = 1.0 + 4.0 * np.abs(np.sin(i * np.pi / (self.dim + 3)) * np.cos(i * np.pi / (self.dim + 4)))
            amp = 1.5 + 0.5 * np.sin(i * np.pi / (self.dim + 5))
            phase = np.tan(i * np.pi / (self.dim + 6))
            sin_sum += amp * np.sin(freq * x_norm[i] + phase) * np.log(np.abs(x_norm[i]) + 1.1)
        
        # Novel hyperbolic cross-dimensional coupling
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling_term = (np.tanh(x_norm[i] * x_norm[j]) + 1) * np.exp(-0.5 * (x_norm[i]**2 + x_norm[j]**2))
                cross_coupling += coupling_term
        
        # Adaptive conditioning with exponential scaling
        condition_factor = 1.0 + 0.5 * np.exp(self.dim / 10.0)
        
        # Valley structure with piecewise hyperbolic tangent
        valley_sum = 0.0
        for i in range(self.dim):
            if x_norm[i] < 0:
                valley_sum += np.tanh(x_norm[i] * 3.0) * (x_norm[i]**6 - 3*x_norm[i]**4 + 3*x_norm[i]**2)
            else:
                valley_sum += np.tanh(x_norm[i] * 2.0) * (x_norm[i]**5 - 2*x_norm[i]**3 + x_norm[i])
        
        # Additional chaotic polynomial interactions
        poly_interaction = 0.0
        for i in range(self.dim):
            poly_interaction += np.sin(x_norm[i]**3) * np.cos(x_norm[i]**2) * np.exp(-x_norm[i]**2)
        
        # Combine all components with dynamic weights
        result = 0.25 * rb_sum + 0.3 * sin_sum + 0.15 * cross_coupling + 0.2 * valley_sum + 0.1 * poly_interaction
        
        return result * condition_factor * (1 + 0.3 * np.sum(np.abs(x_norm)))