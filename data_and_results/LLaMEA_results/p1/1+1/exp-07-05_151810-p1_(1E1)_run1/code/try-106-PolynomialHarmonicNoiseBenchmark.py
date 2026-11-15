import numpy as np

class PolynomialHarmonicNoiseBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial chaos expansion component with adaptive degree
        chaos = 0.0
        for i in range(self.dim):
            poly_term = (x[i]**4 + 0.5 * x[i]**3 - 0.3 * x[i]**2 + 0.1 * x[i])
            chaos += poly_term * (1.0 + 0.2 * np.sin(0.5 * i * x[i]))
        
        # Gradient-based harmonic field with directional coupling
        harmonic = 0.0
        for i in range(self.dim):
            if i == 0:
                grad_field = np.sin(2.0 * x[i]) * np.cos(1.5 * x[i])
            else:
                grad_field = np.sin(2.0 * x[i]) * np.cos(1.5 * x[i]) + 0.3 * np.sin(x[i-1]) * np.cos(x[i-1])
            harmonic += grad_field * (1.0 + 0.1 * np.cos(0.3 * i))
        
        # Adaptive noise injection with spatial correlation
        noise = 0.0
        for i in range(self.dim):
            noise_val = np.random.normal(0, 0.1 * (1.0 + 0.05 * np.abs(x[i])))
            noise += noise_val * np.exp(-0.1 * (x[i]**2)) * (1.0 + 0.15 * np.sin(0.4 * i))
        
        # Multi-scale radial component with dynamic scaling
        radial = np.sum(0.8 * np.abs(x) * (1.0 + 0.2 * np.sin(0.3 * np.sum(x))) * (1.0 + 0.1 * np.cos(0.2 * np.sum(x))))
        
        # Coupled oscillatory terms with frequency modulation
        oscillatory = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.3 * np.sin(0.2 * i)
            oscillatory += np.sin(freq * x[i] + 0.5 * np.cos(0.3 * x[i])) * np.cos(0.7 * x[i] + 0.4 * np.sin(0.2 * x[i]))
        
        # Combine all components with dynamic weights
        weight_chaos = 1.0 + 0.1 * np.sin(0.1 * np.sum(x))
        weight_harmonic = 1.0 + 0.05 * np.cos(0.15 * np.sum(x))
        weight_noise = 1.0 + 0.2 * np.sin(0.2 * np.sum(x))
        weight_radial = 1.0 + 0.15 * np.cos(0.1 * np.sum(x))
        weight_oscillatory = 1.0 + 0.1 * np.sin(0.25 * np.sum(x))
        
        result = weight_chaos * chaos + weight_harmonic * harmonic + weight_noise * noise + weight_radial * radial + weight_oscillatory * oscillatory
        
        return result