import numpy as np

class MultimodalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        self.sigma = 0.5
        self.omega = 2.0 * np.pi
        self.alpha = 0.1
        self.beta = 0.05
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        
        # Radial component with chaotic modulation
        r = np.sqrt(np.sum(x**2))
        
        # Sinusoidal waves in multiple dimensions
        wave_sum = 0
        for i in range(self.dim):
            wave_sum += np.sin(self.omega * x[i]) * np.cos(self.omega * x[i] * 0.5)
        
        # Radial basis function component
        rb_sum = 0
        for i in range(self.dim):
            rb_sum += np.exp(-self.alpha * (x[i] - 1.0)**2) + np.exp(-self.alpha * (x[i] + 1.0)**2)
        
        # Chaotic saddle point component
        chaotic_term = 0
        for i in range(self.dim):
            chaotic_term += np.sin(self.omega * x[i]) * np.cos(self.omega * x[i]) * np.exp(-self.beta * r**2)
        
        # Polynomial interaction terms
        poly_term = 0
        for i in range(self.dim):
            poly_term += x[i]**4 - 2 * x[i]**2
        
        # Combine all components with varying weights
        return (0.3 * r**2 + 
                1.2 * wave_sum + 
                0.8 * rb_sum + 
                0.6 * chaotic_term + 
                0.4 * poly_term)