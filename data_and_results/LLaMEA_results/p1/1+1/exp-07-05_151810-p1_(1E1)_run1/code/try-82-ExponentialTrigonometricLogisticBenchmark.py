import numpy as np

class ExponentialTrigonometricLogisticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay component with varying rates
        exp_component = np.sum(0.5 * np.exp(-0.2 * np.abs(x)) * np.cos(1.5 * x))
        
        # Trigonometric wave component with frequency modulation
        wave_component = np.sum(0.8 * np.sin(2.0 * x) * np.cos(1.0 * x) * (1.0 + 0.3 * np.sin(0.5 * x)))
        
        # Logistic map component with chaotic dynamics
        logistic = 0.0
        r = 3.9  # Chaos parameter
        for i in range(self.dim):
            if i == 0:
                logistic_val = 0.5
            else:
                logistic_val = r * x[i-1] * (1.0 - x[i-1])
            logistic += 0.3 * logistic_val * np.sin(2.0 * x[i])
        
        # Multi-scale harmonic oscillations with amplitude modulation
        harmonic = np.sum(0.4 * np.sin(3.0 * x) * np.cos(2.0 * x) * (1.0 + 0.2 * np.cos(0.8 * x)))
        
        # Radial basis function with chaotic center positioning
        rbf = 0.0
        for i in range(self.dim):
            center = 2.0 * np.sin(0.6 * i + x[i] * 0.4) - 1.0
            rbf += 1.2 * np.exp(-0.5 * (x[i] - center)**2 / (0.2 + 0.1 * np.sin(i)))
        
        # Combine all components
        result = exp_component + wave_component + logistic + harmonic + rbf
        
        return result