import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Quadratic base term for conditioning
        quadratic_term = np.sum(x_normalized**2)
        
        # Sinusoidal perturbations with exponential decay and varying frequencies
        sin_term = 0.0
        for i in range(self.dim):
            freq = 2**(i % 4 + 1)
            sin_term += np.sin(freq * np.pi * x_normalized[i]) * np.exp(-0.5 * x_normalized[i]**2) + \
                       np.cos(freq * np.pi * x_normalized[i]) * np.exp(-0.3 * x_normalized[i]**2)
        
        # Cross-terms with varying interaction strengths and exponential decay
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 0.5 * (i + 1) / (j + 1)
                cross_term += strength * np.sin(np.pi * (x_normalized[i] + x_normalized[j])) * \
                              np.exp(-0.2 * (x_normalized[i]**2 + x_normalized[j]**2)) + \
                              np.cos(np.pi * (x_normalized[i] - x_normalized[j])) * \
                              np.exp(-0.1 * (x_normalized[i]**2 + x_normalized[j]**2))
        
        # Polynomial interaction with mixed exponents and exponential scaling
        poly_term = 0.0
        for i in range(self.dim):
            if i % 4 == 0:
                poly_term += 0.3 * x_normalized[i]**7 * np.exp(-0.1 * x_normalized[i]**2)
            elif i % 4 == 1:
                poly_term += 0.4 * x_normalized[i]**5 * np.exp(-0.2 * x_normalized[i]**2)
            elif i % 4 == 2:
                poly_term += 0.2 * x_normalized[i]**6 * np.exp(-0.15 * x_normalized[i]**2)
            else:
                poly_term += 0.5 * x_normalized[i]**4 * np.exp(-0.25 * x_normalized[i]**2)
        
        # Gaussian-like bumps to generate multiple local minima
        bump_term = 0.0
        for i in range(self.dim):
            bump_term += 0.8 * np.exp(-2.0 * (x_normalized[i] - 0.3)**2) * \
                        np.sin(4 * np.pi * x_normalized[i]) + \
                        0.6 * np.exp(-1.5 * (x_normalized[i] + 0.4)**2) * \
                        np.cos(3 * np.pi * x_normalized[i])
        
        # Final combination with adjusted weights
        return quadratic_term + 0.3 * sin_term + 0.2 * cross_term + 0.15 * poly_term + 0.25 * bump_term