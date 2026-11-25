import numpy as np

class RadialChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with adaptive widths
        rbfs = 0.0
        centers = np.linspace(-5.0, 5.0, min(10, self.dim))
        for i in range(min(10, self.dim)):
            center = centers[i] if self.dim > 1 else 0.0
            width = 0.5 + 0.5 * np.sin(i * 0.5)
            rbfs += np.exp(-0.5 * ((x - center) / width)**2)
        
        # Chaotic gradient component using a modified sine map
        chaotic_grad = 0.0
        a = 3.8
        for i in range(self.dim):
            if i == 0:
                prev_val = x[i]
            else:
                prev_val = x[i-1]
            chaotic_grad += np.sin(a * prev_val * (1 - prev_val)) * (x[i] - prev_val)
        
        # Polynomial interaction terms with varying exponents
        poly_interaction = np.sum((x**3.2 + 0.7 * x**2.8 - 0.4 * x**1.5 + 1.1 * x)**1.3)
        
        # Cross-term with cosine modulation for additional complexity
        cross_cos = 0.0
        for i in range(self.dim - 1):
            cross_cos += np.cos(x[i] * x[i+1]) * (x[i] + x[i+1])**2
        
        # Sine wave modulation to add periodicity
        sine_mod = np.sum(np.sin(2.0 * x) * np.cos(0.5 * x))
        
        # Combine all components with optimized weights
        return 0.3 * rbfs + 0.25 * chaotic_grad + 0.2 * poly_interaction + 0.15 * cross_cos + 0.1 * sine_mod + 1.0