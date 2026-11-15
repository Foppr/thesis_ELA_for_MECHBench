import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base with varying weights
        quadratic = np.sum(0.5 * x_norm**2)
        
        # Chaotic sine wave with varying frequencies and amplitudes
        chaotic_sine = 0.0
        for i in range(self.dim):
            freq = 2**(i % 5 + 1)
            amp = 1.0 / (i + 1)
            chaotic_sine += amp * np.sin(freq * np.pi * x_norm[i])
        
        # Hyperbolic tangent polynomial interaction
        tanh_poly = np.sum(np.tanh(x_norm)**3)
        
        # Embedded saddle point structure using mixed powers
        saddle = 0.0
        for i in range(self.dim):
            saddle += x_norm[i]**4 - 2 * x_norm[i]**2
        
        # Multi-scale radial basis with varying widths and centers
        rbf = 0.0
        centers = np.linspace(-1, 1, min(5, self.dim))
        widths = np.logspace(-2, 1, min(5, self.dim))
        for i in range(min(5, self.dim)):
            center = centers[i]
            width = widths[i]
            rbf += np.exp(-width * (x_norm - center)**2)
        
        # Gradient-based chaotic modulation with logistic map
        gradient_mod = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                logistic_val = 3.8 * x_norm[i] * (1 - x_norm[i])
                gradient_mod += logistic_val * x_norm[i+1]**2
        
        # Non-smooth component with piecewise linear transitions
        non_smooth = 0.0
        for i in range(self.dim):
            if x_norm[i] < -0.5:
                non_smooth += 2 * x_norm[i]**2
            elif x_norm[i] > 0.5:
                non_smooth += 2 * (x_norm[i] - 1)**2
            else:
                non_smooth += 0.5 * x_norm[i]**3
        
        # Combine all components with carefully tuned weights
        return (0.3 * quadratic + 
                0.25 * chaotic_sine + 
                0.2 * tanh_poly + 
                0.15 * saddle + 
                0.1 * rbf + 
                0.05 * gradient_mod + 
                0.05 * non_smooth)