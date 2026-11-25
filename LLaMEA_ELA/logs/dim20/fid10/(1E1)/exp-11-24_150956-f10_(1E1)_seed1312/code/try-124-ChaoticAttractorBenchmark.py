import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Chaotic sinusoidal components with logistic map modulation
        chaotic_terms = np.sum(np.sin(20.0 * np.sin(15.0 * x_scaled)) * 
                              np.cos(18.0 * np.cos(13.0 * x_scaled)) + 
                              0.5 * np.sin(25.0 * np.tan(12.0 * x_scaled)) * 
                              np.cos(22.0 * np.tan(10.0 * x_scaled)))
        
        # Saddle-point landscape with hyperbolic tangent interactions
        saddle_terms = np.sum(np.tanh(3.0 * x_scaled) * np.tanh(2.5 * x_scaled**2) + 
                            0.7 * np.tanh(4.0 * x_scaled**3) * np.tanh(3.5 * x_scaled**4))
        
        # Asymmetric hill-climbing attractors with exponential decay
        attractor_terms = np.sum(np.exp(-2.0 * (x_scaled - 0.5)**2) * 
                               (1.0 + 0.3 * np.sin(10.0 * x_scaled)) + 
                               0.6 * np.exp(-1.5 * (x_scaled + 0.7)**2) * 
                               (1.0 + 0.4 * np.cos(8.0 * x_scaled)))
        
        # Cross-dimensional coupling with fractional Brownian motion-like interactions
        cross_dim = np.sum((x_scaled[:-1]**1.5 + x_scaled[1:]**1.5) * 
                          np.sin(5.0 * (x_scaled[:-1] - x_scaled[1:])) + 
                          (x_scaled[:-2]**2.5 + x_scaled[2:]**2.5) * 
                          np.cos(3.0 * (x_scaled[:-2] + x_scaled[2:])))
        
        # Fractal-like self-similarity with recursive modulation
        fractal_terms = np.sum(np.sin(8.0 * x_scaled) * np.cos(6.0 * x_scaled) + 
                             0.3 * np.sin(16.0 * x_scaled**2) * np.cos(12.0 * x_scaled**2) + 
                             0.1 * np.sin(24.0 * x_scaled**3) * np.cos(18.0 * x_scaled**3))
        
        # Combine all components with adaptive weights
        return 0.25 * chaotic_terms + 0.2 * saddle_terms + 0.25 * attractor_terms + \
               0.15 * cross_dim + 0.15 * fractal_terms + 1.8