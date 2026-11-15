import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute harmonic coefficients for time-varying component
        self.coeffs = np.random.uniform(-1, 1, (dim, 5))
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Polynomial interaction terms with mixed degrees
        poly_term = np.sum(x_norm**2) + 0.5 * np.sum(x_norm**3) + 0.1 * np.sum(x_norm**4)
        
        # Saddle point structure using mixed quadratic forms
        saddle = np.sum(x_norm[:-1]**2 - x_norm[1:]**2) if self.dim > 1 else 0.0
        
        # Chaotic modulation via logistic map
        chaotic = 0.0
        if self.dim > 0:
            logistic = 3.8 * (x_norm[0] * (1 - x_norm[0])) if x_norm[0] is not None else 0.0
            chaotic = logistic * np.sin(5 * np.pi * x_norm[0])
        
        # Time-varying harmonic component
        time_harmonic = 0.0
        for i in range(min(self.dim, 5)):
            time_harmonic += self.coeffs[i, 0] * np.sin(self.coeffs[i, 1] * x_norm[i] + self.coeffs[i, 2]) * \
                             np.cos(self.coeffs[i, 3] * x_norm[i] + self.coeffs[i, 4])
        
        # Cross-term interactions
        cross_term = 0.0
        if self.dim >= 2:
            for i in range(self.dim - 1):
                cross_term += x_norm[i] * x_norm[i+1] * np.sin(3 * np.pi * (x_norm[i] + x_norm[i+1]))
        
        # Penalty for staying away from origin
        penalty = 0.3 * np.sum(x_norm**2)
        
        # Combine all components
        return poly_term + 1.5 * saddle + 0.5 * chaotic + time_harmonic + cross_term + penalty