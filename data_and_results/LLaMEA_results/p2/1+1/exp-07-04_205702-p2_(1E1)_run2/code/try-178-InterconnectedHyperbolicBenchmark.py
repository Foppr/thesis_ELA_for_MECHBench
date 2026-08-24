import numpy as np

class InterconnectedHyperbolicBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = 0.3 * np.sum(x**2)
        
        # Hyperbolic sine and cosine peaks with varying amplitudes and positions
        f2 = 0.0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                f2 += 2.0 * np.sinh(0.5 * x[i]) * np.cosh(0.3 * x[i+1])
        
        # Trigonometric modulations with varying frequencies and phases
        f3 = 0.0
        for i in range(self.dim):
            f3 += np.sin(2.0 * x[i]) * np.cos(1.5 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Cross-dimensional interaction using hyperbolic tangent
        f4 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                f4 += np.tanh(x[i] * x[j]) * np.sin(0.7 * (x[i] + x[j]))
        
        # Asymmetric basin structure with exponential and logarithmic components
        f5 = 0.0
        for i in range(self.dim):
            f5 += 0.5 * np.exp(-0.2 * (x[i] - 2.0)**2) * np.log(1.0 + 0.5 * x[i]**2)
        
        # Multimodal component with Gaussian and sinc functions
        f6 = 0.0
        for i in range(self.dim):
            f6 += 1.0 * np.exp(-0.5 * (x[i] - 1.0)**2) * np.sinc(0.5 * x[i])
        
        # Fractional power and logarithmic interaction
        f7 = 0.0
        for i in range(self.dim):
            f7 += 0.3 * np.abs(x[i])**1.7 * np.log(1.0 + np.abs(x[i]))
        
        # Add noise for robustness
        noise = 0.01 * np.random.rand()
        
        # Combine all components
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + noise