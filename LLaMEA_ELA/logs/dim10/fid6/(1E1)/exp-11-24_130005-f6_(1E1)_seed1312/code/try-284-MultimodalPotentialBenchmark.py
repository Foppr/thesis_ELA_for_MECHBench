import numpy as np

class MultimodalPotentialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Sinusoidal wave component creating oscillating valleys
        wave = 0.0
        for i in range(self.dim):
            wave += np.sin(3.0 * x_scaled[i]) * np.cos(2.0 * x_scaled[i])
        
        # Polynomial potential wells with varying degrees
        polynomial = 0.0
        for i in range(self.dim):
            # Higher degree terms create sharper local minima
            polynomial += (x_scaled[i]**4 + 0.5 * x_scaled[i]**3 + 0.2 * x_scaled[i]**2)
        
        # Radial basis functions creating multiple local optima
        rbf = 0.0
        centers = np.linspace(-0.8, 0.8, min(5, self.dim))
        for i in range(self.dim):
            if i < len(centers):
                center = centers[i]
                rbf += np.exp(-5.0 * (x_scaled[i] - center)**2) + \
                       0.5 * np.exp(-3.0 * (x_scaled[i] + center)**2)
        
        # Cross-term interactions creating coupling between dimensions
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                cross_terms += 0.3 * np.sin(x_scaled[i]) * np.cos(x_scaled[j]) + \
                              0.2 * x_scaled[i] * x_scaled[j]
        
        # Distance-based penalty for being far from origin
        distance_penalty = 0.1 * np.sum(x_scaled**2)
        
        # Combine all components with adjusted weights
        return 1.5 * wave + 1.2 * polynomial + 0.8 * rbf + 0.6 * cross_terms + distance_penalty