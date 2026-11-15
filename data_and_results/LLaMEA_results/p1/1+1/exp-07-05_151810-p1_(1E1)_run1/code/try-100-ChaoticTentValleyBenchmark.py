import numpy as np

class ChaoticTentValleyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Highly chaotic sine wave component with frequency modulation and cross-dimension coupling
        sin_component = np.sum(0.6 * np.sin(3.0 * x + 0.4 * np.sin(0.5 * x + 0.3 * np.sin(0.2 * x))) * 
                              np.cos(2.0 * x + 0.5 * np.cos(0.4 * x + 0.2 * np.cos(0.3 * x))) * 
                              (1.0 + 0.2 * np.sin(0.6 * np.sum(x))))
        
        # Adaptive radial basis function with dynamic centers and dimensionally scaled variances
        rbf = 0.0
        for i in range(self.dim):
            center = 2.5 * np.sin(0.9 * i + 0.7 * x[i]) - 1.5
            variance = 0.3 + 0.1 * np.sin(0.5 * i) + 0.05 * np.cos(0.3 * x[i])
            rbf += 1.5 * np.exp(-0.5 * (x[i] - center)**2 / variance)
        
        # Modified logistic map with multi-dimensional feedback and amplitude damping
        logistic = 0.0
        for i in range(self.dim):
            if i == 0:
                logistic_val = 4.0 * x[i] * (1.0 - x[i])
            else:
                logistic_val = 4.0 * x[i] * (1.0 - x[i])
                logistic_val *= (0.8 + 0.2 * np.sin(0.6 * x[i-1] + 0.3 * np.cos(x[i-2] if i > 1 else x[i-1])))
            logistic += logistic_val
        
        # Multi-scale radial distance with exponential modulation and angular coupling
        radial = np.sum(0.7 * np.sqrt(np.sum(x**2)) * np.exp(-0.1 * np.sum(np.abs(x)) + 0.2 * np.sin(0.5 * np.sum(x))))
        
        # Complex harmonic oscillations with time-varying amplitudes and phase shifts
        harmonic = np.sum(0.4 * np.sin(4.0 * x + 0.3 * np.sin(0.6 * x)) * 
                          np.cos(1.8 * x + 0.4 * np.cos(0.5 * x)) * 
                          (1.0 + 0.3 * np.sin(0.7 * x) * np.cos(0.4 * x)))
        
        # Combine all components with a scaling factor for enhanced multimodality
        result = sin_component + rbf + logistic + radial + harmonic
        
        return result