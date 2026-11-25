import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Radial component with chaotic modulation and multiple frequency bands
        r = np.sqrt(np.sum(x_scaled**2))
        radial = (np.sin(10 * r) * np.exp(-0.3 * r**2) + 
                  0.7 * np.sin(25 * r) * np.exp(-0.7 * r**2) + 
                  0.4 * np.sin(50 * r) * np.exp(-1.5 * r**2) +
                  0.2 * np.sin(100 * r) * np.exp(-3.0 * r**2))
        
        # Angular component with chaotic frequency modulation and non-linear coupling
        angular = 0.0
        if self.dim > 1:
            angles = np.arctan2(x_scaled[1], x_scaled[0])
            for i in range(min(5, self.dim)):
                freq = (i + 1) * 8 + np.sin(i * 2.5) * np.cos(i * 1.3)
                angular += np.sin(freq * angles + np.sin(3 * angles)) * np.cos(freq * angles + np.cos(2 * angles))
        
        # Polynomial chaos with non-uniform exponents and cross-dimensional coupling
        poly_chaos = 0.0
        for i in range(self.dim):
            poly_chaos += (x_scaled[i]**7 + 0.8 * x_scaled[i]**6 + 0.6 * x_scaled[i]**5 + 
                          0.4 * x_scaled[i]**4 + 0.3 * x_scaled[i]**3 + 0.2 * x_scaled[i]**2)
        
        # Cross-dimensional interaction with chaotic coupling weights
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x_scaled[i] * x_scaled[j]) * np.exp(-0.5 * (x_scaled[i] - x_scaled[j])**2)
                cross_interaction += coupling * (i + j + 1) / (self.dim + 1)
        
        # Chaotic perturbation with multi-scale sinusoidal components
        chaos_perturb = 0.0
        for i in range(self.dim):
            chaos_perturb += np.sin(20 * x_scaled[i] + np.sin(5 * x_scaled[i])) * np.cos(15 * x_scaled[i] + np.cos(3 * x_scaled[i]))
        
        # Non-linear transformation with exponential scaling
        nonlinear = np.sum(np.exp(2 * np.abs(x_scaled)) - 2 * np.abs(x_scaled) - 1)
        
        # Combine all components with carefully tuned weights
        return (0.8 * radial + 0.6 * angular + 0.4 * poly_chaos + 
                0.3 * cross_interaction + 0.2 * chaos_perturb + 
                0.1 * nonlinear + 0.001 * np.sum(x_scaled**8))